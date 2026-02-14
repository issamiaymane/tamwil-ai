"use client";

import { ReactNode, useState, createContext, useContext } from "react";
import { AnimatedGridPattern } from "@/components/animated-grid-pattern";
import { Button } from "@/components/ui/button";
import { PanelLeft } from "lucide-react";

interface SidebarContextType {
  collapsed: boolean;
  toggle: () => void;
}

const SidebarContext = createContext<SidebarContextType>({
  collapsed: false,
  toggle: () => {},
});

export function useSidebar() {
  return useContext(SidebarContext);
}

interface ChatLayoutProps {
  sidebar: ReactNode;
  children: ReactNode;
}

export function ChatLayout({ sidebar, children }: ChatLayoutProps) {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <SidebarContext.Provider
      value={{ collapsed, toggle: () => setCollapsed((c) => !c) }}
    >
      <div className="relative flex h-screen overflow-hidden">
        <div className="pointer-events-none fixed inset-0 skew-y-12">
          <AnimatedGridPattern
            numSquares={30}
            maxOpacity={0.1}
            duration={3}
            repeatDelay={1}
            className="[mask-image:radial-gradient(1000px_circle_at_center,orange,transparent)]"
          />
        </div>

        <aside
          className={`relative z-10 shrink-0 bg-sidebar overflow-hidden transition-all duration-300 ease-in-out ${
            collapsed ? "w-0" : "w-[260px]"
          }`}
        >
          <div className="flex h-full w-[260px] flex-col">{sidebar}</div>
        </aside>

        <main className="relative z-10 flex flex-1 flex-col overflow-hidden">
          {/* Reopen button when collapsed */}
          {collapsed && (
            <Button
              variant="ghost"
              size="icon"
              onClick={() => setCollapsed(false)}
              className="absolute left-3 top-3 z-20 size-8 text-muted-foreground hover:text-foreground"
            >
              <PanelLeft className="size-4" />
            </Button>
          )}
          {children}
        </main>
      </div>
    </SidebarContext.Provider>
  );
}
