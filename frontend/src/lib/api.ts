import { ChatRequest, ChatResponse, SourceInfo } from "./types";

const API_URL = "http://localhost:8000/api/chat";
const STREAM_URL = "http://localhost:8000/api/chat/stream";

export async function sendMessage(request: ChatRequest): Promise<ChatResponse> {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  });

  if (!res.ok) {
    throw new Error(`API error: ${res.status}`);
  }

  return res.json();
}

export interface StreamCallbacks {
  onSources: (sources: SourceInfo[]) => void;
  onToken: (token: string) => void;
  onReply: (text: string) => void;
  onDone: () => void;
  onError: (error: Error) => void;
}

export async function sendMessageStream(
  request: ChatRequest,
  callbacks: StreamCallbacks
): Promise<void> {
  const res = await fetch(STREAM_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  });

  if (!res.ok) {
    callbacks.onError(new Error(`API error: ${res.status}`));
    return;
  }

  const reader = res.body?.getReader();
  if (!reader) {
    callbacks.onError(new Error("No response body"));
    return;
  }

  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    const chunk = decoder.decode(value, { stream: true });
    buffer += chunk;
    const parts = buffer.split("\n\n");
    buffer = parts.pop() ?? "";

    for (const part of parts) {
      if (!part.trim()) continue;
      const lines = part.split("\n");
      let eventType = "";
      const dataLines: string[] = [];

      for (const line of lines) {
        if (line.startsWith("event: ")) {
          eventType = line.slice(7);
        } else if (line.startsWith("data: ")) {
          dataLines.push(line.slice(6));
        } else if (line === "data:") {
          dataLines.push("");
        }
      }

      const data = dataLines.join("\n");

      switch (eventType) {
        case "sources":
          callbacks.onSources(JSON.parse(data));
          break;
        case "token":
          callbacks.onToken(data);
          break;
        case "reply":
          callbacks.onReply(JSON.parse(data).text);
          break;
        case "done":
          callbacks.onDone();
          break;
      }
    }
  }
}
