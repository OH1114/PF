from __future__ import annotations

import os

import pandas as pd
import streamlit as st

from core import build_report_prompt, build_rule_based_summary

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


st.set_page_config(page_title="Business Automation Demo", layout="wide")
st.title("Portfolio 03: 業務自動化デモ（CSV集計 + 要約）")

st.write("CSVをアップロードして集計し、必要ならOpenAIで要約します（未設定時はルールベース要約）。")
st.markdown(
    """
### この開発物の目的
- **現場課題**: 手作業レポート作成に時間がかかる
- **ユーザ価値**: CSV投入だけで集計と報告文のたたき台を自動生成
- **工夫**: API未設定でも確実に動くフォールバックで無料デモ可能
"""
)

uploaded = st.file_uploader("CSVを選択", type=["csv"])
use_openai = st.checkbox("OpenAI要約を使う（APIキー必要）", value=False)

if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader("元データ")
    st.dataframe(df.head(30), use_container_width=True)

    st.subheader("自動集計")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        st.warning("数値列が無いため件数のみ集計します。")
        summary = {"rows": len(df), "columns": len(df.columns)}
    else:
        summary = {
            "rows": len(df),
            "columns": len(df.columns),
            "sum": df[numeric_cols].sum().to_dict(),
            "mean": df[numeric_cols].mean().round(2).to_dict(),
        }
    st.json(summary)

    prompt = build_report_prompt(summary)

    if use_openai and os.getenv("OPENAI_API_KEY") and OpenAI is not None:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        resp = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        result = resp.choices[0].message.content or "(空応答)"
        mode = "openai"
    else:
        result = build_rule_based_summary(summary)
        mode = "rule_based"

    st.subheader("要約結果")
    st.write(result)
    st.caption(f"mode: {mode}")

    out_df = pd.DataFrame([{"summary_mode": mode, "summary_text": result}])
    st.download_button(
        label="要約CSVをダウンロード",
        data=out_df.to_csv(index=False),
        file_name="summary_output.csv",
        mime="text/csv",
    )
else:
    st.info("CSVをアップロードしてください。")
