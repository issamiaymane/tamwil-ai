"use client";

import { useState, useEffect } from "react";
import Joyride, {
  type CallBackProps,
  STATUS,
  type Step,
  type TooltipRenderProps,
} from "react-joyride";

const TOUR_STORAGE_KEY = "tamwil-tour-completed";

const ALL_STEPS: Step[] = [
  {
    target: "#tour-sidebar",
    content:
      "Bienvenue sur Tamwil AI ! Voici la barre latérale où vous pouvez gérer toutes vos conversations.",
    title: "Barre latérale",
    placement: "right",
    disableBeacon: true,
  },
  {
    target: "#tour-new-chat",
    content:
      "Cliquez ici pour démarrer une nouvelle conversation avec l'assistant.",
    title: "Nouvelle conversation",
    placement: "bottom",
    disableBeacon: true,
  },
  {
    target: "#tour-profile",
    content:
      "Configurez le profil de votre startup ici pour obtenir des résultats personnalisés (secteur, stade, métriques financières).",
    title: "Profil startup",
    placement: "top",
    disableBeacon: true,
  },
  {
    target: "#tour-suggestions",
    content:
      "Utilisez ces suggestions pour poser rapidement une question courante sur le financement.",
    title: "Questions suggérées",
    placement: "top",
    disableBeacon: true,
  },
  {
    target: "#tour-chat-input",
    content:
      "Tapez votre question ici et appuyez sur Entrée pour envoyer. Shift+Entrée pour un retour à la ligne.",
    title: "Zone de saisie",
    placement: "top",
    disableBeacon: true,
  },
  {
    target: "#tour-theme-toggle",
    content:
      "Basculez entre le mode clair et le mode sombre selon votre préférence.",
    title: "Thème",
    placement: "bottom",
    disableBeacon: true,
  },
];

const SIDEBAR_TARGETS = new Set([
  "#tour-sidebar",
  "#tour-new-chat",
  "#tour-profile",
]);

function CustomTooltip({
  continuous,
  index,
  step,
  backProps,
  closeProps,
  primaryProps,
  skipProps,
  tooltipProps,
  size,
}: TooltipRenderProps) {
  return (
    <div
      {...tooltipProps}
      className="rounded-xl border border-border bg-popover text-popover-foreground shadow-lg p-4 max-w-sm"
    >
      {step.title && (
        <h3 className="text-sm font-semibold mb-1">{step.title as string}</h3>
      )}
      <p className="text-sm text-muted-foreground">{step.content as string}</p>

      <div className="flex items-center justify-between mt-4">
        <button
          {...skipProps}
          className="text-xs text-muted-foreground/60 hover:text-muted-foreground transition-colors"
        >
          Passer le tour
        </button>
        <div className="flex gap-2">
          {index > 0 && (
            <button
              {...backProps}
              className="rounded-md border border-border px-3 py-1.5 text-xs font-medium transition-colors hover:bg-accent"
            >
              Précédent
            </button>
          )}
          {continuous ? (
            <button
              {...primaryProps}
              className="rounded-md bg-primary text-primary-foreground px-3 py-1.5 text-xs font-medium transition-colors hover:bg-primary/90"
            >
              {index === size - 1 ? "Terminer" : "Suivant"}
            </button>
          ) : (
            <button
              {...closeProps}
              className="rounded-md bg-primary text-primary-foreground px-3 py-1.5 text-xs font-medium transition-colors hover:bg-primary/90"
            >
              Fermer
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export function GuidedTour() {
  const [run, setRun] = useState(false);
  const [mounted, setMounted] = useState(false);
  const [steps, setSteps] = useState<Step[]>([]);

  useEffect(() => {
    setMounted(true);
    const completed = localStorage.getItem(TOUR_STORAGE_KEY);
    if (completed) return;

    // On mobile, skip sidebar steps since the sidebar is hidden
    const isMobile = window.innerWidth < 768;
    const filtered = isMobile
      ? ALL_STEPS.filter((s) => !SIDEBAR_TARGETS.has(s.target as string))
      : ALL_STEPS;

    setSteps(filtered);

    // Small delay to ensure all target elements are rendered
    const timer = setTimeout(() => setRun(true), 500);
    return () => clearTimeout(timer);
  }, []);

  const handleCallback = (data: CallBackProps) => {
    const { status } = data;
    if (status === STATUS.FINISHED || status === STATUS.SKIPPED) {
      setRun(false);
      localStorage.setItem(TOUR_STORAGE_KEY, "true");
    }
  };

  // Don't render on server or before hydration
  if (!mounted) return null;

  return (
    <Joyride
      steps={steps}
      run={run}
      continuous
      showSkipButton
      showProgress={false}
      callback={handleCallback}
      tooltipComponent={CustomTooltip}
      locale={{
        back: "Précédent",
        close: "Fermer",
        last: "Terminer",
        next: "Suivant",
        skip: "Passer le tour",
      }}
      styles={{
        options: {
          zIndex: 10000,
          arrowColor: "var(--popover)",
        },
        overlay: {
          backgroundColor: "rgba(0, 0, 0, 0.5)",
        },
      }}
    />
  );
}
