# Portfolio 02: 画像検査デモ

## 概要
- Streamlitで作成した、ローカル実演向けの画像処理PoCです。
- API不要、外部課金なしで動作します。

## 起動
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/app.py --server.port 8502
```

## 実演の見せ方
- 入力画像を変え、しきい値調整で判定が変わる様子を見せる
- READMEに「業務適用時は特徴量やモデル置換で精度向上可能」と明記
