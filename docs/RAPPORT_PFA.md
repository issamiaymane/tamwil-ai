# RAPPORT DE PROJET DE FIN D'ANNÉE (PFA)

---

## PAGE DE GARDE

---

**École Nationale Supérieure d'Arts et Métiers — ENSAM Rabat**

**Filière : Ingénierie en Data Science et Intelligence Artificielle**

**2ème Année**

---

### Projet de Fin d'Année

**Année Universitaire : 2025 – 2026**

---

### Tamwil AI — Chatbot RAG de Recommandation Financière pour Startups

---

**Réalisé par :**
- Aymane ISSAMI
- Houssam KICHCHOU

**Encadré par :**
- Mme Hafsa KHIYAT

**Professeur responsable :**
- Mme Amal TMIRI

---

**Soutenu le : [Date de soutenance]**

---
---

## REMERCIEMENTS

Nous tenons à exprimer notre profonde gratitude à notre encadrante **Mme Hafsa KHIYAT** pour ses conseils précieux, son suivi rigoureux et son accompagnement tout au long de ce projet.

Nous remercions également **Mme Amal TMIRI**, professeur responsable, ainsi que l'ensemble du corps professoral de l'**École Nationale Supérieure d'Arts et Métiers de Rabat (ENSAM)** pour la formation de qualité qui nous a permis d'acquérir les compétences nécessaires à la réalisation de ce travail.

Nos remerciements vont aussi à nos familles et proches pour leur soutien moral et leurs encouragements constants.

Enfin, nous remercions toutes les personnes qui, de près ou de loin, ont contribué à l'aboutissement de ce projet.

---
---

## RÉSUMÉ

Les fondateurs de startups au Maroc et en Afrique francophone font face à un manque criant d'accès à l'information financière structurée. Les réponses à des questions essentielles — quel type de financement choisir, quels investisseurs cibler, suis-je prêt à lever des fonds — sont dispersées entre sites web, documents PDF et réseaux informels, souvent en anglais et inadaptées au contexte local.

**Tamwil AI** est un chatbot intelligent basé sur la technique **RAG (Retrieval-Augmented Generation)** qui combine une base de connaissances structurée sur l'écosystème startup marocain et francophone avec un modèle de langage (LLM) pour générer des réponses contextuelles et personnalisées. Le système offre six fonctionnalités principales : le scoring de « fundability » (évaluation de la préparation à la levée de fonds), le diagnostic financier, le matching avec des investisseurs, la recommandation de subventions, l'explication des métriques financières, et un Q&A conversationnel alimenté par RAG.

Le projet repose sur une architecture hybride combinant un pipeline RAG vectoriel (pour les questions libres) et un système rule-based assisté par LLM (pour le scoring et le matching algorithmique). La stack technique inclut Python/FastAPI pour le backend, LangChain, ChromaDB, sentence-transformers et l'API OpenAI pour le pipeline IA, et Next.js/React 19 avec Tailwind CSS 4 pour l'interface utilisateur.

**Mots-clés :** RAG, LLM, Chatbot, Finance startup, ChromaDB, LangChain, Embeddings, NLP, FastAPI, Next.js, Maroc

---

## ABSTRACT

Startup founders in Morocco and French-speaking Africa face a significant lack of access to structured financial information. Answers to essential questions — which type of financing to choose, which investors to target, whether they are ready to raise funds — are scattered across websites, PDFs, and informal networks, often in English and not adapted to the local context.

**Tamwil AI** is an intelligent chatbot based on the **RAG (Retrieval-Augmented Generation)** technique that combines a structured knowledge base on the Moroccan and Francophone startup ecosystem with a large language model (LLM) to generate contextual and personalized responses. The system provides six core features: fundability scoring, financial diagnostics, investor matching, grant recommendations, financial metrics explanation, and a RAG-powered conversational Q&A.

The project relies on a hybrid architecture combining a vector-based RAG pipeline (for free-form questions) with a rule-based system assisted by an LLM (for algorithmic scoring and matching). The tech stack includes Python/FastAPI for the backend, LangChain, ChromaDB, sentence-transformers and the OpenAI API for the AI pipeline, and Next.js/React 19 with Tailwind CSS 4 for the user interface.

**Keywords:** RAG, LLM, Chatbot, Startup Finance, ChromaDB, LangChain, Embeddings, NLP, FastAPI, Next.js, Morocco

---
---

## TABLE DES MATIÈRES

- Introduction Générale
- Chapitre 1 : Étude de l'Existant et Cadre Théorique
  - 1.1 Contexte général
  - 1.2 État de l'art des chatbots IA
  - 1.3 La technique RAG (Retrieval-Augmented Generation)
  - 1.4 Comparaison avec les solutions existantes
  - 1.5 Justification de l'approche hybride
- Chapitre 2 : Conception et Architecture
  - 2.1 Architecture globale du système
  - 2.2 Description des modules fonctionnels
  - 2.3 Modèle de données
  - 2.4 Pipeline RAG détaillé
  - 2.5 Mapping Dataset → Fonctionnalités
- Chapitre 3 : Réalisation et Implémentation
  - 3.1 Environnement de développement
  - 3.2 Stack technique
  - 3.3 Constitution du dataset
  - 3.4 Implémentation du pipeline RAG
  - 3.5 Implémentation des modules métier
  - 3.6 Implémentation du backend FastAPI
  - 3.7 Implémentation de l'interface utilisateur
  - 3.8 Structure du projet
- Chapitre 4 : Tests et Résultats
  - 4.1 Scénarios de test
  - 4.2 Tests du pipeline RAG
  - 4.3 Tests unitaires
  - 4.4 Discussion et analyse
- Conclusion Générale et Perspectives
- Bibliographie et Webographie
- Annexes

---
---

## INTRODUCTION GÉNÉRALE

### Contexte

L'écosystème des startups au Maroc et en Afrique francophone connaît une croissance remarquable ces dernières années. Selon les rapports de Partech Africa et de la Banque Mondiale, le financement des startups africaines a atteint des niveaux records, avec une diversification des sources de financement allant du capital-risque aux subventions publiques, en passant par les accélérateurs et les business angels.

Cependant, malgré cette dynamique, les fondateurs de startups font face à un défi majeur : **le manque d'accès à l'information financière structurée et adaptée au contexte local**. Les questions essentielles qu'un entrepreneur se pose — « Quel type de financement est adapté à mon stade ? », « Quels investisseurs ciblent mon secteur au Maroc ? », « Suis-je prêt à lever des fonds ? », « Quelles aides publiques existent pour moi ? » — n'ont pas de réponse centralisée et accessible.

Ces informations sont aujourd'hui :
- **Dispersées** entre des sites web, des rapports PDF, des réseaux informels et des événements
- **Souvent en anglais**, inadaptées au cadre juridique et fiscal marocain/francophone
- **Non structurées**, rendant difficile une analyse comparative ou personnalisée
- **Peu accessibles** aux entrepreneurs en dehors des grands centres urbains

### Problématique

Comment concevoir un système intelligent capable de centraliser, structurer et personnaliser l'accès à l'information financière pour les startups au Maroc et en Afrique francophone, tout en s'appuyant sur les avancées récentes en intelligence artificielle et en traitement du langage naturel ?

### Objectif du projet

Le projet **Tamwil AI** vise à développer un chatbot intelligent basé sur la technique RAG (Retrieval-Augmented Generation) qui :
1. **Centralise** une base de connaissances structurée sur l'écosystème startup marocain et francophone
2. **Évalue** la préparation d'une startup à la levée de fonds (scoring de fundability)
3. **Recommande** les investisseurs et subventions les plus pertinents selon le profil de la startup
4. **Diagnostique** la santé financière d'une startup à partir de ses KPIs
5. **Répond** aux questions libres sur la finance startup en s'appuyant sur des données fiables
6. **Communique** en français, la langue principale des utilisateurs cibles

### Plan du rapport

Le présent rapport est structuré en quatre chapitres :
- **Chapitre 1** présente l'étude de l'existant, le cadre théorique et la justification de l'approche choisie
- **Chapitre 2** détaille la conception et l'architecture du système
- **Chapitre 3** décrit la réalisation technique et l'implémentation
- **Chapitre 4** expose les tests réalisés et les résultats obtenus

Nous conclurons par un bilan du projet et les perspectives d'amélioration futures.

---
---

## CHAPITRE 1 : ÉTUDE DE L'EXISTANT ET CADRE THÉORIQUE

### 1.1 Contexte général

Le financement des startups constitue un enjeu crucial pour le développement économique du Maroc et de l'Afrique francophone. L'écosystème comprend une variété d'acteurs :

- **Les fonds de capital-risque (VC)** : investissements en equity dans des startups à fort potentiel de croissance
- **Les business angels (BA)** : investisseurs individuels apportant capital et mentorat
- **Les accélérateurs et incubateurs** : programmes d'accompagnement avec financement initial
- **Les fonds publics** : aides gouvernementales (Tamwilcom, Maroc PME, etc.)
- **Les subventions et concours** : financements non dilutifs pour les jeunes entreprises

Malgré la diversité de ces acteurs, l'information reste fragmentée. Un fondateur de startup doit naviguer entre des dizaines de sources pour trouver les informations pertinentes à sa situation spécifique.

### 1.2 État de l'art des chatbots IA

L'évolution des chatbots a connu plusieurs phases majeures :

**Chatbots à règles (Rule-based)** : Les premières générations de chatbots fonctionnaient sur des arbres de décision et des mots-clés prédéfinis. Simples mais limités, ils ne pouvaient traiter que des scénarios anticipés par les développeurs.

**Chatbots basés sur le Machine Learning** : L'utilisation de modèles de classification (NLU — Natural Language Understanding) a permis de mieux comprendre les intentions des utilisateurs. Des frameworks comme Rasa ou Dialogflow ont démocratisé cette approche.

**Chatbots basés sur les LLMs** : L'émergence des grands modèles de langage (GPT-3, GPT-4, Mistral, LLaMA) a révolutionné le domaine. Ces modèles génèrent des réponses fluides et contextuelles, mais présentent un problème majeur : **les hallucinations** — la génération d'informations plausibles mais fausses.

**Chatbots RAG (Retrieval-Augmented Generation)** : La technique RAG, introduite par Lewis et al. (2020) chez Meta AI, résout le problème des hallucinations en combinant la recherche d'information (retrieval) avec la génération de texte (generation). Le LLM ne répond plus uniquement à partir de ses connaissances internes, mais s'appuie sur des documents externes récupérés dynamiquement.

### 1.3 La technique RAG (Retrieval-Augmented Generation)

#### 1.3.1 Principe général

Le RAG fonctionne en deux phases principales :

1. **Phase de Retrieval (Récupération)** : La question de l'utilisateur est convertie en vecteur (embedding), puis comparée aux vecteurs des documents stockés dans une base vectorielle. Les documents les plus similaires sont récupérés.

2. **Phase de Generation (Génération)** : Les documents récupérés sont injectés dans le prompt du LLM avec la question originale. Le modèle génère alors une réponse basée sur ces documents spécifiques.

#### 1.3.2 Pipeline RAG détaillé

Le pipeline RAG se décompose en six étapes :

```
1. Ingestion     → Chargement des documents sources (JSON, Markdown)
2. Chunking      → Découpage en passages de taille contrôlée (~500 tokens)
3. Embedding     → Vectorisation de chaque chunk via un modèle d'embedding
4. Indexation    → Stockage des vecteurs dans une base vectorielle (ChromaDB)
5. Retrieval     → Recherche des k chunks les plus similaires à la question
6. Generation    → Envoi des chunks + question au LLM pour générer la réponse
```

#### 1.3.3 Avantages du RAG

| Avantage | Description |
|----------|-------------|
| **Anti-hallucination** | Les réponses sont ancrées dans des données réelles et vérifiables |
| **Mise à jour facile** | Modifier la base de connaissances ne nécessite pas de réentraîner le modèle |
| **Traçabilité** | Chaque réponse peut citer ses sources (métadonnées des chunks) |
| **Personnalisation** | Le contexte injecté peut être filtré selon le profil de l'utilisateur |
| **Coût réduit** | Pas besoin de fine-tuning coûteux du modèle |

### 1.4 Comparaison avec les solutions existantes

| Solution | Type | Langue | Personnalisation | Données locales (Maroc) |
|----------|------|--------|-------------------|------------------------|
| ChatGPT générique | LLM seul | Multi | Aucune | Non |
| Crunchbase | Base de données | Anglais | Filtres basiques | Limitée |
| Dealroom | Base de données | Anglais | Filtres avancés | Limitée |
| AngelList | Plateforme matching | Anglais | Profil startup | Non |
| **Tamwil AI** | **RAG + Rule-based** | **Français** | **Scoring + Matching personnalisé** | **Oui (41 investisseurs, 25 subventions)** |

**Conclusion** : Aucune solution existante ne combine à la fois la langue française, le contexte marocain/francophone, la personnalisation basée sur les métriques financières, et l'intelligence conversationnelle d'un LLM. Tamwil AI comble ce vide.

### 1.5 Justification de l'approche hybride

Notre projet adopte une **approche hybride** qui combine deux paradigmes :

**1. RAG vectoriel (pour les questions libres) :**
- L'utilisateur pose une question en langage naturel
- Le système cherche les passages pertinents dans la base de connaissances (FAQ, guides, réglementations)
- Le LLM génère une réponse contextualisée à partir de ces passages

**2. Rule-based + LLM (pour le scoring et le matching) :**
- Les données structurées (investisseurs, subventions, métriques) sont stockées en JSON
- Le filtrage et le scoring sont effectués algorithmiquement (règles précises, pas d'approximation)
- Le LLM intervient uniquement pour formuler la recommandation en langage naturel

**Justification** : Les données structurées (tickets d'investissement, critères d'éligibilité, benchmarks de métriques) nécessitent un traitement déterministe et précis. Un RAG pur risquerait d'approximer des valeurs numériques critiques. L'approche hybride garantit la précision des données tout en offrant la fluidité conversationnelle du LLM.

---
---

## CHAPITRE 2 : CONCEPTION ET ARCHITECTURE

### 2.1 Architecture globale du système

L'architecture de Tamwil AI suit une conception modulaire en couches :

```
┌─────────────────────────────────────────────────────┐
│                  Interface Web                       │
│         (Next.js 16 + React 19 + Tailwind 4)        │
│   Chat SSE streaming, Sidebar, Profil, Dark mode    │
└──────────────────┬──────────────────────────────────┘
                   │ HTTP POST (REST + SSE)
┌──────────────────▼──────────────────────────────────┐
│              Serveur FastAPI                          │
│   POST /api/chat  ·  POST /api/chat/stream           │
│   Formatage Markdown · Attribution des sources       │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│              Orchestrateur / Router                   │
│   Détection d'intention par mots-clés + regex        │
│   (scoring, diagnostic, metrics, investisseurs,      │
│    subventions, greeting, Q&A)                       │
└──┬───────┬───────┬───────┬───────┬───────┬──────────┘
   │       │       │       │       │       │
   ▼       ▼       ▼       ▼       ▼       ▼
┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
│Score ││Diag. ││Expli.││Match ││Grant ││ RAG  │
│Fund. ││Finan.││Métr. ││Invest││Match ││ Q&A  │
└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘
   │       │       │       │       │       │
   ▼       ▼       ▼       ▼       ▼       ▼
┌─────────────────────────────────────────────────────┐
│               Base de Connaissances                  │
│  ┌──────────────┐    ┌───────────────────────────┐  │
│  │  ChromaDB    │    │ JSON structuré            │  │
│  │  (embeddings │    │ (investors, grants,       │  │
│  │   guides,    │    │  metrics, FAQ)            │  │
│  │   FAQ, regs) │    │                           │  │
│  └──────────────┘    └───────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

### 2.2 Description des modules fonctionnels

#### Module 1 : Scoring de Fundability

Le scoring de fundability est la fonctionnalité phare du projet. Il évalue la préparation d'une startup à la levée de fonds.

- **Entrée** : Métriques utilisateur (MRR, burn rate, churn, CAC, LTV, stade)
- **Données utilisées** : `metrics_reference.json` (benchmarks pondérés)
- **Logique** :
  1. Comparer chaque métrique aux benchmarks du stade correspondant (bad/ok/good/excellent)
  2. Calculer un score pondéré sur 100 en utilisant le champ `weight_in_scoring`
  3. Distinguer les métriques inversées (CAC, churn, burn rate — plus bas = meilleur)
  4. Identifier les forces et faiblesses
  5. Générer un plan d'action personnalisé à partir des `improvement_tips`
- **Sortie** : Score /100, détail par métrique, axes d'amélioration, plan d'action

#### Module 2 : Diagnostic Financier

- **Entrée** : KPIs individuels de l'utilisateur
- **Données utilisées** : `metrics_reference.json` (formules, benchmarks, interprétation, conseils)
- **Logique** : Analyser chaque KPI, comparer aux benchmarks du stade, classifier le niveau (bad/ok/good/excellent), générer un résumé global selon la distribution des niveaux
- **Sortie** : Analyse détaillée par métrique avec définition, formule, benchmark, conseils d'amélioration et métriques liées

#### Module 3 : Matching Investisseurs

- **Entrée** : Profil startup (secteur, stade, géographie, montant recherché)
- **Données utilisées** : `investors.json` (41 profils)
- **Logique** :
  1. Calculer un score de matching (0-4) basé sur : secteur (+1), stade (+1), géographie (+1), ticket compatible (+1)
  2. Trier par score décroissant, puis par nom
  3. Retourner les raisons du matching pour chaque investisseur
- **Sortie** : Top 5 investisseurs avec détails, critères spécifiques, portfolio et contacts

#### Module 4 : Matching Subventions

- **Entrée** : Profil startup (secteur, stade, pays, ancienneté)
- **Données utilisées** : `grants.json` (25 programmes)
- **Logique** : Filtrer par pays, stade, secteur (avec support « tous secteurs »), et âge maximum de l'entreprise
- **Sortie** : Liste des aides éligibles avec montants, conditions et deadlines

#### Module 5 : Explication des Métriques

- **Entrée** : Question contenant un terme de métrique (MRR, CAC, churn, etc.)
- **Données utilisées** : `metrics_reference.json`
- **Logique** : Identifier les métriques mentionnées, retourner la définition, formule, interprétation et benchmarks
- **Sortie** : Fiche explicative de chaque métrique demandée

#### Module 6 : Q&A Conversationnel (RAG)

- **Entrée** : Question libre de l'utilisateur en français + historique de conversation
- **Données utilisées** : Tous les documents via ChromaDB
- **Logique** :
  1. Enrichir la requête avec l'historique (2 derniers échanges) pour améliorer la recherche sémantique
  2. Récupérer les top-k chunks similaires dans ChromaDB
  3. Injecter le contexte + les 3 derniers échanges dans le prompt du LLM
  4. Générer la réponse en streaming (token par token)
- **Sortie** : Réponse contextuelle en français avec attribution des sources

### 2.3 Modèle de données

Le dataset a été constitué manuellement et contient environ **504 KB de données de qualité**, organisées comme suit :

#### Données structurées (JSON)

| Fichier | Enregistrements | Contenu |
|---------|----------------|---------|
| `investors.json` | 41 profils | Investisseurs (VC, BA, accélérateurs, fonds publics) avec critères, tickets, secteurs, géographies |
| `grants.json` | 25 programmes | Subventions et aides (Maroc, France, International) avec critères d'éligibilité, montants |
| `metrics_reference.json` | 18 métriques | KPIs startup avec formules, benchmarks par stade (bad/ok/good/excellent), conseils, benchmarks MAD |
| `faq.json` | 54 Q&A | Questions/réponses sur la finance startup, classées par catégorie et difficulté |

**Structure d'un profil investisseur :**
```json
{
  "id": "INV_001",
  "name": "CDG Invest",
  "type": "VC",
  "description": "Fonds d'investissement filiale de la CDG...",
  "sectors": ["fintech", "healthtech", "edtech", "agritech"],
  "stage": ["seed", "series-a", "series-b"],
  "ticket_min": 5000000,
  "ticket_max": 100000000,
  "currency": "MAD",
  "geography": ["Maroc", "Afrique du Nord"],
  "criteria": { "description": "Startups avec traction prouvée et équipe solide" },
  "portfolio_examples": ["Chari", "WafR"],
  "contact": { "website": "...", "linkedin": "..." }
}
```

**Structure d'une métrique de référence :**
```json
{
  "id": "MRR",
  "name": "Monthly Recurring Revenue",
  "name_fr": "Revenu Mensuel Récurrent",
  "definition": "...",
  "formula": "...",
  "unit": "currency",
  "weight_in_scoring": 0.15,
  "benchmarks": {
    "pre_seed": { "bad": "<500", "ok": "500-2000", "good": "2000-5000", "excellent": ">5000" },
    "seed": { "..." }
  },
  "benchmarks_mad": { "seed": { "..." } },
  "interpretation": "...",
  "improvement_tips": ["...", "..."],
  "related_metrics": ["ARR", "CHURN_RATE"]
}
```

#### Données non structurées (Markdown)

| Répertoire | Fichiers | Lignes totales | Contenu |
|------------|---------|----------------|---------|
| `fundraising_guide/` | 6 fichiers | ~3 554 lignes | Types de financement, pitch deck, étapes de levée, term sheet, valorisation, erreurs courantes |
| `regulations/` | 4 fichiers | ~1 817 lignes | Création d'entreprise au Maroc, réglementation fintech, fiscalité startup, RGPD |

### 2.4 Pipeline RAG détaillé

```
┌──────────────────┐
│  Documents       │
│  (JSON + MD)     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  1. Ingestion    │  → Chargement des fichiers via data_loader.py
│  (ingest.py)     │  → Conversion en objets LangChain Document
│                  │  → 6 sources : FAQ, guides, regulations, investors, grants, metrics
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  2. Chunking     │  → RecursiveCharacterTextSplitter
│  (ingest.py)     │  → chunk_size=500, overlap=50
│                  │  → Séparateurs : titres (##), paragraphes, phrases, mots
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  3. Embedding    │  → paraphrase-multilingual-MiniLM-L12-v2
│  (embeddings.py) │  → 384 dimensions, support français
│                  │  → Exécution locale (gratuit, pas d'appel API)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  4. Indexation   │  → ChromaDB en mode persistant
│  (vectorstore.py)│  → Collection : "tamwil_knowledge_base"
│                  │  → Stockage : texte + vecteur + métadonnées
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  5. Retrieval    │  → Cosine similarity search
│  (retriever.py)  │  → Top-k chunks (k=5 par défaut)
│                  │  → Filtrage optionnel par type de document
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  6. Generation   │  → Envoi au LLM (OpenAI GPT-3.5-turbo)
│  (rag_qa.py)     │  → Prompt = system + historique + chunks + question
│                  │  → Réponse en français, streaming token par token
└──────────────────┘
```

### 2.5 Mapping Dataset → Fonctionnalités

Chaque source de données alimente une ou plusieurs fonctionnalités spécifiques :

```
investors.json ──────────→ Matching investisseurs
grants.json ─────────────→ Matching subventions
metrics_reference.json ──→ Scoring + Diagnostic + Explication métriques
faq.json ────────────────→ Q&A conversationnel (RAG) + Explication métriques
fundraising_guide/*.md ──→ Q&A conversationnel (RAG)
regulations/*.md ────────→ Q&A conversationnel (RAG)
```

| Fonctionnalité | JSON principal | Markdown (RAG) |
|---------------|---------------|----------------|
| Scoring | `metrics_reference.json` | — |
| Diagnostic | `metrics_reference.json` | — |
| Explication métriques | `metrics_reference.json` | — |
| Matching investisseurs | `investors.json` | — |
| Matching subventions | `grants.json` | — |
| Q&A RAG | `faq.json` | guides + regulations |

---
---

## CHAPITRE 3 : RÉALISATION ET IMPLÉMENTATION

### 3.1 Environnement de développement

| Élément | Détail |
|---------|--------|
| Système d'exploitation | Linux (Ubuntu) |
| Langage backend | Python 3.11+ |
| Langage frontend | TypeScript 5 |
| IDE | Visual Studio Code |
| Gestionnaire de version | Git + GitHub |
| Environnement virtuel Python | venv |
| Gestionnaire de paquets Node.js | npm |

### 3.2 Stack technique

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| **Backend** | Python 3.11+ | Écosystème IA/NLP riche, nombreuses bibliothèques |
| **Serveur API** | FastAPI + Uvicorn | Framework moderne, asynchrone, SSE streaming natif, documentation auto-générée (Swagger) |
| **LLM** | OpenAI API (GPT-3.5-turbo) | Qualité de génération en français, API fiable, température configurable |
| **Embeddings** | sentence-transformers (`paraphrase-multilingual-MiniLM-L12-v2`) | Gratuit, local, supporte le français, 384 dimensions |
| **Base vectorielle** | ChromaDB | Simple, léger, persistant sur disque (SQLite), parfait pour un dataset de cette taille |
| **Pipeline RAG** | LangChain | Framework mature pour l'orchestration RAG, chunking, prompt templates |
| **Frontend** | Next.js 16 + React 19 | Framework React de production, App Router, rendu côté serveur |
| **Styling** | Tailwind CSS 4 + Radix UI | Utility-first CSS, composants accessibles, dark mode natif |
| **Animations** | Framer Motion | Animations fluides pour le background animé |
| **Guided Tour** | React Joyride | Onboarding interactif pour les nouveaux utilisateurs |
| **Configuration** | python-dotenv | Gestion sécurisée des variables d'environnement |
| **Tests** | pytest | Framework de tests unitaires Python |

**Dépendances principales :**

Backend (`requirements.txt`) :
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

Frontend (`package.json`) :
```
next: 16.1.6
react: 19.2.3
tailwindcss: 4
@radix-ui/* (dialog, select, dropdown-menu, scroll-area, popover, separator)
lucide-react (icônes)
framer-motion: 12.34.0
react-joyride: 2.9.3
next-themes: 0.4.6
```

### 3.3 Constitution du dataset

Le dataset a été construit **manuellement** pour garantir la qualité et la pertinence des données au contexte marocain et francophone. Aucun scraping automatisé n'a été utilisé.

**Volume total** : ~504 KB de données structurées et non structurées.

| Source | Format | Volume | Contenu |
|--------|--------|--------|---------|
| `investors.json` | JSON | 41 profils | Investisseurs du Maroc, de France et d'Afrique (26 VC, 6 accélérateurs, 3 fonds publics, 2 CVC, 2 BA, 2 growth funds) |
| `grants.json` | JSON | 25 programmes | Subventions (9 Maroc, 8 France, 8 International) |
| `metrics_reference.json` | JSON | 18 métriques | KPIs startup avec benchmarks par stade et benchmarks MAD |
| `faq.json` | JSON | 54 Q&A | 10 catégories : fundraising, metrics, grants, regulation, taxation, ecosystem, fintech, IP, HR |
| `fundraising_guide/` | Markdown | 6 guides (~3 554 lignes) | Types de financement, pitch deck, étapes de levée, term sheet, valorisation, erreurs courantes |
| `regulations/` | Markdown | 4 documents (~1 817 lignes) | Création d'entreprise, fintech, fiscalité, RGPD |

**Couverture sectorielle (28 secteurs)** : fintech, SaaS, e-commerce, healthtech, edtech, agritech, cleantech, logistics, deeptech, biotech, AI, cybersecurity, marketplace, mobile, etc.

**Couverture géographique** : Maroc (focus principal), France, Afrique francophone (Tunisie, Sénégal, Côte d'Ivoire), région MENA, International.

**Métriques couvertes (18 KPIs)** :
- Revenue : MRR, ARR, MRR Growth Rate
- Unit Economics : CAC, LTV, LTV/CAC, CAC Payback Period, Gross Margin
- Opérationnel : Burn Rate, Runway, Churn Rate, Revenue Churn (NRR)
- Marketplace : GMV, Take Rate
- Fintech : TPV
- Engagement : DAU/MAU
- Satisfaction : NPS

### 3.4 Implémentation du pipeline RAG

#### 3.4.1 Configuration (`backend/app/config.py`)

Le module `config.py` centralise tous les paramètres du projet. Il charge les variables d'environnement depuis le fichier `.env` situé dans le répertoire `backend/` et exporte des constantes utilisées par tous les modules.

**Paramètres clés :**
- `OPENAI_API_KEY` : Clé API pour le LLM
- `LLM_MODEL` : Modèle utilisé (par défaut : `gpt-3.5-turbo`)
- `EMBEDDING_MODEL` : Modèle d'embedding (par défaut : `paraphrase-multilingual-MiniLM-L12-v2`)
- `CHROMA_PERSIST_DIR` : Répertoire de persistance ChromaDB (`./chroma_db`)
- `CHUNK_SIZE` / `CHUNK_OVERLAP` : 500 / 50 tokens
- `TOP_K` : Nombre de chunks à récupérer (5)

#### 3.4.2 Chargement des données (`backend/app/utils/data_loader.py`)

Le module `data_loader.py` fournit une interface unifiée pour charger et valider toutes les sources de données :

- `load_investors()` → charge et valide les 41 profils (champs requis : id, name, type, sectors, stage, ticket_min/max, currency, geography)
- `load_grants()` → charge et valide les 25 programmes (champs requis : id, name, country, organization, type, amount_min/max, currency, eligibility)
- `load_metrics()` → charge et valide les 18 métriques (champs requis : id, name, definition, formula, unit, benchmarks)
- `load_faq()` → charge et valide les 54 Q&A (champs requis : id, categorie, question, reponse)
- `load_fundraising_guides()` / `load_regulations()` → chargent les fichiers Markdown
- `load_all()` → charge l'ensemble en un seul appel

Chaque fonction gère les erreurs gracieusement : fichier manquant → log + retour vide ; champ manquant → warning.

#### 3.4.3 Ingestion et chunking (`backend/app/rag/ingest.py`)

Le module `ingest.py` transforme les documents bruts en chunks prêts pour la vectorisation. Il construit six types de documents LangChain :

1. **FAQ** : Combine question + réponse en texte unique, avec métadonnées (source, type, catégorie)
2. **Guides fundraising** : Charge les 6 fichiers Markdown
3. **Réglementations** : Charge les 4 fichiers Markdown
4. **Investisseurs** : Convertit chaque profil en texte riche (nom, type, secteurs, tickets, géographie, etc.)
5. **Subventions** : Convertit chaque programme en texte riche (nom, organisation, montant, conditions, etc.)
6. **Métriques** : Convertit chaque KPI en texte riche (nom, définition, formule, benchmarks, etc.)

Le chunking utilise `RecursiveCharacterTextSplitter` avec des séparateurs hiérarchiques : `["\n## ", "\n### ", "\n\n", "\n", ". ", " ", ""]`.

#### 3.4.4 Modèle d'embedding (`backend/app/rag/embeddings.py`)

**Modèle choisi : `paraphrase-multilingual-MiniLM-L12-v2`**

| Caractéristique | Valeur |
|-----------------|--------|
| Dimensions | 384 |
| Langues supportées | 50+ (dont le français) |
| Taille du modèle | ~130 MB |
| Exécution | Locale (CPU, pas de GPU requis) |
| Coût | Gratuit |

**Justification** : Support natif du français, exécution locale sans coût API, performance suffisante pour notre dataset, compatibilité LangChain via `HuggingFaceEmbeddings`.

#### 3.4.5 Base vectorielle (`backend/app/rag/vectorstore.py`)

- **`build_vectorstore()`** : Pipeline complet — supprime les anciennes données, ingère tous les documents, vectorise, stocke dans ChromaDB et persiste sur disque
- **`get_vectorstore()`** : Charge la base existante depuis le disque sans réindexation (démarrage rapide)

**Configuration** : Collection `tamwil_knowledge_base`, backend SQLite, taille après indexation ~7.3 MB.

#### 3.4.6 Recherche sémantique (`backend/app/rag/retriever.py`)

- **`retrieve(query, k=5, filter_type=None)`** : Recherche par similarité cosinus, retourne les k chunks les plus pertinents avec filtrage optionnel par type de document
- **`retrieve_with_scores()`** : Variante incluant les scores de similarité

### 3.5 Implémentation des modules métier

#### 3.5.1 Scoring de fundability (`backend/app/modules/scoring.py`)

L'algorithme de scoring fonctionne en cinq étapes :
1. Pour chaque métrique fournie par l'utilisateur, charger le benchmark correspondant au stade
2. Classifier la valeur (bad/ok/good/excellent) via `_classify_value()`, en distinguant les métriques inversées (CAC, churn, burn rate — plus bas = meilleur)
3. Mapper le niveau vers un score (bad=25, ok=50, good=75, excellent=100)
4. Appliquer le poids de la métrique (`weight_in_scoring`)
5. Calculer le score final : `total_weighted_score / total_weight`

Le résultat inclut : score /100, breakdown par métrique, forces (good/excellent), faiblesses (bad/ok), et plan d'action personnalisé extrait des `improvement_tips`.

#### 3.5.2 Diagnostic financier (`backend/app/modules/diagnostic.py`)

Le diagnostic analyse chaque KPI individuellement et génère un résumé global basé sur la distribution des niveaux :
- 0 métriques « bad » → « Votre startup est en bonne santé financière »
- ≤50% « bad » → « Quelques indicateurs nécessitent attention »
- >50% « bad » → « Plusieurs indicateurs sont en zone critique »

Chaque métrique reçoit : définition, formule, benchmarks, interprétation, 3 conseils d'amélioration, et métriques liées.

#### 3.5.3 Matching investisseurs (`backend/app/modules/matching_investors.py`)

Score de matching (0-4 points) :
- Secteur correspond → +1
- Stade correspond → +1
- Géographie correspond → +1
- Montant dans la fourchette ticket → +1

Résultats triés par score décroissant, top 5 retournés avec raisons détaillées du matching.

#### 3.5.4 Matching subventions (`backend/app/modules/matching_grants.py`)

Filtrage séquentiel par éligibilité : pays → stade → secteur (avec wildcard « tous secteurs ») → âge de l'entreprise. Chaque subvention retenue inclut les raisons de matching.

#### 3.5.5 Q&A conversationnel (`backend/app/modules/rag_qa.py`)

Deux modes de fonctionnement :

**Mode synchrone (`answer_question`)** :
1. Enrichir la requête avec l'historique (2 derniers échanges)
2. Récupérer les top-k chunks
3. Construire un ChatPromptTemplate avec system prompt, historique (3 échanges) et question
4. Invoquer le LLM (GPT-3.5-turbo, température 0.3)
5. Retourner la réponse + sources

**Mode streaming (`answer_question_stream`)** :
1. Même pipeline de retrieval
2. Yield des sources d'abord
3. Streamer les tokens du LLM un par un via `yield`

Le **system prompt** impose 9 règles comportementales : toujours tenter de répondre, accepter le contexte partiel, ne jamais fabriquer de sources, rester dans le domaine, adapter la langue, ton professionnel, etc.

**Mode fallback** : Si l'API OpenAI n'est pas disponible, le système retourne directement les chunks récupérés sans génération LLM.

### 3.6 Implémentation du backend FastAPI

#### 3.6.1 Serveur et endpoints (`backend/app/main.py`)

Le serveur FastAPI expose trois endpoints :

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `/api/chat` | POST | Chat synchrone — retourne la réponse complète en JSON |
| `/api/chat/stream` | POST | Chat streaming — retourne les tokens en temps réel via SSE |
| `/health` | GET | Health check — retourne `{"status": "ok"}` |

**Modèles Pydantic** :
- `StartupProfile` : secteur, stade, pays, mrr, burnRate, churn, cac, ltv
- `HistoryMessage` : role (user/assistant), content
- `ChatRequest` : message + profile (optionnel) + history (optionnel)
- `SourceInfo` : name, type, url
- `ChatResponse` : reply (Markdown) + sources

**CORS** : Configuré pour accepter les requêtes depuis localhost:3000 (frontend de développement).

#### 3.6.2 Détection de greetings

Le système détecte les messages de salutation simples pour éviter un appel LLM inutile :

```python
GREETING_WORDS = {"bonjour", "salut", "hello", "hi", "hey", "bonsoir",
                  "coucou", "salam", "yo", "merci", "ok", "azul", "marhaba", ...}

def _is_greeting(message):
    tokens = message.split()
    return len(tokens) <= 3 and all(t in GREETING_WORDS for t in tokens)
```

Si c'est un greeting, le système répond directement avec un message de bienvenue fixe, sans RAG ni LLM.

#### 3.6.3 Routeur d'intentions (`backend/app/router.py`)

Le routeur détecte l'intention de l'utilisateur par mots-clés avec fallback vers des patterns regex :

| Intention | Exemples de mots-clés |
|-----------|-----------------------|
| `scoring` | score, fundability, noter, évaluer ma startup |
| `diagnostic` | diagnostic, analyser mes KPI, santé financière |
| `metrics` | expliquer les métriques, c'est quoi un KPI, définition |
| `investors` | investisseur, VC, business angel, levée de fonds |
| `grants` | subvention, aide, FORSA, Tamwilcom, financement non dilutif |
| `qa` (fallback) | Toute question non classifiée → RAG |

L'algorithme vérifie aussi les patterns de valeurs métriques (ex: `MRR: 8000`) via regex pour auto-détecter l'intention `scoring` même sans mot-clé explicite.

Le routeur extrait automatiquement le stade, le secteur, le pays et les valeurs métriques depuis le message de l'utilisateur via des expressions régulières.

#### 3.6.4 Server-Sent Events (SSE) streaming

Le streaming SSE permet d'afficher les tokens au fur et à mesure de la génération :

```
Client POST /api/chat/stream
  ↓
Détection greeting / intention
  ↓
Si greeting → réponse fixe immédiate
Si Q&A     → streaming token par token depuis le LLM
Sinon      → exécution synchrone, envoi en une fois

Événements SSE :
  event: sources  → JSON array des sources
  event: token    → Token individuel (Q&A streaming)
  event: reply    → Réponse complète (intentions non-Q&A)
  event: done     → Signal de fin
```

#### 3.6.5 Attribution des sources (`backend/app/source_urls.py`)

Chaque réponse inclut les sources utilisées avec des URLs cliquables. Le système utilise un mapping statique des fichiers vers des URLs réelles, avec fallback vers une recherche Google construite dynamiquement.

#### 3.6.6 Formatage des réponses en Markdown

Chaque type d'intention a son propre formateur Markdown :
- **Scoring** : Score en gras, tableau de breakdown, forces/faiblesses avec emojis, plan d'action
- **Diagnostic** : Résumé, analyse par métrique avec headers, benchmarks, conseils
- **Investisseurs** : Nom, type, ticket, score /4, raisons du matching
- **Subventions** : Nom, organisation, type, montant, conditions
- **Métriques** : Définition, formule, exemple de format d'entrée
- **Q&A** : Texte brut du LLM

### 3.7 Implémentation de l'interface utilisateur

L'interface web a été développée avec **Next.js 16**, **React 19** et **Tailwind CSS 4**, offrant une expérience de chat moderne et responsive.

#### 3.7.1 Architecture des composants

```
RootLayout (layout.tsx)
  └─ ThemeProvider (next-themes)
      └─ Home (page.tsx — gestion d'état globale)
          ├─ ChatLayout (sidebar redimensionnable)
          │   ├─ AnimatedGridPattern (fond SVG animé)
          │   ├─ Sidebar
          │   │   ├─ Bouton nouvelle conversation
          │   │   ├─ Liste des conversations (hover menu)
          │   │   │   └─ DropdownMenu (renommer, supprimer)
          │   │   └─ ProfileForm (dans un Dialog)
          │   └─ ChatPanel
          │       ├─ ThemeToggle (soleil/lune)
          │       ├─ ScrollArea (messages)
          │       │   └─ MessageBubble (×N)
          │       │       └─ SourceChips (URLs cliquables)
          │       └─ ChatInput (textarea auto-resize)
          └─ GuidedTour (React Joyride)
```

#### 3.7.2 Sidebar avec gestion de conversations

La sidebar offre :
- **Bouton nouvelle conversation** pour démarrer un échange vierge
- **Liste des conversations** avec titres tronqués à 4 mots
- **Menu hover** sur chaque conversation : renommer (édition inline) ou supprimer
- **Redimensionnement par drag** : handle draggable entre 180px et 480px (desktop)
- **Mode collapsed** : bande d'icônes de 52px sur desktop
- **Mode mobile** : overlay plein écran avec fermeture au clic

#### 3.7.3 Interface de chat

L'interface de chat comprend :
- **État initial** : message de bienvenue + 4 suggestions cliquables (scoring, investisseurs, subventions, diagnostic)
- **Bulles de message** : user (droite, fond primaire) / assistant (gauche, fond muted)
- **Rendu Markdown** : headers, listes, tableaux, gras, italique, code inline, séparateurs
- **Attribution des sources** : badges numérotés avec lien externe cliquable
- **Indicateur de chargement** : 3 points animés avec rebond décalé

L'input de chat offre un textarea auto-resizable (max 200px), envoi par Enter, retour à la ligne par Shift+Enter.

#### 3.7.4 Formulaire de profil startup

Le formulaire, accessible depuis la sidebar, permet de configurer :
- **Informations** : secteur (14 options), stade (3 options), pays (6 options)
- **Métriques optionnelles** : MRR, burn rate, churn, CAC, LTV (inputs numériques)
- Persistance dans `localStorage` pour conservation entre sessions

#### 3.7.5 Guided Tour

Un tour interactif (React Joyride) guide les nouveaux utilisateurs à travers 6 étapes :
1. Sidebar — gestion des conversations
2. Bouton nouvelle conversation
3. Configuration du profil startup
4. Suggestions de questions
5. Zone de saisie des messages
6. Toggle dark/light mode

Le tour s'affiche une seule fois (flag `localStorage: tamwil-tour-completed`) et s'adapte au mobile (saute les étapes sidebar si largeur < 768px).

#### 3.7.6 Gestion d'état et consommation SSE

L'état global est géré dans `page.tsx` (composant client) avec les hooks React :
- `conversations` et `profile` persistés dans `localStorage`
- Flux SSE consommé via `ReadableStream` + `TextDecoder` dans `lib/api.ts`
- Callbacks pour les événements : `onSources`, `onToken`, `onReply`, `onDone`

#### 3.7.7 Dark mode et design responsive

- **Dark mode** : via `next-themes` avec attribut `class`, 3 modes (light, dark, system)
- **Système de couleurs** : variables CSS en espace colorimétrique oklch (WCAG compliant)
- **Responsive** : breakpoint à 768px (md), sidebar overlay sur mobile, grille adaptative

### 3.8 Structure du projet

```
tamwil-ai/
├── backend/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py                 # Configuration centralisée
│   │   ├── main.py                   # Serveur FastAPI (3 endpoints)
│   │   ├── router.py                 # Orchestrateur / détection d'intention
│   │   ├── source_urls.py            # Mapping fichiers → URLs pour attribution des sources
│   │   ├── modules/
│   │   │   ├── __init__.py
│   │   │   ├── scoring.py            # Scoring de fundability (/100)
│   │   │   ├── diagnostic.py         # Diagnostic financier par KPI
│   │   │   ├── matching_investors.py # Matching investisseurs (score 0-4)
│   │   │   ├── matching_grants.py    # Matching subventions par éligibilité
│   │   │   └── rag_qa.py             # Q&A conversationnel (RAG + LLM streaming)
│   │   ├── rag/
│   │   │   ├── __init__.py
│   │   │   ├── ingest.py             # Ingestion et chunking (6 sources)
│   │   │   ├── embeddings.py         # Modèle d'embedding multilingue
│   │   │   ├── vectorstore.py        # ChromaDB persistant
│   │   │   └── retriever.py          # Recherche sémantique cosinus
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── data_loader.py        # Chargement et validation des données
│   └── .env                          # Variables d'environnement
├── dataset/
│   ├── DISCLAIMER.md                 # Avertissement sur les limites des données
│   ├── investors/investors.json      # 41 profils d'investisseurs
│   ├── grants/grants.json            # 25 programmes de subventions
│   ├── metrics/metrics_reference.json # 18 KPIs avec benchmarks
│   ├── faq/faq.json                  # 54 Q&A
│   ├── fundraising_guide/            # 6 guides Markdown (~3 554 lignes)
│   └── regulations/                  # 4 documents réglementaires (~1 817 lignes)
├── chroma_db/                        # Base vectorielle persistante (gitignored)
├── docs/                             # Documentation du projet
├── frontend/                         # Interface Next.js
│   ├── src/
│   │   ├── app/                      # Pages (layout.tsx, page.tsx, globals.css)
│   │   ├── components/               # 10 composants (chat, sidebar, profil, tour, theme)
│   │   │   └── ui/                   # 11 composants Radix UI (button, dialog, select, etc.)
│   │   └── lib/                      # api.ts (SSE), types.ts, constants.ts, utils.ts
│   ├── package.json
│   └── next.config.ts
├── tests/                            # Tests unitaires (pytest)
│   ├── test_scoring.py
│   ├── test_diagnostic.py
│   ├── test_matching_investors.py
│   ├── test_matching_grants.py
│   ├── test_router.py
│   └── test_rag.py
└── requirements.txt                  # Dépendances Python
```

### 3.9 Règles de développement

1. **Langue** : Le code est écrit en anglais, mais les prompts LLM, les réponses utilisateur et les données sont en français
2. **Pas d'hallucination** : Le chatbot ne répond que sur la base des données fournies via RAG, il ne doit jamais inventer d'informations
3. **Modularité** : Chaque module est indépendant et testable séparément
4. **Gestion d'erreurs** : Gestion gracieuse des données manquantes ou insuffisantes
5. **ChromaDB persistant** : Pas de réindexation à chaque lancement de l'application
6. **Streaming** : Le Q&A RAG utilise le SSE streaming pour une UX responsive ; les autres intentions envoient la réponse en une fois pour garantir l'atomicité

---
---

## CHAPITRE 4 : TESTS ET RÉSULTATS

### 4.1 Scénarios de test

Six scénarios de test ont été définis pour valider les fonctionnalités principales du système :

| # | Scénario | Entrée utilisateur | Sortie attendue |
|---|----------|-------------------|-----------------|
| 1 | Scoring de fundability | "MRR: 8000, burn rate: 15000, churn: 5%, stade: seed" | Score ~58/100, axes d'amélioration, plan d'action |
| 2 | Diagnostic financier | "CAC: 200, LTV: 400, churn: 8%" | Ratio LTV/CAC faible, churn élevé, recommandations |
| 3 | Matching investisseurs | "Fintech, seed, Maroc, MRR 10K" | Top 5 investisseurs pertinents avec critères et contacts |
| 4 | Matching subventions | "Startup edtech, 2 ans, Maroc" | Liste des aides éligibles avec montants et deadlines |
| 5 | Explication métriques | "C'est quoi le MRR ?" | Définition, formule, interprétation, benchmarks |
| 6 | Q&A conversationnel | "Comment valoriser ma startup en pré-seed ?" | Réponse détaillée basée sur les guides de valorisation |

### 4.2 Tests du pipeline RAG

#### Test de l'ingestion des données

Le module `data_loader.py` a été exécuté en standalone pour valider le chargement de toutes les sources de données :

| Source | Résultat | Statut |
|--------|----------|--------|
| Investisseurs | 41 profils chargés et validés | OK |
| Subventions | 25 programmes chargés et validés | OK |
| Métriques | 18 métriques chargées et validées | OK |
| FAQ | 54 Q&A chargés et validés | OK |
| Guides fundraising | 6 fichiers Markdown chargés | OK |
| Réglementations | 4 fichiers Markdown chargés | OK |

#### Test du chunking

Le module `ingest.py` a produit ~100+ chunks à partir de l'ensemble des documents, avec les paramètres configurés (chunk_size=500, overlap=50). Les chunks préservent les métadonnées (source, type de document) nécessaires à l'attribution des sources.

#### Test des embeddings

Le modèle `paraphrase-multilingual-MiniLM-L12-v2` génère des vecteurs de 384 dimensions. Un test qualitatif a confirmé la qualité des embeddings en français : les requêtes en français retournent des documents pertinents avec des scores de similarité élevés.

#### Test de la base vectorielle

ChromaDB a été construit et persisté sur le disque (~7.3 MB). Le chargement depuis le disque est quasi instantané, sans réindexation nécessaire.

#### Test du retriever

Le moteur de recherche sémantique a été testé avec des requêtes en français. Les résultats sont pertinents et correctement ordonnés par similarité cosinus. Le filtrage par type de document fonctionne correctement.

### 4.3 Tests unitaires

Six fichiers de tests unitaires couvrent l'ensemble des modules :

| Fichier | Module testé | Tests |
|---------|-------------|-------|
| `test_scoring.py` | Scoring de fundability | Classification des valeurs, calcul du score pondéré, gestion des métriques inversées |
| `test_diagnostic.py` | Diagnostic financier | Analyse par KPI, génération de résumé, gestion des cas limites |
| `test_matching_investors.py` | Matching investisseurs | Score de matching, filtrage multi-critères, tri par pertinence |
| `test_matching_grants.py` | Matching subventions | Éligibilité, filtrage par pays/stade/secteur/âge |
| `test_router.py` | Routeur d'intentions | Détection de chaque intention, extraction de métriques par regex, fallback Q&A |
| `test_rag.py` | Pipeline RAG | Retrieval, enrichissement de requête, construction du prompt |

### 4.4 Discussion et analyse

**Points forts du système :**
- Le pipeline RAG fonctionne de bout en bout avec des résultats pertinents en français
- Les embeddings multilingues offrent une excellente compréhension du français et des termes financiers
- ChromaDB persistant permet un démarrage rapide de l'application
- L'architecture modulaire facilite le développement itératif et les tests
- Le dataset original et adapté au contexte marocain est un atout différenciateur majeur
- Le SSE streaming offre une expérience utilisateur fluide et réactive pour le Q&A
- L'interface moderne avec dark mode, guided tour et sidebar redimensionnable rend l'outil accessible
- La détection de greetings économise des appels LLM inutiles

**Limites identifiées :**
- Le dataset reste relativement petit (~504 KB) et pourrait être enrichi avec davantage d'investisseurs et de subventions
- Le LLM utilisé (GPT-3.5-turbo) pourrait être remplacé par un modèle plus performant (GPT-4)
- La détection d'intention est basée sur des mots-clés — une classification LLM serait plus intelligente
- Le CORS est limité à localhost — une configuration production est nécessaire pour le déploiement
- L'historique des conversations est stocké uniquement côté client (localStorage), il serait perdu en changeant de navigateur
- Les tests d'intégration end-to-end ne couvrent pas encore tous les scénarios

---
---

## CONCLUSION GÉNÉRALE ET PERSPECTIVES

### Bilan du projet

Le projet Tamwil AI a permis de concevoir et d'implémenter un chatbot intelligent de recommandation financière, centré sur l'écosystème startup marocain et incluant les options de financement internationales accessibles aux fondateurs marocains (France, Afrique, MENA).

**Réalisations principales :**

1. **Constitution d'un dataset original** de ~504 KB couvrant l'écosystème startup marocain et francophone : 41 profils d'investisseurs, 25 programmes de subventions, 18 métriques financières avec benchmarks MAD, 54 Q&A, 6 guides de fundraising et 4 documents réglementaires.

2. **Implémentation complète du pipeline RAG** : ingestion de 6 types de documents, chunking avec LangChain, embedding avec le modèle multilingue `paraphrase-multilingual-MiniLM-L12-v2` (384 dimensions), indexation dans ChromaDB, et recherche sémantique par similarité cosinus.

3. **Développement de six modules métier** : scoring de fundability (pondéré /100), diagnostic financier, matching investisseurs (score 0-4), matching subventions, explication des métriques, et Q&A conversationnel RAG avec streaming — tous fonctionnels et testés.

4. **Développement de l'orchestrateur/router** : détection d'intention par mots-clés et regex, extraction automatique de métriques/stade/secteur/pays depuis le message, routage vers le module approprié avec fallback RAG, détection de greetings.

5. **Mise en place du serveur FastAPI** : API REST avec endpoint synchrone et endpoint SSE streaming, gestion CORS, attribution structurée des sources avec URLs cliquables, formatage des réponses en Markdown.

6. **Construction de l'interface frontend Next.js** : application React 19 avec Tailwind CSS 4, sidebar draggable avec historique de conversations et menu hover, chat conversationnel avec SSE streaming et rendu Markdown, formulaire de profil startup, guided tour interactif (React Joyride), dark/light mode, design responsive mobile-first.

7. **Tests unitaires** : 6 fichiers de tests couvrant tous les modules (scoring, diagnostic, matching investisseurs, matching subventions, router, RAG).

### Compétences acquises

Ce projet nous a permis de développer des compétences dans plusieurs domaines :
- **NLP et LLMs** : compréhension des modèles de langage, des embeddings et de la technique RAG
- **Bases de données vectorielles** : utilisation de ChromaDB pour le stockage et la recherche de vecteurs
- **Développement backend** : conception d'API REST avec FastAPI, SSE streaming, gestion CORS
- **Développement frontend** : React 19, Next.js, Tailwind CSS, gestion d'état, consommation SSE
- **Ingénierie logicielle** : architecture modulaire, gestion de configuration, tests unitaires
- **Écosystème Python IA** : maîtrise de LangChain, sentence-transformers, OpenAI API
- **Domaine métier** : compréhension approfondie de l'écosystème de financement des startups au Maroc

### Perspectives d'amélioration

Plusieurs axes d'amélioration sont envisagés pour les versions futures du projet :

1. **Enrichir le dataset** : ajouter de nouveaux investisseurs, subventions et contenus éducatifs au-delà des 41 investisseurs et 25 subventions actuels
2. **Optimiser les prompts LLM** : améliorer la qualité et la cohérence des réponses générées en français
3. **Migration vers GPT-4 ou un modèle local** : augmenter la qualité des réponses tout en réduisant la dépendance à l'API OpenAI
4. **Classification d'intention par LLM** : remplacer le routing par mots-clés par une classification plus intelligente via le LLM
5. **Tests d'intégration end-to-end** : valider le parcours complet utilisateur, du frontend à la réponse LLM
6. **Déploiement cloud** : rendre l'application accessible en ligne (Vercel pour le frontend, Railway/AWS pour le backend)
7. **Multilinguisme étendu** : support de l'arabe (darija) pour toucher un public plus large au Maroc
8. **Authentification et persistance serveur** : gestion des comptes utilisateurs et sauvegarde des conversations côté serveur
9. **Fonctionnalités avancées** : simulateur de runway, recommandation de type de financement, estimation de valorisation, calculateur de dilution

---
---

## BIBLIOGRAPHIE ET WEBOGRAPHIE

### Articles scientifiques

1. Lewis, P., Perez, E., Piktus, A., et al. (2020). « Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks ». *Advances in Neural Information Processing Systems (NeurIPS 2020)*.

2. Vaswani, A., Shazeer, N., Parmar, N., et al. (2017). « Attention Is All You Need ». *Advances in Neural Information Processing Systems (NeurIPS 2017)*.

3. Reimers, N. & Gurevych, I. (2019). « Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks ». *Proceedings of EMNLP-IJCNLP 2019*.

4. Brown, T., Mann, B., Ryder, N., et al. (2020). « Language Models are Few-Shot Learners ». *NeurIPS 2020*.

5. Devlin, J., Chang, M., Lee, K., Toutanova, K. (2019). « BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding ». *NAACL-HLT 2019*.

### Documentation technique

6. LangChain Documentation — https://python.langchain.com/docs/

7. ChromaDB Documentation — https://docs.trychroma.com/

8. Sentence-Transformers Documentation — https://www.sbert.net/

9. OpenAI API Documentation — https://platform.openai.com/docs/

10. Next.js Documentation — https://nextjs.org/docs/

11. FastAPI Documentation — https://fastapi.tiangolo.com/

12. React Documentation — https://react.dev/

13. Tailwind CSS Documentation — https://tailwindcss.com/docs/

### Ressources écosystème startup

14. Partech Africa — « Africa Tech Venture Capital Report » — https://partechpartners.com/

15. Maroc PME — Programmes d'appui aux startups — https://www.marocpme.gov.ma/

16. Tamwilcom — Instruments de financement — https://www.tamwilcom.ma/

17. StartupMaroc — Écosystème entrepreneurial marocain — https://startupmaroc.org/

18. Bank Al-Maghrib — Réglementation bancaire — https://www.bkam.ma/

19. CNDP — Commission Nationale de Contrôle de la Protection des Données — https://www.cndp.ma/

---
---

## ANNEXES

### Annexe A : Structure des données JSON

#### A.1 Structure d'un investisseur (`investors.json`)

```json
{
  "id": "INV_001",
  "name": "CDG Invest",
  "type": "VC",
  "description": "Fonds d'investissement filiale de la CDG...",
  "sectors": ["fintech", "healthtech", "edtech", "agritech"],
  "stage": ["seed", "series-a", "series-b"],
  "ticket_min": 5000000,
  "ticket_max": 100000000,
  "currency": "MAD",
  "geography": ["Maroc", "Afrique du Nord"],
  "criteria": {
    "description": "Startups avec traction prouvée et équipe solide"
  },
  "portfolio_examples": ["Chari", "WafR"],
  "contact": {
    "website": "https://cdginvest.ma",
    "linkedin": "https://linkedin.com/company/cdg-invest"
  }
}
```

#### A.2 Structure d'une subvention (`grants.json`)

```json
{
  "id": "GRANT_001",
  "name": "Innov Start",
  "country": "Maroc",
  "organization": "Tamwilcom",
  "type": "pret_honneur",
  "amount_min": 50000,
  "amount_max": 400000,
  "currency": "MAD",
  "eligibility": {
    "stage": ["pre-seed", "seed"],
    "sectors": ["tous secteurs innovants"],
    "age_max_company": "5 ans",
    "conditions": ["Entreprise innovante", "Siège social au Maroc"]
  },
  "deadline_type": "rolling"
}
```

#### A.3 Structure d'une métrique (`metrics_reference.json`)

```json
{
  "id": "MRR",
  "name": "Monthly Recurring Revenue",
  "name_fr": "Revenu Mensuel Récurrent",
  "definition": "Revenu mensuel récurrent provenant des abonnements",
  "formula": "Somme des revenus récurrents mensuels",
  "unit": "currency",
  "weight_in_scoring": 0.15,
  "benchmarks": {
    "pre_seed": { "bad": "<500", "ok": "500-2000", "good": "2000-5000", "excellent": ">5000" },
    "seed": { "..." },
    "serie_a": { "..." }
  },
  "benchmarks_mad": { "seed": { "..." } },
  "interpretation": "Mesure la traction commerciale récurrente",
  "improvement_tips": [
    "Convertir les clients one-shot en abonnements",
    "Augmenter le panier moyen via l'upsell"
  ],
  "related_metrics": ["ARR", "CHURN_RATE"]
}
```

#### A.4 Structure d'une FAQ (`faq.json`)

```json
{
  "id": 1,
  "categorie": "levee_de_fonds",
  "question": "C'est quoi une levée de fonds ?",
  "reponse": "Une levée de fonds consiste à...",
  "tags": ["levée", "financement", "equity"],
  "difficulte": "débutant"
}
```

### Annexe B : Liste des guides de fundraising

| # | Fichier | Lignes | Contenu |
|---|---------|--------|---------|
| 1 | `types_financement.md` | 576 | 10 types : love money, bootstrapping, BA, VC seed, série A, série B+, crowdfunding, RBF, prêts, subventions |
| 2 | `pitch_deck.md` | 559 | Structure 12-20 slides, métriques par stade, formats 3/7/20 min |
| 3 | `etapes_levee.md` | 600 | 6 étapes : préparation, prospection, due diligence, term sheet, closing, post-closing |
| 4 | `term_sheet.md` | 647 | Valorisation, liquidation preference, anti-dilution, vesting, ESOP, board, red flags |
| 5 | `valorisation.md` | 582 | 6 méthodes : revenue multiples, DCF, scorecard, Berkus, VC method, risk factor summation |
| 6 | `erreurs_courantes.md` | 596 | 20 erreurs fatales avec benchmarks, exemples et solutions |

### Annexe C : Liste des documents réglementaires

| # | Fichier | Lignes | Contenu |
|---|---------|--------|---------|
| 1 | `creation_entreprise_maroc.md` | 456 | SARL (Loi 5-96), SA (Loi 17-95), SAS (Loi 19-20), auto-entrepreneur, CRI, CFC |
| 2 | `fintech_maroc.md` | 380 | BAM (Loi 103-12), établissement de paiement (5M MAD capital), sandbox, crowdfunding (AMMC), KYC |
| 3 | `fiscalite_startup.md` | 604 | IS 10-35% Maroc vs 25% France, CFC, zones franches, JEI, CIR, convention fiscale |
| 4 | `rgpd.md` | 381 | RGPD (UE 2016/679) vs Loi 09-08 (Maroc), CNDP vs CNIL, DPO, sanctions |

### Annexe D : Détail des investisseurs par type

| Type | Nombre | Exemples |
|------|--------|----------|
| Fonds VC | 26 | CDG Invest, 212 Founders, Partech Africa, TLcom Capital, Azur Innovation Fund |
| Accélérateurs | 6 | Y Combinator, Techstars, 500 Global, Flat6Labs, Plug and Play |
| Fonds publics | 3 | Mohammed VI Fund, Tamwilcom, Innov Invest |
| Corporate VC | 2 | UM6P Ventures, OCP Group |
| Business Angels | 2 | Kalys Ventures, Kima Ventures |
| Growth funds | 2 | SEAF Morocco, AfricInvest |

### Annexe E : Variables d'environnement (`.env`)

```
OPENAI_API_KEY=sk-proj-...
LLM_MODEL=gpt-3.5-turbo
EMBEDDING_MODEL=paraphrase-multilingual-MiniLM-L12-v2
CHROMA_PERSIST_DIR=./chroma_db
CHUNK_SIZE=500
CHUNK_OVERLAP=50
TOP_K=5
DATASET_DIR=./dataset
```

---

*Rapport rédigé dans le cadre du Projet de Fin d'Année — Filière Data Science et Intelligence Artificielle — ENSAM Rabat — Année Universitaire 2025-2026*
