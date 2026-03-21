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

function ConversationItem({
  conv,
  isActive,
  isEditing,
  editValue,
  inputRef,
  onSelect,
  onEditChange,
  onCommitRename,
  onCancelRename,
  onStartRename,
  onDelete,
}: {
  conv: Conversation;
  isActive: boolean;
  isEditing: boolean;
  editValue: string;
  inputRef: React.RefObject<HTMLInputElement | null>;
  onSelect: () => void;
  onEditChange: (v: string) => void;
  onCommitRename: () => void;
  onCancelRename: () => void;
  onStartRename: () => void;
  onDelete: () => void;
}) {
  const [hovered, setHovered] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const showBtn = hovered || menuOpen;

  return (
    <div
      role="button"
      tabIndex={0}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      onClick={() => {
        if (!isEditing) onSelect();
      }}
      onKeyDown={(e) => {
        if (!isEditing && (e.key === "Enter" || e.key === " ")) {
          e.preventDefault();
          onSelect();
        }
      }}
      className={`relative flex w-full items-center gap-1 rounded-lg px-2 py-2 text-left text-sm transition-colors cursor-pointer overflow-hidden
        ${
          isActive
            ? "bg-sidebar-accent text-sidebar-accent-foreground"
            : "text-sidebar-foreground/70 hover:bg-sidebar-accent/50 hover:text-sidebar-foreground"
        }`}
    >
      {isEditing ? (
        <input
          ref={inputRef}
          value={editValue}
          onChange={(e) => onEditChange(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              e.preventDefault();
              onCommitRename();
            } else if (e.key === "Escape") {
              onCancelRename();
            }
            e.stopPropagation();
          }}
          onBlur={onCommitRename}
          onClick={(e) => e.stopPropagation()}
          className="flex-1 min-w-0 bg-transparent border border-sidebar-border rounded px-1 py-0.5 text-[13px] text-sidebar-foreground outline-none focus:border-primary"
        />
      ) : (
        <span className="truncate text-[13px]" style={{ flex: "1 1 0", minWidth: 0 }}>
          {conv.title}
        </span>
      )}

      {!isEditing && (
        <DropdownMenu onOpenChange={setMenuOpen}>
          <DropdownMenuTrigger asChild>
            <button
              onClick={(e) => e.stopPropagation()}
              style={{
                opacity: showBtn ? 1 : 0,
                pointerEvents: showBtn ? "auto" : "none",
              }}
              className="flex-shrink-0 flex size-6 items-center justify-center rounded text-sidebar-foreground/70 hover:text-sidebar-foreground hover:bg-sidebar-accent transition-opacity"
            >
              <Ellipsis className="size-4" />
            </button>
          </DropdownMenuTrigger>
          <DropdownMenuContent side="right" align="start">
            <DropdownMenuItem onClick={onStartRename}>
              <Pencil className="size-4" />
              Renommer
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem
              onClick={onDelete}
              className="text-destructive focus:text-destructive"
            >
              <Trash2 className="size-4" />
              Supprimer
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      )}
    </div>
  );
}

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
    <div id="tour-sidebar" className="flex h-full flex-col bg-sidebar text-sidebar-foreground">
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
          id="tour-new-chat"
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
            <ConversationItem
              key={conv.id}
              conv={conv}
              isActive={conv.id === activeId}
              isEditing={editingId === conv.id}
              editValue={editValue}
              inputRef={inputRef}
              onSelect={() => {
                onSelectConversation(conv.id);
                setMobileOpen(false);
              }}
              onEditChange={setEditValue}
              onCommitRename={commitRename}
              onCancelRename={cancelRename}
              onStartRename={() => startRename(conv)}
              onDelete={() => onDeleteConversation(conv.id)}
            />
          ))}
        </div>
      </ScrollArea>

      {/* Bottom — profile */}
      <div className="border-t border-sidebar-border p-2">
        <Dialog>
          <DialogTrigger asChild>
            <button id="tour-profile" className="flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-left text-sm transition-colors hover:bg-sidebar-accent">
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
