"use client";

import { useState, useEffect, useCallback } from "react";
import { ChatLayout } from "@/components/chat-layout";
import { Sidebar } from "@/components/sidebar";
import { ChatPanel } from "@/components/chat-panel";
import { sendMessage } from "@/lib/api";
import { DEFAULT_PROFILE } from "@/lib/constants";
import { GuidedTour } from "@/components/guided-tour";
import { StartupProfile, Message, Conversation } from "@/lib/types";

function generateId(): string {
  if (typeof crypto !== "undefined" && crypto.randomUUID) {
    return crypto.randomUUID();
  }
  return Date.now().toString(36) + Math.random().toString(36).slice(2);
}

const STORAGE_KEY = "tamwil-conversations";
const PROFILE_KEY = "tamwil-profile";

function loadConversations(): Conversation[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : [];
  } catch {
    return [];
  }
}

function saveConversations(conversations: Conversation[]) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(conversations));
}

function loadProfile(): StartupProfile | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = localStorage.getItem(PROFILE_KEY);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
}

function saveProfile(profile: StartupProfile) {
  localStorage.setItem(PROFILE_KEY, JSON.stringify(profile));
}

function createNewConversation(): Conversation {
  return {
    id: generateId(),
    title: "Nouvelle conversation",
    messages: [],
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
}

export default function Home() {
  const [profile, setProfile] = useState<StartupProfile>(DEFAULT_PROFILE);
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [activeId, setActiveId] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [hydrated, setHydrated] = useState(false);

  // Load from localStorage on mount
  useEffect(() => {
    const saved = loadConversations();
    setConversations(saved);
    if (saved.length > 0) {
      setActiveId(saved[0].id);
    }
    const savedProfile = loadProfile();
    if (savedProfile) {
      setProfile(savedProfile);
    }
    setHydrated(true);
  }, []);

  // Save to localStorage whenever conversations change
  useEffect(() => {
    if (hydrated) {
      saveConversations(conversations);
    }
  }, [conversations, hydrated]);

  // Save profile to localStorage whenever it changes
  useEffect(() => {
    if (hydrated) {
      saveProfile(profile);
    }
  }, [profile, hydrated]);

  const activeConversation = conversations.find((c) => c.id === activeId);
  const activeMessages = activeConversation?.messages ?? [];

  const handleNewChat = useCallback(() => {
    const conv = createNewConversation();
    setConversations((prev) => [conv, ...prev]);
    setActiveId(conv.id);
  }, []);

  const handleSelectConversation = useCallback((id: string) => {
    setActiveId(id);
  }, []);

  const handleDeleteConversation = useCallback(
    (id: string) => {
      setConversations((prev) => {
        const next = prev.filter((c) => c.id !== id);
        if (activeId === id) {
          setActiveId(next.length > 0 ? next[0].id : null);
        }
        return next;
      });
    },
    [activeId]
  );

  const handleRenameConversation = useCallback(
    (id: string, newTitle: string) => {
      setConversations((prev) =>
        prev.map((c) =>
          c.id === id
            ? { ...c, title: newTitle, updatedAt: new Date().toISOString() }
            : c
        )
      );
    },
    []
  );

  const handleSend = async (text: string) => {
    let convId = activeId;

    // Auto-create a conversation if none active
    if (!convId) {
      const conv = createNewConversation();
      setConversations((prev) => [conv, ...prev]);
      convId = conv.id;
      setActiveId(conv.id);
    }

    const userMessage: Message = {
      id: generateId(),
      role: "user",
      content: text,
      timestamp: new Date(),
    };

    setConversations((prev) =>
      prev.map((c) => {
        if (c.id !== convId) return c;
        const isFirst = c.messages.length === 0;
        return {
          ...c,
          messages: [...c.messages, userMessage],
          title: isFirst ? text : c.title,
          updatedAt: new Date().toISOString(),
        };
      })
    );
    setIsLoading(true);

    try {
      const currentConv = conversations.find((c) => c.id === convId);
      const history = (currentConv?.messages ?? []).map((m) => ({
        role: m.role,
        content: m.content,
      }));

      const response = await sendMessage({
        message: text,
        profile,
        history,
      });

      const assistantMessage: Message = {
        id: generateId(),
        role: "assistant",
        content: response.reply,
        timestamp: new Date(),
      };

      setConversations((prev) =>
        prev.map((c) =>
          c.id === convId
            ? {
                ...c,
                messages: [...c.messages, assistantMessage],
                updatedAt: new Date().toISOString(),
              }
            : c
        )
      );
    } catch {
      const errorMessage: Message = {
        id: generateId(),
        role: "assistant",
        content: "Désolé, une erreur est survenue. Veuillez réessayer.",
        timestamp: new Date(),
      };

      setConversations((prev) =>
        prev.map((c) =>
          c.id === convId
            ? {
                ...c,
                messages: [...c.messages, errorMessage],
                updatedAt: new Date().toISOString(),
              }
            : c
        )
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <ChatLayout
        sidebar={
          <Sidebar
            conversations={conversations}
            activeId={activeId}
            onNewChat={handleNewChat}
            onSelectConversation={handleSelectConversation}
            onDeleteConversation={handleDeleteConversation}
            onRenameConversation={handleRenameConversation}
            profile={profile}
            onProfileChange={setProfile}
          />
        }
      >
        <ChatPanel
          messages={activeMessages}
          isLoading={isLoading}
          onSend={handleSend}
        />
      </ChatLayout>
      <GuidedTour />
    </>
  );
}
