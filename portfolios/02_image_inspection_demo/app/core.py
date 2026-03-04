from __future__ import annotations

from typing import Iterable, Sequence, Tuple


def simple_defect_score_from_values(values: Sequence[Sequence[int]], threshold: int = 50) -> Tuple[float, int, int]:
    """2次元画素値配列から異常スコアを算出する。

    Returns:
        score_percent, bright_count, total_count
    """
    flat = [int(v) for row in values for v in row]
    total = len(flat)
    if total == 0:
        return 0.0, 0, 0
    bright = sum(1 for v in flat if v > threshold)
    ratio = bright / total
    return ratio * 100.0, bright, total


def judge_defect(score_percent: float, threshold_percent: float) -> str:
    return "要確認" if score_percent >= threshold_percent else "許容範囲"
