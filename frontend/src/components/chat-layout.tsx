"use client";

import {
  ReactNode,
  useState,
  useCallback,
  useRef,
  createContext,
  useContext,
} from "react";
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

const MIN_WIDTH = 180;
const MAX_WIDTH = 480;
const DEFAULT_WIDTH = 260;
const COLLAPSED_WIDTH = 52;

interface ChatLayoutProps {
  sidebar: ReactNode;
  children: ReactNode;
}

export function ChatLayout({ sidebar, children }: ChatLayoutProps) {
  const [collapsed, setCollapsed] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [sidebarWidth, setSidebarWidth] = useState(DEFAULT_WIDTH);
  const [isDragging, setIsDragging] = useState(false);
  const startXRef = useRef(0);
  const startWidthRef = useRef(DEFAULT_WIDTH);

  const handleMouseDown = useCallback(
    (e: React.MouseEvent) => {
      e.preventDefault();
      setIsDragging(true);
      startXRef.current = e.clientX;
      startWidthRef.current = sidebarWidth;

      const handleMouseMove = (e: MouseEvent) => {
        const delta = e.clientX - startXRef.current;
        const newWidth = Math.min(
          MAX_WIDTH,
          Math.max(MIN_WIDTH, startWidthRef.current + delta)
        );
        setSidebarWidth(newWidth);
      };

      const handleMouseUp = () => {
        setIsDragging(false);
        document.removeEventListener("mousemove", handleMouseMove);
        document.removeEventListener("mouseup", handleMouseUp);
      };

      document.addEventListener("mousemove", handleMouseMove);
      document.addEventListener("mouseup", handleMouseUp);
    },
    [sidebarWidth]
  );

  const displayWidth = collapsed ? COLLAPSED_WIDTH : sidebarWidth;

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
            fixed inset-y-0 left-0 z-50 bg-sidebar
            transition-transform duration-300 ease-in-out
            ${mobileOpen ? "translate-x-0" : "-translate-x-full"}
            md:relative md:z-10 md:translate-x-0 md:shrink-0
            md:overflow-hidden
            ${isDragging ? "" : "md:transition-all md:duration-300"}
          `}
          style={{ width: `${displayWidth}px` }}
        >
          <div className="flex h-full w-full flex-col overflow-hidden">
            {sidebar}
          </div>
        </aside>

        {/* Resize handle — desktop only */}
        {!collapsed && (
          <div
            onMouseDown={handleMouseDown}
            className="hidden md:flex z-20 w-1 shrink-0 cursor-col-resize items-center justify-center hover:bg-primary/20 active:bg-primary/30 transition-colors"
          >
            <div className="h-8 w-0.5 rounded-full bg-border" />
          </div>
        )}

        <main className="relative z-10 flex flex-1 flex-col overflow-hidden">
          {children}
        </main>
      </div>

      {/* Prevent text selection while dragging */}
      {isDragging && (
        <div className="fixed inset-0 z-[9999] cursor-col-resize" />
      )}
    </SidebarContext.Provider>
  );
}
