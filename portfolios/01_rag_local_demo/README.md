# Portfolio 01: RAG Local Demo (0円運用対応)

## 概要
- FastAPIで作った最小RAGデモです。
- デフォルトは**モックローカル回答**で動作し、APIキー無しで実演できます。
- `OPENAI_API_KEY` を設定したときのみ、実API呼び出しを試せます。

## 起動
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

## 動作確認
```bash
curl -s -X POST http://127.0.0.1:8001/query \
  -H 'Content-Type: application/json' \
  -d '{"question":"APIキー管理のルールは？","use_openai":false}'

curl -s http://127.0.0.1:8001/demo-info
```

## API課金を防ぐ設計
- `.env` は作成しても **絶対にコミットしない**
- リポジトリには `.env.example` のみ置く
- 実演時は `use_openai=false` で無料運用可能
