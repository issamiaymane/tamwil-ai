import { ChatRequest, ChatResponse } from "./types";

const MOCK_DELAY_MS = 1200;

export async function sendMessage(request: ChatRequest): Promise<ChatResponse> {
  // TODO: Replace this mock with a real fetch when the FastAPI backend is ready
  // const res = await fetch("http://localhost:8000/api/chat", {
  //   method: "POST",
  //   headers: { "Content-Type": "application/json" },
  //   body: JSON.stringify(request),
  // });
  // return res.json();

  await new Promise((resolve) => setTimeout(resolve, MOCK_DELAY_MS));

  const { message, profile } = request;
  const msg = message.toLowerCase();

  if (msg.includes("score") || msg.includes("fundability")) {
    return {
      reply: `**Score de Fundability : 62/100**\n\n| Métrique | Valeur | Benchmark (${profile.stade || "seed"}) | Statut |\n|----------|--------|-----------|--------|\n| MRR | ${profile.mrr || "N/A"} € | 10 000 € | ${Number(profile.mrr) >= 10000 ? "✅ Bon" : "⚠️ À améliorer"} |\n| Burn Rate | ${profile.burnRate || "N/A"} € | < 20 000 € | OK |\n| Churn | ${profile.churn || "N/A"}% | < 5% | ${Number(profile.churn) <= 5 ? "✅ Bon" : "⚠️ Élevé"} |\n\n**Recommandations :**\n1. Concentrez-vous sur l'augmentation du MRR\n2. Optimisez votre ratio LTV/CAC\n3. Réduisez le churn en améliorant l'onboarding`,
    };
  }

  if (msg.includes("investisseur") || msg.includes("investor") || msg.includes("vc")) {
    return {
      reply: `Voici les investisseurs correspondant à votre profil (**${profile.secteur || "non précisé"}**, **${profile.stade || "non précisé"}**) :\n\n1. **Atlas Ventures** — Seed, Fintech, Maroc — Ticket : 50K-500K €\n2. **CDG Invest** — Pre-seed à Series A — Ticket : 100K-2M MAD\n3. **Outlierz Ventures** — Seed, Tech — Ticket : 100K-500K USD\n4. **212 Founders** — Pre-seed, Maroc — Ticket : 50K-200K €\n5. **Azur Innovation Fund** — Seed, Afrique francophone — Ticket : 100K-1M €`,
    };
  }

  if (msg.includes("subvention") || msg.includes("aide") || msg.includes("programme")) {
    return {
      reply: `Voici les subventions éligibles pour votre profil :\n\n1. **Innov Invest** — Tamwilcom — Prêt d'honneur jusqu'à 500K MAD\n2. **Maroc PME** — Subvention jusqu'à 50% des investissements\n3. **Forsa** — Programme d'accompagnement + financement\n4. **French Tech Ticket** — Pour les startups à potentiel international`,
    };
  }

  if (msg.includes("diagnostic") || msg.includes("kpi") || msg.includes("analyser")) {
    return {
      reply: `**Diagnostic Financier**\n\n| KPI | Valeur | Interprétation |\n|-----|--------|----------------|\n| MRR | ${profile.mrr || "N/A"} € | ${Number(profile.mrr) >= 5000 ? "Traction correcte" : "Traction insuffisante"} |\n| Churn | ${profile.churn || "N/A"}% | ${Number(profile.churn) <= 5 ? "Acceptable" : "Trop élevé — objectif < 5%"} |\n| LTV/CAC | ${Number(profile.ltv) && Number(profile.cac) ? (Number(profile.ltv) / Number(profile.cac)).toFixed(1) : "N/A"} | ${Number(profile.ltv) / Number(profile.cac) >= 3 ? "Bon ratio" : "Ratio faible — objectif > 3x"} |\n\n**Conseils :**\n- Améliorez l'onboarding pour réduire le churn\n- Augmentez le LTV via l'upsell et la rétention\n- Optimisez le CAC via des canaux organiques`,
    };
  }

  return {
    reply: `Bienvenue sur **Tamwil AI** ! Je suis votre assistant en financement de startups.\n\nJe peux vous aider avec :\n\n- **Score de fundability** — Évaluez votre préparation à la levée de fonds\n- **Diagnostic financier** — Analysez vos KPIs\n- **Matching investisseurs** — Trouvez les bons VCs et Business Angels\n- **Matching subventions** — Identifiez les aides disponibles\n- **Questions générales** — Tout sur le financement startup\n\nRemplissez votre profil dans la barre latérale, puis posez-moi une question !`,
  };
}
