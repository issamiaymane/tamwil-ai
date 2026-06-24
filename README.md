# Tamwil AI

> AI-powered financing recommendation platform for startups using RAG + LLM. **[Academic]**

## Overview

Tamwil AI is a RAG-based chatbot that helps Moroccan and Francophone startup founders navigate financing options. It combines a curated knowledge base (investors, grants, regulations, FAQs) with an LLM to deliver personalized recommendations: investor matching, fundability scoring, grant eligibility, and free Q&A.

## Tech Stack

- **Backend**: Python, FastAPI, LangChain, ChromaDB, OpenAI
- **Frontend**: Next.js, TypeScript, Tailwind CSS
- **Testing**: pytest

## Project Structure

```
code/
├── backend/        # FastAPI app with RAG pipeline, routers, modules
├── frontend/       # Next.js UI
├── tests/          # pytest test suite
└── requirements.txt
docs/
├── dataset/        # Knowledge base: investors, grants, metrics, FAQs, guides
├── chroma_db/      # Vector store (local)
└── *.md            # Design docs, dataset report, development plan
```

## Setup & Run

```bash
# Backend
cd code
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp env.example .env  # fill in your API keys
uvicorn backend.app.main:app --reload

# Frontend
cd code/frontend
npm install
npm run dev
```

## Features

- **Fundability scoring** — inputs startup metrics, outputs a fundability score with action plan
- **Investor matching** — filters 41 investor profiles by sector, stage, geography, ticket size
- **Grant matching** — recommends eligible grants from 25 programs
- **Financial diagnostic** — KPI analysis with benchmarks by stage
- **Conversational Q&A** — RAG over fundraising guides, regulations, and FAQ
