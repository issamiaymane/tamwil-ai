# 🤖 Tamwil AI — Project Brief for AI Agent

> **Donne ce fichier à ton agent AI (Copilot, Cursor, Claude Code, etc.) pour qu'il comprenne ton projet.**

---

## 🎯 Objectif du Projet

Tamwil AI est un **chatbot intelligent RAG** (Retrieval-Augmented Generation) qui aide les fondateurs de startups au Maroc et en Afrique francophone à :
- Évaluer leur "fundability" (score de préparation à la levée de fonds)
- Trouver les bons investisseurs
- Identifier les subventions/aides disponibles
- Obtenir des diagnostics financiers
- Répondre à des questions sur la finance startup via RAG

La langue principale est le **français**.

---

## 🏗️ Architecture Technique

### Approche Hybride
- **RAG (vectoriel)** → pour les questions libres (Q&A conversationnel)
- **Rule-based + LLM** → pour le scoring et le matching (filtrage algorithmique sur JSON, puis le LLM formule la réponse)

### Stack Technique

| Composant | Technologie |
|-----------|-------------|
| Backend | **Python 3.11+** |
| LLM | **OpenAI API** (GPT-4 ou GPT-3.5-turbo) |
| Embeddings | **sentence-transformers** (`paraphrase-multilingual-MiniLM-L12-v2`) |
| Base vectorielle | **ChromaDB** |
| Interface | **Next.js** |
| Pipeline RAG | **LangChain** |
| Config | **python-dotenv** |

---

## 📁 Structure du Projet

```
tamwil-ai/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # Point d'entrée principal (FastAPI ou fonction main)
│   │   ├── config.py               # Chargement des clés API et paramètres (.env)
│   │   ├── router.py               # Détection d'intention / Orchestrateur
│   │   │                           # → Route vers le bon module selon la requête
│   │   ├── modules/
│   │   │   ├── __init__.py
│   │   │   ├── scoring.py          # Scoring de fundability (compare métriques aux benchmarks)
│   │   │   ├── diagnostic.py       # Diagnostic financier (analyse KPIs individuels)
│   │   │   ├── matching_investors.py  # Matching investisseurs (filtrage + ranking)
│   │   │   ├── matching_grants.py     # Matching subventions (filtrage par éligibilité)
│   │   │   └── rag_qa.py           # Pipeline RAG Q&A (retrieval + génération LLM)
│   │   ├── rag/
│   │   │   ├── __init__.py
│   │   │   ├── ingest.py           # Chargement et chunking des documents
│   │   │   ├── embeddings.py       # Configuration sentence-transformers
│   │   │   ├── vectorstore.py      # Initialisation et gestion de ChromaDB
│   │   │   └── retriever.py        # Recherche par similarité (top-k)
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── prompts.py          # Templates de prompts pour le LLM (en français)
│   │       └── helpers.py          # Fonctions utilitaires
│   └── .env                        # Clés API (OPENAI_API_KEY, etc.)
│
├── dataset/
│   ├── investors/
│   │   └── investors.json              # 41 profils d'investisseurs
│   ├── grants/
│   │   └── grants.json                 # 25 programmes de subventions
│   ├── metrics/
│   │   └── metrics_reference.json      # 18 métriques/KPIs avec benchmarks
│   ├── faq/
│   │   └── faq.json                    # 54 questions/réponses
│   ├── fundraising_guide/
│   │   ├── types_financement.md    # Guide sur les types de financement
│   │   ├── pitch_deck.md           # Guide pitch deck
│   │   ├── etapes_levee.md         # Étapes d'une levée de fonds
│   │   ├── term_sheet.md           # Comprendre le term sheet
│   │   ├── valorisation.md         # Méthodes de valorisation
│   │   └── erreurs_courantes.md    # Erreurs courantes à éviter
│   └── regulations/
│       ├── creation_entreprise_maroc.md  # Création d'entreprise au Maroc
│       ├── fintech_maroc.md           # Réglementation fintech
│       ├── fiscalite_startup.md       # Fiscalité des startups
│       └── rgpd.md           # RGPD / protection des données au Maroc
│
├── frontend/                       # Next.js frontend application
│
├── chroma_db/                      # Stockage ChromaDB (gitignored)
├── tests/
│   ├── test_scoring.py
│   ├── test_diagnostic.py
│   ├── test_matching_investors.py
│   ├── test_matching_grants.py
│   ├── test_router.py
│   └── test_rag.py
├── .gitignore
├── README.md

```

---

## 📊 Dataset — Structure des Données

### 1. `dataset/investors/investors.json` — 41 profils
```json
{
  "investors": [
    {
      "id": "inv_001",
      "name": "Nom du VC/BA",
      "type": "VC | BA | accelerator | public_fund",
      "sectors": ["fintech", "healthtech", "edtech"],
      "stages": ["pre-seed", "seed", "series-a"],
      "geography": ["Maroc", "Afrique francophone"],
      "ticket_min": 50000,
      "ticket_max": 500000,
      "currency": "EUR",
      "criteria": ["MRR > 5000€", "Traction prouvée", "Équipe tech solide"],
      "contact": "email@example.com",
      "website": "https://example.com",
      "description": "Description du fonds..."
    }
  ]
}
```

### 2. `dataset/grants/grants.json` — 25 programmes
```json
{
  "grants": [
    {
      "id": "grant_001",
      "name": "Nom du programme",
      "organization": "Organisme",
      "country": "Maroc",
      "type": "subvention | prêt_honneur | concours | accompagnement",
      "amount_min": 10000,
      "amount_max": 100000,
      "currency": "MAD",
      "eligibility": {
        "stages": ["pre-seed", "seed"],
        "sectors": ["all"],
        "max_age_years": 3,
        "country_required": "Maroc"
      },
      "success_rate": 0.25,
      "deadline": "2025-12-31",
      "description": "Description du programme...",
      "url": "https://example.com"
    }
  ]
}
```

### 3. `dataset/metrics/metrics_reference.json` — 18 métriques
```json
{
  "metrics": [
    {
      "id": "mrr",
      "name": "Monthly Recurring Revenue",
      "category": "revenue",
      "formula": "Somme des revenus récurrents mensuels",
      "unit": "EUR",
      "benchmarks": {
        "pre-seed": { "bad": 0, "ok": 1000, "good": 3000, "excellent": 5000 },
        "seed": { "bad": 0, "ok": 5000, "good": 10000, "excellent": 25000 },
        "series-a": { "bad": 10000, "ok": 30000, "good": 80000, "excellent": 150000 }
      },
      "weight_in_scoring": 0.2,
      "interpretation": "Mesure la traction commerciale récurrente",
      "improvement_tips": [
        "Convertir les clients one-shot en abonnements",
        "Augmenter le panier moyen via l'upsell",
        "Réduire le churn pour stabiliser le MRR"
      ]
    }
  ]
}
```

### 4. `dataset/faq/faq.json` — 54 Q&A
```json
{
  "faq": [
    {
      "id": "faq_001",
      "question": "C'est quoi la différence entre pré-money et post-money ?",
      "answer": "La valorisation pré-money est la valeur de l'entreprise avant l'investissement...",
      "category": "valorisation",
      "difficulty": "débutant",
      "related": ["faq_015", "faq_022"]
    }
  ]
}
```

### 5. `dataset/fundraising_guide/*.md` — 6 guides Markdown

Fichiers Markdown longs (~500 lignes chacun) couvrant en détail les sujets de levée de fonds. Ces fichiers sont découpés en chunks, vectorisés, et stockés dans ChromaDB pour le RAG.

### 6. `dataset/regulations/*.md` — 4 documents Markdown

Documents réglementaires sur le contexte juridique marocain. Même traitement RAG que les guides.

---

## 🔧 Fonctionnalités à Implémenter

### Fonctionnalité 1 : Scoring de Fundability (`modules/scoring.py`)
- **Input** : Métriques utilisateur (MRR, burn rate, churn, CAC, LTV, stade)
- **Données** : `metrics_reference.json` (principal) + `investors.json` (secondaire)
- **Logique** :
  1. Comparer chaque métrique aux benchmarks du stade correspondant
  2. Calculer un score pondéré /100 (utiliser `weight_in_scoring`)
  3. Identifier forces et faiblesses
  4. Générer un plan d'action via le LLM
- **Output** : Score /100, détail par métrique, plan d'action personnalisé

### Fonctionnalité 2 : Diagnostic Financier (`modules/diagnostic.py`)
- **Input** : KPIs individuels de l'utilisateur
- **Données** : `metrics_reference.json` (formules, benchmarks, interpretation, improvement_tips)
- **Logique** : Analyser chaque KPI, comparer aux benchmarks, donner des conseils
- **Output** : Analyse détaillée avec recommandations d'amélioration

### Fonctionnalité 3 : Matching Investisseurs (`modules/matching_investors.py`)
- **Input** : Profil startup (secteur, stade, géographie, métriques)
- **Données** : `investors.json` (41 profils)
- **Logique** :
  1. Filtrer par `sectors`, `stages`, `geography`
  2. Filtrer par `ticket_min/max` si montant recherché fourni
  3. Calculer un score de matching (nombre de critères satisfaits)
  4. Trier par pertinence
- **Output** : Top 5 investisseurs avec détails et critères spécifiques

### Fonctionnalité 4 : Matching Subventions (`modules/matching_grants.py`)
- **Input** : Profil startup (secteur, stade, pays, ancienneté)
- **Données** : `grants.json` (25 programmes)
- **Logique** : Filtrer par `eligibility` (stages, sectors, country, max_age)
- **Output** : Liste des aides éligibles avec montants et deadlines

### Fonctionnalité 5 : Q&A Conversationnel RAG (`modules/rag_qa.py`)
- **Input** : Question libre de l'utilisateur
- **Données** : `faq.json` + `fundraising_guide/*.md` + `regulations/*.md` (via ChromaDB)
- **Logique** :
  1. Embedding de la question
  2. Recherche top-k chunks similaires dans ChromaDB
  3. Envoi des chunks + question au LLM
  4. Génération de la réponse en français
- **Output** : Réponse contextuelle basée sur la base de connaissances

---

## 🔀 Orchestrateur / Router (`router.py`)

Le router détecte l'intention de l'utilisateur et dirige vers le bon module :

| Intention détectée | Module appelé | Mots-clés / Signaux |
|-------------------|---------------|---------------------|
| Scoring | `scoring.py` | "score", "fundability", "prêt à lever", métriques fournies |
| Diagnostic | `diagnostic.py` | "diagnostic", "analyser mes KPIs", "comment va ma startup" |
| Investisseurs | `matching_investors.py` | "investisseur", "VC", "business angel", "qui peut investir" |
| Subventions | `matching_grants.py` | "subvention", "aide", "programme", "financement public" |
| Q&A général | `rag_qa.py` | Tout le reste (questions libres) |

L'approche peut être :
- **Keyword-based** (simple, rapide) : détecter des mots-clés
- **LLM-based** (plus intelligent) : demander au LLM de classifier l'intention

---

## 🔄 Pipeline RAG — Détail Technique

### Ingestion (`rag/ingest.py`)
```
1. Charger tous les fichiers :
   - JSON → extraire les champs textuels pertinents
   - Markdown → charger le contenu brut
2. Chunking avec RecursiveCharacterTextSplitter :
   - chunk_size = 500 tokens
   - chunk_overlap = 50 tokens
   - Ajouter des métadonnées (source, type)
```

### Embeddings (`rag/embeddings.py`)
```
- Modèle : paraphrase-multilingual-MiniLM-L12-v2
- Gratuit et local (pas besoin d'API)
- Supporte le français
- Dimension : 384
```

### Vector Store (`rag/vectorstore.py`)
```
- ChromaDB en mode persistant (dossier chroma_db/)
- Collection unique ou par type de document
- Stocke : texte du chunk + vecteur + métadonnées
```

### Retriever (`rag/retriever.py`)
```
- Recherche par cosine similarity
- Retourne top-k chunks (k=5 par défaut)
- Filtrage optionnel par métadonnées (source, type)
```

---

## 🖥️ Frontend Next.js (`frontend/`)

### Layout souhaité :
- **Sidebar** : Formulaire pour saisir le profil startup
  - Secteur (dropdown : fintech, healthtech, edtech, etc.)
  - Stade (dropdown : pre-seed, seed, series-a)
  - Pays (dropdown : Maroc, France, etc.)
  - Métriques (inputs numériques : MRR, burn rate, churn, CAC, LTV)
- **Zone principale** : Chat conversationnel
  - Historique des messages (user + assistant)
  - Input texte pour les questions
  - Affichage formaté des réponses (scores, tableaux, listes)
- **State management** : Conserver l'historique de conversation

---

## 📦 Dépendances (`requirements.txt`)

```
langchain>=0.1.0
langchain-community>=0.0.10
langchain-openai>=0.0.5
openai>=1.0.0
tiktoken>=0.5.0
sentence-transformers>=2.2.0
torch>=2.10.0
chromadb>=0.4.0
python-dotenv>=1.0.0
fastapi>=0.100.0
uvicorn>=0.20.0
pytest>=7.0.0
```

---

## 🔐 Variables d'environnement (`.env`)

```
OPENAI_API_KEY=sk-your-key-here
CHROMA_PERSIST_DIR=./chroma_db
EMBEDDING_MODEL=paraphrase-multilingual-MiniLM-L12-v2
LLM_MODEL=gpt-3.5-turbo
CHUNK_SIZE=500
CHUNK_OVERLAP=50
TOP_K=5
```

---

## ✅ Scénarios de Test (pour validation)

| # | Scénario | Input | Output attendu |
|---|----------|-------|----------------|
| 1 | Scoring | "MRR: 8000€, burn rate: 15000€, churn: 5%, stade: seed" | Score ~58/100, axes d'amélioration |
| 2 | Diagnostic | "CAC: 200€, LTV: 400€, churn: 8%" | "Ratio LTV/CAC=2 (faible), churn élevé..." |
| 3 | Matching | "Fintech, seed, Maroc, MRR 10K€" | Top 5 investisseurs pertinents |
| 4 | Subventions | "Startup edtech, 2 ans, Maroc" | Liste des aides éligibles |
| 5 | Q&A | "Comment valoriser ma startup en pré-seed ?" | Réponse basée sur les guides |

---

## 📋 Ordre de Développement

1. **Phase 1** : Structure + data layer + config
2. **Phase 2** : Pipeline RAG (ingest → embed → store → retrieve → generate)
3. **Phase 3** : Modules métier (scoring, diagnostic, matching)
4. **Phase 4** : Router / orchestrateur
5. **Phase 5** : Frontend Next.js
6. **Phase 6** : Tests + polish + prompts tuning

---

## ⚠️ Règles Importantes pour l'Agent AI

1. **Langue** : Tout le code est en anglais, mais les prompts LLM, les réponses utilisateur, et les données sont en **français**
2. **Pas de hallucination** : Le chatbot ne doit répondre que sur la base des données fournies (RAG), jamais inventer
3. **Modularité** : Chaque module est indépendant et testable séparément
4. **Gestion d'erreurs** : Toujours gérer les cas où les données sont manquantes ou insuffisantes
5. **Performance** : ChromaDB doit être en mode persistant pour ne pas réindexer à chaque lancement