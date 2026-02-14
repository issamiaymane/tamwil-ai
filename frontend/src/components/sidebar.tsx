"use client";

import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogTrigger,
} from "@/components/ui/dialog";
import { ScrollArea } from "@/components/ui/scroll-area";
import { ProfileForm } from "@/components/profile-form";
import { useSidebar } from "@/components/chat-layout";
import { Conversation, StartupProfile } from "@/lib/types";
import {
  PanelLeftClose,
  SquarePen,
  MessageSquare,
  Trash2,
  CircleUserRound,
} from "lucide-react";

interface SidebarProps {
  conversations: Conversation[];
  activeId: string | null;
  onNewChat: () => void;
  onSelectConversation: (id: string) => void;
  onDeleteConversation: (id: string) => void;
  profile: StartupProfile;
  onProfileChange: (profile: StartupProfile) => void;
}

function timeAgo(dateStr: string): string {
  const seconds = Math.floor(
    (Date.now() - new Date(dateStr).getTime()) / 1000
  );
  if (seconds < 60) return "à l'instant";
  const minutes = Math.floor(seconds / 60);
  if (minutes < 60) return `il y a ${minutes}min`;
  const hours = Math.floor(minutes / 60);
  if (hours < 24) return `il y a ${hours}h`;
  const days = Math.floor(hours / 24);
  return `il y a ${days}j`;
}

export function Sidebar({
  conversations,
  activeId,
  onNewChat,
  onSelectConversation,
  onDeleteConversation,
  profile,
  onProfileChange,
}: SidebarProps) {
  const { toggle } = useSidebar();

  return (
    <div className="flex h-full flex-col bg-sidebar text-sidebar-foreground">
      {/* Top bar — collapse + new chat */}
      <div className="flex items-center justify-between p-2">
        <Button
          variant="ghost"
          size="icon"
          onClick={toggle}
          className="size-8 text-sidebar-foreground/60 hover:text-sidebar-foreground hover:bg-sidebar-accent"
        >
          <PanelLeftClose className="size-4" />
        </Button>
        <Button
          variant="ghost"
          size="icon"
          onClick={onNewChat}
          className="size-8 text-sidebar-foreground/60 hover:text-sidebar-foreground hover:bg-sidebar-accent"
        >
          <SquarePen className="size-4" />
        </Button>
      </div>

      {/* Conversation list */}
      <ScrollArea className="flex-1">
        <div className="flex flex-col gap-0.5 px-2 pb-2">
          {conversations.length === 0 && (
            <div className="flex flex-col items-center justify-center py-16 px-4">
              <p className="text-xs text-sidebar-foreground/40 text-center">
                Aucune conversation
              </p>
            </div>
          )}

          {conversations.map((conv) => (
            <button
              key={conv.id}
              onClick={() => onSelectConversation(conv.id)}
              className={`group relative flex w-full items-center gap-2 rounded-lg px-3 py-2 text-left text-sm transition-colors
                ${
                  conv.id === activeId
                    ? "bg-sidebar-accent text-sidebar-accent-foreground"
                    : "text-sidebar-foreground/70 hover:bg-sidebar-accent/50 hover:text-sidebar-foreground"
                }`}
            >
              <span className="flex-1 truncate text-[13px]">
                {conv.title}
              </span>
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  onDeleteConversation(conv.id);
                }}
                className="opacity-0 group-hover:opacity-100 shrink-0 rounded p-1 text-sidebar-foreground/30 hover:text-destructive transition-opacity"
              >
                <Trash2 className="size-3.5" />
              </button>
            </button>
          ))}
        </div>
      </ScrollArea>

      {/* Bottom — profile */}
      <div className="border-t border-sidebar-border p-2">
        <Dialog>
          <DialogTrigger asChild>
            <button className="flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-left text-sm transition-colors hover:bg-sidebar-accent">
              <div className="flex size-8 items-center justify-center rounded-full bg-sidebar-accent">
                <CircleUserRound className="size-4 text-sidebar-foreground/70" />
              </div>
              <div className="flex-1 min-w-0">
                <p className="truncate text-[13px] font-medium text-sidebar-foreground">
                  Mon profil
                </p>
                <p className="truncate text-[11px] text-sidebar-foreground/50">
                  Configurer ma startup
                </p>
              </div>
            </button>
          </DialogTrigger>
          <DialogContent className="max-w-md max-h-[85vh] overflow-y-auto">
            <DialogHeader>
              <DialogTitle>Profil Startup</DialogTitle>
              <DialogDescription>
                Personnalisez vos résultats
              </DialogDescription>
            </DialogHeader>
            <ProfileForm profile={profile} onProfileChange={onProfileChange} />
          </DialogContent>
        </Dialog>
      </div>
    </div>
  );
}
