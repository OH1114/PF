# 04 Next.js SaaS管理画面 模擬案件

## 案件想定
- クライアント: 小規模SaaS企業
- 依頼内容: 管理画面MVP（ユーザ一覧・契約プラン表示・簡易分析）
- 納期感: 2〜4週間

## 技術スタック
- Next.js (App Router)
- TypeScript
- Tailwind CSS（想定）
- PostgreSQL（想定）

## ファイル構成（学習用）
```txt
app/
  page.tsx                # ダッシュボードTOP
  users/page.tsx          # ユーザ一覧画面
components/
  KPIBox.tsx              # KPIカード
lib/
  api.ts                  # API呼び出しラッパ
.env.example              # 環境変数テンプレ
package.json              # スクリプト/依存関係の定義
```

## .env の例
- `NEXT_PUBLIC_API_BASE_URL`: フロントが参照するAPIのベースURL
- `INTERNAL_API_TOKEN`: サーバ側で使う内部連携トークン

