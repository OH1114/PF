from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Chunk:
    source: str
    text: str


def load_chunks(data_dir: Path) -> List[Chunk]:
    chunks: List[Chunk] = []
    for p in sorted(data_dir.glob("*.txt")):
        text = p.read_text(encoding="utf-8").strip()
        if text:
            chunks.append(Chunk(source=p.name, text=text))
    return chunks


def score(question: str, text: str) -> int:
    q_words = set(question.lower().split())
    t_words = set(text.lower().split())
    return len(q_words & t_words)


def retrieve(question: str, chunks: List[Chunk], top_k: int = 2) -> List[Chunk]:
    ranked = sorted(chunks, key=lambda c: score(question, c.text), reverse=True)
    return [c for c in ranked[:top_k] if score(question, c.text) > 0] or ranked[:1]


def answer_with_local_template(question: str, hits: List[Chunk]) -> str:
    context = "\n\n".join(f"[{c.source}] {c.text[:180]}" for c in hits)
    return (
        "ローカルRAGモードの回答です。\n"
        f"質問: {question}\n"
        "以下の資料を根拠に要点をまとめます。\n"
        f"{context}"
    )
