# デモ準備ガイド（0円運用・APIキー安全管理）

## 1. 何を公開して何を公開しないか

### 公開してよい
- ソースコード（秘密情報なし）
- スクリーンショット
- 2〜3分のデモ動画
- 起動手順
- `.env.example`

### 公開してはいけない
- `.env` 実ファイル
- APIキー
- 実運用データ
- クラウド管理画面の資格情報

---

## 2. APIを用意しないといけない要素

### Portfolio 01: RAG Local Demo
- API不要で実演可: `use_openai=false`
- APIが必要な場合: OpenAI（`OPENAI_API_KEY`）

### Portfolio 02: 画像検査
- API不要（完全ローカル）

### Portfolio 03: 業務自動化
- API不要で実演可（ルールベース要約）
- APIが必要な場合: OpenAI（`OPENAI_API_KEY`）

---

## 3. ローカルで本物を書く必要があるファイル

各プロジェクトで必要なら、ローカルに `.env` を作成します。
このファイルは `.gitignore` によりコミットされません。

例（Portfolio 01 / 03 共通）:

```bash
cp .env.example .env
# .env を開いて APIキーを追記
```

`.env` の中身（例）:

```env
OPENAI_API_KEY=sk-xxxxx
OPENAI_MODEL=gpt-4o-mini
```

---

## 4. デモ実演当日の手順（アプリ以外の準備込み）

1. 事前に `pip install -r requirements.txt`
2. デモで使うサンプルデータ（CSV/画像）を準備
3. 30分前にローカル起動
4. 画面共有で操作（動画を保険として準備）
5. 終了後はアプリ停止

---

## 5. 課金事故を防ぐチェックリスト
- [ ] `git status` に `.env` が出ていない
- [ ] APIキーは環境変数のみ
- [ ] OpenAI管理画面で利用上限を設定
- [ ] 公開READMEに「キー不要モードあり」と明記

---

## 6. 最小デモコマンド

### Portfolio 01
```bash
cd portfolios/01_rag_local_demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8001
```

### Portfolio 02
```bash
cd portfolios/02_image_inspection_demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/app.py --server.port 8502
```

### Portfolio 03
```bash
cd portfolios/03_business_automation_demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/app.py --server.port 8503
```

---

## 7. デモ版から有料版へ移行する詳細手順

### 7.1 先に決めるべき仕様
- プラン: `demo` / `pro` / `enterprise`
- 制限対象: 利用回数、保存件数、エクスポート可否、外部連携可否
- 切り替え契機: 決済成功、支払失敗、解約、管理者手動変更

### 7.2 必須データ設計（最低限）
- `organizations`: 契約主体（会社・チーム）
- `subscriptions`: プラン、ステータス、期限
- `usage_metrics`: API回数、生成回数、容量
- `billing_events`: Webhook受信履歴（冪等処理用）

### 7.3 Demo版実装
1. ログイン直後は `demo` で開始する。
2. コア価値が伝わる範囲だけ使えるようにする。
3. 制限に達した時点でアップグレード画面へ遷移させる。
4. 実運用データは使わず、サンプルデータを同梱する。

### 7.4 有料版実装
1. 決済プロバイダ（例: Stripe）でプランを作成する。
2. Checkout/Customer Portal を実装する。
3. Webhook署名を検証し、契約状態をDBへ反映する。
4. `pro` になったら機能ゲートを解除する。
5. 支払い失敗時は即停止ではなく猶予期間を設ける。

### 7.5 運用と障害対応
- 二重課金防止: `event_id` で冪等化
- 障害検知: Webhook失敗を監視し、再送キューを実装
- 問い合わせ導線: 請求履歴、領収書、解約方法を画面表示
- 返金対応: 管理画面操作手順を社内Runbookに固定
