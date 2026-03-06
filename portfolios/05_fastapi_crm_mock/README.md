# 05 FastAPI 顧客対応自動化API 模擬案件

## 案件想定
- クライアント: 営業代行会社
- 依頼内容: 顧客問い合わせをタグ分類し、優先度を返すAPI
- 納期感: 2〜3週間

## 学習ポイント
- Pydanticによる入力バリデーション
- APIレスポンスの設計
- `.env` でLLMキーやDB URLを分離

## 構成
```txt
app/
  main.py               # FastAPIエントリポイント
  schemas.py            # 入出力スキーマ
  service.py            # 業務ロジック
.env.example
requirements.txt
```
