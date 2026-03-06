# 案件別サービス選定プレイブック（2026版・早見表）

この資料は、実案件でよく使うサービスを「何に使うか」「どう使い分けるか」「どの案件で選ぶか」をすぐ判断できるように整理した実務向け早見表です。  
対象は Web制作〜SaaS開発〜業務システム〜AI連携までを想定しています。

---

## 1. 最初に決める選定ルール（3ステップ）

1. 案件タイプを決める  
   - 例: LP/コーポレート、SaaS MVP、業務システム、EC、AI機能付き、Bot/連携基盤
2. 制約を明確化する  
   - 納期、予算、運用体制、個人情報/監査要件、将来の拡張性
3. 「最小構成」で開始し、必要に応じて拡張する  
   - 先に全部入れない。最初は運用可能最小セットを採用する

---

## 2. 案件タイプ別 おすすめ構成（即決用）

| 案件タイプ | 推奨アプリ基盤 | 推奨周辺サービス | まず避けるべき失敗 |
|---|---|---|---|
| LP/コーポレート | Next.js / Nuxt | GA4, Resend, Vercel | 計測設計なしで公開して改善不能になる |
| SaaS MVP | Next.js + FastAPI/NestJS | Clerk/Auth0, Stripe, PostgreSQL, Sentry, GitHub Actions | 課金と権限制御を後回しにする |
| 業務システム（予約/在庫/受発注） | Django / Laravel | PostgreSQL/MySQL, Redis, S3, Sentry, SES | ログ・監査・CSV出力を後付けにする |
| AI機能付き業務改善 | FastAPI | PostgreSQL, Redis, S3/R2, Sentry, PostHog | 料金上限とフォールバック未設計で課金事故 |
| API/Bot連携 | NestJS / FastAPI | OpenAPI, Redis Queue, Sentry, Datadog | Webhook署名検証・再送制御なし |
| EC/課金系 | Next.js + Laravel/FastAPI | Stripe, PostgreSQL, S3, SendGrid, Datadog | 決済イベントの冪等処理不足 |

---

## 3. 分野別サービス早見表（定番 + 使い分け）

## 3.1 認証（Clerk / Auth0 / Firebase Auth / Cognito）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| Clerk | Next.js SaaS MVP | 実装が速い、UI同梱 | 高度要件は設計確認が必要 | 短納期SaaSなら第一候補 |
| Auth0 | B2B/企業案件 | 企業向け機能が厚い | 設定が多く学習コストあり | 組織/権限が重いなら有力 |
| Firebase Auth | 小〜中規模Web/App | 導入が簡単、他Firebaseと相性 | ベンダーロックに注意 | MVPで速度重視なら有力 |
| Cognito | AWS前提案件 | AWS統合しやすい | 初期設定が複雑 | AWS運用チームがあるなら強い |

## 3.2 決済（Stripe / Paddle）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| Stripe | SaaS/EC/サブスク | 機能豊富、実績多数、APIが強い | Webhook運用の実装が必要 | 国内外問わず第一候補 |
| Paddle | グローバルSaaS | 課税・請求処理を簡略化しやすい | 地域・商流により要確認 | 海外販売比率が高いとき候補 |

## 3.3 DB（PostgreSQL / MySQL / Supabase）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| PostgreSQL | SaaS/業務システム全般 | 拡張性・信頼性が高い | 運用設計は必要 | 迷ったら第一候補 |
| MySQL | 既存運用・LAMP系 | 実績豊富、既存資産が多い | 高度クエリは設計差が出る | 既存連携前提で有力 |
| Supabase | MVP/小規模SaaS | 立ち上げが速い（DB+Auth+Storage） | 大規模化時に設計見直し | 早く検証したいとき強い |

## 3.4 キャッシュ/キュー（Redis）
| 使い道 | 代表機能 | 注意点 |
|---|---|---|
| キャッシュ | API高速化、セッション保持、レート制御 | TTL未設計で古いデータを返す |
| キュー | メール送信、Webhook再送、非同期処理 | 冪等性・再試行回数を定義しないと事故る |

## 3.5 ファイル保存（S3 / Cloudflare R2）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| S3 | 企業案件/標準構成 | 実績豊富、周辺サービスが多い | コスト管理は要設計 | 標準化したいなら第一候補 |
| R2 | 配信コストを抑えたい案件 | コスト最適化しやすい | AWS資産との統一性は落ちる | コスト重視時に有力 |

## 3.6 監視（Sentry / Datadog）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| Sentry | 小〜中規模Web/SaaS | 導入が速い、エラー追跡が強い | ノイズ削減設計が必要 | まず入れる監視として最適 |
| Datadog | 中〜大規模運用 | メトリクス・ログ・APM統合 | コストと設定が重め | インフラ監視まで一元化したい時 |

## 3.7 分析（GA4 / Mixpanel / PostHog）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| GA4 | Web集客系 | 標準分析に強い | プロダクトイベント分析は工夫必要 | Web流入分析なら第一候補 |
| Mixpanel | SaaSプロダクト改善 | ファネル/継続分析に強い | 計測設計の質が重要 | PMF改善フェーズで有力 |
| PostHog | プロダクト主導開発 | 解析と機能群をまとめやすい | 運用方針の整理が必要 | プロダクト分析中心なら有力 |

## 3.8 メール送信（SendGrid / Resend / SES）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| SendGrid | 汎用案件 | テンプレ運用しやすい | 到達率チューニングは別途必要 | 一般案件の第一候補 |
| Resend | 開発体験重視 | 実装しやすい | 大量配信要件は要確認 | MVP〜中規模で有力 |
| SES | AWS統一案件 | 低コスト運用しやすい | 初期セットアップがやや重い | AWS前提なら有力 |

## 3.9 CI/CD（GitHub Actions）
| サービス | 向いている案件 | 強み | 注意点 |
|---|---|---|---|
| GitHub Actions | GitHub管理のほぼ全案件 | 連携が簡単、テンプレ豊富 | ワークフロー肥大化に注意 |

## 3.10 ホスティング（Vercel / AWS / GCP / Render）
| サービス | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| Vercel | Next.js中心 | デプロイが速い | 複雑構成は設計分離が必要 | フロント中心なら第一候補 |
| AWS | 中〜大規模/企業 | 拡張性と選択肢が広い | 設計・運用難度が高い | 企業要件・監査要件で強い |
| GCP | データ/分析系 | データ基盤との親和性 | チーム経験差が出る | GCP既存資産があるなら有力 |
| Render | 小〜中規模 | 運用が軽い | 細かな最適化は制約あり | 少人数で早く公開するなら有力 |

---

## 4. 追加で覚えると案件で効く分野（よく使う）

| 分野 | 代表サービス | 使う場面 |
|---|---|---|
| API仕様管理 | OpenAPI / Swagger | 連携案件、引継ぎ、保守契約 |
| キュー/ジョブ実行 | BullMQ / Celery / Sidekiq | 非同期処理、再送、夜間バッチ |
| 検索 | Elasticsearch / Meilisearch / Algolia | 商品検索、全文検索、絞り込み |
| Feature Flag | LaunchDarkly / Unleash / PostHog Flags | 段階リリース、A/Bテスト |
| IaC | Terraform / Pulumi / AWS CDK | 環境再現性、監査、複数環境管理 |
| API Gateway | APIGW / Kong / Cloudflare | 認証統合、レート制限、監査ログ |
| CMS | microCMS / Contentful / Strapi | 更新を非エンジニアに移譲 |
| 通知基盤 | Slack API / LINE Messaging API | 運用通知、顧客通知、自動連携 |
| E2Eテスト | Playwright / Cypress | 回帰防止、納品前品質担保 |
| 監査/ログ保管 | CloudWatch / Loki / BigQuery | 障害解析、セキュリティ監査 |

---

## 5. フレームワーク選定早見表（FastAPI含む）

| 技術 | 向いている案件 | 強み | 注意点 | 推し判断 |
|---|---|---|---|---|
| FastAPI | AI連携/API中心 | 実装速度、型、安全なAPI設計 | 認証/権限設計は別途必要 | API中心案件の第一候補 |
| Django | 業務システム | 管理画面・ORMが強い | SPA連携時に設計追加 | 管理画面重視なら有力 |
| NestJS | TS統一のAPI基盤 | 構造化・保守性が高い | 初期学習コストあり | 中長期保守案件で有力 |
| Laravel | 国内業務/EC | 案件母数が多く速く作れる | TS統一が難しい場合あり | PHP案件なら第一候補 |
| Next.js | Web/SaaSフロント | SSR/SEO/運用速度が高い | App Router知識が必要 | フロント主軸なら第一候補 |
| Nuxt | Vue案件 | Vueの開発速度 | React市場より母数少なめ | Vue前提なら第一候補 |

---

## 6. 最小構成テンプレ（案件別）

## 6.1 小規模SaaS MVP（短納期）
- App: Next.js + FastAPI
- Auth: Clerk
- Billing: Stripe
- DB: PostgreSQL
- Storage: S3
- Monitoring: Sentry
- CI/CD: GitHub Actions
- Hosting: Vercel（フロント）+ Render/AWS（API）

## 6.2 業務システム（中規模）
- App: Django または Laravel
- DB: PostgreSQL/MySQL
- Cache/Queue: Redis
- Mail: SES/SendGrid
- Monitoring: Sentry + Datadog（必要に応じて）
- Hosting: AWS/GCP

## 6.3 AI業務自動化
- App: FastAPI + Next.js/Streamlit
- Model連携: OpenAI等（環境変数で切替）
- DB: PostgreSQL
- Queue: Redis/Celery
- Monitoring: Sentry
- Analytics: PostHog

---

## 7. 運用コストを下げる設計原則

1. 監視は最初から入れる（Sentryだけでも必須）  
2. Webhookは署名検証 + 冪等化 + 再送処理をセットにする  
3. `.env.example` と Secrets管理を統一する  
4. API仕様（OpenAPI）を先に固定して後工程の手戻りを減らす  
5. CIで `lint/test/build` を必須化し、手動デプロイを減らす  
6. 最初から完璧を目指さず、MVP構成で公開して計測で改善する

---

## 8. 受注前ヒアリングで必ず確認する質問

1. ユーザー数とピークアクセスはどれくらいか  
2. 有料化予定の時期と課金モデル（月額/従量/買い切り）は何か  
3. 個人情報・監査要件（保存期間、IP制限、SSO要否）はあるか  
4. 障害時の対応時間（SLA）と連絡フローはどうするか  
5. 将来の連携先（会計、CRM、チャット、BI）は何か

この5点が曖昧なままだと、技術選定がぶれて運用コストが跳ねやすくなります。
