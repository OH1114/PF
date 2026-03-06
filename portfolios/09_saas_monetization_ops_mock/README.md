# 09 SaaS課金運用（Demo版/有料版切替）模擬案件

## 案件想定
- クライアント: B2B向け小規模SaaS企業
- 依頼内容: 既存デモアプリを有料化し、運用できる形まで整備
- 納期感: 3〜5週間

## このPFで示すこと
- `demo/pro/enterprise` のプラン設計
- 機能ゲートによる権限制御
- 課金イベント（Webhook）を契約状態へ反映する流れ
- 障害時に運用できる監視・通知の前提

## 構成
```txt
app/
  dashboard/page.tsx         # プラン別の機能利用表示
  pricing/page.tsx           # 料金表とアップグレード導線
lib/
  plans.ts                   # プラン定義と料金設定
  feature-gate.ts            # プラン別の機能可否判定
.env.example
package.json
```

## デモ版と有料版の差分

| 項目 | Demo版 | Pro版 |
|---|---|---|
| 月額 | 0円 | 9,800円（例） |
| 月次レポートDL | 不可 | 可 |
| API連携 | 不可 | 可 |
| 利用上限 | 50リクエスト/月 | 5,000リクエスト/月 |
| サポート | コミュニティ | メール24h以内 |

## `.env` 例
- `NEXT_PUBLIC_APP_URL`: アプリURL
- `STRIPE_SECRET_KEY`: Stripeのシークレットキー
- `STRIPE_WEBHOOK_SECRET`: Webhook署名検証キー
- `NEXT_PUBLIC_STRIPE_PRICE_PRO_MONTHLY`: ProプランのPrice ID
- `SENTRY_DSN`: 障害監視用DSN

## 実務向け補足
1. プラン変更は「即時反映」と「次回更新時反映」を分けて設計する。
2. 支払い失敗時は猶予期間を設け、段階的に機能制限する。
3. `billing_events` テーブルでWebhookイベントを冪等処理する。
