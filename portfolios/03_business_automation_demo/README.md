# Portfolio 03: 業務自動化デモ

## 概要
- CSVの自動集計と要約生成を行うStreamlitアプリです。
- API未設定でもルールベース要約で実演可能です。

## 起動
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/app.py --server.port 8503
```

## APIキーを使う場合
- `.env` をローカル作成し `OPENAI_API_KEY` を設定
- `.env` はコミット禁止
- デモ時だけ有効化し、通常は `use_openai` をOFFにして無料運用
