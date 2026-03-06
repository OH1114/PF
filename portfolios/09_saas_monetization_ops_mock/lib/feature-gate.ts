import type { PlanName } from "./plans";

export type FeatureKey =
  | "monthly_report_export"
  | "api_integration"
  | "advanced_audit_log";

type FeatureFlags = Record<FeatureKey, boolean>;

const FLAGS_BY_PLAN: Record<PlanName, FeatureFlags> = {
  demo: {
    monthly_report_export: false,
    api_integration: false,
    advanced_audit_log: false
  },
  pro: {
    monthly_report_export: true,
    api_integration: true,
    advanced_audit_log: false
  },
  enterprise: {
    monthly_report_export: true,
    api_integration: true,
    advanced_audit_log: true
  }
};

export function isFeatureEnabled(plan: PlanName, feature: FeatureKey): boolean {
  return FLAGS_BY_PLAN[plan][feature];
}
