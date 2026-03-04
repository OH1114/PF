from __future__ import annotations

import os
from pathlib import Path
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from .rag_core import Chunk, answer_with_local_template, load_chunks, retrieve

try:
    from openai import OpenAI
except ImportError:  # optional dependency at runtime
    OpenAI = None


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


class QueryRequest(BaseModel):
    question: str
    use_openai: bool = False


class QueryResponse(BaseModel):
    answer: str
    citations: List[str]
    mode: str


app = FastAPI(title="RAG Local Demo")

DEMO_STORY = {
    "purpose": "社内資料検索の一次回答を高速化し、問い合わせ対応の属人化を下げる",
    "user_problem": "資料が分散しており、回答までのリードタイムが長い",
    "design": [
        "API無しでも動くモックモードで常時無料デモ可能",
        "ヒットした根拠ファイル名を citations で返して説明責任を担保",
        "use_openai=true の時だけ外部APIを使う安全設計",
    ],
}


def answer_with_openai(question: str, hits: List[Chunk]) -> str:
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key or OpenAI is None:
        return "OPENAI_API_KEY が未設定のため、モック回答にフォールバックしました。"

    client = OpenAI(api_key=api_key)
    context = "\n\n".join(f"[{c.source}] {c.text}" for c in hits)
    prompt = (
        "あなたは業務文書アシスタントです。"
        "必ず日本語で、根拠に沿って短く回答してください。\n"
        f"# 質問\n{question}\n\n"
        f"# 参考資料\n{context}"
    )
    completion = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return completion.choices[0].message.content or "(空の回答)"


@app.get("/")
def root() -> dict:
    return {"message": "RAG local demo is running"}


@app.get("/demo-info")
def demo_info() -> dict:
    return DEMO_STORY


@app.post("/query", response_model=QueryResponse)
def query(req: QueryRequest) -> QueryResponse:
    hits = retrieve(req.question, load_chunks(DATA_DIR))
    citations = [h.source for h in hits]

    if req.use_openai:
        answer = answer_with_openai(req.question, hits)
        mode = "openai_or_fallback"
    else:
        answer = answer_with_local_template(req.question, hits)
        mode = "mock_local"

    return QueryResponse(answer=answer, citations=citations, mode=mode)
