# Term Sheet : Guide Complet avec Exemples Reels

## Introduction

La term sheet (lettre d'intention ou memorandum d'entente) est le document qui formalise les conditions principales d'un investissement. Bien qu'elle soit generalement non contraignante juridiquement (sauf les clauses d'exclusivite et de confidentialite), elle constitue la base de toute la documentation juridique qui suivra.

Comprendre chaque clause d'une term sheet est essentiel pour tout fondateur. Les termes acceptes au seed auront des consequences sur les 10 prochaines annees de l'entreprise et sur chaque tour de financement futur.

---

## Structure Generale d'une Term Sheet

Une term sheet typique fait 5 a 15 pages et couvre :
1. **Termes economiques** : valorisation, type d'actions, liquidation preference, anti-dilution
2. **Termes de gouvernance** : board, droits de vote, decisions reservees
3. **Termes de protection** : vesting (4 ans, 1 an cliff), non-concurrence, IP assignment
4. **Termes de sortie** : drag-along, tag-along, ROFR
5. **Conditions de closing** : DD satisfaisante, conditions suspensives
6. **Autres** : exclusivite, confidentialite, frais juridiques

---

## 1. Pre-money / Post-money et Calcul de Dilution

### Definition
- **Pre-money** : valorisation de l'entreprise avant l'investissement
- **Post-money** : pre-money + montant investi
- **Prix par action** : pre-money / nombre total d'actions existantes (incluant ESOP)

### Exemple detaille

**Situation initiale :**
- 1 000 000 actions existantes
- 100 000 actions ESOP (pool deja cree)
- Total fully diluted : 1 100 000 actions

**Conditions du tour :**
- Pre-money : 5M EUR
- Investissement : 1.5M EUR
- Post-money : 6.5M EUR

**Calcul :**
- Prix par action : 5M / 1 100 000 = 4.545 EUR
- Nouvelles actions emises : 1 500 000 / 4.545 = 330 000 actions
- Total post-investissement : 1 430 000 actions

**Cap table resultant :**

| Actionnaire | Actions | % pre-money | % post-money |
|-------------|---------|-------------|-------------|
| Fondateur A | 600 000 | 54.5% | 42.0% |
| Fondateur B | 400 000 | 36.4% | 28.0% |
| ESOP | 100 000 | 9.1% | 7.0% |
| Investisseur | 330 000 | - | 23.1% |
| **Total** | **1 430 000** | **100%** | **100%** |

### Point de negociation cle : ESOP dans le pre-money

**Version investisseur (standard)** : l'ESOP est inclus dans le pre-money. Le pool dilue uniquement les fondateurs. C'est la pratique de la majorite des fonds (CDG Invest, Partech Africa, Kima Ventures, Breega, etc.).

**Version fondateur (plus favorable)** : l'ESOP est cree post-money et dilue tout le monde proportionnellement. Cela donne effectivement une valorisation plus elevee aux fondateurs.

**Impact concret** : sur un tour de 1.5M EUR a 5M EUR pre-money avec un ESOP de 10%, la difference entre les deux approches represente environ 2-3 points de pourcentage de dilution supplementaire pour les fondateurs.

### Clause type
> "La societe procede a une augmentation de capital d'un montant nominal de [X] EUR, assortie d'une prime d'emission de [Y] EUR, soit un prix de souscription de [Z] EUR par action, sur la base d'une valorisation pre-money de 5 000 000 EUR, incluant un pool d'options salaries (ESOP) representant 10% du capital post-money."

---

## 2. Cap Table : Avant/Apres avec Pool ESOP

### Importance du cap table
Le cap table (tableau de capitalisation) est le document de reference qui recense tous les actionnaires, le nombre et le type d'actions detenues, et les instruments dilutifs (options, BSA, obligations convertibles).

### Pool ESOP standard

**Taille recommandee par stade :**
| Stade | ESOP recommande | Justification |
|-------|----------------|---------------|
| Pre-seed | 5-10% | Premiers recrutements cles |
| Seed | 10-15% | CTO, premiers ingenieurs |
| Serie A | 15-20% (recharge) | VP Engineering, VP Sales, Head of Product |
| Serie B+ | 10-15% (recharge) | C-suite, scaling de l'equipe |

**Repartition typique du pool ESOP :**
| Role | % du pool |
|------|-----------|
| CTO (si non-fondateur) | 15-25% du pool |
| VP Engineering | 5-10% du pool |
| VP Sales/Marketing | 5-10% du pool |
| Lead developers | 2-5% du pool chacun |
| Autres employes | 0.5-2% du pool chacun |

### Exemple de cap table complet (pre-seed a Serie A)

| Actionnaire | Creation | Post Pre-seed | Post Seed | Post Serie A |
|-------------|----------|---------------|-----------|-------------|
| Fondateur A | 60% | 54% | 40.5% | 32.4% |
| Fondateur B | 40% | 36% | 27.0% | 21.6% |
| ESOP | - | 5% | 12.5% | 16.0% |
| BA (pre-seed, Kalys Ventures) | - | 5% | 4.0% | 3.2% |
| VC Seed (CDG Invest) | - | - | 16.0% | 12.8% |
| VC Serie A (Partech Africa) | - | - | - | 14.0% |
| **Total** | **100%** | **100%** | **100%** | **100%** |

**Observations :**
- Les fondateurs passent de 100% a 54% en 3 tours -- c'est un scenario realiste et sain
- Le pool ESOP augmente a chaque tour pour accompagner les recrutements
- Les investisseurs precedents sont dilues a chaque nouveau tour (mais la valeur de leurs parts augmente si la valorisation monte)

---

## 3. Liquidation Preference

### Definition
La liquidation preference definit l'ordre de priorite de remboursement des actionnaires en cas de "liquidity event" (vente, fusion, liquidation). Les detenteurs d'actions de preference sont rembourses avant les detenteurs d'actions ordinaires.

### Les 3 types principaux

**1x Non-participating (standard du marche, founder-friendly)**
- L'investisseur recupere 1x son investissement OU sa part pro-rata du produit de la vente, selon ce qui est le plus favorable
- Il ne peut pas cumuler les deux
- **C'est le standard accepte par CDG Invest, Partech Africa, Kima Ventures, Breega, Elaia Partners, et la quasi-totalite des fonds europeens et africains**

**Exemple (1x non-participating) :**
- Investissement : 2M EUR pour 20% du capital
- Sortie a 20M EUR :
  - Option A : 1x = 2M EUR
  - Option B : 20% de 20M = 4M EUR
  - L'investisseur choisit le plus favorable : **4M EUR** (il convertit ses preferred en common)
- Sortie a 5M EUR :
  - Option A : 1x = 2M EUR
  - Option B : 20% de 5M = 1M EUR
  - L'investisseur choisit : **2M EUR** (il garde sa preference)

**1x Participating (agressif, a eviter si possible)**
- L'investisseur recupere 1x son investissement ET sa part pro-rata du solde restant
- C'est le "double dipping" : il est paye deux fois

**Exemple (1x participating) :**
- Investissement : 2M EUR pour 20%
- Sortie a 20M EUR :
  - Etape 1 : l'investisseur recupere 2M EUR (sa preference)
  - Etape 2 : sur les 18M EUR restants, il prend 20% = 3.6M EUR
  - Total investisseur : **5.6M EUR** (vs 4M en non-participating)
  - Fondateurs : 14.4M EUR (vs 16M en non-participating)

**2x ou 3x Liquidation Preference (toxique, a refuser)**
- L'investisseur recupere 2x ou 3x son investissement avant que les fondateurs ne recoivent quoi que ce soit
- Extremement defavorable. Acceptable uniquement dans des situations de sauvetage (bridge round desespere)

**Exemple (2x non-participating) :**
- Investissement : 2M EUR pour 20%
- Sortie a 8M EUR :
  - Preference 2x : 4M EUR pour l'investisseur
  - Fondateurs : 4M EUR seulement (50% au lieu de 80%)
- Sortie a 3M EUR :
  - Preference 2x : 3M EUR pour l'investisseur (plafonne au produit de vente)
  - Fondateurs : **0 EUR**

### Standard du marche

| Geographie | Standard seed | Standard Serie A |
|-----------|--------------|-----------------|
| Maroc | 1x non-part | 1x non-part |
| France | 1x non-part | 1x non-part |
| US | 1x non-part (seed) | 1x non-part ou 1x part (Serie A) |

### Conseil de negociation
Insister fermement sur **1x non-participating**. C'est le standard du marche en Europe et au Maroc. Si un investisseur demande du participating ou du 2x+, c'est un signal d'agressivite qui devrait vous faire reflechir.

---

## 4. Anti-dilution

### Definition
La clause d'anti-dilution protege les investisseurs en cas de "down round" (tour suivant a une valorisation inferieure). Elle ajuste retroactivement le prix d'achat des actions de l'investisseur.

### Les 2 types principaux

**Weighted Average (standard, acceptable) :**
Le prix par action est recalcule en tenant compte du nombre d'actions emises lors du down round et du prix. La formule lisse l'impact.

```
Nouveau prix = Prix ancien x (A + B) / (A + C)

Ou :
A = nombre d'actions avant le down round
B = montant du down round / prix ancien par action (actions qui auraient ete emises a l'ancien prix)
C = nombre d'actions reellement emises dans le down round
```

**Full Ratchet (agressif, a refuser) :**
Le prix par action est ajuste au prix le plus bas de toute emission future, quelle que soit la taille du down round. Extremement punitif pour les fondateurs.

**Exemple comparatif :**
- Seed : investissement 1M EUR a 5 EUR/action (200K actions)
- Down round Serie A : 2M EUR a 3 EUR/action

**Avec Weighted Average :**
- Nouveau prix seed ajuste : ~4.20 EUR (depend de la formule exacte)
- L'investisseur seed recoit quelques actions supplementaires pour compenser
- Impact fondateurs : modere

**Avec Full Ratchet :**
- Nouveau prix seed ajuste : 3 EUR (aligne sur le prix le plus bas)
- L'investisseur seed recoit 133K actions supplementaires (1M/3 - 200K = ~133K)
- Impact fondateurs : dilution massive supplementaire

### Clause type (weighted average)
> "En cas d'emission de nouvelles actions a un prix par action inferieur au prix de souscription, le prix de conversion des actions de preference sera ajuste selon la formule de la moyenne ponderee a base large (broad-based weighted average)."

### Conseil
Accepter le **weighted average** anti-dilution, c'est un standard de marche raisonnable utilise par tous les fonds reconnus (CDG Invest, Partech, Kima, Breega, Elaia, Alven). Refuser categoriquement le **full ratchet** : il peut detruire la detention des fondateurs en cas de mauvaise passe temporaire.

---

## 5. Vesting des Fondateurs

### Definition
Le vesting est un mecanisme par lequel les actions des fondateurs sont acquises progressivement sur une periode de temps. Si un fondateur quitte avant la fin du vesting, il perd les actions non vestees.

### Standard du marche

| Parametre | Standard |
|-----------|---------|
| Duree totale | **4 ans** |
| Cliff | **1 an** (25% veste au bout de 12 mois) |
| Vesting post-cliff | Mensuel (1/48eme par mois) |
| Acceleration | Single trigger (en cas d'acquisition, acceleration de 25-100%) |

### Exemple de vesting

**Fondateur avec 600 000 actions, vesting 4 ans avec cliff de 1 an :**

| Mois | Actions vestees | % total | Actions non vestees |
|------|----------------|---------|-------------------|
| 0-11 | 0 | 0% | 600 000 |
| 12 (cliff) | 150 000 | 25% | 450 000 |
| 24 | 300 000 | 50% | 300 000 |
| 36 | 450 000 | 75% | 150 000 |
| 48 | 600 000 | 100% | 0 |

### Single vs Double Trigger Acceleration

**Single trigger** : toutes les actions vestent immediatement en cas d'evenement declencheur unique (typiquement : acquisition de l'entreprise).
- Avantage fondateur : protege en cas de rachat
- Standard pour les fondateurs au seed

**Double trigger** : les actions vestent en acceleration uniquement si DEUX conditions sont remplies (typiquement : acquisition + licenciement du fondateur dans les 12 mois).
- Plus courant pour les employes
- Certains VC preferent le double trigger meme pour les fondateurs

### Good leaver vs Bad leaver

**Good leaver** (depart "positif") :
- Causes : deces, invalidite, licenciement sans cause, non-renouvellement de mandat
- Consequences : le fondateur garde toutes ses actions vestees, et souvent un buyback a la fair market value

**Bad leaver** (depart "negatif") :
- Causes : demission volontaire, faute grave, violation de non-concurrence
- Consequences : le fondateur perd ses actions non vestees, et parfois doit revendre ses actions vestees a prix nominal

### Conseil de negociation
- Accepter le vesting : c'est standard et montre l'engagement
- Negocier le credit du temps passe : si vous travaillez sur le projet depuis 2 ans avant la levee, demander un credit de 24 mois (donc seuls 24 mois restants)
- Insister sur le single trigger acceleration
- Definir clairement les cas de good/bad leaver dans le pacte d'associes

---

## 6. BSA-AIR / SAFE et Instruments Pre-Seed

### BSA-AIR (Accord d'Investissement Rapide) - France

**Definition** : equivalent francais du SAFE americain (cree par Y Combinator). C'est un instrument simplifie pour les investissements pre-seed.

**Fonctionnement :**
- L'investisseur souscrit des BSA qui se convertiront automatiquement en actions lors du prochain tour de financement
- La conversion se fait avec un **discount** (typiquement 15-25%) ou un **cap** (valorisation maximale)
- Pas besoin de fixer une valorisation immediatement

**Avantages :**
- Rapidite : 2-4 pages vs 30+ pages pour un tour classique
- Cout juridique reduit : 2-5K EUR vs 10-20K EUR
- Pas de valorisation a negocier

**Quand utiliser :**
- Pre-seed avec des BA (tickets de 10K-150K EUR)
- Kalys Ventures ($50K-$200K) utilise souvent ce type d'instrument
- Premier financement avant le seed institutionnel

### SAFE (Simple Agreement for Future Equity) - US / International

**Definition** : instrument cree par Y Combinator en 2013. Standard pour les tours pre-seed aux US et de plus en plus utilise en Afrique.

**Terms du SAFE Y Combinator standard :**
- $500K pour 7% d'equity (standard deal YC)
- Techstars : $120K pour 6%
- 500 Global : $150K seed

**Fonctionnement :**
- L'investisseur apporte du capital qui se convertira en actions lors du prochain tour "qualifiant" (prix)
- Conversion avec un discount (souvent 20%) et/ou un valuation cap

### BSPCE (Bons de Souscription de Parts de Createur d'Entreprise) - France

**Definition** : instrument specifiquement francais permettant d'attribuer des stock options a fiscalite avantageuse aux employes et dirigeants de startups.

**Conditions d'eligibilite :**
- Societe soumise a l'IS en France
- Moins de 15 ans d'existence
- Non cotee ou capitalisation < 150M EUR
- 25% minimum du capital detenu par des personnes physiques

**Fiscalite avantageuse :**
- Plus-value imposee au PFU (Prelevement Forfaitaire Unique) de 12.8% + 17.2% de prelevements sociaux = **30% total**
- Si detention < 1 an : imposition au bareme progressif IR (jusqu'a 45%) + PS
- Compare a des stock options classiques : bien plus avantageux

**Exemple :**
- BSPCE avec prix d'exercice de 1 EUR/action
- L'employe exerce quand l'action vaut 10 EUR
- Plus-value : 9 EUR/action
- Impot (si detention > 1 an) : 9 x 30% = 2.7 EUR
- Net : 6.3 EUR/action

### BSA (Bons de Souscription d'Actions)

**Definition** : droit d'acheter des actions a un prix fixe dans le futur. Utilise pour les advisors, consultants externes, ou investisseurs.

**Differences avec les BSPCE :**
| Critere | BSPCE | BSA |
|---------|-------|-----|
| Beneficiaires | Salaries et mandataires sociaux | Toute personne (y compris externe) |
| Fiscalite | 30% (PFU) | 30% (PFU) + evaluation avantage en nature |
| Prix | Peut etre a la valeur nominale | Doit refleter la valeur reelle |
| Condition d'emploi | Oui | Non |
| Attractivite | Tres attractive | Moins attractive (cout d'acquisition) |

---

## 7. Drag-along / Tag-along

### Tag-along (droit de sortie conjointe)

**Definition** : si un actionnaire majoritaire vend ses actions, les minoritaires ont le droit de vendre les leurs aux memes conditions.

**Objectif** : proteger les minoritaires contre une vente par les fondateurs qui les laisserait coinces avec un nouvel actionnaire qu'ils n'ont pas choisi.

**Standard** : systematiquement inclus, c'est une clause protectrice pour les investisseurs. Les fondateurs doivent l'accepter.

**Clause type :**
> "En cas de cession par les Fondateurs de plus de 50% du capital, les Investisseurs beneficient d'un droit de sortie conjointe leur permettant de ceder leurs actions aux memes conditions de prix et modalites que celles convenues par les Fondateurs."

### Drag-along (obligation de sortie forcee)

**Definition** : si une majorite qualifiee d'actionnaires accepte une offre d'acquisition, ils peuvent forcer les minoritaires a vendre egalement aux memes conditions.

**Objectif** : eviter qu'un actionnaire minoritaire bloque une vente souhaitee par la majorite.

**Seuils typiques :**
- Seed : 66-75% des droits de vote (ou majorite des preferred + majorite des common)
- Serie A+ : souvent abaisse a 60-66%

**Points de negociation :**
- **Prix plancher** : le drag ne peut s'activer que si le prix de vente depasse un minimum (typiquement le montant de la liquidation preference 1x)
- **Majorite qualifiee** : exiger que le drag necessite l'accord de X% des fondateurs ET des investisseurs
- **Delai** : prevoir un delai de notification suffisant (30-60 jours)

### Clause type drag-along :
> "En cas d'offre d'acquisition de 100% du capital a un prix superieur a [X] EUR par action, si les detenteurs de plus de 66% du capital approuvent la cession, tous les actionnaires seront tenus de ceder leurs actions aux memes conditions."

---

## 8. Composition du Board

### Standard par stade

**Pre-seed / Seed :**
- **Composition typique** : 3 sieges
  - 2 fondateurs + 1 investisseur (si lead avec ticket significatif, ex: CDG Invest, Partech Africa)
  - Ou 3 fondateurs (pas de siege investisseur pour les petits tickets, ex: Kalys Ventures, Kima Ventures)
- Les fondateurs conservent la majorite

**Serie A :**
- **Composition typique** : 5 sieges
  - 2 fondateurs + 2 investisseurs (ex: Partech Africa + CDG Invest) + 1 independant
  - L'independant est choisi d'un commun accord
- Equilibre des pouvoirs : personne n'a la majorite seul

**Serie B+ :**
- **Composition typique** : 5-7 sieges
  - 2 fondateurs + 2-3 investisseurs + 1-2 independants
  - Les investisseurs peuvent avoir la majorite a ce stade

### Droits du board

**Decisions courantes (CEO seul) :**
- Operations quotidiennes
- Recrutements sous un certain seuil de salaire
- Depenses dans le budget approuve

**Decisions necessitant l'accord du board :**
- Budget annuel
- Recrutement des executives (C-suite)
- Contrats au-dela d'un certain montant (typiquement >50K-100K EUR)
- Modifications de la strategie
- Rapports financiers trimestriels

### Observer seats

Les investisseurs qui n'ont pas de siege au board peuvent negocier un "observer seat" (siege d'observateur) :
- Droit d'assister aux reunions du board
- Pas de droit de vote
- Acces aux memes informations que les membres du board
- Courant pour les co-investisseurs (le lead prend le siege, les co-investisseurs sont observateurs)

---

## 9. Protective Provisions (droits de veto)

### Definition
Les protective provisions sont des decisions qui necessitent l'accord specifique des investisseurs (detenteurs d'actions de preference), au-dela du vote normal en AG.

### Liste standard des decisions reservees

| Decision | Standard seed | Standard Serie A |
|----------|--------------|-----------------|
| Emettre de nouvelles actions | Oui | Oui |
| Contracter une dette >50K EUR | Souvent | Oui |
| Vendre ou liquider l'entreprise | Oui | Oui |
| Modifier les statuts | Oui | Oui |
| Changer la nature de l'activite | Oui | Oui |
| Payer des dividendes | Oui | Oui |
| Augmenter le pool ESOP | Souvent | Oui |
| Recruter/licencier le CEO | Rarement | Oui |
| Budget annuel | Rarement | Oui |
| Transactions avec parties liees | Oui | Oui |
| Investissements >100K EUR | Rarement | Oui |

### Conseil de negociation
- Au seed : limiter les protective provisions au strict minimum (emission d'actions, vente/liquidation, modification des statuts). Trop de vetoes au seed = fondateur paralyse.
- En Serie A : accepter des provisions plus larges, c'est standard. Mais veiller a ce que les seuils soient raisonnables.
- Toujours negocier des seuils : "approbation necessaire pour toute depense >100K EUR" plutot que "approbation necessaire pour toute depense".

---

## 10. Information Rights et Reporting

### Standard du marche

**Reporting mensuel (standard seed et au-dela) :**
- MRR, croissance, churn, NRR (mediane 102%, SaaS Capital 2025)
- Nombre de clients / utilisateurs
- Cash en banque et runway restant
- Recrutements
- Top 3 faits marquants
- Top 3 defis

**Reporting trimestriel :**
- Etats financiers (bilan, P&L)
- Budget vs realise
- Pipeline commercial
- Roadmap produit mise a jour
- KPIs detailles (LTV:CAC, marge brute, Rule of 40)

**Reporting annuel :**
- Comptes annuels certifies (si >1M EUR de CA ou obligation legale)
- Budget previsionnel N+1
- Plan strategique actualise

### Clause type
> "La Societe s'engage a fournir aux Investisseurs, dans un delai de 15 jours suivant la fin de chaque mois calendaire, un reporting mensuel comprenant les indicateurs cles de performance, la situation de tresorerie et les faits marquants. Des etats financiers trimestriels seront fournis dans un delai de 30 jours suivant la fin de chaque trimestre."

### Conseil
Le reporting n'est pas une corvee -- c'est un outil de gestion. Les fondateurs qui envoient des updates reguliers construisent la confiance avec leurs investisseurs (CDG Invest, Partech Africa, etc.) et obtiennent plus de support (introductions, conseils, reinvestissement).

---

## 11. Red Flags Checklist

### Clauses toxiques a identifier et refuser

| Red Flag | Pourquoi c'est problematique | Alternative acceptable |
|----------|-----------------------------|-----------------------|
| Full ratchet anti-dilution | Dilution massive en cas de down round | Weighted average |
| 2x+ liquidation preference | Les fondateurs ne touchent rien en cas de sortie moyenne | 1x non-participating |
| Participating preferred | Double dipping, l'investisseur est paye deux fois | Non-participating |
| Redemption rights (<5 ans) | L'investisseur peut exiger le remboursement | Pas de redemption, ou >7 ans |
| Board majority investisseur (seed) | Les fondateurs perdent le controle des le debut | Majorite fondateurs au seed |
| No single trigger acceleration | En cas d'acquisition, le fondateur continue a vester pour l'acheteur | Single trigger (au moins partiel) |
| Super voting rights investisseur | Les investisseurs controlent les decisions avec une minorite du capital | Proportionnel au capital |
| Pay-to-play agressif | Les investisseurs qui ne reinvestissent pas perdent leurs droits | Pay-to-play raisonnable ou pas de pay-to-play |
| Exclusivite >60 jours | Bloque le fondateur trop longtemps sans garantie de closing | 30-45 jours maximum |
| Ratchet sur les milestones | L'investisseur recoit plus d'equity si les milestones ne sont pas atteints | Milestones comme objectifs, pas comme penalites |

### Signaux d'alerte dans le comportement de l'investisseur
- Pression pour signer rapidement ("c'est a prendre ou a laisser")
- Refus de partager des references de fondateurs de son portefeuille
- Modification des termes entre la term sheet et les documents definitifs
- Demande de garantie personnelle du fondateur
- Ajout de clauses non discutees dans les documents juridiques finaux

---

## 12. Modele de Term Sheet Simplifie (Seed)

### Exemple commente

```
TERM SHEET - MEMORANDUM D'ENTENTE
(Document non contraignant, sauf clauses d'exclusivite et confidentialite)

DATE : [date]
SOCIETE : [nom], SAS au capital de [X] EUR, RCS [ville] [numero]
INVESTISSEUR(S) : [nom(s)]

1. MONTANT DE L'INVESTISSEMENT
   Montant total : 1 500 000 EUR
   Lead investor : [nom] pour 900 000 EUR
   Co-investisseurs : [noms] pour 600 000 EUR

2. VALORISATION
   Pre-money : 5 000 000 EUR (fully diluted, incluant un ESOP de 10%)
   Post-money : 6 500 000 EUR
   Prix par action : [X] EUR

3. TYPE D'ACTIONS
   Actions de preference de categorie A
   Convertibles en actions ordinaires a tout moment au gre du porteur

4. LIQUIDATION PREFERENCE
   1x non-participating
   Priorite de remboursement en cas de liquidite event

5. ANTI-DILUTION
   Broad-based weighted average

6. POOL D'OPTIONS (ESOP)
   10% du capital post-money reserve pour les futurs employes
   Inclus dans le pre-money

7. VESTING FONDATEURS
   4 ans, cliff 1 an
   Acceleration single trigger a 100% en cas de changement de controle
   Credit de [X] mois pour le temps passe avant le closing

8. GOUVERNANCE
   Board de 3 sieges : 2 fondateurs + 1 investisseur (lead)
   Decisions reservees : emission d'actions, vente/liquidation,
   dette >100K EUR, modification statuts

9. DROITS D'INFORMATION
   Reporting mensuel (KPIs, cash position)
   Etats financiers trimestriels
   Comptes annuels

10. DROIT DE PREEMPTION (ROFR)
    En cas de cession d'actions par un actionnaire, droit de preemption
    au profit des autres actionnaires, au prorata de leur participation

11. TAG-ALONG / DRAG-ALONG
    Tag-along : 100% des investisseurs
    Drag-along : majorite de 66% du capital, prix plancher = 1x
    liquidation preference

12. EXCLUSIVITE
    45 jours a compter de la signature de la presente term sheet
    Pendant cette periode, la Societe s'engage a ne pas negocier
    avec d'autres investisseurs potentiels

13. CONFIDENTIALITE
    Les parties s'engagent a maintenir confidentiel le contenu
    de la presente term sheet

14. CONDITIONS SUSPENSIVES
    - Due diligence satisfaisante (financiere, legale, technique)
    - Approbation du comite d'investissement de [nom du fonds]
    - Absence d'evenement materiel negatif avant le closing

15. FRAIS JURIDIQUES
    La Societe prend en charge les frais juridiques de l'Investisseur
    dans la limite de 15 000 EUR HT

16. DROIT APPLICABLE
    Droit francais. Competence exclusive des tribunaux de [ville]
```

---

## Negocier sa Term Sheet : Les 10 Regles d'Or

1. **Engager un avocat specialise en VC** avant de negocier (5-15K EUR bien investis)
2. **Comprendre chaque clause** : ne jamais signer ce que vous ne comprenez pas
3. **Prioriser les termes economiques** (valorisation, liquidation preference 1x non-participating, anti-dilution weighted average) sur les termes de gouvernance au seed
4. **Negocier en lot** : ne pas negocier point par point, mais proposer un package
5. **Avoir un BATNA (Best Alternative)** : si vous avez une autre term sheet (ex: de CDG Invest et Partech Africa en parallele), votre pouvoir de negociation est enorme
6. **Ne pas se battre sur tout** : choisir 3-5 points cruciaux et lacher le reste
7. **Documenter tous les accords oraux** par ecrit (email de confirmation)
8. **Comparer avec les standards du marche** : les arguments "c'est le standard" sont puissants
9. **Penser long terme** : cette term sheet definit les bases des prochains tours
10. **Garder une bonne relation** : vous allez travailler avec cet investisseur pendant 5-10 ans

---

## Specificites Maroc

### Cadre juridique
- **SAS recommandee** pour les levees de fonds au Maroc (permet les actions de preference depuis la loi 19-20 de 2021)
- **SARL** : plus simple mais moins flexible (pas d'actions de preference, parts sociales uniquement)
- **Pacte d'associes** : reconnu par le droit marocain, mais certaines clauses (drag-along, liquidation preference) sont moins testees en jurisprudence qu'en France

### Specificites reglementaires
- **Office des Changes** : tout investissement etranger dans une societe marocaine necessite une declaration aupres de l'Office des Changes. Les flux sortants (dividendes, cession) sont egalement reglementes.
- **AMMC** : pour les operations de marche et le crowdfunding (loi 15-18 sur le financement collaboratif)
- **Delais** : les formalites administratives (RC, AGE, depots legaux) prennent typiquement 2-6 semaines au Maroc
- **Frais de notaire** : les PV d'AGE et modifications de statuts doivent etre notaries. Cout : 1-5K MAD selon la complexite.

### Fiscalite (CGI 2025)
- **IS** : 10% (<300K MAD), 20% (300K-1M MAD), 35% (>1M MAD)
- La fiscalite sur les plus-values de cession d'actions est de 20% au Maroc (avec un minimum de 15% de l'IR)
- Les conventions de compte courant d'associe sont courantes pour les apports temporaires
- Site de reference : https://www.tax.gov.ma/

### Points d'attention specifiques
- Les clauses de vesting (4 ans, 1 an cliff) et de liquidation preference (1x non-participating) sont moins familieres des juristes marocains generalistes. Engager un avocat d'affaires ayant l'experience des deals VC.
- CDG Invest, MNF Ventures, et Outlierz Ventures sont les fonds locaux les plus familiers avec ces structures.

---

## Sources

- [CDG Invest - Fonds d'investissement marocain](https://www.cdginvest.ma/)
- [Partech Partners - Fonds VC Europe et Afrique](https://partechpartners.com/)
- [BPI France - Financements et subventions startups](https://www.bpifrance.fr/)
- [AMMC - Autorite Marocaine du Marche des Capitaux](https://www.ammc.ma/)
- [Direction Generale des Impots Maroc](https://www.tax.gov.ma/)
- [SaaS Capital - Annual B2B SaaS Benchmarks 2025](https://www.saas-capital.com/research/)
- [Bessemer Venture Partners - Cloud 100 Benchmarks](https://www.bvp.com/atlas/the-cloud-100-benchmarks-report)
- [Innov Invest / Tamwilcom](https://innovinvest.ma/)
- [FORSA - Programme national d'entrepreneuriat](https://forsa.ma/)

---

*Donnees basees sur les standards du marche 2024-2025. Les termes peuvent varier significativement selon les investisseurs et les juridictions. Sources verifiees au moment de la redaction.*
