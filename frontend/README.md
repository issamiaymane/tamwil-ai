# Tamwil AI — Frontend

Next.js 16 + React 19 + Tailwind CSS 4 interface for the Tamwil AI chatbot.

## Getting Started

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). The backend must be running on port 8000.

```bash
# Terminal 1 — Backend
uvicorn backend.app.main:app --reload --port 8000

# Terminal 2 — Frontend
cd frontend && npm run dev
```

## Project Structure

```
src/
├── app/
│   ├── layout.tsx              # Root layout
│   └── page.tsx                # Main page
├── components/
│   ├── chat-layout.tsx         # Main layout (sidebar + chat panel)
│   ├── chat-panel.tsx          # Message area with SSE streaming
│   ├── chat-input.tsx          # User message input
│   ├── message-bubble.tsx      # Message rendering (markdown + sources)
│   ├── sidebar.tsx             # Draggable sidebar with conversation list
│   ├── profile-form.tsx        # Startup profile form
│   ├── guided-tour.tsx         # Interactive onboarding tour (React Joyride)
│   ├── theme-toggle.tsx        # Dark/light mode toggle
│   ├── theme-provider.tsx      # Theme context provider
│   ├── animated-grid-pattern.tsx # Decorative background
│   └── ui/                     # Reusable UI primitives (button, card, dialog, etc.)
└── lib/
    ├── api.ts                  # API client (REST + SSE streaming)
    ├── types.ts                # TypeScript interfaces
    ├── constants.ts            # Constants
    └── utils.ts                # Utilities
```

## API Connection

- **REST**: `POST http://localhost:8000/api/chat` — non-streaming responses
- **SSE**: `POST http://localhost:8000/api/chat/stream` — streaming responses (used for Q&A)

## Features

- Chat conversationnel with markdown rendering
- SSE streaming for real-time Q&A responses
- Startup profile form (sector, stage, country, metrics)
- Multiple conversations with local storage persistence
- Draggable/resizable sidebar with conversation hover menu
- Dark/light mode
- Interactive guided tour for first-time users
- Structured source display with clickable URLs
