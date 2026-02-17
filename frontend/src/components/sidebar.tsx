"use client";

import { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogTrigger,
} from "@/components/ui/dialog";
import {
  DropdownMenu,
  DropdownMenuTrigger,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
} from "@/components/ui/dropdown-menu";
import { ScrollArea } from "@/components/ui/scroll-area";
import { ProfileForm } from "@/components/profile-form";
import { useSidebar } from "@/components/chat-layout";
import { Conversation, StartupProfile } from "@/lib/types";
import {
  PanelLeftClose,
  PanelLeft,
  SquarePen,
  Trash2,
  CircleUserRound,
  Ellipsis,
  Pencil,
} from "lucide-react";

interface SidebarProps {
  conversations: Conversation[];
  activeId: string | null;
  onNewChat: () => void;
  onSelectConversation: (id: string) => void;
  onDeleteConversation: (id: string) => void;
  onRenameConversation: (id: string, title: string) => void;
  profile: StartupProfile;
  onProfileChange: (profile: StartupProfile) => void;
}

export function Sidebar({
  conversations,
  activeId,
  onNewChat,
  onSelectConversation,
  onDeleteConversation,
  onRenameConversation,
  profile,
  onProfileChange,
}: SidebarProps) {
  const { collapsed, toggle, setMobileOpen } = useSidebar();
  const [editingId, setEditingId] = useState<string | null>(null);
  const [editValue, setEditValue] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (editingId && inputRef.current) {
      inputRef.current.focus();
      inputRef.current.select();
    }
  }, [editingId]);

  const startRename = (conv: Conversation) => {
    setEditingId(conv.id);
    setEditValue(conv.title);
  };

  const commitRename = () => {
    if (editingId && editValue.trim()) {
      onRenameConversation(editingId, editValue.trim());
    }
    setEditingId(null);
  };

  const cancelRename = () => {
    setEditingId(null);
  };

  /* ── Collapsed icon strip (desktop only) ── */
  if (collapsed) {
    return (
      <div className="hidden md:flex h-full w-[52px] flex-col items-center bg-sidebar text-sidebar-foreground py-2 gap-1">
        <Button
          variant="ghost"
          size="icon"
          onClick={toggle}
          className="size-8 text-sidebar-foreground/60 hover:text-sidebar-foreground hover:bg-sidebar-accent"
        >
          <PanelLeft className="size-4" />
        </Button>
        <Button
          variant="ghost"
          size="icon"
          onClick={onNewChat}
          className="size-8 text-sidebar-foreground/60 hover:text-sidebar-foreground hover:bg-sidebar-accent"
        >
          <SquarePen className="size-4" />
        </Button>

        <div className="flex-1" />

        <Dialog>
          <DialogTrigger asChild>
            <button className="flex size-8 items-center justify-center rounded-lg transition-colors hover:bg-sidebar-accent">
              <CircleUserRound className="size-4 text-sidebar-foreground/60" />
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
    );
  }

  /* ── Expanded sidebar ── */
  return (
    <div className="flex h-full flex-col bg-sidebar text-sidebar-foreground">
      {/* Top bar — close (mobile) / collapse (desktop) + new chat */}
      <div className="flex items-center justify-between p-2">
        {/* Mobile: close overlay */}
        <Button
          variant="ghost"
          size="icon"
          onClick={() => setMobileOpen(false)}
          className="size-8 text-sidebar-foreground/60 hover:text-sidebar-foreground hover:bg-sidebar-accent md:hidden"
        >
          <PanelLeftClose className="size-4" />
        </Button>
        {/* Desktop: collapse sidebar */}
        <Button
          variant="ghost"
          size="icon"
          onClick={toggle}
          className="hidden md:flex size-8 text-sidebar-foreground/60 hover:text-sidebar-foreground hover:bg-sidebar-accent"
        >
          <PanelLeftClose className="size-4" />
        </Button>
        <Button
          variant="ghost"
          size="icon"
          onClick={() => {
            onNewChat();
            setMobileOpen(false);
          }}
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
            <div
              key={conv.id}
              role="button"
              tabIndex={0}
              onClick={() => {
                if (editingId !== conv.id) {
                  onSelectConversation(conv.id);
                  setMobileOpen(false);
                }
              }}
              onKeyDown={(e) => {
                if (
                  editingId !== conv.id &&
                  (e.key === "Enter" || e.key === " ")
                ) {
                  e.preventDefault();
                  onSelectConversation(conv.id);
                }
              }}
              className={`group relative flex w-full items-center gap-2 rounded-lg px-3 py-2 text-left text-sm transition-colors cursor-pointer
                ${
                  conv.id === activeId
                    ? "bg-sidebar-accent text-sidebar-accent-foreground"
                    : "text-sidebar-foreground/70 hover:bg-sidebar-accent/50 hover:text-sidebar-foreground"
                }`}
            >
              {editingId === conv.id ? (
                <input
                  ref={inputRef}
                  value={editValue}
                  onChange={(e) => setEditValue(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") {
                      e.preventDefault();
                      commitRename();
                    } else if (e.key === "Escape") {
                      cancelRename();
                    }
                    e.stopPropagation();
                  }}
                  onBlur={commitRename}
                  onClick={(e) => e.stopPropagation()}
                  className="flex-1 bg-transparent border border-sidebar-border rounded px-1 py-0.5 text-[13px] text-sidebar-foreground outline-none focus:border-primary"
                />
              ) : (
                <span className="flex-1 min-w-0 truncate text-[13px]">
                  {conv.title}
                </span>
              )}

              {editingId !== conv.id && (
                <DropdownMenu>
                  <DropdownMenuTrigger asChild>
                    <button
                      onClick={(e) => e.stopPropagation()}
                      className="opacity-0 group-hover:opacity-100 data-[state=open]:opacity-100 shrink-0 rounded p-1 text-sidebar-foreground/40 hover:text-sidebar-foreground transition-opacity"
                    >
                      <Ellipsis className="size-4" />
                    </button>
                  </DropdownMenuTrigger>
                  <DropdownMenuContent side="right" align="start">
                    <DropdownMenuItem onClick={() => startRename(conv)}>
                      <Pencil className="size-4" />
                      Renommer
                    </DropdownMenuItem>
                    <DropdownMenuSeparator />
                    <DropdownMenuItem
                      onClick={() => onDeleteConversation(conv.id)}
                      className="text-destructive focus:text-destructive"
                    >
                      <Trash2 className="size-4" />
                      Supprimer
                    </DropdownMenuItem>
                  </DropdownMenuContent>
                </DropdownMenu>
              )}
            </div>
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
