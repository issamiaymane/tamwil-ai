# Protection des Donnees : Loi 09-08 et RGPD

## Introduction

La protection des donnees personnelles est un enjeu majeur pour toute startup, en particulier celles qui operent dans le domaine numerique. Au Maroc, la **Loi 09-08** relative a la protection des personnes physiques a l'egard du traitement des donnees a caractere personnel constitue le cadre de reference, tandis que le **Reglement General sur la Protection des Donnees (RGPD — Reglement UE 2016/679)** de l'Union Europeenne s'applique des lors que la startup traite des donnees de residents europeens ou dispose d'un etablissement dans l'UE. Ce guide presente les deux cadres reglementaires, leurs differences, et propose une checklist de conformite pour les startups.

---

## 1. Loi 09-08 au Maroc

### Contexte
La **Loi 09-08** relative a la protection des personnes physiques a l'egard du traitement des donnees a caractere personnel a ete promulguee par le Dahir 1-09-15 du 18 fevrier 2009. Elle est largement inspiree de la directive europeenne 95/46/CE (predecesseur du RGPD). Son decret d'application est le **Decret 2-09-165** du 21 mai 2009.

### Autorite de controle : la CNDP
La **Commission Nationale de controle de la protection des Donnees a caractere Personnel (CNDP)** est l'autorite marocaine en charge de l'application de la Loi 09-08.

**Site officiel** : https://www.cndp.ma/

**Missions (art. 27-30 Loi 09-08) :**
- Recevoir et instruire les declarations et demandes d'autorisation de traitement
- Controler la conformite des traitements
- Recevoir les plaintes des citoyens
- Sensibiliser et accompagner les responsables de traitement
- Cooperer avec les autorites etrangeres de protection des donnees

### Principes fondamentaux de la Loi 09-08

| Principe | Description | Article |
|----------|-------------|---------|
| **Finalite** | Les donnees doivent etre collectees pour des finalites determinees, explicites et legitimes | art. 3-I |
| **Proportionnalite** | Les donnees collectees doivent etre adequates, pertinentes et non excessives | art. 3-II |
| **Exactitude** | Les donnees doivent etre exactes et mises a jour | art. 3-III |
| **Conservation limitee** | Les donnees ne doivent pas etre conservees au-dela de la duree necessaire | art. 3-IV |
| **Securite** | Le responsable du traitement doit assurer la securite des donnees | art. 23-24 |
| **Consentement** | Le traitement est soumis au consentement de la personne concernee (sauf exceptions) | art. 4 |
| **Transparence** | Les personnes doivent etre informees du traitement de leurs donnees | art. 5 |

### Obligations des responsables de traitement

**Declaration prealable obligatoire (art. 12-14 Loi 09-08) :**
- Tout traitement de donnees personnelles doit faire l'objet d'une **declaration prealable** aupres de la CNDP
- Formulaire en ligne sur cndp.ma
- Cout : gratuit pour la declaration, les demandes d'autorisation sont egalement gratuites
- Delai : la CNDP dispose de **2 mois** pour repondre (silence = acceptation pour les declarations simples)

**Autorisation prealable pour les donnees sensibles (art. 12 et 21 Loi 09-08) :**
Certains traitements necessitent une **autorisation expresse** de la CNDP :
- Donnees sensibles : origines raciales ou ethniques, opinions politiques, convictions religieuses ou philosophiques, appartenance syndicale, sante, vie sexuelle (art. 1 Loi 09-08)
- Donnees genetiques et biometriques
- Interconnexion de fichiers
- Utilisation de donnees a des fins de prospection
- Transferts de donnees vers des pays ne disposant pas d'un niveau de protection adequat (art. 43-44)

**Droits des personnes concernees (art. 5-8 Loi 09-08) :**
- **Droit d'acces** (art. 7) : toute personne peut demander au responsable du traitement si des donnees la concernant sont traitees, et obtenir communication de ces donnees
- **Droit de rectification** (art. 8) : faire corriger des donnees inexactes
- **Droit d'opposition** (art. 9) : s'opposer au traitement de ses donnees pour des motifs legitimes
- **Droit de suppression** : demander l'effacement de donnees traitees en violation de la loi

### Transferts internationaux de donnees (art. 43-44 Loi 09-08)

- Les transferts de donnees a caractere personnel vers un pays etranger ne peuvent avoir lieu que si ce pays assure un **niveau de protection suffisant**
- Autorisation de la CNDP requise pour les transferts vers des pays sans protection adequate
- La CNDP publie une liste de pays consideres comme ayant un niveau de protection adequat

### Sanctions (art. 51-66 Loi 09-08)

| Type de violation | Sanction | Article |
|-------------------|---------|---------|
| Traitement sans declaration/autorisation | **10 000 a 100 000 MAD** d'amende + emprisonnement 3 mois a 1 an | art. 52 |
| Non-respect des droits des personnes | **20 000 a 200 000 MAD** d'amende | art. 53-54 |
| Transfert non autorise de donnees a l'etranger | **10 000 a 100 000 MAD** d'amende | art. 60 |
| Collecte frauduleuse de donnees | **100 000 a 300 000 MAD** d'amende + emprisonnement 3 mois a 1 an | art. 57 |
| Utilisation de donnees sensibles sans autorisation | **50 000 a 300 000 MAD** d'amende + emprisonnement 6 mois a 2 ans | art. 58 |
| Entrave a l'action de la CNDP | **10 000 a 50 000 MAD** d'amende | art. 61 |

**Note** : les amendes prevues par la Loi 09-08 vont de **10 000 a 300 000 MAD**, et des peines de prison sont possibles pour les infractions les plus graves.

---

## 2. RGPD (Reglement General sur la Protection des Donnees — Reglement UE 2016/679)

### Champ d'application (art. 3 RGPD)

Le RGPD (Reglement 2016/679 du Parlement europeen et du Conseil du 27 avril 2016) s'applique a toute organisation qui :
1. Est etablie dans l'UE et traite des donnees personnelles (quel que soit le lieu du traitement)
2. N'est pas etablie dans l'UE mais traite des donnees de personnes se trouvant dans l'UE si elle :
   - Offre des biens ou services a des personnes dans l'UE (art. 3-2-a)
   - Suit le comportement de personnes dans l'UE (art. 3-2-b)

**Pour une startup marocaine, le RGPD s'applique si :**
- Elle a des clients en Europe (meme un seul)
- Elle a un site web en francais ciblant le marche francais
- Elle utilise des outils de tracking (Google Analytics, cookies) sur des visiteurs europeens
- Elle a des employes en Europe
- Elle a une filiale ou un etablissement en Europe

**Autorite de controle en France : la CNIL** (Commission Nationale de l'Informatique et des Libertes) — https://www.cnil.fr/

### Les 7 principes du RGPD (art. 5)

| # | Principe | Description | Article |
|---|----------|-------------|---------|
| 1 | **Liceite, loyaute, transparence** | Traitement licite, loyal et transparent envers la personne concernee | art. 5-1-a |
| 2 | **Limitation des finalites** | Donnees collectees pour des finalites determinees, explicites et legitimes | art. 5-1-b |
| 3 | **Minimisation des donnees** | Donnees adequates, pertinentes et limitees au necessaire | art. 5-1-c |
| 4 | **Exactitude** | Donnees exactes et tenues a jour | art. 5-1-d |
| 5 | **Limitation de la conservation** | Conservees pendant une duree n'excedant pas celle necessaire | art. 5-1-e |
| 6 | **Integrite et confidentialite** | Securite appropriee (contre traitement non autorise, perte, destruction) | art. 5-1-f |
| 7 | **Responsabilite (accountability)** | Le responsable du traitement doit pouvoir demontrer la conformite | art. 5-2 |

### Bases legales du traitement (art. 6 RGPD)

| Base legale | Exemple pour une startup | Article |
|------------|------------------------|---------|
| **Consentement** | Newsletter, cookies non essentiels, marketing | art. 6-1-a |
| **Execution d'un contrat** | Traitement des donnees client pour fournir le service | art. 6-1-b |
| **Obligation legale** | Conservation de factures (obligation comptable) | art. 6-1-c |
| **Interet vital** | Urgence medicale (healthtech) | art. 6-1-d |
| **Mission d'interet public** | Rarement applicable aux startups | art. 6-1-e |
| **Interet legitime** | Analytics, securite, prospection B2B (sous conditions) | art. 6-1-f |

### DPO — Delegue a la Protection des Donnees (art. 37-39 RGPD)

**Quand est-il obligatoire (art. 37-1 RGPD) ?**
- Organismes publics
- Activites de base consistant en un suivi regulier et systematique a grande echelle des personnes
- Traitement a grande echelle de donnees sensibles

**Pour les startups :**
- Le DPO n'est generalement pas obligatoire au seed/Serie A, sauf si le coeur de l'activite est le traitement de donnees (adtech, healthtech, fintech)
- Meme si non obligatoire, designer un "referent RGPD" est recommande
- Le DPO peut etre interne ou externe (cabinet specialise : 500-2000 EUR/mois)

### Registre des traitements (art. 30 RGPD)

**Obligatoire** pour toute organisation. Le registre doit contenir :
- Le nom et les coordonnees du responsable du traitement
- Les finalites du traitement
- Les categories de personnes concernees et de donnees personnelles
- Les categories de destinataires
- Les transferts vers des pays tiers
- Les delais de conservation
- Les mesures de securite techniques et organisationnelles

### Privacy by design, Privacy by default (art. 25 RGPD)

- **Privacy by design** : la protection des donnees doit etre integree des la conception du produit ou service
- **Privacy by default** : par defaut, seules les donnees strictement necessaires doivent etre traitees
- Ces obligations s'appliquent au responsable du traitement des la phase de developpement

### DPIA — Analyse d'impact (art. 35 RGPD)

L'analyse d'impact relative a la protection des donnees est obligatoire quand le traitement est "susceptible d'engendrer un risque eleve" pour les droits et libertes des personnes.

**Cas declencheurs :**
- Profilage systematique (scoring credit, recommandations personnalisees)
- Traitement a grande echelle de donnees sensibles (sante, financieres)
- Surveillance systematique d'un lieu public
- Croisement de bases de donnees a grande echelle
- Traitements innovants utilisant de nouvelles technologies (IA, biometrie)

### Notification des violations de donnees (art. 33-34 RGPD)

- Notification a l'autorite de controle dans un delai de **72 heures** apres la decouverte de la violation (art. 33)
- Notification aux personnes concernees si le risque est eleve (art. 34)

### Sanctions RGPD (art. 83)

| Niveau | Montant maximum | Exemples de violations | Article |
|--------|----------------|----------------------|---------|
| Niveau 1 | **10M EUR ou 2% du CA mondial** | Manquements techniques (securite, DPO, registre) | art. 83-4 |
| Niveau 2 | **20M EUR ou 4% du CA mondial** | Violations des principes, droits des personnes, transferts | art. 83-5 |

**Exemples reels de sanctions :**
- **Amazon** : 746M EUR (Luxembourg, 2021) pour violations liees au ciblage publicitaire
- **Google** : 150M EUR (CNIL France, 2022) pour cookies non conformes
- **Meta** : 1.2 milliard EUR (Irlande, 2023) pour transferts de donnees vers les US
- **Clearview AI** : 20M EUR (CNIL France, 2022) pour collecte illegale de donnees biometriques

---

## 3. Tableau Comparatif : Loi 09-08 vs RGPD

| Critere | Loi 09-08 (Maroc) | RGPD (UE — Reglement 2016/679) |
|---------|-------------------|-----------|
| Date d'adoption | 2009 (Dahir 1-09-15) | 2016 (applicable 25 mai 2018) |
| Autorite de controle | CNDP (https://www.cndp.ma/) | CNIL en France (https://www.cnil.fr/), et autorites nationales de chaque Etat membre |
| Formalite prealable | Declaration/autorisation CNDP obligatoire (art. 12) | Pas de declaration prealable (accountability, art. 5-2) |
| Registre des traitements | Non obligatoire (mais recommande) | **Obligatoire** (art. 30) |
| DPO | Non prevu par la Loi 09-08 | Obligatoire dans certains cas (art. 37) |
| DPIA | Non prevue formellement | Obligatoire si risque eleve (art. 35) |
| Droit a la portabilite | Non prevu | **Oui** (art. 20) |
| Droit a l'effacement | Limite (art. 8) | **Oui** — droit a l'oubli (art. 17) |
| Notification de violation | Non prevue par la Loi 09-08 | **72 heures** pour notifier l'autorite (art. 33) |
| Sanctions max | 300 000 MAD (~30K EUR) + prison possible | 20M EUR ou 4% du CA mondial (art. 83) |
| Transferts internationaux | Autorisation CNDP necessaire (art. 43-44) | Decisions d'adequation, SCCs, BCRs (art. 44-49) |
| Consentement | Requis — opt-in (art. 4) | Requis, libre, specifique, eclaire, univoque (art. 7) |
| Privacy by design | Non prevu explicitement | **Obligatoire** (art. 25) |
| Privacy by default | Non prevu explicitement | **Obligatoire** (art. 25) |
| Profilage | Non traite specifiquement | Encadre (art. 22, droit d'opposition) |
| Base legale | Consentement, contrat, obligation legale (art. 4) | Consentement, contrat, interet legitime, obligation legale, interet vital, mission publique (art. 6) |

---

## 4. Checklist de Conformite par Stade de Startup

### Pre-seed / MVP

**Priorite : les bases**
- [ ] Rediger une politique de confidentialite (privacy policy) pour le site web et l'app
- [ ] Mettre en place un bandeau cookies conforme (consentement avant depot de cookies non essentiels)
- [ ] Declarer les traitements aupres de la CNDP si operations au Maroc (art. 12 Loi 09-08)
- [ ] Identifier les donnees collectees et documenter les finalites
- [ ] Securiser les donnees de base : HTTPS, mots de passe hashes, acces limites
- [ ] Ne collecter que les donnees strictement necessaires (minimisation — art. 5-1-c RGPD / art. 3-II Loi 09-08)

### Seed (premiers clients)

**Priorite : structuration**
- [ ] Tenir un registre des traitements (art. 30 RGPD — meme simplifie)
- [ ] Rediger des CGU et CGV incluant les clauses de protection des donnees
- [ ] Mettre en place les processus de gestion des droits des personnes (acces, rectification, suppression — art. 7-9 Loi 09-08 / art. 15-21 RGPD)
- [ ] Evaluer si un DPO/referent RGPD est necessaire (art. 37 RGPD)
- [ ] Verifier la conformite des sous-traitants (hebergement cloud, outils SaaS) : clauses contractuelles types (SCCs) si transfert hors UE (art. 46 RGPD)
- [ ] Mettre en place un processus de gestion des violations de donnees
- [ ] Former l'equipe aux bonnes pratiques (sensibilisation RGPD / Loi 09-08)

### Serie A (scaling)

**Priorite : conformite complete**
- [ ] Nommer un DPO ou referent RGPD (interne ou externe — art. 37-39 RGPD)
- [ ] Realiser une DPIA pour les traitements a risque (art. 35 RGPD)
- [ ] Auditer la conformite des processus et systemes
- [ ] Mettre en place le Privacy by Design dans les processus de developpement produit (art. 25 RGPD)
- [ ] Contractualiser avec tous les sous-traitants (Data Processing Agreements — art. 28 RGPD)
- [ ] Implementer des mecanismes de consentement granulaire
- [ ] Definir et documenter les durees de conservation pour chaque type de donnee
- [ ] Planifier des audits reguliers (annuels minimum)
- [ ] Mettre en place un processus de notification de violation (72h — art. 33 RGPD)

### Serie B+ (expansion internationale)

**Priorite : compliance multi-juridictions**
- [ ] Evaluer les reglementations locales de chaque nouveau marche
- [ ] Mettre en place des BCRs (Binding Corporate Rules) si transferts intra-groupe (art. 47 RGPD)
- [ ] Certifications (ISO 27001, SOC 2) pour demontrer la conformite
- [ ] Equipe compliance dediee (DPO + juriste + security officer)
- [ ] Audit externe par un cabinet specialise

---

## 5. Cas Particuliers par Type de Startup

### 5.1 SaaS B2B

**Specificites :**
- Le client est generalement le "responsable du traitement" et la startup est "sous-traitant" (processor — art. 28 RGPD)
- Un DPA (Data Processing Agreement) est obligatoire avec chaque client (art. 28 RGPD)
- L'hebergement des donnees est un sujet sensible (les clients europeens peuvent exiger un hebergement en UE)
- Les donnees traitees sont souvent des donnees d'employes ou de clients du client

**Checklist specifique SaaS B2B :**
- [ ] DPA template pret et conforme RGPD (art. 28)
- [ ] Documentation des mesures de securite techniques et organisationnelles (TOMs)
- [ ] Choix d'hebergement : AWS EU (Ireland/Frankfurt), OVH, Scaleway pour les clients UE
- [ ] Politique de sous-traitance ulterieure (liste des sous-processeurs)
- [ ] SLA incluant les obligations de notification de violation
- [ ] Processus d'assistance au client pour les demandes de droits (acces, suppression)

### 5.2 Application Mobile (B2C)

**Specificites :**
- Collecte potentielle de nombreuses donnees : geolocalisation, contacts, photos, identifiants publicitaires
- Les app stores (Apple, Google) imposent leurs propres regles de privacy
- Le consentement doit etre obtenu avant l'activation de chaque permission

**Checklist specifique app mobile :**
- [ ] Privacy policy accessible depuis l'app et depuis l'app store listing
- [ ] Consentement explicite avant chaque permission (camera, GPS, contacts)
- [ ] Possibilite de retirer le consentement dans l'app
- [ ] Conformite App Tracking Transparency (ATT) pour iOS
- [ ] Conformite Google Play Data Safety
- [ ] Minimisation : ne demander que les permissions strictement necessaires
- [ ] Mecanisme de suppression de compte et des donnees (obligatoire Apple et Google depuis 2023)

### 5.3 E-commerce

**Specificites :**
- Donnees de paiement (PCI-DSS en plus de RGPD/Loi 09-08)
- Donnees de livraison (adresse, telephone)
- Historique d'achat et profilage pour la personnalisation
- Cookies de remarketing et tracking

**Checklist specifique e-commerce :**
- [ ] Bandeau cookies avec consentement granulaire (analytics, marketing, reseaux sociaux)
- [ ] Separation des consentements (newsletter != conditions de vente)
- [ ] Ne pas stocker les numeros de carte bancaire (utiliser un PSP certifie PCI-DSS : Stripe, CMI)
- [ ] Politique de retour et suppression des donnees post-commande
- [ ] Duree de conservation definie (donnees client : 3 ans apres le dernier achat est un standard)
- [ ] Droit d'opposition a la prospection commerciale

### 5.4 Fintech / Donnees Financieres

**Specificites :**
- Les donnees financieres sont considerees comme sensibles (meme si pas dans la categorie "donnees sensibles" au sens strict du RGPD)
- Obligations LCB-FT (Loi 43-05) qui imposent la conservation de certaines donnees (10 ans)
- Regulation sectorielle (BAM au Maroc — Loi 103-12, ACPR en France) en plus du RGPD
- Scoring et profilage financier soumis a des regles strictes

**Checklist specifique fintech :**
- [ ] DPIA obligatoire (profilage financier = risque eleve — art. 35 RGPD)
- [ ] Information claire sur les criteres de scoring/decision automatisee
- [ ] Droit d'obtenir une intervention humaine dans les decisions automatisees (art. 22 RGPD)
- [ ] Conservation des donnees KYC : 10 ans post-relation (obligation legale — Loi 43-05)
- [ ] Chiffrement des donnees financieres au repos et en transit
- [ ] Audit de securite regulier (pentest annuel minimum)
- [ ] Separation des environnements (production, staging, dev) avec anonymisation des donnees hors production

---

## 6. Transferts Internationaux de Donnees

### Maroc vers UE
- Le Maroc n'a pas encore obtenu de decision d'adequation de la Commission Europeenne
- Les transferts de donnees de l'UE vers le Maroc necessitent des garanties appropriees :
  - **Clauses Contractuelles Types (SCCs)** : le mecanisme le plus courant (art. 46-2-c RGPD)
  - **BCRs** : pour les groupes multinationaux (art. 47 RGPD)
  - **Derogations** : consentement explicite, execution d'un contrat (art. 49 RGPD)

### UE vers Maroc
- Les entreprises europeennes qui transferent des donnees vers un sous-traitant marocain doivent mettre en place des SCCs
- Depuis l'arret Schrems II (CJUE, 16 juillet 2020, C-311/18), une evaluation de la legislation du pays de destination est recommandee

### Maroc vers pays tiers
- La CNDP doit autoriser les transferts vers des pays ne disposant pas d'un niveau de protection adequat (art. 43-44 Loi 09-08)
- La CNDP publie une liste de pays consideres comme adequats

### Recommandation pratique pour les startups
Pour une startup marocaine ciblant le marche europeen :
1. Heberger les donnees des clients UE dans un data center en UE (AWS Ireland, OVH France)
2. Mettre en place des SCCs avec les clients UE
3. Documenter les mesures de protection supplementaires
4. Si possible, obtenir une certification ISO 27001 ou SOC 2

---

## 7. Ressources et Contacts

### Maroc
- **CNDP** : cndp.ma — declarations en ligne, guides pratiques, decisions
- **Loi 09-08** : texte integral disponible sur le site du Secretariat General du Gouvernement (sgg.gov.ma)

### France / UE
- **CNIL** : cnil.fr — guides, modeles, outils en ligne (registre des traitements, PIA)
- **RGPD** : texte integral sur eur-lex.europa.eu
- **EDPB** (European Data Protection Board) : edpb.europa.eu — lignes directrices europeennes

### Outils utiles
- **OneTrust** : plateforme de gestion de la conformite privacy (freemium)
- **Cookiebot / Axeptio** : gestion des cookies conforme RGPD (a partir de 9 EUR/mois)
- **iubenda** : generateur de privacy policy et cookie policy
- **Osano** : plateforme de consent management
- **CNIL PIA tool** : outil gratuit de la CNIL pour realiser des DPIA

---

## Sources

- [CNDP — Commission Nationale de controle de la protection des Donnees a caractere Personnel](https://www.cndp.ma/)
- [Loi 09-08 relative a la protection des donnees a caractere personnel (Dahir 1-09-15)](https://www.cndp.ma/)
- [CNIL — Commission Nationale de l'Informatique et des Libertes (France)](https://www.cnil.fr/)
- [RGPD — Reglement UE 2016/679 (texte integral)](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679)
- [EDPB — European Data Protection Board](https://edpb.europa.eu/)
- [Secretariat General du Gouvernement du Maroc (textes legislatifs)](https://www.sgg.gov.ma/)
- [Bank Al-Maghrib (BAM)](https://www.bkam.ma/)
- [Loi 43-05 relative a la lutte contre le blanchiment de capitaux](https://www.sgg.gov.ma/)
- [Loi 103-12 relative aux etablissements de credit et organismes assimiles](https://www.bkam.ma/)

*Donnees basees sur la legislation en vigueur en 2025. La protection des donnees est un domaine en evolution constante. Consultez les autorites competentes (CNDP, CNIL) pour les mises a jour. Consultez le fichier DISCLAIMER.md pour les avertissements importants.*
