# 06 Django 予約管理システム 模擬案件

## 案件想定
- クライアント: クリニック/サロン
- 依頼内容: スタッフ別予約管理、日別一覧、CSV出力

## 構成（学習用）
```txt
config/settings.py          # Django設定（DB/アプリ登録）
reservations/models.py      # 予約モデル
reservations/views.py       # 一覧/登録ビュー
reservations/admin.py       # 管理画面設定
.env.example                # SECRET_KEYやDB設定
```

## 最初に理解すべき点
- Djangoは管理画面が強く、業務システムPoCに向く
- 標準認証とORMで短期開発しやすい
