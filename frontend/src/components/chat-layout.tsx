"use client";

import { ReactNode, useState, createContext, useContext } from "react";
import { AnimatedGridPattern } from "@/components/animated-grid-pattern";

interface SidebarContextType {
  collapsed: boolean;
  toggle: () => void;
  mobileOpen: boolean;
  setMobileOpen: (open: boolean) => void;
}

const SidebarContext = createContext<SidebarContextType>({
  collapsed: false,
  toggle: () => {},
  mobileOpen: false,
  setMobileOpen: () => {},
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
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <SidebarContext.Provider
      value={{
        collapsed,
        toggle: () => setCollapsed((c) => !c),
        mobileOpen,
        setMobileOpen,
      }}
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

        {/* Mobile sidebar overlay */}
        {mobileOpen && (
          <div
            className="fixed inset-0 z-40 bg-black/50 md:hidden"
            onClick={() => setMobileOpen(false)}
          />
        )}

        <aside
          className={`
            /* Mobile: fixed overlay */
            fixed inset-y-0 left-0 z-50 w-[260px] bg-sidebar
            transition-transform duration-300 ease-in-out
            ${mobileOpen ? "translate-x-0" : "-translate-x-full"}
            /* Desktop: inline sidebar */
            md:relative md:z-10 md:translate-x-0 md:shrink-0
            md:overflow-hidden md:transition-all md:duration-300
            ${collapsed ? "md:w-[52px]" : "md:w-[260px]"}
          `}
        >
          <div className="flex h-full w-[260px] flex-col">{sidebar}</div>
        </aside>

        <main className="relative z-10 flex flex-1 flex-col overflow-hidden">
          {children}
        </main>
      </div>
    </SidebarContext.Provider>
  );
}
