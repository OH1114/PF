export type PlanName = "demo" | "pro" | "enterprise";

export type PlanDefinition = {
  name: PlanName;
  monthlyPriceJpy: number;
  monthlyUsageLimit: number;
  features: string[];
};

export const PLAN_DEFINITIONS: Record<PlanName, PlanDefinition> = {
  demo: {
    name: "demo",
    monthlyPriceJpy: 0,
    monthlyUsageLimit: 50,
    features: [
      "基本ダッシュボード",
      "サンプルデータ閲覧",
      "メールサポートなし"
    ]
  },
  pro: {
    name: "pro",
    monthlyPriceJpy: 9800,
    monthlyUsageLimit: 5000,
    features: [
      "月次レポートダウンロード",
      "API連携",
      "メールサポート（24h以内）"
    ]
  },
  enterprise: {
    name: "enterprise",
    monthlyPriceJpy: 49800,
    monthlyUsageLimit: 50000,
    features: [
      "SSO/SAML",
      "監査ログ保持",
      "専任サポート"
    ]
  }
};
