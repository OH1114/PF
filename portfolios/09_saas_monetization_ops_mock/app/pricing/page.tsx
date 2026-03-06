import { PLAN_DEFINITIONS } from "../../lib/plans";

export default function PricingPage() {
  const plans = Object.values(PLAN_DEFINITIONS);

  return (
    <main style={{ padding: 24 }}>
      <h1>SaaS Pricing</h1>
      <p>デモ版から有料版に移行するための料金設計サンプルです。</p>
      <ul>
        {plans.map((plan) => (
          <li key={plan.name} style={{ marginBottom: 16 }}>
            <h2>{plan.name.toUpperCase()}</h2>
            <p>
              月額: {plan.monthlyPriceJpy.toLocaleString("ja-JP")}円 / 上限:
              {plan.monthlyUsageLimit.toLocaleString("ja-JP")} リクエスト
            </p>
            <ul>
              {plan.features.map((feature) => (
                <li key={feature}>{feature}</li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </main>
  );
}
