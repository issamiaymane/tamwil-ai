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
| Investors | `matching_investors.py` | "investisseur", "VC", "business angel", "qui peut investir" |
| Grants | `matching_grants.py` | "subvention", "aide", "programme", "financement public" |
| General Q&A | `rag_qa.py` | Everything else (free-form questions) |

**Approach options:**
- **Keyword-based** — simple, fast, pattern matching
- **LLM-based** — more intelligent, asks the LLM to classify intent

**Deliverables:**
- [x] `router.py` correctly routing queries to all 5 modules (keyword-based approach)
- [x] Fallback to RAG Q&A for unclassified queries

---

## Phase 4.5 — FastAPI Backend Server

**Goal:** Expose the router/orchestrator as an HTTP API for the Next.js frontend.

| File | Responsibility |
|------|---------------|
| `backend/app/main.py` | FastAPI app with `POST /api/chat` endpoint, CORS, profile mapping, markdown response formatting |
| `frontend/src/lib/api.ts` | Real `fetch()` call to `http://localhost:8000/api/chat` (replaces mock) |

### API Contract

- **Request:** `POST /api/chat` with `{message, profile, history}`
- **Response:** `{reply: "markdown string"}`
- Profile fields mapped: `secteur→sector`, `stade→stage`, `pays→country`, `mrr/burnRate/churn/cac/ltv→metrics`
- Response formatted as French markdown (tables, lists, emojis) per intent type

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
- [x] Frontend `api.ts` using real `fetch()` instead of mocks
- [x] Health check endpoint `GET /health`

---

## Phase 5 — Next.js Frontend

**Goal:** Build a user-friendly web interface for the chatbot using Next.js.

### Layout

| Section | Content |
|---------|---------|
| **Sidebar** | Startup profile form — sector (dropdown), stage (dropdown), country (dropdown), metrics (numeric inputs: MRR, burn rate, churn, CAC, LTV) |
| **Main area** | Chat interface — message history (user + assistant), text input, formatted responses (scores, tables, lists) |
| **State management** | Conversation history preserved across interactions |

**Deliverables:**
- [x] Sidebar with startup profile form and conversation history
- [x] Chat interface with message history and dark mode
- [x] Formatted display of scores, tables, and lists
- [x] State management with React 19

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
