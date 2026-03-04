from __future__ import annotations

from typing import Dict, Any


def build_rule_based_summary(summary: Dict[str, Any]) -> str:
    rows = int(summary.get("rows", 0))
    return (
        f"合計{rows}件を処理しました。"
        "主要数値の平均値を確認し、外れ値候補の点検を推奨します。"
        "（ルールベース要約モード）"
    )


def build_report_prompt(summary: Dict[str, Any]) -> str:
    return (
        "以下の集計結果を、業務報告向けに日本語で3行以内で要約してください。\n"
        f"{summary}"
    )
