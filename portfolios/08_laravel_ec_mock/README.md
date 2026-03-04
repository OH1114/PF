# 08 Laravel ECバックオフィス 模擬案件

## 案件想定
- クライアント: D2C小売
- 依頼内容: 受注管理、在庫引当、発送ステータス更新

## 構成（学習用）
```txt
routes/web.php                         # 画面ルート
app/Http/Controllers/OrderController.php
database/migrations/2026_03_04_create_orders_table.php
.env.example
```

## 学習ポイント
- MVC分離とルーティング
- migrationでDB変更を履歴管理
- `.env`でAPP_KEY/DB情報を管理
