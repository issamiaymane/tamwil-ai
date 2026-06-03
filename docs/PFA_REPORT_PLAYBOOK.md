# PFA Report Playbook

> **Read this once, rebuild a PFA report for any project.**
>
> Frozen from the Tamwil~AI build (Apr~2026) that went through Mme Hafsa Khiyat's feedback loop at ENSAM Rabat. Every template is verbatim from a document that compiles to a 49-page PDF with zero LaTeX warnings.

---

## 0. TL;DR — bootstrap

To start a new PFA report:

```bash
# 1. Copy the reference skeleton
cp -r /home/aymane-issami/Desktop/tamwil-ai/docs/rapport/latex ~/my-new-pfa/

# 2. Clear old content but keep structure
cd ~/my-new-pfa
rm -rf chroma_db/ rapport.{aux,log,bbl,blg,toc,lof,lot,out,pdf}

# 3. Substitute 6 placeholders (§1 below) in:
#    - titlepage.tex
#    - preamble.tex (fancyhead right, footer year)
#    - frontmatter/remerciements.tex, resume.tex

# 4. Drop your logos in images/
#    images/logo_ensam.png  images/logo_um5r.png

# 5. Fill chapters/*.tex with your content (§9 gives a skeleton per chapter)

# 6. Update figures/gantt.tex dates + swimlanes to your timeline

# 7. Compile
make clean && make
```

Placeholders you will substitute (6 total):

| Placeholder | Example |
|---|---|
| `<PROJECT_NAME>` | Tamwil AI |
| `<PROJECT_SUBTITLE>` | Chatbot RAG de recommandation financière pour startups |
| `<AUTHORS>` | Aymane Issami, Houssam Kichchou |
| `<ENCADRANTE>` | Mme Hafsa Khiyat |
| `<PROFESSEUR_RESPONSABLE>` | Mme Amal Tmiri |
| `<ANNEE_UNIVERSITAIRE>` | 2025/2026 |

---

## 1. Inputs — gather these before writing a line

### 1.1 Identity
- **Project name** and a one-line subtitle.
- **Authors**: full names, family name in `\textsc{}` small caps by convention.
- **Encadrante/encadrant** (direct supervisor).
- **Professeur responsable** (module coordinator, if applicable).
- **Filière** (program): e.g. *Ingénierie en Data Science et Intelligence Artificielle* (IDSIA), *INDIA*, *GIND*, etc.
- **Année universitaire** in the `YYYY/YYYY` format.

### 1.2 Artefacts
- **Logos**: ENSAM + UM5R (or your university's). Supervisor will flag their absence. `.png` under 10~KB is enough.
- **Previous feedback**: if it's a v2, the supervisor likely returned a `.docx` with inline annotations. See §18 for extraction.
- **The actual thing you're documenting**: a codebase, a prototype, a study. The playbook assumes a code project — adjust §3/§9 if it's a study/survey report instead.

### 1.3 Stack awareness
Before writing Chapter~3 (Réalisation) you need to know, with file-level precision:
- Language(s) used, framework(s), libraries (with versions).
- Directory structure.
- Dataset or data sources (counts, sizes — run `jq length` / `du -sh`).
- Deployment state (local-only? cloud? nothing yet?).
- Test coverage (which modules, how).

The **truth pass** (§17) verifies everything you claim against what the code actually does.

---

## 2. Hard constraints — supervisor conventions (9 rules)

Generalized from Mme Khiyat's remarks on the Tamwil~AI v1. These are **universal** at ENSAM Rabat; apply them up-front and you skip the costly v1→v2 rewrite.

| # | Rule | Implementation |
|---|---|---|
| 1 | **Logos** of university + school on the cover | Two `\includegraphics` slots in `titlepage.tex`; `\IfFileExists` fallback to a placeholder box so the document compiles before images are dropped in. |
| 2 | **Font consistency** everywhere, especially in tables and diagrams | Body font for all TikZ nodes (`\footnotesize\sffamily`); `booktabs` tables; `\ttfamily` only for code identifiers. |
| 3 | **GANTT chart** is not optional | `pgfgantt` figure in the Introduction, **with real dates** seeded from your actual Git history (not fantasy). |
| 4 | **Each major section on its own page** | `\clearpage` before Remerciements, Résumé, Abstract, TOC, LoF, LoT, acronymes, every chapter, bibliographie, every annexe. |
| 5 | **No unexplained transitions** ("Pourquoi ce vide ??") | Before any bullet list of sub-items, write a paragraph that *motivates* the list. Never jump from "X comprises several actors:" straight into a list. |
| 6 | **Diagrams made with a real tool**, not AI-generated | TikZ-native, explicit coordinates, or Diagrams.net (drawio) exports. Never DALL·E/Midjourney/Gemini-image. |
| 7 | **Academic integrity** for all figures | Header comment on each TikZ file: `% Manually authored layout; positions in cm.` |
| 8 | **"Année Universitaire YYYY/YYYY" in the footer** of every page | `\fancyfoot[L]{\footnotesize Année Universitaire <ANNEE_UNIVERSITAIRE>}` in preamble, also inside `\fancypagestyle{plain}` so frontmatter pages get it. |
| 9 | **Typography consistency in diagrams** | Never mix font families inside a figure. Keep sans-serif uniformly in TikZ. No raster imports with foreign fonts except logos/screenshots. |

Plus **implicit conventions**:
- Formal French, *nous* (first-person plural) when narrating.
- Passive voice frequent; active for user-facing narratives.
- Bold for key concepts on first mention.
- Italics for foreign terms, quoted speech, emphasis.
- Tables use `booktabs` (\toprule, \midrule, \bottomrule), never vertical rules.

---

## 3. Document structure — canonical 5-chapter PFA

```
Page de garde (logos + identity + signatures)
Dédicace
Remerciements                       ← own page
Résumé (FR)                          ← own page
Abstract (EN)                        ← own page
Table des matières                   ← own page
Liste des figures                    ← own page
Liste des tableaux                   ← own page
Liste des acronymes                  ← own page

Introduction générale
  Contexte
  Problématique
  Objectifs
  Méthodologie
  Planification (GANTT)              ← MANDATORY figure
  Plan du rapport

Chapitre 1 — Étude de l'existant et cadre théorique
  1.1 Contexte métier (acteurs, enjeux)
  1.2 État de l'art (techniques, solutions concurrentes)
  1.3 Cadre théorique (technique centrale du projet)
  1.4 Positionnement vs solutions existantes
  1.5 Justification des choix

Chapitre 2 — Conception et architecture
  2.1 Architecture globale                  ← TikZ figure
  2.2 Modules fonctionnels
  2.3 Modèle de données
  2.4 Pipeline / flux principal             ← TikZ figure
  2.5 Mapping données ↔ fonctionnalités

Chapitre 3 — Réalisation et implémentation
  3.1 Environnement de développement
  3.2 Stack technique
  3.3 Constitution du dataset / des données
  3.4 Implémentation du cœur métier
  3.5 Modules métier individuels
  3.6 Backend / API
  3.7 Interface utilisateur
  3.8 Structure du projet
  3.9 Règles de développement

Chapitre 4 — Tests et résultats
  4.1 Scénarios fonctionnels                ← captures d'écran
  4.2 Tests unitaires
  4.3 Tests d'intégration (ou reconnaissance d'absence)
  4.4 Discussion et limites

Chapitre 5 — Conclusion et perspectives
  5.1 Bilan
  5.2 Apports personnels
  5.3 Perspectives d'amélioration

Bibliographie et webographie
Annexe A — Schémas de données
Annexe B — Variables d'environnement
Annexe C — Référence API
Annexe D — Artefact remarquable (prompt système, DAO, config, etc.)
```

---

## 4. Directory layout

```
latex/
├── rapport.tex               ← main, \input's everything
├── preamble.tex              ← packages, macros, acronymes
├── titlepage.tex             ← page de garde
├── frontmatter/
│   ├── dedicace.tex
│   ├── remerciements.tex
│   ├── resume.tex            ← FR + EN
│   └── acronymes.tex
├── chapters/
│   ├── 00_introduction.tex   ← inc. GANTT
│   ├── 01_etat_de_lart.tex
│   ├── 02_conception.tex
│   ├── 03_realisation.tex
│   ├── 04_tests.tex
│   └── 05_conclusion.tex
├── annexes/
│   ├── a_dataset_schema.tex
│   ├── b_env_vars.tex
│   ├── c_api_reference.tex
│   └── d_prompt_systeme.tex
├── figures/
│   ├── architecture.tex      ← TikZ
│   ├── pipeline.tex          ← TikZ
│   ├── gantt.tex             ← pgfgantt
│   └── sequence.tex          ← TikZ
├── images/
│   ├── logo_ensam.png
│   ├── logo_um5r.png
│   └── screenshots/
│       ├── ui_dark.jpeg
│       ├── ui_light.jpeg
│       └── ...
├── references.bib
└── Makefile
```

---

## 5. FULL PREAMBLE (`preamble.tex`)

Paste as-is. Adjust `\fancyhead[R]` with your project name.

```latex
% ============================================================================
% Préambule — Rapport PFA
% ============================================================================

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{lmodern}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{enumitem}
\usepackage{tikz}
\usepackage{float}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{caption}
\usepackage{tcolorbox}
\usepackage{pgfgantt}
\usepackage{acronym}
\usepackage{csquotes}

% Bibliographie : BibTeX classique (biber/biblatex non disponibles sur la machine cible).
% \bibliographystyle + \bibliography sont appelés depuis rapport.tex.

\usetikzlibrary{shapes.geometric, arrows.meta, positioning, fit, backgrounds, calc, chains, decorations.pathreplacing}

% ---------------------------- Mise en page ----------------------------------
\geometry{a4paper, margin=2.5cm, headheight=15pt}

\hypersetup{
    colorlinks=true,
    linkcolor=blue!60!black,
    urlcolor=blue!60!black,
    citecolor=blue!60!black
}

% ---------------------------- Listings (code) -------------------------------
\definecolor{codebg}{HTML}{F5F5F5}
\definecolor{codegreen}{HTML}{28A745}
\definecolor{codepurple}{HTML}{6F42C1}
\definecolor{codegray}{HTML}{6A737D}
\definecolor{codeblue}{HTML}{0366D6}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{codebg},
    commentstyle=\color{codegray}\itshape,
    keywordstyle=\color{codepurple}\bfseries,
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codegreen},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2,
    frame=single,
    rulecolor=\color{gray!30},
    extendedchars=true,
    inputencoding=utf8,
    literate=%
      {é}{{\'e}}1 {è}{{\`e}}1 {ê}{{\^e}}1 {ë}{{\"e}}1
      {à}{{\`a}}1 {â}{{\^a}}1 {ä}{{\"a}}1
      {î}{{\^i}}1 {ï}{{\"i}}1
      {ô}{{\^o}}1 {ö}{{\"o}}1
      {ù}{{\`u}}1 {û}{{\^u}}1 {ü}{{\"u}}1
      {ç}{{\c c}}1 {Ç}{{\c C}}1
      {É}{{\'E}}1 {È}{{\`E}}1 {À}{{\`A}}1
}
\lstset{style=mystyle}

% ---------------------------- En-tête / pied --------------------------------
% Année universitaire en pied de page (convention ENSAM Rabat).
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\nouppercase{\leftmark}}
\fancyhead[R]{<PROJECT_NAME>}
\fancyfoot[L]{\footnotesize Année Universitaire <ANNEE_UNIVERSITAIRE>}
\fancyfoot[R]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[L]{\footnotesize Année Universitaire <ANNEE_UNIVERSITAIRE>}%
  \fancyfoot[R]{\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}

% ---------------------------- Titres chapitres ------------------------------
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{blue!60!black}}
  {\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titlespacing*{\chapter}{0pt}{-20pt}{30pt}

% ---------------------------- Légendes --------------------------------------
\captionsetup{font=small, labelfont=bf, labelsep=period}

% ---------------------------- Macros utiles ---------------------------------
\newcommand{\project}{\textbf{<PROJECT_NAME>}}
\newcommand{\code}[1]{\texttt{#1}}

\newtcolorbox{callout}[1][]{colback=blue!5, colframe=blue!40!black, sharp corners,
  boxrule=0.5pt, left=8pt, right=8pt, top=6pt, bottom=6pt, #1}
\newtcolorbox{success}[1][]{colback=green!6, colframe=green!60!black, sharp corners,
  boxrule=0.5pt, left=8pt, right=8pt, top=6pt, bottom=6pt, #1}
\newtcolorbox{warn}[1][]{colback=orange!6, colframe=orange!70!black, sharp corners,
  boxrule=0.5pt, left=8pt, right=8pt, top=6pt, bottom=6pt, #1}

\setlist[itemize]{itemsep=2pt, topsep=3pt}
\setlist[enumerate]{itemsep=2pt, topsep=3pt}

% ---------------------------- Acronymes -------------------------------------
% Définis ici pour être disponibles dès le Résumé (avant la Liste des acronymes).
% Ajouter/retirer selon le projet.
\acrodef{API}{Application Programming Interface}
\acrodef{CPU}{Central Processing Unit}
\acrodef{CSV}{Comma-Separated Values}
\acrodef{FAQ}{Foire Aux Questions}
\acrodef{GPU}{Graphics Processing Unit}
\acrodef{JSON}{JavaScript Object Notation}
\acrodef{KPI}{Key Performance Indicator}
\acrodef{PDF}{Portable Document Format}
\acrodef{PFA}{Projet de Fin d'Ann\'ee}
\acrodef{REST}{Representational State Transfer}
\acrodef{SSE}{Server-Sent Events}
\acrodef{URL}{Uniform Resource Locator}
% ... ajouter les acronymes métier du projet ...

\endinput
```

---

## 6. TITLE PAGE (`titlepage.tex`)

```latex
% ============================================================================
% Page de garde — convention ENSAM Rabat.
% Placeholders auto si les logos ne sont pas encore déposés.
% ============================================================================

\newcommand{\logoPlaceholder}[2]{%
  \fbox{\parbox[c][#2][c]{#1}{\centering\small\itshape Logo à déposer\\(\code{images/#2})}}%
}

\IfFileExists{images/logo_um5r.png}{%
  \newcommand{\logoUM}{\includegraphics[height=2.2cm]{images/logo_um5r.png}}
}{%
  \newcommand{\logoUM}{\logoPlaceholder{3.2cm}{2.2cm}}
}

\IfFileExists{images/logo_ensam.png}{%
  \newcommand{\logoENSAM}{\includegraphics[height=2.2cm]{images/logo_ensam.png}}
}{%
  \newcommand{\logoENSAM}{\logoPlaceholder{3.2cm}{2.2cm}}
}

\begin{titlepage}
    \centering

    \begin{minipage}[c]{0.28\textwidth}
        \centering \logoUM
    \end{minipage}\hfill
    \begin{minipage}[c]{0.40\textwidth}
        \centering
        {\small\textbf{Université Mohammed V de Rabat}}\\[0.15cm]
        {\small\textbf{École Nationale Supérieure}}\\
        {\small\textbf{d'Arts et Métiers — ENSAM Rabat}}\\[0.15cm]
        {\footnotesize Filière <FILIERE> — <ANNEE> année}\\[0.15cm]
        {\footnotesize Année Universitaire <ANNEE_UNIVERSITAIRE>}
    \end{minipage}\hfill
    \begin{minipage}[c]{0.28\textwidth}
        \centering \logoENSAM
    \end{minipage}

    \vspace{1.8cm}

    \rule{\textwidth}{1.5pt}\\[0.4cm]
    {\LARGE\textbf{Projet de Fin d'Année}}\\[0.8cm]
    {\Huge\textbf{<PROJECT_NAME>}}\\[0.4cm]
    {\Large <PROJECT_SUBTITLE>}\\[0.4cm]
    \rule{\textwidth}{1.5pt}

    \vspace{1.2cm}
    {\normalsize\itshape <ONE_LINE_TAGLINE>}

    \vspace{2cm}

    \begin{minipage}{0.45\textwidth}
        \centering
        {\large\textbf{Réalisé par :}}\\[0.4cm]
        {\large <AUTHOR_1_FIRST> \textsc{<AUTHOR_1_LAST>}}\\[0.15cm]
        {\large <AUTHOR_2_FIRST> \textsc{<AUTHOR_2_LAST>}}
    \end{minipage}\hfill
    \begin{minipage}{0.45\textwidth}
        \centering
        {\large\textbf{Encadré par :}}\\[0.4cm]
        {\large M\textsuperscript{me} <ENCADRANTE_FIRST> \textsc{<ENCADRANTE_LAST>}}\\[0.4cm]
        {\normalsize\textit{Professeur responsable :}}\\[0.1cm]
        {\normalsize M\textsuperscript{me} <PROF_FIRST> \textsc{<PROF_LAST>}}
    \end{minipage}

    \vfill

    \rule{0.5\textwidth}{0.4pt}\\[0.3cm]
    {\small Soutenu publiquement le \underline{\hspace{3.5cm}}}

\end{titlepage}
```

---

## 7. MAIN FILE (`rapport.tex`)

```latex
\documentclass[12pt,a4paper,openany]{report}
\input{preamble.tex}

\begin{document}

\input{titlepage.tex}

\pagenumbering{roman}
\input{frontmatter/dedicace.tex}
\clearpage
\input{frontmatter/remerciements.tex}
\clearpage
\input{frontmatter/resume.tex}
\clearpage

\renewcommand{\contentsname}{Table des matières}
\tableofcontents
\clearpage
\listoffigures
\clearpage
\listoftables
\clearpage
\input{frontmatter/acronymes.tex}
\clearpage

\pagenumbering{arabic}
\setcounter{page}{1}

\input{chapters/00_introduction.tex}
\input{chapters/01_etat_de_lart.tex}
\input{chapters/02_conception.tex}
\input{chapters/03_realisation.tex}
\input{chapters/04_tests.tex}
\input{chapters/05_conclusion.tex}

\clearpage
\phantomsection
\addcontentsline{toc}{chapter}{Bibliographie et webographie}
\renewcommand{\bibname}{Bibliographie et webographie}
\nocite{*}
\bibliographystyle{plain}
\bibliography{references}

\appendix
\input{annexes/a_dataset_schema.tex}
\input{annexes/b_env_vars.tex}
\input{annexes/c_api_reference.tex}
\input{annexes/d_prompt_systeme.tex}

\end{document}
```

---

## 8. FRONTMATTER

### 8.1 `frontmatter/dedicace.tex`

```latex
\thispagestyle{plain}
\begin{center}
\vspace*{2cm}

\textit{\Large À nos familles,}\\[0.6cm]
\textit{\large pour leur soutien indéfectible tout au long\\
de notre parcours scolaire et universitaire.}\\[1.2cm]

\textit{\Large À nos enseignants,}\\[0.6cm]
\textit{\large dont la rigueur et la passion nous ont donné\\
le goût du travail bien fait.}\\[1.2cm]

\textit{\Large À <ECOSYSTEME_OU_COMMUNAUTE_CIBLE>,}\\[0.6cm]
\textit{\large qui nous a inspirés ce projet,\\
dans l'espoir qu'il lui soit utile.}

\vfill
\end{center}
```

### 8.2 `frontmatter/remerciements.tex`

```latex
\chapter*{Remerciements}
\addcontentsline{toc}{chapter}{Remerciements}
\thispagestyle{plain}

Au terme de ce projet, nous tenons à exprimer notre profonde reconnaissance à toutes les personnes qui ont contribué, de près ou de loin, à son aboutissement.

Nous adressons nos remerciements les plus sincères à notre encadrante, Madame \textbf{<ENCADRANTE>}, pour son suivi rigoureux, la qualité de ses conseils, la pertinence de ses remarques et la disponibilité dont elle a fait preuve tout au long de ce travail.

Nos remerciements vont également à Madame \textbf{<PROFESSEUR_RESPONSABLE>}, professeur responsable, pour la coordination du projet.

Nous remercions chaleureusement l'ensemble du corps professoral de l'\textbf{École Nationale Supérieure d'Arts et Métiers de Rabat} (ENSAM), de la filière \textit{<FILIERE>}, pour la formation de qualité qui nous a permis d'acquérir les compétences techniques et méthodologiques mobilisées dans ce travail.

Nous exprimons enfin notre gratitude à nos familles pour leur soutien moral constant, et à nos camarades de promotion pour les échanges enrichissants.

Que toutes et tous trouvent ici l'expression de notre sincère reconnaissance.
```

### 8.3 `frontmatter/resume.tex`

Structure: 4–5 paragraphs. (1) the problem, (2) what the project is, (3) the architecture, (4) the implementation stack, (5) validation + limits. Mirror in English for Abstract.

```latex
\chapter*{Résumé}
\addcontentsline{toc}{chapter}{Résumé}
\thispagestyle{plain}

<PARAGRAPH_1_PROBLEM_STATEMENT>

Ce projet, \textbf{<PROJECT_NAME>}, propose <ONE_LINE_DESCRIPTION>. <TECHNICAL_APPROACH>.

L'architecture est <ARCHITECTURE_SUMMARY>.

Le backend est développé en <BACKEND_STACK>. L'interface utilisateur repose sur <FRONTEND_STACK>.

Le système a été validé par <N> scénarios fonctionnels et <TESTING_SUMMARY>. Les limites identifiées --- <LIMITS> --- ouvrent la voie à des évolutions futures.

\vspace{0.4cm}
\textbf{Mots-clés :} <5-10 KEYWORDS>.

\vspace{1.2cm}

\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}
\thispagestyle{plain}

<MIRRORED_ENGLISH_CONTENT>

\textbf{Keywords:} <ENGLISH_KEYWORDS>.
```

### 8.4 `frontmatter/acronymes.tex` + preamble pattern

Define acronyms with `\acrodef` in the **preamble** (see §5) so they work in the Résumé which renders before the acronym list. In this file, just format the visible list:

```latex
\chapter*{Liste des acronymes}
\addcontentsline{toc}{chapter}{Liste des acronymes}
\thispagestyle{plain}

\begin{acronym}[WIDEST-LABEL]
  \acro{API}{Application Programming Interface}
  \acro{KPI}{Key Performance Indicator}
  \acro{LLM}{Large Language Model}
  % ... one line per acronym used in the document ...
\end{acronym}
```

The argument `[WIDEST-LABEL]` sets the column width to the widest acronym label — use the actual widest one in your list for clean alignment.

---

## 9. CHAPTER SKELETONS

Each skeleton tells you **what to write** section by section. Fill in, then delete the comments.

### 9.1 `chapters/00_introduction.tex`

```latex
\chapter*{Introduction générale}
\addcontentsline{toc}{chapter}{Introduction générale}
\markboth{Introduction générale}{}

\section*{Contexte}
% Panorama du domaine (secteur, enjeux, chiffres clés, sources crédibles).
% 2-3 paragraphes. Fait la bascule vers la problématique.

\section*{Problématique}
% Une seule question, formulée avec précision. Éviter les questions multiples.

\section*{Objectifs}
% Liste numérotée de 4-7 objectifs fonctionnels, commençant chacun par un verbe d'action.

\section*{Méthodologie}
% 2-3 axes : étude de l'existant, constitution des données, développement itératif.

\section*{Planification du projet}
Le projet s'est déroulé sur <N> semaines. La figure~\ref{fig:gantt} présente le planning.
\input{figures/gantt.tex}

\section*{Plan du rapport}
Le présent rapport est structuré en cinq chapitres. Le \textbf{chapitre~1} [...]. Le \textbf{chapitre~2} [...]. [...]
```

### 9.2 `chapters/01_etat_de_lart.tex`

```latex
\chapter{Étude de l'existant et cadre théorique}

% Paragraphe d'ouverture (1-2 phrases) qui annonce le plan du chapitre.

\section{<DOMAINE_METIER>}

\subsection{Panorama et enjeux}
% Contexte large, enjeux, acteurs-clés (macro).

\subsection{<CATEGORIE_D_ACTEURS>}
% RÈGLE SUPERVISEUR #5 : avant toute bullet-list d'acteurs/outils/approches,
% écrire un paragraphe qui MOTIVE la liste. Jamais enchaîner directement.
Pour naviguer dans cette diversité, il est utile de distinguer [...]. Chaque catégorie
répond à un besoin spécifique [...]. Les principaux acteurs sont les suivants :
\begin{itemize}
  \item \textbf{<TYPE_1>} : <description + exemples locaux>.
  \item \textbf{<TYPE_2>} : <description + exemples locaux>.
  \item [...]
\end{itemize}

\section{<TECHNIQUE_CENTRALE> : bref panorama}
% Évolution historique, limites, raison pour laquelle la technique centrale s'impose.

\section{<TECHNIQUE_CENTRALE>}

\subsection{Principe}
% 1 paragraphe.

\subsection{Pipeline détaillé}
\input{figures/pipeline.tex}
\begin{table}[H]
\centering
\caption{Les <N> étapes du pipeline <TECHNIQUE_CENTRALE> de \project.}
\label{tab:pipeline}
\begin{tabularx}{\textwidth}{@{}l l X@{}}
\toprule
\textbf{Étape} & \textbf{Module} & \textbf{Rôle} \\
\midrule
% ...
\bottomrule
\end{tabularx}
\end{table}

\subsection{Apports par rapport à <ALTERNATIVE>}
% Bullets comparatifs.

\section{Positionnement par rapport aux solutions existantes}
\begin{table}[H]
\centering
\caption{Positionnement de \project{} par rapport aux solutions existantes.}
\label{tab:comparaison}
\small
\begin{tabularx}{\textwidth}{@{}l l l X X@{}}
\toprule
\textbf{Solution} & \textbf{Type} & \textbf{Langue} & \textbf{Critère 1} & \textbf{Critère 2} \\
\midrule
% ...
\textbf{\project} & ... & ... & ... & ... \\
\bottomrule
\end{tabularx}
\end{table}

\section{Justification des choix}
% Pourquoi cette approche, pas une autre.
```

### 9.3 `chapters/02_conception.tex`

```latex
\chapter{Conception et architecture}

\section{Architecture globale}
\input{figures/architecture.tex}
% 1-2 paragraphes qui décrivent les couches visibles sur le schéma.

\section{Modules fonctionnels}
% Un paragraphe \paragraph{} par module. RÈGLE DE VÉRITÉ : ne pas surestimer
% la modularité. Si un "module" est en réalité une fonction dans le routeur,
% le dire explicitement (voir §17).

\paragraph{Module 1 --- <NOM>.} Description.
\begin{itemize}
  \item \textbf{Entrée} : ...
  \item \textbf{Données} : ...
  \item \textbf{Logique} : ...
  \item \textbf{Sortie} : ...
\end{itemize}

% ... répéter par module ...

\section{Modèle de données}
\begin{table}[H]
% tabularx avec composition du dataset
\end{table}

\section{Pipeline <TECHNIQUE_CENTRALE>}
% Rappel figure pipeline, choix techniques étape par étape.

\section{Mapping données \texorpdfstring{$\to$}{->} fonctionnalités}
\begin{table}[H]
% tabularx : pour chaque fonctionnalité, quelles sources de données sont mobilisées
\end{table}
```

### 9.4 `chapters/03_realisation.tex`

Longest chapter. Subsections: environnement, stack, constitution données, cœur technique, modules métier, backend, frontend, structure projet, règles de développement. Utilise des tableaux (`tabularx` + `booktabs`) pour la stack et les endpoints. `lstlisting` pour les extraits de code.

### 9.5 `chapters/04_tests.tex`

```latex
\chapter{Tests et résultats}

\section{Scénarios fonctionnels}
% Tableau des scénarios (entrée / sortie attendue).
% Captures d'écran (cf. §10 pour les placeholders en attendant).

\begin{figure}[H]
\centering
\includegraphics[width=0.92\textwidth]{images/screenshots/<nom>.jpeg}
\caption{Scénario ... --- <description>.}
\label{fig:scenario_X}
\end{figure}

\section{Tests unitaires}
\begin{table}[H]
% Tableau fichier → module testé → périmètre
\end{table}

\section{Tests d'intégration}
% Si non implémentés, le reconnaître (la vérité > l'illusion de complétude).

\section{Discussion et limites}
% Forces (bullets), limites identifiées (bullets). Pas de langue de bois.
```

### 9.6 `chapters/05_conclusion.tex`

```latex
\chapter{Conclusion et perspectives}

\section{Bilan du projet}
% Paragraphe d'ouverture + réalisations principales en liste numérotée.

\section{Apports personnels}
% Compétences acquises, bullets.

\section{Perspectives d'amélioration}
% Axes, un \paragraph{} par axe majeur. Rester honnête sur ce qui reste à faire.
```

---

## 10. TIKZ FIGURE PATTERNS (4 archetypes)

**Règle absolue** : `\node[step]` ne compile pas, `step` est réservé dans TikZ. Utilisez un préfixe (`pipebox`, `mybox`, `tsstep`) pour tous les styles personnalisés.

### 10.1 Architecture 3-couches (`figures/architecture.tex`)

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  font=\footnotesize\sffamily,
  every node/.style={align=center, rounded corners=2pt, inner sep=5pt},
  layerband/.style={draw=black!15, fill=black!3, rounded corners=6pt},
  ui/.style={draw=blue!40!black, fill=blue!10, thick, minimum width=3.6cm, minimum height=1.1cm},
  back/.style={draw=green!50!black, fill=green!10, thick, minimum width=3.6cm, minimum height=1.1cm},
  data/.style={draw=orange!60!black, fill=orange!15, thick, minimum width=3.6cm, minimum height=1.1cm},
  ext/.style={draw=red!50!black, fill=red!8, thick, dashed, minimum width=2.6cm, minimum height=0.9cm},
  mod/.style={draw=green!50!black, fill=green!5, thin, minimum width=2.0cm, minimum height=0.8cm},
  arrow/.style={-Stealth, thick, gray!70!black},
]

\begin{scope}[on background layer]
  \node[layerband, minimum width=13cm, minimum height=1.8cm] (UIband) at (0, 5.0) {};
  \node[layerband, minimum width=13cm, minimum height=3.6cm] (BEband) at (0, 1.6) {};
  \node[layerband, minimum width=13cm, minimum height=1.8cm] (DATAband) at (0, -2.1) {};
\end{scope}

\node[anchor=west, font=\scriptsize\sffamily\itshape] at ([xshift=0.25cm] UIband.west) {Interface utilisateur};
\node[anchor=west, font=\scriptsize\sffamily\itshape] at ([xshift=0.25cm, yshift=1.4cm] BEband.west) {Service applicatif};
\node[anchor=west, font=\scriptsize\sffamily\itshape] at ([xshift=0.25cm] DATAband.west) {Couche de données};

\node[ui]   (front)  at (0, 5.0)    {\textbf{<FRONTEND_STACK>}};
\node[back] (api)    at (0, 2.9)    {\textbf{<BACKEND>}\\\code{/endpoint1} \textbullet{} \code{/endpoint2}};
\node[back, minimum width=6.8cm] (router) at (0, 1.5) {\textbf{<ROUTEUR>}};

\node[mod] (m1) at (-5.1, 0.1) {\textbf{Module 1}};
\node[mod] (m2) at (-2.5, 0.1) {\textbf{Module 2}};
\node[mod] (m3) at  (0.0, 0.1) {\textbf{Module 3}};
\node[mod] (m4) at  (2.5, 0.1) {\textbf{Module 4}};
\node[mod] (m5) at  (5.1, 0.1) {\textbf{Module 5}};

\node[data] (db)    at (-3.6, -2.1) {\textbf{<DATABASE>}};
\node[data] (files) at  (0.2, -2.1) {\textbf{<DATA_FILES>}};
\node[data] (other) at  (4.1, -2.1) {\textbf{<AUTRE>}};

\node[ext] (llm) at (5.9, 2.9) {<API_EXTERNE>};

\draw[arrow] (front) -- (api);
\draw[arrow] (api) -- (router);
\draw[arrow] (router.south west) -- (m1.north);
\draw[arrow] (router.south) -- (m2.north);
\draw[arrow] (router.south) -- (m3.north);
\draw[arrow] (router.south) -- (m4.north);
\draw[arrow] (router.south east) -- (m5.north);
\draw[arrow] (m1) -- (db);
\draw[arrow] (m3) -- (files);
\draw[arrow, dashed] (m5.east) to[bend left=20] (llm.west);

\end{tikzpicture}
\caption{Architecture globale de \project{} --- trois couches (interface, service, données).}
\label{fig:architecture}
\end{figure}
```

Note: on background layer uses `layer` — c'est un mot-clé TikZ. Ne le renommez pas.

### 10.2 Pipeline linéaire (`figures/pipeline.tex`)

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  font=\footnotesize\sffamily,
  every node/.style={align=center, rounded corners=3pt, inner sep=5pt},
  pipebox/.style={draw=blue!40!black, fill=blue!8, thick, minimum width=2.7cm, minimum height=1.3cm},
  arr/.style={-Stealth, thick, gray!70!black},
]

\node[pipebox] (s1) at (0, 2)    {\textbf{1. <ETAPE>}};
\node[pipebox] (s2) at (3.4, 2)  {\textbf{2. <ETAPE>}};
\node[pipebox] (s3) at (6.8, 2)  {\textbf{3. <ETAPE>}};
\node[pipebox] (s4) at (0, -0.3) {\textbf{4. <ETAPE>}};
\node[pipebox] (s5) at (3.4,-0.3){\textbf{5. <ETAPE>}};
\node[pipebox] (s6) at (6.8,-0.3){\textbf{6. <ETAPE>}};

\draw[arr] (s1) -- (s2);
\draw[arr] (s2) -- (s3);
\draw[arr] (s3.south) to[bend left=20] (s4.north);
\draw[arr] (s4) -- (s5);
\draw[arr] (s5) -- (s6);

\end{tikzpicture}
\caption{Pipeline <TECHNIQUE_CENTRALE> en six étapes.}
\label{fig:pipeline}
\end{figure}
```

### 10.3 GANTT (`figures/gantt.tex`)

```latex
\begin{figure}[H]
\centering
\begin{ganttchart}[
  hgrid, vgrid,
  x unit=0.52cm,
  y unit chart=0.55cm,
  y unit title=0.6cm,
  canvas/.style={draw=black!30, dash pattern=on 1pt off 1pt},
  bar/.style={fill=blue!40!black, draw=blue!60!black, rounded corners=1pt},
  bar label font=\footnotesize\sffamily,
  bar top shift=0.15,
  bar height=0.6,
  group/.style={fill=blue!70!black, draw=blue!80!black},
  group left shift=0,
  group right shift=0,
  group peaks width=0,
  group label font=\footnotesize\sffamily\bfseries,
  milestone/.style={fill=orange!70!black, draw=orange!80!black},
  milestone label font=\scriptsize\sffamily\itshape,
  title label font=\scriptsize\sffamily,
  title/.style={draw=black!30, fill=black!5},
]{1}{<N_WEEKS>}

  \gantttitle{<MOIS_1>}{<W>}
  \gantttitle{<MOIS_2>}{<W>}
  \gantttitle{<MOIS_3>}{<W>} \\
  \gantttitlelist{1,...,<N_WEEKS>}{1} \\

  \ganttgroup{Phase 1 --- <NOM>}{1}{<W>} \\
  \ganttbar{<TACHE>}{1}{<W>} \\
  \ganttbar{<TACHE>}{1}{<W>} \\
  \ganttmilestone{<JALON>}{<W>} \\

  \ganttgroup{Phase 2 --- <NOM>}{...}{...} \\
  % ... etc.

\end{ganttchart}
\caption{Planning prévisionnel et réel du projet \project.}
\label{fig:gantt}
\end{figure}
```

**Conseils** :
- Graines les dates depuis `git log --date=short --pretty=format:"%ad %s" | head -40`.
- 5-6 phases, 3 jalons majeurs, 10-12 semaines couvrent un PFA typique.
- `bar` pour les tâches, `group` pour les phases (bandeau plus foncé), `milestone` pour les livrables (losange orange).

### 10.4 Séquence (`figures/sequence.tex`)

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[
  font=\footnotesize\sffamily,
  every node/.style={align=center, inner sep=3pt},
  actor/.style={draw=black!40, fill=black!5, rounded corners=2pt, minimum width=2.2cm, minimum height=0.7cm},
  lifeline/.style={dashed, gray!60},
  msg/.style={-Stealth, thick, blue!40!black},
  ret/.style={-Stealth, thick, dashed, green!50!black},
]

\def\ux{0}  \def\ax{3}  \def\bx{6}  \def\cx{9}  \def\dx{12}

\node[actor] (U) at (\ux, 0) {\textbf{<ACTEUR_1>}};
\node[actor] (A) at (\ax, 0) {\textbf{<ACTEUR_2>}};
\node[actor] (B) at (\bx, 0) {\textbf{<ACTEUR_3>}};
\node[actor] (C) at (\cx, 0) {\textbf{<ACTEUR_4>}};
\node[actor] (D) at (\dx, 0) {\textbf{<ACTEUR_5>}};

\foreach \x in {\ux, \ax, \bx, \cx, \dx}
  \draw[lifeline] (\x, -0.35) -- (\x, -7);
\foreach \x/\n in {\ux/U, \ax/A, \bx/B, \cx/C, \dx/D}
  \node[actor] at (\x, -7.2) {\textbf{\n}};

\draw[msg] (\ux, -0.9) -- node[above, font=\scriptsize] {<MESSAGE>} (\ax, -0.9);
\draw[msg] (\ax, -1.6) -- node[above, font=\scriptsize] {<MESSAGE>} (\bx, -1.6);
\draw[ret] (\bx, -2.3) -- node[above, font=\scriptsize] {<RETOUR>} (\ax, -2.3);
% ... continuer ...

\end{tikzpicture}
\caption{Diagramme de séquence --- <SCENARIO>.}
\label{fig:sequence}
\end{figure}
```

---

## 11. ANNEXES

### 11.1 `annexes/a_dataset_schema.tex`

Schémas JSON ou DDL SQL des structures de données. Un `\begin{lstlisting}` par type, avec caption.

### 11.2 `annexes/b_env_vars.tex`

Fichier `.env` type + tableau variable/défaut/rôle. **Ne jamais commiter de vraie clé.**

### 11.3 `annexes/c_api_reference.tex`

Modèles Pydantic/DTO + exemples `curl` + formats d'événements SSE si applicable.

### 11.4 `annexes/d_prompt_systeme.tex`

Prompt LLM complet, ou autre artefact remarquable (DAG de workflow, grammaire ANTLR, schéma Terraform, etc.).

---

## 12. BIBLIOGRAPHIE (`references.bib`)

Format BibTeX classique (pas biblatex — voir §14).

```bibtex
% --------- Articles scientifiques ---------
@inproceedings{lewis2020rag,
  title     = {Retrieval-Augmented Generation for Knowledge-Intensive {NLP} Tasks},
  author    = {Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and ...},
  booktitle = {NeurIPS 2020},
  year      = {2020}
}

@inproceedings{reimers2019sbert,
  title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
  author    = {Reimers, Nils and Gurevych, Iryna},
  booktitle = {EMNLP-IJCNLP 2019},
  year      = {2019}
}

% --------- Documentation technique (webographie) ---------
@misc{langchain,
  author       = {{LangChain}},
  title        = {{LangChain} --- Documentation},
  year         = {<YYYY>},
  howpublished = {\url{https://python.langchain.com/docs/}},
  note         = {consulté le <JJ MM YYYY>}
}

@misc{<slug>,
  author       = {{<ORG>}},
  title        = {<TITRE>},
  year         = {<YYYY>},
  howpublished = {\url{<URL>}},
  note         = {consulté le <JJ MM YYYY>}
}
```

Dans `rapport.tex`, `\nocite{*}` force l'inclusion de **toutes** les entrées même non citées (webographie complète).

---

## 13. MAKEFILE

```makefile
MAIN = rapport
TEX  = pdflatex -interaction=nonstopmode -halt-on-error
BIB  = bibtex

.PHONY: all clean cleanall watch

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex preamble.tex titlepage.tex \
             $(wildcard frontmatter/*.tex) \
             $(wildcard chapters/*.tex) \
             $(wildcard annexes/*.tex) \
             $(wildcard figures/*.tex) \
             references.bib
	$(TEX) $(MAIN).tex
	-$(BIB) $(MAIN)
	$(TEX) $(MAIN).tex
	$(TEX) $(MAIN).tex

clean:
	rm -f *.aux *.log *.toc *.lof *.lot *.out *.bbl *.blg *.bcf *.run.xml *.synctex.gz
	rm -f chapters/*.aux frontmatter/*.aux annexes/*.aux figures/*.aux

cleanall: clean
	rm -f $(MAIN).pdf

watch:
	while inotifywait -e modify $(MAIN).tex chapters/*.tex frontmatter/*.tex annexes/*.tex figures/*.tex preamble.tex; do \
	    make; \
	done
```

---

## 14. TOOLCHAIN ASSUMPTIONS (Ubuntu)

Paquets nécessaires :

```bash
sudo apt install \
  texlive-base \
  texlive-binaries \
  texlive-fonts-recommended \
  texlive-lang-french \
  texlive-latex-base \
  texlive-latex-extra \
  texlive-latex-recommended \
  texlive-pictures \
  texlive-plain-generic
```

Ce qui **n'est PAS** installé par défaut et qu'on contourne :

| Manque | Alternative utilisée |
|---|---|
| `biber`    | `bibtex` classique (plain) |
| `biblatex` | `\bibliographystyle{plain}` + `\bibliography{...}` |
| `latexmk`  | `Makefile` qui orchestre `pdflatex → bibtex → pdflatex × 2` |
| `minted`   | `listings` |
| `xelatex`-only fonts | `lmodern` suffit |

Check rapide :

```bash
which pdflatex bibtex   # doivent exister
kpsewhich pgfgantt.sty  # doit renvoyer un chemin
```

---

## 15. LaTeX pitfalls & fixes

| # | Symptôme | Cause | Fix |
|---|---|---|---|
| 1 | `! Package pgfkeys Error: The key '/tikz/step' requires a value.` | `step` est réservé dans TikZ. | Renommer votre style en `pipebox`, `mybox`, `tsstep`. |
| 2 | `! LaTeX Error: File 'biblatex.sty' not found.` | `biblatex` pas installé. | Retirer `\usepackage{biblatex}` et passer à `\bibliographystyle{plain}` + `\bibliography{references}`. Remplacer `@online` par `@misc` dans `.bib`. |
| 3 | `Package acronym Warning: Acronym 'RAG' is not defined` dans le Résumé | Liste d'acronymes rendue **après** première utilisation. | Définir les acronymes avec `\acrodef{...}{...}` dans le **préambule**. Garder `\begin{acronym}` uniquement pour l'affichage. |
| 4 | `Package fancyhdr Warning: \headheight is too small (12.0pt)` | Hauteur d'en-tête par défaut trop petite. | `\geometry{a4paper, margin=2.5cm, headheight=15pt}`. |
| 5 | `Overfull \hbox` sur une identification longue type `module/sub/file.py` | `\texttt{}` ne coupe pas les mots sans séparateurs. | Encadrer dans `\url{...}`, ou ajouter des `\allowbreak` aux points, ou utiliser `\sloppy` localement. |
| 6 | Caractères accentués cassés dans un `lstlisting` | `listings` ne gère pas UTF-8 nativement. | Le préambule fourni inclut déjà `literate=...` pour tous les accents français. |
| 7 | `Reference 'fig:xxx' on page N undefined` après build | Il faut deux passes `pdflatex` pour résoudre les refs croisées. | Le `Makefile` fait déjà `pdflatex × 3` (avec `bibtex` au milieu). |
| 8 | Les acronymes se re-développent partout au lieu de s'abréger après la première occurrence | Comportement normal pour `\ac{...}`. | Si un abrégé dans une légende/titre pose problème, utiliser `\acs{FOO}` (short) ou `\acl{FOO}` (long) explicitement. |

---

## 16. Style conventions

### Voice
- Formal French. *Nous* collectif pour le récit. Passive voice pour les descriptions techniques.
- Éviter « je » / « j'ai ».
- Présent de l'indicatif par défaut. Passé simple et passé composé pour la narration de ce qui a été fait.

### Mise en forme
- `\textbf{...}` : concept-clé à la première mention.
- `\textit{...}` : mots étrangers (*streaming*, *dataset*, *chunk*), citations, emphase.
- `\texttt{...}` / `\code{...}` : identifiants, fichiers, commandes shell.
- `\og ... \fg{}` pour les guillemets français, ou `«~...~»` manuellement.

### Tableaux
- `tabularx` avec `\textwidth`, `booktabs` (\toprule, \midrule, \bottomrule). Jamais de `\hline`, jamais de barres verticales.
- Légende **au-dessus** par convention française.
- Label sous la forme `tab:<slug>`.

### Figures
- `[H]` (package `float`) pour forcer l'emplacement dans le flux.
- Légende **sous** la figure.
- Label sous la forme `fig:<slug>`.
- Référence via `figure~\ref{fig:xxx}` (tilde insécable pour éviter une coupure de ligne).

### Listings
- `\begin{lstlisting}[language=<lang>, caption={<légende>}] ... \end{lstlisting}`.
- Langues utiles : `bash`, `Python`, `TeX`, ou sans langue pour JSON/pseudo.

### Boîtes colorées (définies dans le préambule)
- `callout` (bleu) : rappel, définition, encadré neutre.
- `success` (vert) : jalon atteint, résumé positif.
- `warn` (orange) : limitation, attention.

---

## 17. Truth-pass protocol

**Avant de soumettre**, lister chaque affirmation numérique ou structurelle du rapport et la **vérifier** contre la réalité du code. Un rapport honnête vaut mieux qu'un rapport flatteur. Mme Khiyat vérifie.

### Commandes de vérification

```bash
# Taille du dataset (dir size)
du -sh dataset/ chroma_db/

# Nombre d'éléments dans un JSON array
jq 'length' dataset/investors.json
jq 'if type == "array" then length else (keys | length) end' path.json

# Nombre de lignes de code
wc -l backend/app/**/*.py

# Nombre de tests
ls tests/ | wc -l
grep -c "def test_" tests/*.py

# Historique git pour les dates du GANTT
git log --date=short --pretty=format:"%ad %s" | head -50

# Versions des dépendances
cat frontend/package.json | jq '.dependencies'
cat requirements.txt
```

### Modèle de checklist de vérité

Pour chaque chapitre, se poser :

1. **Chapitre 2 (Conception)** — les modules listés correspondent-ils à des fichiers `.py` distincts, ou certains sont-ils des fonctions dans un module plus large ? Si oui, le dire.
2. **Chapitre 3 (Réalisation)** — les versions citées sont-elles celles du `package.json` / `requirements.txt` actuels ? Les chiffres (taille dataset, nombre de lignes) sont-ils mesurés ou estimés ?
3. **Chapitre 4 (Tests)** — chaque fichier de tests cité existe-t-il ? Les tests d'intégration sont-ils **réellement** en place, ou prévus ?
4. **Conclusion** — les "réalisations principales" reprennent-elles des capacités effectivement en production, ou en partie aspirationnelles ?

### Exemple (Tamwil AI)

| Claim initial | Vérif | Correction |
|---|---|---|
| "6 modules métier" | `ls backend/app/modules/*.py` → 5 fichiers | « 5 modules + 1 utilitaire dans le routeur » |
| "ChromaDB ~7.3 MB" | `du -sh chroma_db/` → 9.4 MB | Chiffre corrigé |
| "Tests d'intégration end-to-end" | Aucun fichier `test_e2e*` | Déplacé en Perspectives |
| "Intent detection: mots-clés OU LLM" | Code n'a que mots-clés | Reformulé, variante LLM en Perspectives |

---

## 18. Supervisor feedback (.docx) — extraction

Un `.docx` n'est qu'une archive ZIP. Deux emplacements à examiner :

### 18.1 Annotations inline (texte ajouté dans le corps)

```bash
unzip -p RAPPORT_v1_annoté.docx word/document.xml | \
  python3 -c "
import sys, re, xml.etree.ElementTree as ET
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
root = ET.fromstring(sys.stdin.read())
for t in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'):
    if t.text and t.text.strip():
        print(t.text)
"
```

C'est souvent là que se trouvent les remarques du type *« Pourquoi ce vide ?? »*, *« Ajouter les logos »*, *« Regler la police !! »*.

### 18.2 Commentaires Word (feature Révision)

```bash
unzip -p RAPPORT_v1_annoté.docx word/comments.xml
```

Moins fréquent mais à vérifier systématiquement.

### 18.3 Suivi des modifications (track changes)

Chercher les balises `<w:ins>` et `<w:del>` dans `word/document.xml`.

### 18.4 Conversion rapide en texte

```bash
# Si pandoc est dispo :
pandoc RAPPORT.docx -o RAPPORT.md

# Sinon :
docx2txt RAPPORT.docx
# ou :
libreoffice --headless --convert-to txt RAPPORT.docx
```

---

## 19. Compile workflow

### Build complet (production)

```bash
cd latex/
make clean && make
```

Fait `pdflatex → bibtex → pdflatex → pdflatex`. Produit `rapport.pdf`.

### Build rapide (itération contenu, refs déjà résolues)

```bash
pdflatex -interaction=nonstopmode rapport.tex
```

### Build continu (watch mode)

```bash
make watch
# (nécessite `inotify-tools` : sudo apt install inotify-tools)
```

### Diagnostic si échec

```bash
# Dernières lignes du log
tail -40 rapport.log

# Toutes les erreurs/warnings non-cosmétiques
grep -iE "warning|error|not defined" rapport.log | \
  grep -vE "Font Warning|Overfull|Underfull|Some font shapes|rerunfilecheck" | head -20
```

---

## 20. Submission checklist (10 points)

Avant d'envoyer le PDF à l'encadrante, exécuter :

- [ ] `pdfinfo rapport.pdf | grep Pages` — nombre de pages raisonnable (40–70 pour un PFA).
- [ ] `pdfgrep -c "TODO\|XXX\|placeholder\|lorem\|Logo à déposer" rapport.pdf` → **0**.
- [ ] Ouvrir page 1 → les deux logos rendus, pas de boîte grise.
- [ ] Ouvrir une page quelconque du corps → footer = `Année Universitaire <YYYY/YYYY>`.
- [ ] Table des matières → toutes les sections listées, numérotation cohérente.
- [ ] Liste des figures + liste des tableaux → peuplées.
- [ ] GANTT rendu avec vrais noms de phases (pas de `\ganttbar{<TACHE>}`).
- [ ] Bibliographie → au moins 10 entrées, toutes avec `note=consulté le ...`.
- [ ] Résumé + Abstract → mots-clés en bas.
- [ ] `grep -iE "warning|not defined" rapport.log | grep -vE "Font|Overfull|Underfull"` → vide.

Taille finale typique : 800 KB – 2 MB selon le nombre de captures d'écran.

---

## Appendix A — Worked example: Tamwil AI

**Instantiation complète** à `/home/aymane-issami/Desktop/tamwil-ai/docs/rapport/latex/`. Build : `make`. Résultat : 49 pages, 1.3 MB, zéro warning.

Variables substituées :

| Placeholder | Valeur |
|---|---|
| `<PROJECT_NAME>` | Tamwil AI |
| `<PROJECT_SUBTITLE>` | Chatbot RAG de recommandation financière pour startups |
| `<AUTHORS>` | Aymane Issami, Houssam Kichchou |
| `<ENCADRANTE>` | Mme Hafsa Khiyat |
| `<PROFESSEUR_RESPONSABLE>` | Mme Amal Tmiri |
| `<ANNEE_UNIVERSITAIRE>` | 2025/2026 |
| `<FILIERE>` | Ingénierie en Data Science et Intelligence Artificielle (IDSIA) |
| `<TECHNIQUE_CENTRALE>` | Retrieval-Augmented Generation (RAG) |
| `<BACKEND_STACK>` | Python 3.11 + FastAPI + LangChain + ChromaDB |
| `<FRONTEND_STACK>` | Next.js 16 + React 19 + Tailwind CSS 4 |

Chiffres réels : 41 investisseurs, 25 subventions, 18 KPI, 54 FAQ, 10 documents Markdown, 1885 lignes de Python backend, ChromaDB 9,4 MB.

Supervisor turnaround : v1 (Markdown, 4 chapitres, 30 pages) → 9 remarques → v2 (LaTeX, 5 chapitres, 49 pages, zéro warning).

---

## Appendix B — Memory mirror (Claude auto-memory)

Ce playbook est doublé par deux entrées dans le système de mémoire de Claude Code :

```
~/.claude/projects/-home-aymane-issami-Desktop-tamwil-ai/memory/
├── MEMORY.md                          ← index
├── reference_pfa_playbook.md         ← pointeur vers ce fichier
└── feedback_pfa_style.md             ← préférences stylistiques lockées
```

Dans une nouvelle conversation, Claude lira ces entrées automatiquement et saura qu'il doit appliquer les conventions de ce playbook sans qu'on ait à les lui rappeler.

---

*Fin du playbook. Dernière mise à jour : 2026-04-23. Issu de la session de finalisation du rapport Tamwil~AI pour Mme Hafsa Khiyat, ENSAM Rabat.*
