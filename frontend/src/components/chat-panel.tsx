"use client";

import { useRef, useEffect } from "react";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Badge } from "@/components/ui/badge";
import { MessageBubble } from "@/components/message-bubble";
import { ChatInput } from "@/components/chat-input";
import { ThemeToggle } from "@/components/theme-toggle";
import { Message } from "@/lib/types";
import { Bot, TrendingUp, Users, Landmark, MessageCircle } from "lucide-react";

interface ChatPanelProps {
  messages: Message[];
  isLoading: boolean;
  onSend: (text: string) => void;
}

const SUGGESTIONS = [
  { icon: TrendingUp, text: "Calculer mon score de fundability" },
  { icon: Users, text: "Trouver des investisseurs pour ma startup" },
  { icon: Landmark, text: "Quelles subventions sont disponibles ?" },
  { icon: MessageCircle, text: "Faire un diagnostic financier" },
];

export function ChatPanel({ messages, isLoading, onSend }: ChatPanelProps) {
  const scrollRef = useRef<HTMLDivElement>(null);

  // Auto-scroll when new messages arrive
  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  return (
    <div className="flex flex-1 flex-col overflow-hidden">
      <div className="flex items-center justify-between bg-gradient-to-b from-background/80 via-background/60 to-background/40 backdrop-blur-md border-b border-primary/10 px-6 py-3">
        <div className="flex items-center gap-3">
          <div className="flex size-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
            <Bot className="size-4" />
          </div>
          <h1 className="text-lg font-semibold">Tamwil AI</h1>
          <Badge variant="secondary" className="text-xs">Beta</Badge>
        </div>
        <ThemeToggle />
      </div>

      <div className="relative flex-1 overflow-hidden">
        <ScrollArea className="h-full px-6 py-4">
          {messages.length === 0 && (
            <div className="flex flex-col items-center justify-center py-16">
              <div className="flex size-16 items-center justify-center rounded-2xl bg-primary/10 mb-6">
                <Bot className="size-8 text-primary" />
              </div>
              <h2 className="text-2xl font-semibold tracking-tight">
                Bienvenue sur Tamwil AI
              </h2>
              <p className="mt-2 max-w-md text-center text-muted-foreground">
                Votre assistant IA pour le financement des startups au Maroc et en Afrique francophone.
              </p>
              <div className="mt-8 grid grid-cols-2 gap-3 w-full max-w-lg">
                {SUGGESTIONS.map((s) => (
                  <button
                    key={s.text}
                    onClick={() => onSend(s.text)}
                    className="flex items-start gap-3 rounded-xl border bg-card p-4 text-left text-sm transition-colors hover:bg-accent hover:border-orange-300/30"
                  >
                    <s.icon className="size-4 mt-0.5 shrink-0 text-primary" />
                    <span>{s.text}</span>
                  </button>
                ))}
              </div>
            </div>
          )}

          {messages.map((message) => (
            <MessageBubble key={message.id} message={message} />
          ))}

          {isLoading && (
            <div className="flex justify-start mb-3">
              <div className="rounded-2xl rounded-bl-sm bg-muted px-4 py-3">
                <div className="flex gap-1">
                  <span className="size-2 animate-bounce rounded-full bg-primary/50" style={{ animationDelay: "0ms" }} />
                  <span className="size-2 animate-bounce rounded-full bg-primary/50" style={{ animationDelay: "150ms" }} />
                  <span className="size-2 animate-bounce rounded-full bg-primary/50" style={{ animationDelay: "300ms" }} />
                </div>
              </div>
            </div>
          )}

          <div ref={scrollRef} />
        </ScrollArea>
      </div>

      <ChatInput onSend={onSend} isLoading={isLoading} />
    </div>
  );
}
