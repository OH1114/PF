# 07 NestJS LINE通知Bot 模擬案件

## 案件想定
- クライアント: 教育系サービス運営
- 依頼内容: 申込発生時にLINE通知、管理者向けログ保存API

## 構成（学習用）
```txt
src/main.ts               # エントリポイント
src/app.module.ts         # モジュール定義
src/webhook.controller.ts # LINE Webhook受信
src/notify.service.ts     # 通知処理
prisma/schema.prisma      # DBスキーマ
.env.example
```
