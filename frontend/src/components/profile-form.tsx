"use client";

import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import { SECTEUR_OPTIONS, STADE_OPTIONS, PAYS_OPTIONS } from "@/lib/constants";
import { StartupProfile } from "@/lib/types";
import { BarChart3, Globe, Layers, Briefcase } from "lucide-react";

interface ProfileFormProps {
  profile: StartupProfile;
  onProfileChange: (profile: StartupProfile) => void;
}

export function ProfileForm({ profile, onProfileChange }: ProfileFormProps) {
  const handleNumericChange =
    (field: keyof StartupProfile) =>
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const val = e.target.value;
      onProfileChange({ ...profile, [field]: val === "" ? "" : Number(val) });
    };

  const preventInvalidKeys = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (["e", "E", "+", "-"].includes(e.key)) e.preventDefault();
  };

  return (
    <div className="grid grid-cols-2 gap-6">
      {/* Left column — Informations */}
      <div className="flex flex-col gap-4">
        <span className="text-sm font-semibold">Informations</span>

        <div className="space-y-1.5">
          <label className="flex items-center gap-1.5 text-sm font-medium text-muted-foreground">
            <Briefcase className="size-3.5" />
            Secteur
          </label>
          <Select
            value={profile.secteur}
            onValueChange={(v) =>
              onProfileChange({ ...profile, secteur: v })
            }
          >
            <SelectTrigger className="h-9 text-sm">
              <SelectValue placeholder="Choisir un secteur" />
            </SelectTrigger>
            <SelectContent>
              {SECTEUR_OPTIONS.map((opt) => (
                <SelectItem key={opt.value} value={opt.value}>
                  {opt.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-1.5">
          <label className="flex items-center gap-1.5 text-sm font-medium text-muted-foreground">
            <Layers className="size-3.5" />
            Stade
          </label>
          <Select
            value={profile.stade}
            onValueChange={(v) =>
              onProfileChange({ ...profile, stade: v })
            }
          >
            <SelectTrigger className="h-9 text-sm">
              <SelectValue placeholder="Choisir un stade" />
            </SelectTrigger>
            <SelectContent>
              {STADE_OPTIONS.map((opt) => (
                <SelectItem key={opt.value} value={opt.value}>
                  {opt.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div className="space-y-1.5">
          <label className="flex items-center gap-1.5 text-sm font-medium text-muted-foreground">
            <Globe className="size-3.5" />
            Pays
          </label>
          <Select
            value={profile.pays}
            onValueChange={(v) =>
              onProfileChange({ ...profile, pays: v })
            }
          >
            <SelectTrigger className="h-9 text-sm">
              <SelectValue placeholder="Choisir un pays" />
            </SelectTrigger>
            <SelectContent>
              {PAYS_OPTIONS.map((opt) => (
                <SelectItem key={opt.value} value={opt.value}>
                  {opt.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
      </div>

      {/* Right column — Métriques */}
      <div className="flex flex-col gap-4">
        <div className="flex items-center justify-between">
          <span className="flex items-center gap-1.5 text-sm font-semibold">
            <BarChart3 className="size-3.5" />
            Métriques
          </span>
          <Badge variant="outline" className="text-[10px] font-normal">
            Optionnel
          </Badge>
        </div>

        {[
          { label: "MRR (€)", field: "mrr" as const, placeholder: "Ex: 8000" },
          { label: "Burn Rate (€/mois)", field: "burnRate" as const, placeholder: "Ex: 15000" },
          { label: "Churn (%)", field: "churn" as const, placeholder: "Ex: 5" },
          { label: "CAC (€)", field: "cac" as const, placeholder: "Ex: 200" },
          { label: "LTV (€)", field: "ltv" as const, placeholder: "Ex: 2000" },
        ].map(({ label, field, placeholder }) => (
          <div key={field} className="space-y-1.5">
            <label className="text-sm font-medium text-muted-foreground">
              {label}
            </label>
            <Input
              type="number"
              placeholder={placeholder}
              value={profile[field]}
              onChange={handleNumericChange(field)}
              onKeyDown={preventInvalidKeys}
              className="h-9 text-sm"
            />
          </div>
        ))}
      </div>
    </div>
  );
}
