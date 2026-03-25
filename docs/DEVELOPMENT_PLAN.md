# Tamwil AI — Development Plan

> Step-by-step build order for the Tamwil AI chatbot project.

---

## Phase 1 — Project Structure + Config + Data Layer

**Goal:** Set up the foundation — folders, dependencies, configuration, and data validation.

| Task | Details |
|------|---------|
| Create folder structure | `backend/app/`, `backend/app/modules/`, `backend/app/rag/`, `backend/app/utils/`, `frontend/`, `tests/` |
| `requirements.txt` | LangChain, ChromaDB, sentence-transformers, OpenAI, python-dotenv, tiktoken |
| `.env` | `OPENAI_API_KEY`, `CHROMA_PERSIST_DIR`, `EMBEDDING_MODEL`, `LLM_MODEL`, `CHUNK_SIZE`, `CHUNK_OVERLAP`, `TOP_K` |
| `.gitignore` | `.env`, `chroma_db/`, `__pycache__/`, `*.pyc`, `.venv/` |
| `config.py` | Load all env variables via `python-dotenv` |
| Data validation | Load and validate all 4 JSON files + 10 Markdown documents |

**Deliverables:**
- [x] Full folder structure created
- [x] `requirements.txt` written and dependencies installable
- [x] `.env` template and `.gitignore` in place
- [x] `config.py` loading all settings
- [x] All data files accessible and validated

---

## Phase 2 — RAG Pipeline (the backbone)

**Goal:** Build the retrieval-augmented generation pipeline that powers the Q&A feature.

| File | Responsibility |
|------|---------------|
| `rag/ingest.py` | Load JSON fields + Markdown content, chunk with `RecursiveCharacterTextSplitter` (~500 tokens, 50 overlap), attach metadata (source, type) |
| `rag/embeddings.py` | Configure `paraphrase-multilingual-MiniLM-L12-v2` — free, local, French-capable, 384 dimensions |
| `rag/vectorstore.py` | Initialize ChromaDB in persistent mode (`chroma_db/` directory), store chunks + vectors + metadata |
| `rag/retriever.py` | Cosine similarity search, return top-k chunks (k=5 default), optional metadata filtering |

**Deliverables:**
- [x] Documents ingested and chunked
- [x] Embeddings generated locally (no API cost)
- [x] ChromaDB populated and persisted to disk
- [x] Retriever returning relevant chunks for test queries

---

## Phase 3 — Business Modules

**Goal:** Implement the 5 core features — scoring, diagnostic, investor matching, grant matching, and RAG Q&A.

### 3.1 — Scoring de Fundability (`modules/scoring.py`)

- **Input:** User metrics (MRR, burn rate, churn, CAC, LTV, stage)
- **Data:** `metrics_reference.json` (primary) + `investors.json` (secondary)
- **Logic:**
  1. Compare each metric to stage-specific benchmarks (bad/ok/good/excellent)
  2. Compute weighted score /100 using `weight_in_scoring`
  3. Identify strengths and weaknesses
  4. Generate personalized action plan via LLM
- **Output:** Score /100, per-metric breakdown, action plan

### 3.2 — Diagnostic Financier (`modules/diagnostic.py`)

- **Input:** Individual KPIs from the user
- **Data:** `metrics_reference.json` (formulas, benchmarks, interpretation, improvement_tips)
- **Logic:** Analyze each KPI, compare to benchmarks, provide advice
- **Output:** Detailed analysis with improvement recommendations

### 3.3 — Matching Investisseurs (`modules/matching_investors.py`)

- **Input:** Startup profile (sector, stage, geography, metrics)
- **Data:** `investors.json` (38 profiles)
- **Logic:**
  1. Filter by `sectors`, `stages`, `geography`
  2. Filter by `ticket_min/max` if funding amount provided
  3. Compute matching score (number of satisfied criteria)
  4. Sort by relevance
- **Output:** Top 5 investors with details and specific criteria

### 3.4 — Matching Subventions (`modules/matching_grants.py`)

- **Input:** Startup profile (sector, stage, country, age)
- **Data:** `grants.json` (25 programs)
- **Logic:** Filter by `eligibility` (stages, sectors, country, max_age)
- **Output:** List of eligible grants with amounts and deadlines

### 3.5 — Q&A Conversationnel RAG (`modules/rag_qa.py`)

- **Input:** Free-form user question
- **Data:** `faq.json` + `fundraising_guide/*.md` + `regulations/*.md` (via ChromaDB)
- **Logic:**
  1. Embed the question
  2. Retrieve top-k similar chunks from ChromaDB
  3. Send chunks + question to LLM
  4. Generate answer in French
- **Output:** Contextual answer based on the knowledge base

**Deliverables:**
- [x] Scoring module returning score /100 with action plan
- [x] Diagnostic module analyzing KPIs with recommendations
- [x] Investor matching returning top 5 relevant investors
- [x] Grant matching returning eligible programs
- [x] RAG Q&A generating contextual French answers

---

## Phase 4 — Router / Orchestrator

**Goal:** Build the intent detection layer that routes user queries to the correct module.

| Detected Intent | Module Called | Keywords / Signals |
|----------------|-------------|-------------------|
| Scoring | `scoring.py` | "score", "fundability", "pret a lever", metrics provided |
| Diagnostic | `diagnostic.py` | "diagnostic", "analyser mes KPIs", "comment va ma startup" |
| Metrics | `router.py` (_explain_metrics) | "expliquer les métriques", "c'est quoi les KPI", "c'est quoi MRR" |
| Investors | `matching_investors.py` | "investisseur", "VC", "business angel", "qui peut investir" |
| Grants | `matching_grants.py` | "subvention", "aide", "programme", "financement public" |
| Greeting | `main.py` (_is_greeting) | "bonjour", "salut", "hello", "salam" (≤3 words) |
| General Q&A | `rag_qa.py` | Everything else (free-form questions) |

**Approach options:**
- **Keyword-based** — simple, fast, pattern matching
- **LLM-based** — more intelligent, asks the LLM to classify intent

**Deliverables:**
- [x] `router.py` correctly routing queries to all 5 modules + metrics explainer (keyword-based approach)
- [x] Fallback to RAG Q&A for unclassified queries
- [x] Greeting detection bypassing the router for casual messages

---

## Phase 4.5 — FastAPI Backend Server

**Goal:** Expose the router/orchestrator as an HTTP API for the Next.js frontend.

| File | Responsibility |
|------|---------------|
| `backend/app/main.py` | FastAPI app with `POST /api/chat` and `POST /api/chat/stream` endpoints, CORS, profile mapping, markdown response formatting, SSE streaming, greeting detection |
| `backend/app/source_urls.py` | Mapping of dataset filenames to real internet URLs for structured source attribution |
| `frontend/src/lib/api.ts` | Real `fetch()` calls to `http://localhost:8000/api/chat` and `/api/chat/stream` with SSE parsing |

### API Contract

- **Request:** `POST /api/chat` with `{message, profile, history}`
- **Response:** `{reply: "markdown string", sources: [{name, type, url}]}`
- **Request:** `POST /api/chat/stream` with `{message, profile, history}`
- **Response:** SSE stream with events: `sources` (JSON array), `token` (text chunk), `reply` (full text for non-QA), `done`
- Profile fields mapped: `secteur→sector`, `stade→stage`, `pays→country`, `mrr/burnRate/churn/cac/ltv→metrics`
- Response formatted as French markdown (tables, lists, emojis) per intent type
- Greeting messages (≤3 words matching common greetings) return a fixed French welcome without calling the router

### How to run

```bash
# Terminal 1 — Backend
uvicorn backend.app.main:app --reload --port 8000

# Terminal 2 — Frontend
cd frontend && npm run dev
```

**Deliverables:**
- [x] FastAPI server with CORS on port 8000
- [x] `POST /api/chat` endpoint calling `route()` and formatting markdown
- [x] `POST /api/chat/stream` endpoint with SSE streaming for real-time token delivery
- [x] Frontend `api.ts` using real `fetch()` and SSE stream parsing
- [x] Health check endpoint `GET /health`
- [x] Structured source attribution with clickable URLs (`source_urls.py`)
- [x] Greeting detection to bypass router for casual messages

---

## Phase 5 — Next.js Frontend

**Goal:** Build a user-friendly web interface for the chatbot using Next.js.

### Layout

| Section | Content |
|---------|---------|
| **Sidebar** | Draggable/resizable sidebar with startup profile form (sector, stage, country, metrics), conversation history with hover menu, new conversation button |
| **Main area** | Chat interface — message history (user + assistant), text input, formatted responses (scores, tables, lists), SSE streaming display |
| **State management** | Multiple conversations preserved in local storage, conversation switching |

### Components

| Component | File | Description |
|-----------|------|-------------|
| Chat Layout | `chat-layout.tsx` | Main layout orchestrating sidebar + chat panel |
| Chat Panel | `chat-panel.tsx` | Message display area with streaming support |
| Chat Input | `chat-input.tsx` | User message input |
| Message Bubble | `message-bubble.tsx` | Individual message rendering with markdown + sources |
| Sidebar | `sidebar.tsx` | Draggable sidebar with conversation list + hover menu |
| Profile Form | `profile-form.tsx` | Startup profile form (sector, stage, country, metrics) |
| Guided Tour | `guided-tour.tsx` | Interactive onboarding tour for first-time users (React Joyride) |
| Theme Toggle | `theme-toggle.tsx` | Dark/light mode toggle |
| Theme Provider | `theme-provider.tsx` | Theme context provider |
| Animated Grid | `animated-grid-pattern.tsx` | Decorative background pattern |
| UI Components | `ui/` | Reusable primitives (button, card, dialog, input, select, badge, etc.) |

**Deliverables:**
- [x] Draggable/resizable sidebar with conversation history and hover menu
- [x] Chat interface with SSE streaming, message history, and dark mode
- [x] Formatted display of scores, tables, and lists with markdown rendering
- [x] State management with React 19, multiple conversations in local storage
- [x] Interactive guided tour for first-time users
- [x] Structured source display with clickable URLs
- [x] Conversation title truncation (4 words) in sidebar

---

## Phase 6 — Tests + Polish

**Goal:** Validate all features, tune prompts, and ensure quality.

### Test Scenarios

| # | Scenario | Input | Expected Output |
|---|----------|-------|----------------|
| 1 | Scoring | "MRR: 8000, burn rate: 15000, churn: 5%, stade: seed" | Score ~58/100, improvement axes |
| 2 | Diagnostic | "CAC: 200, LTV: 400, churn: 8%" | "Ratio LTV/CAC=2 (faible), churn eleve..." |
| 3 | Matching | "Fintech, seed, Maroc, MRR 10K" | Top 5 relevant investors |
| 4 | Grants | "Startup edtech, 2 ans, Maroc" | List of eligible grants |
| 5 | Q&A | "Comment valoriser ma startup en pre-seed ?" | Answer based on guides |

**Deliverables:**
- [x] Unit tests for each module (`tests/test_scoring.py`, `test_diagnostic.py`, `test_matching_investors.py`, `test_matching_grants.py`, `test_router.py`, `test_rag.py`)
- [ ] Prompt tuning for French response quality
- [ ] End-to-end validation against all 5 scenarios
- [ ] Error handling for edge cases

---

## Tech Stack Summary

| Component | Technology |
|-----------|-----------|
| Backend | **Python 3.11+** |
| LLM | **OpenAI API** (GPT-4 / GPT-3.5-turbo) |
| Embeddings | **sentence-transformers** (`paraphrase-multilingual-MiniLM-L12-v2`) |
| Vector DB | **ChromaDB** (persistent) |
| Frontend | **Next.js** |
| RAG Pipeline | **LangChain** |
| Config | **python-dotenv** |

---

## Key Rules

1. **Language** — Code in English, prompts/responses/data in French
2. **No hallucination** — The chatbot only answers based on provided data (RAG), never invents
3. **Modular design** — Each module is independent and testable separately
4. **Error handling** — Graceful handling of missing or incomplete data
5. **Persistent ChromaDB** — No re-indexing on every launch
