import { StartupProfile } from "./types";

export const SECTEUR_OPTIONS = [
  { value: "fintech", label: "Fintech" },
  { value: "healthtech", label: "Healthtech" },
  { value: "edtech", label: "Edtech" },
  { value: "agritech", label: "Agritech" },
  { value: "proptech", label: "Proptech" },
  { value: "insurtech", label: "Insurtech" },
  { value: "cleantech", label: "Cleantech" },
  { value: "biotech", label: "Biotech" },
  { value: "legaltech", label: "Legaltech" },
  { value: "logistique", label: "Logistique" },
  { value: "e-commerce", label: "E-commerce" },
  { value: "saas", label: "SaaS" },
  { value: "marketplace", label: "Marketplace" },
  { value: "autre", label: "Autre" },
] as const;

export const STADE_OPTIONS = [
  { value: "pre-seed", label: "Pre-seed" },
  { value: "seed", label: "Seed" },
  { value: "series-a", label: "Series A" },
] as const;

export const PAYS_OPTIONS = [
  { value: "maroc", label: "Maroc" },
  { value: "france", label: "France" },
  { value: "tunisie", label: "Tunisie" },
  { value: "senegal", label: "Sénégal" },
  { value: "cote-divoire", label: "Côte d'Ivoire" },
  { value: "autre", label: "Autre" },
] as const;

export const DEFAULT_PROFILE: StartupProfile = {
  secteur: "",
  stade: "",
  pays: "",
  mrr: "",
  burnRate: "",
  churn: "",
  cac: "",
  ltv: "",
};
