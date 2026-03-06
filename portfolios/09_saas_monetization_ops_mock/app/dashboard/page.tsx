import { isFeatureEnabled } from "../../lib/feature-gate";
import type { PlanName } from "../../lib/plans";

const CURRENT_PLAN: PlanName = "demo";

export default function DashboardPage() {
  const canExport = isFeatureEnabled(CURRENT_PLAN, "monthly_report_export");
  const canUseApi = isFeatureEnabled(CURRENT_PLAN, "api_integration");

  return (
    <main style={{ padding: 24 }}>
      <h1>Dashboard ({CURRENT_PLAN.toUpperCase()})</h1>
      <p>プラン別の機能制限を確認する画面です。</p>
      <ul>
        <li>月次レポートエクスポート: {canExport ? "有効" : "無効"}</li>
        <li>外部API連携: {canUseApi ? "有効" : "無効"}</li>
      </ul>
      {!canExport && (
        <p>
          この機能は Pro 以上で利用できます。料金ページからアップグレードしてください。
        </p>
      )}
    </main>
  );
}
