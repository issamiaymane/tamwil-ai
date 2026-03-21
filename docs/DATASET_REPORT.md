# Tamwil AI â Présentation du Dataset

**Base de connaissances centrée sur l'écosystème startup marocain, incluant les options de financement internationales accessibles aux fondateurs marocains (France, Afrique, MENA).**

**Projet de Fin d'Année 2025-2026**

---

## 1. Introduction

Dans le cadre du projet **Tamwil AI**, nous avons constitué une base de connaissances centrée sur l'écosystème startup marocain, incluant les options de financement internationales accessibles aux fondateurs marocains (France, Afrique, MENA). Ce dataset alimente les cinq fonctionnalités du chatbot : scoring de fundability, diagnostic financier, matching investisseurs, recommandation de subventions, et Q&A conversationnel (RAG).

L'ensemble des données a été **construit manuellement** à partir de sources officielles et vérifiées, sans recours au scraping automatique, afin de garantir la qualité, la pertinence et l'adaptation au contexte local.

---

## 2. Vue d'ensemble

| Composant | Format | Enregistrements | Taille |
|-----------|--------|-----------------|--------|
| Base investisseurs | JSON | 41 profils | 55 KB |
| Base subventions | JSON | 25 programmes | 36 KB |
| Référentiel métriques | JSON | 18 KPIs | 48 KB |
| Base FAQ | JSON | 54 Q&A | 62 KB |
| Guides fundraising | Markdown | 6 fichiers (3 554 lignes) | 176 KB |
| Documents réglementaires | Markdown | 4 fichiers (1 817 lignes) | 100 KB |
| **Total** | | **138 entrées + 10 documents** | **~521 KB** |

**Langue principale** : français | **Couverture géographique** : Maroc, France, Afrique, International

---

## 3. Base Investisseurs — 41 profils

### 3.1 Répartition par type

| Type | Nombre | Exemples |
|------|--------|----------|
| **VC (Capital-risque)** | 26 | CDG Invest, 212 Founders, Partech Africa, TLcom Capital, STV, BECO Capital, Wamda Capital |
| **Accélérateur** | 6 | Y Combinator, Techstars, 500 Global, Flat6Labs, Seedstars, Plug and Play |
| **Fonds public** | 3 | Fonds Mohammed VI, Tamwilcom, Innov Invest |
| **CVC (Corporate VC)** | 2 | UM6P Ventures, R&D Maroc (OCP Group) |
| **Business Angel** | 2 | Kalys Ventures, Kima Ventures |
| **Fonds de croissance** | 2 | SEAF Morocco, AfricInvest |

### 3.2 Répartition géographique

| Zone | Investisseurs | Exemples |
|------|---------------|----------|
| **Maroc** | 12 | CDG Invest, 212 Founders, MNF, Azur Innovation Fund, MITC Capital |
| **Pan-africain** | 8 | Partech Africa, TLcom Capital, Launch Africa, Saviu Ventures |
| **France / Europe** | 10 | Breega, Elaia Partners, Eurazeo, XAnge, Serena Capital, Alven |
| **International** | 8 | Y Combinator, Techstars, 500 Global, Cathay Innovation |
| **MENA / Golfe** | 3 | STV (Arabie Saoudite), BECO Capital (EAU), Wamda Capital (EAU) |

### 3.3 Secteurs couverts (28 secteurs)

`fintech` · `SaaS` · `e-commerce` · `healthtech` · `edtech` · `agritech` · `cleantech` · `logistique` · `deeptech` · `biotech` · `intelligence artificielle` · `cybersecurité` · `enterprise software` · `marketplace` · `mobile` · `TIC` · `infrastructure` · `technologie` · `industrie` · `services financiers` · `immobilier` · `mining tech` · `énergie` · `santé` · `éducation` · `biens de consommation` · `agribusiness` · `offshoring`

### 3.4 Stades d'investissement

`pre-seed` → `seed` → `série A` → `série B+` → `growth`

### 3.5 Structure d'un profil investisseur

Chaque profil contient les champs suivants :

| Champ | Description | Exemple |
|-------|-------------|---------|
| `id` | Identifiant unique | `INV_001` |
| `name` | Nom de l'investisseur | CDG Invest |
| `type` | Catégorie | VC, BA, Accelerator, Public Fund, CVC |
| `description` | Présentation détaillée | Texte de 3 à 5 lignes |
| `sectors` | Secteurs d'investissement | `["fintech", "SaaS", "healthtech"]` |
| `stage` | Stades ciblés | `["seed", "série A"]` |
| `ticket_min` / `ticket_max` | Fourchette d'investissement | 3 000 000 – 10 000 000 MAD |
| `currency` | Devise | MAD, EUR, USD |
| `geography` | Zone géographique | `["Maroc", "Afrique"]` |
| `criteria` | Critères d'investissement | Description textuelle |
| `portfolio_examples` | Exemples de portfolio | `["Chari", "WafR", "Dabadoc"]` |
| `contact` | Coordonnées | Site web + LinkedIn |
| `sources` | Références | URLs des sources utilisées |

### 3.6 Exemple : profil de 212 Founders

```json
{
  "id": "INV_002",
  "name": "212 Founders",
  "type": "VC",
  "description": "Fonds de capital-risque marocain lancé par CDG Invest, dédié au financement de startups technologiques en phase d'amorçage et de croissance au Maroc.",
  "sectors": ["fintech", "SaaS", "e-commerce", "healthtech", "edtech", "logistique"],
  "stage": ["seed", "série A"],
  "ticket_min": 3000000,
  "ticket_max": 10000000,
  "currency": "MAD",
  "geography": ["Maroc"],
  "criteria": {
    "description": "Startups technologiques marocaines avec un MVP validé, une traction initiale et une équipe fondatrice solide."
  },
  "portfolio_examples": ["Chari", "Épicerie Verte", "WafR", "Dabadoc"],
  "contact": {
    "website": "https://www.212founders.com/",
    "linkedin": "https://www.linkedin.com/company/212founders/"
  }
}
```

---

## 4. Base Subventions — 25 programmes

### 4.1 Répartition par pays

| Pays | Nombre | Programmes |
|------|--------|------------|
| **Maroc** | 9 | Innov Start, Tech Boost, Tech Scale, FORSA, INTILAKA, Istitmar PME, Istitmar TPE, Tamwilcom Garanties, 1000 Fikra |
| **France** | 8 | Bourse French Tech, Bourse FT Emergence, Concours i-Nov, CIR, CII, JEI, Innov'up, ACRE |
| **International** | 8 | Tony Elumelu Foundation, EIC Accelerator, Google for Startups Africa, Mastercard Foundation, Orange Digital Center, GSMA Innovation Fund, AfDB Boost Africa, French Tech Tremplin |

### 4.2 Types de financement

| Type | Nombre | Description |
|------|--------|-------------|
| Prêt d'honneur | 8 | Sans intérêt et sans garantie personnelle |
| Subvention | 7 | Financement non remboursable |
| Crédit d'impôt | 2 | Réduction fiscale (CIR, CII) |
| Statut fiscal | 2 | Exonérations (JEI, ACRE) |
| Garantie | 1 | Garantie bancaire |
| Accompagnement | 1 | Programme de formation et coaching (1000 Fikra) |
| Crédit taux zéro | 1 | Prêt sans intérêt |
| Concours | 1 | Financement par compétition |

### 4.3 Fourchettes de montants

| Programme | Montant min | Montant max | Devise |
|-----------|-------------|-------------|--------|
| Innov Start | 50 000 | 400 000 | MAD |
| Tech Boost | 200 000 | 750 000 | MAD |
| Tech Scale | 500 000 | 3 000 000 | MAD |
| FORSA | 10 000 | 100 000 | MAD |
| INTILAKA | 50 000 | 1 200 000 | MAD |
| Istitmar PME | 1 000 000 | 10 000 000 | MAD |
| Bourse French Tech | 10 000 | 30 000 | EUR |
| Concours i-Nov | 100 000 | 5 000 000 | EUR |
| EIC Accelerator | 2 500 000 | 17 500 000 | EUR |
| GSMA Innovation Fund | 100 000 | 250 000 | USD |

### 4.4 Structure d'un programme de subvention

| Champ | Description |
|-------|-------------|
| `id` | Identifiant unique (GRANT_001) |
| `name` | Nom du programme |
| `country` | Pays d'origine |
| `organization` | Organisme gestionnaire |
| `type` | Type de financement |
| `description` | Présentation détaillée |
| `amount_min` / `amount_max` | Fourchette de financement |
| `currency` | Devise |
| `eligibility` | Critères d'éligibilité (stade, secteurs, âge max, conditions) |
| `application_process` | Processus de candidature |
| `deadline_type` | Type de deadline (rolling / fixe) |
| `deadline_info` | Informations détaillées sur les dates et fenêtres de candidature |
| `website` | Site officiel |
| `sources` | Références |

### 4.5 Exemple : Innov Start (Tamwilcom)

```json
{
  "id": "GRANT_001",
  "name": "Innov Start",
  "country": "Maroc",
  "organization": "Tamwilcom (Fonds Innov Invest)",
  "type": "pret_honneur",
  "amount_min": 50000,
  "amount_max": 400000,
  "currency": "MAD",
  "eligibility": {
    "stage": ["pre-seed", "seed"],
    "sectors": ["tous secteurs innovants"],
    "age_max_company": "5 ans",
    "conditions": [
      "Startup marocaine a caractere innovant",
      "Etre accompagne par une structure labellisee Tamwilcom",
      "Projet post-preuve de concept (POC)"
    ]
  },
  "deadline_type": "rolling"
}
```

---

## 5. Référentiel Métriques — 18 KPIs

### 5.1 Liste des métriques par catégorie

| Catégorie | Métriques |
|-----------|-----------|
| **Revenus** | MRR (Revenu Mensuel Récurrent), ARR (Revenu Annuel Récurrent), MRR Growth Rate |
| **Unit Economics** | CAC (Coût d'Acquisition Client), LTV (Valeur Vie Client), Ratio LTV/CAC, CAC Payback Period, Gross Margin, Unit Economics |
| **Opérationnel** | Burn Rate, Runway, Churn Rate (Logo Churn), Revenue Churn / NRR |
| **Marketplace** | GMV (Volume Brut de Marchandises), Take Rate |
| **Fintech** | TPV (Total Payment Volume) |
| **Engagement** | DAU/MAU (Stickiness Ratio) |
| **Satisfaction** | NPS (Net Promoter Score) |

### 5.2 Système de benchmarks

Chaque métrique dispose de **benchmarks à 4 niveaux** pour **4 stades** de maturité :

| Niveau | Signification |
|--------|---------------|
| `bad` | Performance insuffisante, action urgente requise |
| `ok` | Performance acceptable, axe d'amélioration |
| `good` | Bonne performance, critère satisfait |
| `excellent` | Performance exceptionnelle, avantage compétitif |

**Stades couverts** : `pre_seed`, `seed`, `serie_a`, `serie_b`

### 5.3 Benchmarks en MAD

7 métriques monétaires disposent de benchmarks convertis en MAD (taux 1 EUR = 10.5 MAD) : MRR, ARR, CAC, LTV, BURN_RATE, GMV, TPV. Ces benchmarks sont indexés dans ChromaDB pour répondre aux requêtes en dirhams.

### 5.4 Exemple : MRR (Monthly Recurring Revenue)

| Stade | Bad | OK | Good | Excellent |
|-------|-----|----|------|-----------|
| **Pre-seed** | <500€/mois | 500-2 000€ | 2 000-5 000€ | >5 000€ |
| **Seed** | <5 000€/mois | 5 000-15 000€ | 15 000-50 000€ | >50 000€ |
| **Série A** | <50 000€/mois | 50 000-150 000€ | 150 000-500 000€ | >500 000€ |
| **Série B** | <500 000€/mois | 500 000-1,5M€ | 1,5M-5M€ | >5M€ |

### 5.5 Structure d'une métrique

Chaque métrique contient :

| Champ | Contenu |
|-------|---------|
| `id` / `name` / `name_fr` | Identifiant et noms (EN/FR) |
| `definition` | Définition détaillée (3 à 5 lignes) |
| `formula` | Formule de calcul avec exemples |
| `unit` | Unité (currency, percentage, ratio, months, score) |
| `applicable_sectors` | Secteurs concernés |
| `benchmarks` | Seuils par stade (bad/ok/good/excellent) |
| `benchmarks_mad` | Seuils convertis en MAD (×10.5) pour métriques monétaires |
| `interpretation` | Guide d'interprétation avec sources (SaaS Capital 2025, Bessemer Cloud 100) |
| `improvement_tips` | 4 à 6 conseils d'amélioration actionables |
| `related_metrics` | Métriques corrélées |
| `sources` | Références académiques et industrielles |

### 5.6 Secteurs applicables (14)

`SaaS` · `abonnement` · `marketplace` · `e-commerce` · `fintech` · `enterprise software` · `healthtech` · `edtech` · `agritech` · `logistique` · `mobile money` · `consumer tech` · `deeptech` · `tous`

---

## 6. Base FAQ — 54 Questions/Réponses

### 6.1 Répartition par catégorie

| Catégorie | Nombre | Thèmes couverts |
|-----------|--------|-----------------|
| **Levée de fonds** | 12 | Fonctionnement, timing, stades, pitch deck, term sheet, SAFE, négociation |
| **Métriques** | 9 | MRR, CAC, LTV, churn, burn rate, ratio LTV/CAC, payback period |
| **Subventions** | 8 | Innov Invest, FORSA, aides publiques Maroc, financement non-dilutif |
| **Réglementation Maroc** | 6 | SARL, SA, SAS (Loi 19-20), procédures de création |
| **Fiscalité** | 5 | IS, TVA, charges sociales, avantages fiscaux startups |
| **Écosystème** | 5 | Incubateurs, accélérateurs, réseau entrepreneurial marocain |
| **Fintech** | 3 | Réglementation BAM, agrément, capital minimum |
| **Réglementation France** | 2 | Statuts JEI, comparaison France/Maroc |
| **Propriété intellectuelle** | 2 | OMPIC, marques, brevets, protection logiciel (BMDA, Loi 2-00) |
| **Ressources humaines** | 2 | Code du Travail, SMIG, CNSS, recrutement tech, salaires dev |

### 6.2 Répartition par niveau de difficulté

| Niveau | Nombre | Description |
|--------|--------|-------------|
| **Débutant** | 22 | Concepts fondamentaux, questions de base |
| **Intermédiaire** | 22 | Analyse approfondie, cas pratiques |
| **Avancé** | 10 | Term sheets, négociations complexes, fiscalité avancée |

### 6.3 Exemple d'entrée FAQ

```json
{
  "id": 1,
  "categorie": "levee_de_fonds",
  "question": "C'est quoi une levée de fonds et comment ça fonctionne pour une startup marocaine ?",
  "reponse": "Une levée de fonds consiste à ouvrir le capital de sa startup à des investisseurs externes en échange de parts de la société. Au Maroc, les levées en seed se situent entre 1 et 10 millions MAD via des fonds comme CDG Invest, 212 Founders ou Outlierz Ventures...",
  "tags": ["levée", "financement", "capital", "investisseurs", "basics"],
  "difficulte": "débutant",
  "sources": ["https://innovinvest.ma/", "https://www.cdginvest.ma/"]
}
```

---

## 7. Guides et Documentation

### 7.1 Guides de fundraising (6 fichiers — 3 554 lignes)

| Fichier | Lignes | Contenu |
|---------|--------|---------|
| `types_financement.md` | 575 | Love money, bootstrapping, subventions, prêts bancaires, VC, business angels, crowdfunding. Montants réels du marché marocain et européen. |
| `pitch_deck.md` | 558 | Structure 10-15 slides, contenu par slide, conseils pour investisseurs marocains vs internationaux. |
| `etapes_levee.md` | 599 | Préparation, sourcing (50-100 contacts), due diligence, négociation, closing. Timeline : 6-12 mois (France), 8-14 mois (Maroc). |
| `term_sheet.md` | 646 | Valorisation pre/post-money, préférences de liquidation, clauses anti-dilution, droits de gouvernance. |
| `valorisation.md` | 581 | Méthode des comparables (5-15x ARR pour SaaS), méthode scorecard, méthode VC, multiples spécifiques au marché marocain. |
| `erreurs_courantes.md` | 595 | Pièges à éviter : lever trop tôt, sur-évaluation, dilution excessive, mauvaise gestion du cash. |
| **Total** | **3 554** | |

### 7.2 Documents réglementaires (4 fichiers — 1 817 lignes)

| Fichier | Lignes | Contenu |
|---------|--------|---------|
| `creation_entreprise_maroc.md` | 455 | SARL, SA, SAS (Loi 19-20 de 2022), capital minimum, procédures d'immatriculation, régimes fiscaux (IS à partir de 10%, CGI 2025). |
| `fiscalite_startup.md` | 603 | IS par tranches, TVA, charges sociales, régimes spéciaux pour startups innovantes, déductions et amortissements accélérés. |
| `fintech_maroc.md` | 379 | Agrément Bank Al-Maghrib (BAM), établissements de paiement, obligations AML/KYC, capital minimum 5M MAD. |
| `rgpd.md` | 380 | Protection des données au Maroc (Loi 09-08), CNDP, droits des personnes concernées, sanctions. |
| **Total** | **1 817** | |

---

## 8. Mapping Dataset → Fonctionnalités

Chaque source de données alimente une ou plusieurs fonctionnalités du chatbot :

```
investors.json ──────────→ Matching investisseurs + Scoring fundability
grants.json ────────────→ Matching subventions
metrics_reference.json ─→ Scoring fundability + Diagnostic financier
faq.json ───────────────→ Q&A conversationnel (RAG)
fundraising_guide/*.md ─→ Q&A conversationnel (RAG)
regulations/*.md ───────→ Q&A conversationnel (RAG)
```

| Fonctionnalité | Données JSON (rule-based) | Données Markdown (RAG) |
|---------------|--------------------------|--------------------------|
| **Scoring fundability** | `metrics_reference.json` + `investors.json` | — |
| **Diagnostic financier** | `metrics_reference.json` | — |
| **Matching investisseurs** | `investors.json` | — |
| **Matching subventions** | `grants.json` | — |
| **Q&A conversationnel** | `faq.json` | Guides + Réglementations |

---

## 9. Méthodologie de construction

### 9.1 Approche

Le dataset a été entièrement **curé manuellement**. Ce choix se justifie par :

- **Qualité des données** : les informations sur les investisseurs marocains et les subventions locales ne sont pas disponibles dans des bases de données structurées (contrairement à Crunchbase pour les marchés US/EU)
- **Adaptation au contexte local** : les benchmarks de métriques ont été ajustés pour le marché marocain (seuils 30-50% inférieurs aux benchmarks américains)
- **Langue française** : les FAQ et guides sont rédigés directement en français, la langue des utilisateurs cibles
- **Fiabilité** : chaque entrée inclut un champ `sources` traçant l'origine de l'information

### 9.2 Sources utilisées

| Catégorie | Sources |
|-----------|---------|
| **Investisseurs** | Sites officiels des fonds (CDG Invest, 212 Founders, Partech...), LinkedIn, rapports AMIC, Partech Africa Reports |
| **Subventions** | Tamwilcom, Innov Invest, Bpifrance, portails gouvernementaux |
| **Métriques** | SaaS Capital 2025, Bessemer Cloud 100, SaaStr, OpenView Partners |
| **Réglementation** | CGI 2025, Bank Al-Maghrib, CNDP, législation marocaine (dahirs et lois) |
| **Fundraising** | Y Combinator Library, First Round Capital, Atomico |

### 9.3 Contrôle qualité

- Vérification de la présence de tous les champs obligatoires via le module `data_loader.py`
- Validation automatique à chaque chargement avec logs structurés
- Cross-référencement entre les données (ex : investisseurs cités dans les FAQ correspondent aux profils de `investors.json`)

---

*Document préparé dans le cadre du Projet de Fin d'Année — Année Universitaire 2025-2026*
