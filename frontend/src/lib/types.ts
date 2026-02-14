export interface StartupProfile {
  secteur: string;
  stade: string;
  pays: string;
  mrr: number | "";
  burnRate: number | "";
  churn: number | "";
  cac: number | "";
  ltv: number | "";
}

export interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
}

export interface ChatRequest {
  message: string;
  profile: StartupProfile;
  history: Pick<Message, "role" | "content">[];
}

export interface ChatResponse {
  reply: string;
}

export interface Conversation {
  id: string;
  title: string;
  messages: Message[];
  createdAt: string;
  updatedAt: string;
}
