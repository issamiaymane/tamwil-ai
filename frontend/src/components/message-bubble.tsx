"use client";

import { cn } from "@/lib/utils";
import { Message } from "@/lib/types";

interface MessageBubbleProps {
  message: Message;
}

function formatContent(content: string): React.ReactNode {
  const lines = content.split("\n");
  const elements: React.ReactNode[] = [];
  let tableRows: string[][] = [];
  let inTable = false;

  const flushTable = () => {
    if (tableRows.length === 0) return;
    const headers = tableRows[0];
    const dataRows = tableRows.slice(1).filter(
      (row) => !row.every((cell) => cell.replace(/-/g, "").trim() === "")
    );
    elements.push(
      <div key={`table-${elements.length}`} className="my-2 overflow-x-auto">
        <table className="w-full text-sm border-collapse">
          <thead>
            <tr>
              {headers.map((h, i) => (
                <th key={i} className="border border-border px-2 py-1 text-left font-medium bg-muted/50">
                  {renderInline(h.trim())}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {dataRows.map((row, ri) => (
              <tr key={ri}>
                {row.map((cell, ci) => (
                  <td key={ci} className="border border-border px-2 py-1">
                    {renderInline(cell.trim())}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
    tableRows = [];
    inTable = false;
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    if (line.startsWith("|") && line.endsWith("|")) {
      inTable = true;
      const cells = line.split("|").slice(1, -1);
      tableRows.push(cells);
      continue;
    }

    if (inTable) {
      flushTable();
    }

    if (line.trim() === "") {
      elements.push(<br key={`br-${i}`} />);
    } else if (line.match(/^\d+\.\s/)) {
      elements.push(
        <p key={`li-${i}`} className="ml-4">
          {renderInline(line)}
        </p>
      );
    } else if (line.startsWith("- ")) {
      elements.push(
        <p key={`ul-${i}`} className="ml-4">
          {renderInline("• " + line.slice(2))}
        </p>
      );
    } else {
      elements.push(
        <p key={`p-${i}`}>{renderInline(line)}</p>
      );
    }
  }

  if (inTable) flushTable();

  return <>{elements}</>;
}

function renderInline(text: string): React.ReactNode {
  const parts = text.split(/(\*\*[^*]+\*\*)/g);
  return parts.map((part, i) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={i}>{part.slice(2, -2)}</strong>;
    }
    return part;
  });
}

export function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <div className={cn("flex mb-3", isUser ? "justify-end" : "justify-start")}>
      <div
        className={cn(
          "max-w-[75%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed",
          isUser
            ? "rounded-br-sm bg-primary text-primary-foreground"
            : "rounded-bl-sm bg-muted text-foreground"
        )}
      >
        {isUser ? message.content : formatContent(message.content)}
      </div>
    </div>
  );
}
