import { ChatRequest, ChatResponse } from "./types";

const API_URL = "http://localhost:8000/api/chat";

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
