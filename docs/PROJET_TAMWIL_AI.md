# Tamwil AI — Chatbot RAG de recommandation financière pour startups

## 1. Problématique

Les fondateurs de startups au Maroc et en Afrique francophone font face à un manque d'accès à l'information financière structurée : quel type de financement choisir ? Quels investisseurs cibler ? Suis-je prêt à lever des fonds ? Quelles aides existent pour moi ? Ces réponses sont dispersées entre des sites web, des PDFs, des réseaux informels, et souvent en anglais — inadaptées au contexte local.

## 2. Solution proposée

**Tamwil AI** est un chatbot intelligent basé sur la technique **RAG (Retrieval-Augmented Generation)** qui combine :
- Une **base de connaissances structurée** sur l'écosystème startup marocain/francophone
- Un **modèle de langage (LLM)** pour générer des réponses contextuelles et personnalisées

L'utilisateur décrit sa startup (secteur, stade, métriques financières) et le chatbot lui fournit des recommandations personnalisées.

## 3. Dataset constitué

Le dataset a été construit manuellement et contient **~521 KB de données de qualité** :

| Source | Format | Contenu | Volume |
|--------|--------|---------|--------|
| `investors.json` | JSON structuré | Profils d'investisseurs (VC, BA, accélérateurs, fonds publics) avec critères d'investissement, tickets, secteurs, géographies | **41 profils** |
| `grants.json` | JSON structuré | Programmes de subventions et aides (Maroc, France, International) avec critères d'éligibilité, montants, taux de succès | **25 programmes** |
| `metrics_reference.json` | JSON structuré | Définitions de KPIs startup avec formules, benchmarks par stade (bad/ok/good/excellent), et conseils d'amélioration | **18 métriques** |
| `faq.json` | JSON structuré | Questions/réponses sur la finance startup, classées par catégorie et difficulté | **54 Q&A** |
| `fundraising_guide/` | Markdown | Guides complets : types de financement, pitch deck, étapes de levée, term sheet, valorisation, erreurs courantes | **6 guides (~3 554 lignes)** |
| `regulations/` | Markdown | Réglementations : création d'entreprise, fintech, fiscalité, RGPD au Maroc | **4 documents (~1 817 lignes)** |

## 4. Fonctionnalités principales

### a) Scoring de "Fundability" (fonctionnalité phare)

**Source de données :** `metrics_reference.json` (principal) + `investors.json` (secondaire)

L'utilisateur saisit ses métriques (MRR, burn rate, churn, CAC, LTV...) et le système :
- Compare chaque métrique aux **benchmarks par stade** issus de `metrics_reference.json`
- Calcule un **score global de fundability** (ex: 65/100)
- Identifie les **points forts et faiblesses**
- Génère un **plan d'action** : "Avant de lever, améliore ton churn et atteins 10K€ MRR"

### b) Diagnostic financier

**Source de données :** `metrics_reference.json` (source unique — formules, benchmarks, interpretation, improvement_tips)

Analyse des KPIs de l'utilisateur avec comparaison sectorielle et recommandations.

### c) Matching investisseurs

**Source de données :** `investors.json` (source unique — 41 profils)

À partir du profil de la startup (secteur, stade, géographie, métriques), le système :
- Filtre les investisseurs compatibles (filtrage par `sectors`, `stage`, `geography`, `ticket_min/max`, `criteria`)
- Classe par pertinence (score de matching)
- Affiche les critères spécifiques de chaque investisseur
- Ex: "Tu es une fintech seed au Maroc → voici 5 investisseurs pertinents"

### d) Matching subventions/aides

**Source de données :** `grants.json` (source unique — 25 programmes, filtrage par `eligibility`, `country`, `stage`)

Recommandation de subventions éligibles selon le profil (25 programmes disponibles).

### e) Q&A conversationnel via RAG

**Sources de données :** `faq.json` (54 Q&A) + `fundraising_guide/*.md` (6 guides) + `regulations/*.md` (4 docs)

Le chatbot répond aux questions libres en s'appuyant sur toute la base de connaissances :
- "C'est quoi la différence entre pré-money et post-money ?"
- "Comment préparer mon pitch deck ?"
- "Quelles sont les obligations RGPD ?"

## 5. Mapping Dataset → Fonctionnalités

```
investors.json ──────────→ Matching investisseurs + Scoring fundability
grants.json ─────────────→ Matching subventions
metrics_reference.json ──→ Scoring fundability + Diagnostic financier
faq.json ────────────────→ Q&A conversationnel (RAG)
fundraising_guide/*.md ──→ Q&A conversationnel (RAG)
regulations/*.md ────────→ Q&A conversationnel (RAG)
```

| Fonctionnalité | JSON principal | JSON secondaire | Markdown (RAG) |
|---------------|---------------|----------------|----------------|
| a) Scoring | `metrics_reference.json` | `investors.json` | — |
| b) Diagnostic | `metrics_reference.json` | — | — |
| c) Matching investisseurs | `investors.json` | — | — |
| d) Matching subventions | `grants.json` | — | — |
| e) Q&A RAG | `faq.json` | — | guides + regulations |

## 6. Cas d'usage supplémentaires (supportés par le dataset)

| # | Cas d'usage | Données utilisées | Exemple d'interaction |
|---|------------|-------------------|----------------------|
| 6 | Simulateur de runway | `metrics_reference.json` | "Burn rate 20K€, cash 80K€ → il te reste 4 mois" |
| 7 | Recommandation type de financement | `types_financement.md` | "Pré-seed sans revenu → love money ou subventions" |
| 8 | Estimation de valorisation | `valorisation.md` | "SaaS seed, MRR 10K€ → valorisation 1.2M-2.4M€" |
| 9 | Aide pitch deck financier | `pitch_deck.md` | "Voici les 4 slides financières à inclure" |
| 10 | Guide réglementaire | `regulations/` | "Fintech → agrément BAM, 5M MAD capital minimum" |
| 11 | Calcul de dilution | `term_sheet.md` + `valorisation.md` | "1M€ levés à 4M€ pré-money → 20% de dilution" |
| 12 | Erreurs à éviter | `erreurs_courantes.md` | "Top 3 erreurs : lever trop tôt, mauvaise valorisation..." |

### Priorisation

**Tier 1 — Fonctionnalités phares (à démontrer en soutenance) :**
1. Scoring de fundability
2. Diagnostic financier
3. Matching investisseurs
4. Matching subventions/programmes
5. Q&A conversationnel (RAG)

**Tier 2 — Fonctionnalités complémentaires :**
6. Simulateur de runway
7. Recommandation type de financement
8. Estimation de valorisation

**Tier 3 — Bonus si le temps le permet :**
9. Aide pitch deck financier
10. Calcul de dilution
11. Guide réglementaire

## 7. Architecture technique

```
┌─────────────────────────────────────────────────┐
│                 Interface Web                    │
│      (Next.js 16 + React 19 + Tailwind CSS 4)   │
└──────────────────┬──────────────────────────────┘
                   │  SSE streaming / REST
┌──────────────────▼──────────────────────────────┐
│           Serveur API (FastAPI + uvicorn)         │
│   POST /api/chat  ·  POST /api/chat/stream       │
│   Greeting detection · Source URL resolution      │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│              Orchestrateur / Router              │
│   (détecte l'intention : scoring, diagnostic,   │
│    metrics, matching, subventions, Q&A)          │
└──┬───────┬───────┬───────┬───────┬──────────────┘
   │       │       │       │       │
   ▼       ▼       ▼       ▼       ▼
┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
│Score ││Diag. ││Match ││Grant ││ RAG  │
│Fund. ││Finan.││Invest││Match ││ Q&A  │
└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘
   │       │       │       │       │
   ▼       ▼       ▼       ▼       ▼
┌─────────────────────────────────────────────────┐
│              Base de connaissances               │
│  ┌─────────────┐  ┌──────────────────────────┐  │
│  │ ChromaDB    │  │ JSON structuré           │  │
│  │ (embeddings │  │ (investors, grants,      │  │
│  │  guides,    │  │  metrics, FAQ)           │  │
│  │  FAQ, regs) │  │                          │  │
│  └─────────────┘  └──────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

**Approche hybride :**
- **RAG (vectoriel)** pour les questions libres → chercher les passages pertinents dans les guides/FAQ/réglementations, puis le LLM génère une réponse contextualisée
- **Rule-based + LLM** pour le scoring et le matching → filtrage algorithmique sur les critères structurés (JSON), puis le LLM formule la recommandation

## 8. Stack technique

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| Backend | **Python 3.11+** | Écosystème IA/NLP riche |
| Serveur API | **FastAPI + uvicorn** | Framework Python moderne, asynchrone, SSE streaming |
| LLM | **OpenAI API** (GPT-3.5-turbo / GPT-4) | Qualité de génération en français |
| Embeddings | **sentence-transformers** (`paraphrase-multilingual-MiniLM-L12-v2`) | Gratuit, local, supporte le français, 384 dimensions |
| Base vectorielle | **ChromaDB** | Simple, léger, persistant, parfait pour un petit dataset |
| Interface | **Next.js 16 + React 19 + Tailwind CSS 4** | Application web moderne avec SSE streaming et dark mode |
| Pipeline RAG | **LangChain** | Outils de découpage et orchestration RAG |
| Config | **python-dotenv** | Gestion sécurisée des variables d'environnement |

## 9. Méthodologie RAG

1. **Ingestion** : charger les JSON et Markdown
2. **Chunking** : découper les documents en passages (~500 tokens chacun)
3. **Embedding** : vectoriser chaque chunk avec un modèle multilingue
4. **Indexation** : stocker dans ChromaDB
5. **Retrieval** : à chaque question, chercher les k chunks les plus similaires
6. **Generation** : envoyer les chunks + la question au LLM pour générer la réponse

## 10. Cas d'usage démontrables (soutenance)

| Scénario | Entrée utilisateur | Sortie attendue |
|----------|-------------------|-----------------|
| Scoring | "MRR: 8000€, burn rate: 15000€, churn: 5%, stade: seed" | Score 58/100, axes d'amélioration, plan d'action |
| Diagnostic | "CAC: 200€, LTV: 400€, churn: 8%" | "Ratio LTV/CAC=2 (faible), churn élevé, voici comment améliorer..." |
| Matching | "Fintech, seed, Maroc, MRR 10K€" | Top 5 investisseurs avec critères et contacts |
| Subventions | "Startup edtech, 2 ans, Maroc" | Liste des aides éligibles avec montants et deadlines |
| Q&A | "Comment valoriser ma startup en pré-seed ?" | Réponse détaillée basée sur les guides |

## 11. Points forts du projet (PFA)

- **Combine plusieurs domaines** : NLP, systèmes de recommandation, finance, données structurées
- **RAG = technique très actuelle** (2024-2026), demandée par l'industrie
- **Dataset original** : construit manuellement, adapté au contexte marocain
- **Résultat concret et démontrable** : un chatbot fonctionnel avec interface web
- **Valeur réelle** : utile pour de vrais entrepreneurs
