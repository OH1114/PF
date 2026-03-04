# テスト実行エビデンス（2026-03-04）

## 実行コマンドと結果

### 1. 構文チェック
```bash
python -m py_compile \
  portfolios/01_rag_local_demo/app/main.py \
  portfolios/01_rag_local_demo/app/rag_core.py \
  portfolios/02_image_inspection_demo/app/app.py \
  portfolios/02_image_inspection_demo/app/core.py \
  portfolios/03_business_automation_demo/app/app.py \
  portfolios/03_business_automation_demo/app/core.py
```
結果: 成功（エラーなし）

### 2. ユニットテスト
```bash
python -m unittest discover -s tests -v
```
結果:

```text
test_prompt_contains_summary (test_business_core.TestBusinessCore) ... ok
test_rule_summary_contains_rows (test_business_core.TestBusinessCore) ... ok
test_empty_values (test_image_core.TestImageCore) ... ok
test_judge (test_image_core.TestImageCore) ... ok
test_score_from_values (test_image_core.TestImageCore) ... ok
test_answer_template_contains_citation (test_rag_core.TestRagCore) ... ok
test_load_chunks_from_data (test_rag_core.TestRagCore) ... ok
test_retrieve_returns_relevant_or_fallback (test_rag_core.TestRagCore) ... ok
test_score_overlap (test_rag_core.TestRagCore) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.002s

OK
```

## テスト観点
- RAG: スコアリング・検索・テンプレ回答・データ読み込み
- 画像検査: スコア計算・空入力・判定分岐
- 業務自動化: 要約生成・プロンプト生成

---

## 追試（初心者向け一枚解説資料追加後）

```bash
python -m unittest discover -s tests -v
```

結果: 9 tests, `OK`（既存機能の回帰なし）
