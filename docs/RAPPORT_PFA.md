# RAPPORT DE PROJET DE FIN D'ANNÉE (PFA)

---

## PAGE DE GARDE

---

**[Nom de l'Université / École]**

**[Nom de la Filière / Département]**

---

### Projet de Fin d'Année

**Année Universitaire : 2025 – 2026**

---

### Tamwil AI — Chatbot RAG de Recommandation Financière pour Startups

---

**Réalisé par :**
- [Nom et Prénom de l'étudiant 1]
- [Nom et Prénom de l'étudiant 2]

**Encadré par :**
- [Nom et Prénom de l'encadrant]

---

**Soutenu le : [Date de soutenance]**

---
---

## REMERCIEMENTS

Nous tenons à exprimer notre profonde gratitude à notre encadrant **[Nom de l'encadrant]** pour ses conseils précieux, son suivi rigoureux et son accompagnement tout au long de ce projet.

Nous remercions également l'ensemble du corps professoral de **[Nom de l'école/université]** pour la formation de qualité qui nous a permis d'acquérir les compétences nécessaires à la réalisation de ce travail.

Nos remerciements vont aussi à nos familles et proches pour leur soutien moral et leurs encouragements constants.

Enfin, nous remercions toutes les personnes qui, de près ou de loin, ont contribué à l'aboutissement de ce projet.

---
---

## RÉSUMÉ

Les fondateurs de startups au Maroc et en Afrique francophone font face à un manque criant d'accès à l'information financière structurée. Les réponses à des questions essentielles — quel type de financement choisir, quels investisseurs cibler, suis-je prêt à lever des fonds — sont dispersées entre sites web, documents PDF et réseaux informels, souvent en anglais et inadaptées au contexte local.

**Tamwil AI** est un chatbot intelligent basé sur la technique **RAG (Retrieval-Augmented Generation)** qui combine une base de connaissances structurée sur l'écosystème startup marocain et francophone avec un modèle de langage (LLM) pour générer des réponses contextuelles et personnalisées. Le système offre cinq fonctionnalités principales : le scoring de « fundability » (évaluation de la préparation à la levée de fonds), le diagnostic financier, le matching avec des investisseurs, la recommandation de subventions, et un Q&A conversationnel alimenté par RAG.

Le projet repose sur une architecture hybride combinant un pipeline RAG vectoriel (pour les questions libres) et un système rule-based assisté par LLM (pour le scoring et le matching algorithmique). La stack technique inclut Python, LangChain, ChromaDB, sentence-transformers et l'API OpenAI.

**Mots-clés :** RAG, LLM, Chatbot, Finance startup, ChromaDB, LangChain, Embeddings, NLP, Maroc

---

## ABSTRACT

Startup founders in Morocco and French-speaking Africa face a significant lack of access to structured financial information. Answers to essential questions — which type of financing to choose, which investors to target, whether they are ready to raise funds — are scattered across websites, PDFs, and informal networks, often in English and not adapted to the local context.

**Tamwil AI** is an intelligent chatbot based on the **RAG (Retrieval-Augmented Generation)** technique that combines a structured knowledge base on the Moroccan and Francophone startup ecosystem with a large language model (LLM) to generate contextual and personalized responses. The system provides five core features: fundability scoring, financial diagnostics, investor matching, grant recommendations, and a RAG-powered conversational Q&A.

The project relies on a hybrid architecture combining a vector-based RAG pipeline (for free-form questions) with a rule-based system assisted by an LLM (for algorithmic scoring and matching). The tech stack includes Python, LangChain, ChromaDB, sentence-transformers, and the OpenAI API.

**Keywords:** RAG, LLM, Chatbot, Startup Finance, ChromaDB, LangChain, Embeddings, NLP, Morocco

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
  - 2.5 Diagramme de flux de données
- Chapitre 3 : Réalisation et Implémentation
  - 3.1 Environnement de développement
  - 3.2 Stack technique
  - 3.3 Constitution du dataset
  - 3.4 Implémentation du pipeline RAG
  - 3.5 Implémentation des modules métier
  - 3.6 Interface utilisateur
- Chapitre 4 : Tests et Résultats
  - 4.1 Scénarios de test
  - 4.2 Résultats obtenus
  - 4.3 Discussion et analyse
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
4. **Répond** aux questions libres sur la finance startup en s'appuyant sur des données fiables
5. **Communique** en français, la langue principale des utilisateurs cibles

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
1. Ingestion     → Chargement des documents sources (JSON, Markdown, PDF)
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
│           (Next.js + React 19)                       │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────┐
│              Orchestrateur / Router                   │
│   (Détection d'intention : scoring, matching,        │
│    Q&A, diagnostic, subventions)                     │
└──┬───────┬───────┬───────┬───────┬──────────────────┘
   │       │       │       │       │
   ▼       ▼       ▼       ▼       ▼
┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
│Score ││Diag. ││Match ││Grant ││ RAG  │
│Fund. ││Finan.││Invest││Match ││ Q&A  │
└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘
   │       │       │       │       │
   ▼       ▼       ▼       ▼       ▼
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
- **Données utilisées** : `metrics_reference.json` (principal) + `investors.json` (secondaire)
- **Logique** :
  1. Comparer chaque métrique aux benchmarks du stade correspondant (bad/ok/good/excellent)
  2. Calculer un score pondéré sur 100 en utilisant le champ `weight_in_scoring`
  3. Identifier les forces et faiblesses
  4. Générer un plan d'action personnalisé via le LLM
- **Sortie** : Score /100, détail par métrique, axes d'amélioration, plan d'action

#### Module 2 : Diagnostic Financier

- **Entrée** : KPIs individuels de l'utilisateur
- **Données utilisées** : `metrics_reference.json` (formules, benchmarks, interprétation, conseils)
- **Logique** : Analyser chaque KPI, comparer aux benchmarks, identifier les anomalies
- **Sortie** : Analyse détaillée avec recommandations d'amélioration

#### Module 3 : Matching Investisseurs

- **Entrée** : Profil startup (secteur, stade, géographie, métriques)
- **Données utilisées** : `investors.json` (41 profils)
- **Logique** :
  1. Filtrer par `sectors`, `stages`, `geography`
  2. Filtrer par `ticket_min/max` si montant recherché fourni
  3. Calculer un score de matching (nombre de critères satisfaits)
  4. Trier par pertinence
- **Sortie** : Top 5 investisseurs avec détails, critères spécifiques et contacts

#### Module 4 : Matching Subventions

- **Entrée** : Profil startup (secteur, stade, pays, ancienneté)
- **Données utilisées** : `grants.json` (25 programmes)
- **Logique** : Filtrer par `eligibility` (stages, secteurs, pays, âge maximum)
- **Sortie** : Liste des aides éligibles avec montants et deadlines

#### Module 5 : Q&A Conversationnel (RAG)

- **Entrée** : Question libre de l'utilisateur en français
- **Données utilisées** : `faq.json` + `fundraising_guide/*.md` + `regulations/*.md` (via ChromaDB)
- **Logique** :
  1. Embedding de la question avec le modèle multilingue
  2. Recherche des top-k chunks similaires dans ChromaDB
  3. Envoi des chunks + question au LLM
  4. Génération de la réponse en français
- **Sortie** : Réponse contextuelle basée sur la base de connaissances

### 2.3 Modèle de données

Le dataset a été constitué manuellement et contient environ **464 KB de données de qualité**, organisées comme suit :

#### Données structurées (JSON)

| Fichier | Enregistrements | Contenu |
|---------|----------------|---------|
| `investors.json` | 41 profils | Investisseurs (VC, BA, accélérateurs, fonds publics) avec critères d'investissement, tickets, secteurs, géographies |
| `grants.json` | 25 programmes | Subventions et aides (Maroc, France, International) avec critères d'éligibilité, montants |
| `metrics_reference.json` | 18 métriques | KPIs startup avec formules, benchmarks par stade (bad/ok/good/excellent), conseils |
| `faq.json` | 54 Q&A | Questions/réponses sur la finance startup, classées par catégorie et difficulté |

**Structure d'un profil investisseur :**
```json
{
  "id": "INV_001",
  "name": "CDG Invest",
  "type": "VC",
  "description": "...",
  "sectors": ["fintech", "healthtech"],
  "stage": ["seed", "series-a"],
  "ticket_min": 5000000,
  "ticket_max": 100000000,
  "currency": "MAD",
  "geography": ["Maroc", "Afrique"],
  "criteria": { "description": "..." },
  "portfolio_examples": ["Chari", "WafR"],
  "contact": { "website": "...", "linkedin": "..." }
}
```

**Structure d'une métrique de référence :**
```json
{
  "id": "MRR",
  "name": "Monthly Recurring Revenue",
  "definition": "...",
  "formula": "...",
  "unit": "currency",
  "benchmarks": {
    "pre_seed": { "bad": "<500€", "ok": "500-2000€", "good": "2000-5000€", "excellent": ">5000€" },
    "seed": { ... },
    "serie_a": { ... }
  },
  "interpretation": "...",
  "improvement_tips": [...]
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
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  2. Chunking     │  → RecursiveCharacterTextSplitter
│  (ingest.py)     │  → chunk_size=500, overlap=50
│                  │  → Séparateurs : titres, paragraphes, phrases
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  3. Embedding    │  → paraphrase-multilingual-MiniLM-L12-v2
│  (embeddings.py) │  → 384 dimensions, support français
│                  │  → Exécution locale (gratuit)
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
│  (rag_qa.py)     │  → Prompt = chunks + question
│                  │  → Réponse en français
└──────────────────┘
```

### 2.5 Mapping Dataset → Fonctionnalités

Chaque source de données alimente une ou plusieurs fonctionnalités spécifiques :

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
| Scoring | `metrics_reference.json` | `investors.json` | — |
| Diagnostic | `metrics_reference.json` | — | — |
| Matching investisseurs | `investors.json` | — | — |
| Matching subventions | `grants.json` | — | — |
| Q&A RAG | `faq.json` | — | guides + regulations |

---
---

## CHAPITRE 3 : RÉALISATION ET IMPLÉMENTATION

### 3.1 Environnement de développement

| Élément | Détail |
|---------|--------|
| Système d'exploitation | Windows 11 Pro |
| Langage | Python 3.11+ |
| IDE | Visual Studio Code |
| Gestionnaire de version | Git |
| Environnement virtuel | venv |

### 3.2 Stack technique

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| **Backend** | Python 3.11+ | Écosystème IA/NLP riche, nombreuses bibliothèques |
| **LLM** | OpenAI API (GPT-3.5-turbo) | Qualité de génération en français, API fiable |
| **Embeddings** | sentence-transformers (`paraphrase-multilingual-MiniLM-L12-v2`) | Gratuit, local, supporte le français, 384 dimensions |
| **Base vectorielle** | ChromaDB | Simple, léger, persistant, parfait pour un dataset de cette taille |
| **Pipeline RAG** | LangChain | Framework mature pour l'orchestration RAG |
| **Serveur API** | FastAPI + uvicorn | Framework Python moderne, asynchrone, avec documentation auto-générée |
| **Interface** | Next.js 16.1.6 + React 19 + Tailwind CSS 4 | Application web moderne avec chat conversationnel et dark mode |
| **Configuration** | python-dotenv | Gestion sécurisée des variables d'environnement |
| **Tokenisation** | tiktoken | Comptage précis des tokens pour les appels LLM |

**Dépendances principales (`requirements.txt`) :**

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

### 3.3 Constitution du dataset

Le dataset a été construit **manuellement** pour garantir la qualité et la pertinence des données au contexte marocain et francophone. Aucune source automatisée n'a été utilisée.

**Volume total** : ~521 KB de données structurées et non structurées.

| Source | Format | Volume | Contenu |
|--------|--------|--------|---------|
| `investors.json` | JSON | 41 profils | Investisseurs (VC, BA, accélérateurs, fonds publics) du Maroc et d'Afrique |
| `grants.json` | JSON | 25 programmes | Subventions et aides publiques (Maroc, France, International) |
| `metrics_reference.json` | JSON | 18 métriques | KPIs startup avec formules, benchmarks par stade, conseils |
| `faq.json` | JSON | 54 Q&A | Questions-réponses sur la finance startup |
| `fundraising_guide/` | Markdown | 6 guides (~3 554 lignes) | Types de financement, pitch deck, étapes de levée, term sheet, valorisation, erreurs courantes |
| `regulations/` | Markdown | 4 documents (~1 817 lignes) | Création d'entreprise, fintech, fiscalité, RGPD au Maroc |

### 3.4 Implémentation du pipeline RAG

#### 3.4.1 Configuration (`backend/app/config.py`)

Le module `config.py` centralise tous les paramètres du projet. Il charge les variables d'environnement depuis le fichier `.env` et exporte des constantes utilisées par tous les autres modules.

**Paramètres clés :**
- `OPENAI_API_KEY` : Clé API pour le LLM
- `LLM_MODEL` : Modèle utilisé (par défaut : `gpt-3.5-turbo`)
- `EMBEDDING_MODEL` : Modèle d'embedding (par défaut : `paraphrase-multilingual-MiniLM-L12-v2`)
- `CHROMA_PERSIST_DIR` : Répertoire de persistance ChromaDB (`./chroma_db`)
- `CHUNK_SIZE` : Taille des chunks (500 tokens)
- `CHUNK_OVERLAP` : Chevauchement entre chunks (50 tokens)
- `TOP_K` : Nombre de chunks à récupérer (5)
- Chemins vers tous les fichiers de données

#### 3.4.2 Chargement des données (`backend/app/utils/data_loader.py`)

Le module `data_loader.py` fournit une interface unifiée pour charger et valider toutes les sources de données :

- `load_investors()` → charge et valide les 41 profils d'investisseurs
- `load_grants()` → charge et valide les 25 programmes de subventions
- `load_metrics()` → charge et valide les 18 métriques de référence
- `load_faq()` → charge et valide les 54 Q&A
- `load_fundraising_guides()` → charge les 6 guides Markdown
- `load_regulations()` → charge les 4 documents réglementaires
- `load_all()` → charge l'ensemble des données en un seul appel

Chaque fonction vérifie la présence des champs obligatoires et fournit des logs structurés pour le debugging. Le module peut être exécuté en standalone pour valider l'intégrité de toutes les données.

#### 3.4.3 Ingestion et chunking (`backend/app/rag/ingest.py`)

Le module `ingest.py` transforme les documents bruts en chunks prêts pour la vectorisation :

1. **`_build_faq_documents()`** : Convertit les entrées JSON du FAQ en objets `Document` LangChain. Chaque document combine la question et la réponse dans un seul texte.

2. **`_build_markdown_documents()`** : Charge les fichiers Markdown depuis les répertoires (guides et réglementations) en objets `Document` avec métadonnées (nom du fichier source, type de document).

3. **`load_all_documents()`** : Charge l'ensemble des documents (FAQ + guides + réglementations).

4. **`chunk_documents()`** : Découpe les documents longs en passages de taille contrôlée en utilisant `RecursiveCharacterTextSplitter` de LangChain :
   - **Taille des chunks** : 500 tokens
   - **Chevauchement** : 50 tokens (préserve le contexte entre chunks adjacents)
   - **Séparateurs hiérarchiques** : titres (`##`, `###`), paragraphes (`\n\n`), phrases (`.`), mots (` `)

5. **`ingest()`** : Orchestre le pipeline complet (chargement → découpage), produisant ~100+ chunks prêts pour l'embedding.

#### 3.4.4 Modèle d'embedding (`backend/app/rag/embeddings.py`)

Le module `embeddings.py` configure le modèle d'embedding multilingue utilisé pour vectoriser les documents et les questions.

**Modèle choisi : `paraphrase-multilingual-MiniLM-L12-v2`**

| Caractéristique | Valeur |
|-----------------|--------|
| Dimensions | 384 |
| Langues supportées | 50+ (dont le français) |
| Taille du modèle | ~130 MB |
| Exécution | Locale (pas d'appel API) |
| Coût | Gratuit |
| Normalisation | Activée (pour la similarité cosinus) |

**Justification du choix** :
- Support natif du français, essentiel pour notre dataset francophone
- Exécution locale sans coût API, contrairement aux embeddings OpenAI
- Performance suffisante pour un dataset de cette taille
- Compatibilité avec LangChain via `HuggingFaceEmbeddings`

#### 3.4.5 Base vectorielle (`backend/app/rag/vectorstore.py`)

Le module `vectorstore.py` gère l'initialisation et la persistance de ChromaDB :

- **`build_vectorstore()`** : Pipeline complet de construction :
  1. Supprime les anciennes données (si existantes)
  2. Ingère tous les documents via `ingest.py`
  3. Vectorise les chunks avec le modèle d'embedding
  4. Stocke dans ChromaDB (backend SQLite)
  5. Persiste sur le disque

- **`get_vectorstore()`** : Charge la base vectorielle existante depuis le disque, sans réindexation. Cela permet un démarrage rapide de l'application.

**Configuration ChromaDB :**
- Collection : `tamwil_knowledge_base`
- Backend : SQLite (`chroma.sqlite3`)
- Taille : ~7.3 MB après indexation
- Contenu : texte du chunk + vecteur 384D + métadonnées (source, type)

#### 3.4.6 Moteur de recherche sémantique (`backend/app/rag/retriever.py`)

Le module `retriever.py` est le moteur de recherche du système :

- **`retrieve(query, k, filter_type)`** :
  1. Convertit la question en vecteur via le modèle d'embedding
  2. Effectue une recherche par similarité cosinus dans ChromaDB
  3. Retourne les k chunks les plus similaires (k=5 par défaut)
  4. Supporte le filtrage par type de document (faq, fundraising_guide, regulation)

- **`retrieve_with_scores()`** : Variante qui inclut les scores de similarité pour chaque résultat.

### 3.5 Structure du projet

```
tamwil-ai/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py                 # Configuration centralisée
│   │   ├── main.py                   # Serveur FastAPI (POST /api/chat, GET /health)
│   │   ├── router.py                 # Orchestrateur / détection d'intention (regex + mots-clés)
│   │   ├── modules/                  # Modules métier
│   │   │   ├── __init__.py
│   │   │   ├── scoring.py            # Scoring de fundability
│   │   │   ├── diagnostic.py         # Diagnostic financier
│   │   │   ├── matching_investors.py # Matching investisseurs
│   │   │   ├── matching_grants.py    # Matching subventions
│   │   │   └── rag_qa.py             # Q&A conversationnel (RAG + LLM)
│   │   ├── rag/                      # Pipeline RAG
│   │   │   ├── __init__.py
│   │   │   ├── ingest.py             # Ingestion et chunking
│   │   │   ├── embeddings.py         # Modèle d'embedding
│   │   │   ├── vectorstore.py        # ChromaDB
│   │   │   └── retriever.py          # Recherche sémantique
│   │   └── utils/
│   │       ├── __init__.py
│   │       └── data_loader.py        # Chargement et validation des données
│   ├── __init__.py
│   └── .env                          # Variables d'environnement
├── dataset/                          # Base de connaissances
│   ├── investors/investors.json      # 41 profils d'investisseurs
│   ├── grants/grants.json            # 25 programmes de subventions
│   ├── metrics/metrics_reference.json # 18 KPIs avec benchmarks
│   ├── faq/faq.json                  # 54 Q&A
│   ├── fundraising_guide/            # 6 guides Markdown (~3 554 lignes)
│   └── regulations/                  # 4 documents réglementaires (~1 817 lignes)
├── chroma_db/                        # Base vectorielle persistante
├── frontend/                         # Interface Next.js (React 19 + Tailwind CSS 4)
│   ├── src/
│   │   ├── app/                      # Pages Next.js (App Router)
│   │   ├── components/               # Composants React (chat, sidebar, profil)
│   │   └── lib/                      # API client, types, constantes
│   ├── package.json
│   └── tsconfig.json
├── tests/                            # Tests unitaires (pytest)
│   ├── test_scoring.py
│   ├── test_diagnostic.py
│   ├── test_matching_investors.py
│   ├── test_matching_grants.py
│   ├── test_router.py
│   └── test_rag.py
├── requirements.txt                  # Dépendances Python
├── PROJET_TAMWIL_AI.md              # Spécification du projet
└── DEVELOPMENT_PLAN.md              # Plan de développement
```

### 3.6 Règles de développement

1. **Langue** : Le code est écrit en anglais, mais les prompts LLM, les réponses utilisateur et les données sont en français
2. **Pas d'hallucination** : Le chatbot ne répond que sur la base des données fournies via RAG, il ne doit jamais inventer d'informations
3. **Modularité** : Chaque module est indépendant et testable séparément
4. **Gestion d'erreurs** : Gestion gracieuse des données manquantes ou insuffisantes
5. **ChromaDB persistant** : Pas de réindexation à chaque lancement de l'application

---
---

## CHAPITRE 4 : TESTS ET RÉSULTATS

### 4.1 Scénarios de test

Cinq scénarios de test ont été définis pour valider les fonctionnalités principales du système :

| # | Scénario | Entrée utilisateur | Sortie attendue |
|---|----------|-------------------|-----------------|
| 1 | Scoring de fundability | "MRR: 8000€, burn rate: 15000€, churn: 5%, stade: seed" | Score ~58/100, axes d'amélioration, plan d'action |
| 2 | Diagnostic financier | "CAC: 200€, LTV: 400€, churn: 8%" | "Ratio LTV/CAC=2 (faible), churn élevé, voici comment améliorer..." |
| 3 | Matching investisseurs | "Fintech, seed, Maroc, MRR 10K€" | Top 5 investisseurs pertinents avec critères et contacts |
| 4 | Matching subventions | "Startup edtech, 2 ans, Maroc" | Liste des aides éligibles avec montants et deadlines |
| 5 | Q&A conversationnel | "Comment valoriser ma startup en pré-seed ?" | Réponse détaillée basée sur les guides de valorisation |

### 4.2 Tests du pipeline RAG

#### Test de l'ingestion des données

Le module `data_loader.py` a été exécuté en standalone pour valider le chargement de toutes les sources de données :

- 41 profils d'investisseurs chargés et validés
- 25 programmes de subventions chargés et validés
- 18 métriques de référence chargées et validées
- 54 Q&A chargés et validés
- 6 guides de fundraising chargés (Markdown)
- 4 documents réglementaires chargés (Markdown)

#### Test du chunking

Le module `ingest.py` a produit ~100+ chunks à partir de l'ensemble des documents, avec les paramètres configurés (chunk_size=500, overlap=50).

#### Test des embeddings

Le modèle `paraphrase-multilingual-MiniLM-L12-v2` génère des vecteurs de 384 dimensions. Un test qualitatif a été effectué pour vérifier la qualité des embeddings en français.

#### Test de la base vectorielle

ChromaDB a été construit et persisté sur le disque (~7.3 MB). Le chargement depuis le disque est quasi instantané, sans réindexation.

#### Test du retriever

Le moteur de recherche sémantique a été testé avec des requêtes en français. Les résultats sont pertinents et correctement ordonnés par similarité cosinus.

### 4.3 Discussion et analyse

**Points forts du système :**
- Le pipeline RAG fonctionne de bout en bout avec des résultats pertinents
- Les embeddings multilingues offrent une excellente compréhension du français
- ChromaDB persistant permet un démarrage rapide de l'application
- L'architecture modulaire facilite le développement itératif et les tests
- Le dataset original et adapté au contexte marocain est un atout différenciateur

**Limites identifiées :**
- Le dataset reste relativement petit (~521 KB) et pourrait être enrichi avec davantage d'investisseurs et de subventions
- La gestion des erreurs peut être renforcée dans certains cas limites
- Le LLM utilisé (GPT-3.5-turbo) pourrait être remplacé par un modèle plus performant (GPT-4)
- Le CORS est limité à localhost — une configuration production est nécessaire pour le déploiement
- Les tests d'intégration end-to-end ne couvrent pas encore tous les scénarios

---
---

## CONCLUSION GÉNÉRALE ET PERSPECTIVES

### Bilan du projet

Le projet Tamwil AI a permis de concevoir et d'implémenter un chatbot intelligent de recommandation financière, centré sur l'écosystème startup marocain et incluant les options de financement internationales accessibles aux fondateurs marocains (France, Afrique, MENA).

**Réalisations principales :**

1. **Constitution d'un dataset original** de ~521 KB couvrant l'écosystème startup marocain et francophone : 41 profils d'investisseurs, 25 programmes de subventions, 18 métriques financières, 54 Q&A, 6 guides de fundraising et 4 documents réglementaires.

2. **Implémentation complète du pipeline RAG** : ingestion des documents, chunking avec LangChain, embedding avec le modèle multilingue `paraphrase-multilingual-MiniLM-L12-v2` (384 dimensions), indexation dans ChromaDB, et recherche sémantique par similarité cosinus.

3. **Implémentation des cinq modules métier** : scoring de fundability, diagnostic financier, matching investisseurs, matching subventions, et Q&A conversationnel RAG — tous fonctionnels et testés.

4. **Développement de l'orchestrateur/router** : détection d'intention par regex et mots-clés, routage automatique vers le module approprié avec fallback vers le RAG Q&A.

5. **Mise en place du serveur FastAPI** : API REST avec endpoint `POST /api/chat` et `GET /health`, gestion CORS, formatage des réponses en Markdown.

6. **Construction de l'interface frontend Next.js** : application React 19 avec Tailwind CSS 4, sidebar avec historique de conversations, chat conversationnel avec dark mode, formulaire de profil startup, et connexion au backend FastAPI.

7. **Tests unitaires** : 6 fichiers de tests couvrant tous les modules (scoring, diagnostic, matching investisseurs, matching subventions, router, RAG).

### Compétences acquises

Ce projet nous a permis de développer des compétences dans plusieurs domaines :
- **NLP et LLMs** : compréhension des modèles de langage, des embeddings et de la technique RAG
- **Bases de données vectorielles** : utilisation de ChromaDB pour le stockage et la recherche de vecteurs
- **Ingénierie logicielle** : conception modulaire, gestion de configuration, chargement et validation de données
- **Écosystème Python IA** : maîtrise de LangChain, sentence-transformers, OpenAI API

### Perspectives d'amélioration

Plusieurs axes d'amélioration sont envisagés pour les versions futures du projet :

1. **Enrichir le dataset** : ajouter de nouveaux investisseurs, subventions et contenus éducatifs au-delà des 41 investisseurs et 25 subventions actuels
2. **Optimiser les prompts LLM** : améliorer la qualité et la cohérence des réponses générées en français
3. **Migration vers GPT-4 ou un modèle local** : augmenter la qualité des réponses tout en réduisant la dépendance à l'API OpenAI
4. **Tests d'intégration end-to-end** : valider le parcours complet utilisateur, du frontend à la réponse LLM
5. **Déploiement cloud** : rendre l'application accessible en ligne (Vercel pour le frontend Next.js, Railway/AWS pour le backend FastAPI)
6. **Multilinguisme étendu** : support de l'arabe (darija) pour toucher un public plus large au Maroc
7. **Historique et authentification** : persistance des conversations utilisateur et gestion des comptes
8. **Fonctionnalités Tier 2** : simulateur de runway, recommandation de type de financement, estimation de valorisation

---
---

## BIBLIOGRAPHIE ET WEBOGRAPHIE

### Articles scientifiques

1. Lewis, P., Perez, E., Piktus, A., et al. (2020). « Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks ». *Advances in Neural Information Processing Systems (NeurIPS 2020)*.

2. Vaswani, A., Shazar, N., Parmar, N., et al. (2017). « Attention Is All You Need ». *Advances in Neural Information Processing Systems (NeurIPS 2017)*.

3. Reimers, N. & Gurevych, I. (2019). « Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks ». *Proceedings of EMNLP-IJCNLP 2019*.

4. Brown, T., Mann, B., Ryder, N., et al. (2020). « Language Models are Few-Shot Learners ». *NeurIPS 2020*.

### Documentation technique

5. LangChain Documentation — https://python.langchain.com/docs/

6. ChromaDB Documentation — https://docs.trychroma.com/

7. Sentence-Transformers Documentation — https://www.sbert.net/

8. OpenAI API Documentation — https://platform.openai.com/docs/

9. Next.js Documentation — https://nextjs.org/docs/

10. FastAPI Documentation — https://fastapi.tiangolo.com/

### Ressources écosystème startup

11. Partech Africa — « Africa Tech Venture Capital Report » — https://partechpartners.com/

12. Maroc PME — Programmes d'appui aux startups — https://www.marocpme.gov.ma/

13. Tamwilcom — Instruments de financement — https://www.tamwilcom.ma/

14. StartupMaroc — Écosystème entrepreneurial marocain — https://startupmaroc.org/

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
  "definition": "Revenu mensuel récurrent provenant des abonnements",
  "formula": "Somme des revenus récurrents mensuels",
  "unit": "currency",
  "benchmarks": {
    "pre_seed": {
      "bad": "<500€/mois",
      "ok": "500-2000€/mois",
      "good": "2000-5000€/mois",
      "excellent": ">5000€/mois"
    },
    "seed": { "..." },
    "serie_a": { "..." }
  },
  "interpretation": "Mesure la traction commerciale récurrente",
  "improvement_tips": [
    "Convertir les clients one-shot en abonnements",
    "Augmenter le panier moyen via l'upsell"
  ]
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

| # | Fichier | Contenu |
|---|---------|---------|
| 1 | `types_financement.md` | Love money, bootstrapping, subventions, prêts bancaires, VC, business angels |
| 2 | `pitch_deck.md` | Structure d'un pitch deck, contenu de chaque slide, exemples et conseils |
| 3 | `etapes_levee.md` | Pré-lancement, sourcing investisseurs, due diligence, négociation, closing |
| 4 | `term_sheet.md` | Valorisation post-money, préférences de liquidation, dilution, clauses clés |
| 5 | `valorisation.md` | Méthode des comparables, DCF, méthode basée sur l'usage |
| 6 | `erreurs_courantes.md` | Pièges à éviter : lever trop tôt, mauvaise valorisation, dilution excessive |

### Annexe C : Liste des documents réglementaires

| # | Fichier | Contenu |
|---|---------|---------|
| 1 | `creation_entreprise_maroc.md` | Formes juridiques (SARL, SA, SAS), capital minimum, démarches |
| 2 | `fintech_maroc.md` | Agrément BAM, établissement de paiement, capital minimum 5M MAD |
| 3 | `fiscalite_startup.md` | IS (10-30%), TVA, charges sociales, avantages fiscaux startups |
| 4 | `rgpd.md` | Obligations de protection des données au Maroc, CNDP |

---

*Rapport rédigé dans le cadre du Projet de Fin d'Année — Année Universitaire 2025-2026*
