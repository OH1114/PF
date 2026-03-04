from __future__ import annotations

import io

import numpy as np
import streamlit as st
from PIL import Image, ImageFilter, ImageOps

from core import judge_defect, simple_defect_score_from_values


def detect_edges(image: Image.Image) -> Image.Image:
    gray = ImageOps.grayscale(image)
    return gray.filter(ImageFilter.FIND_EDGES)


def simple_defect_score(edge_image: Image.Image):
    arr = np.array(edge_image)
    score, bright, _ = simple_defect_score_from_values(arr.tolist(), threshold=50)
    return score, bright


st.set_page_config(page_title="Image Inspection Demo", layout="wide")
st.title("Portfolio 02: 画像検査デモ（ローカル無料実演向け）")
st.write("アップロード画像に対して簡易エッジ検出と異常スコア算出を行います。")
st.markdown(
    """
### この開発物の目的
- **現場課題**: 目視検査が属人化し、判定ばらつきが出る
- **ユーザ価値**: 画像を入れるだけで一次判定の目安を即時提示
- **工夫**: しきい値をスライダーで調整し、業務条件に合わせた説明が可能
"""
)

uploaded = st.file_uploader("画像を選択", type=["png", "jpg", "jpeg"])
threshold = st.slider("異常判定しきい値(%)", 0.0, 20.0, 4.0, 0.1)

if uploaded:
    raw = uploaded.read()
    image = Image.open(io.BytesIO(raw)).convert("RGB")
    edge = detect_edges(image)
    score, bright = simple_defect_score(edge)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("入力画像")
        st.image(image, use_container_width=True)
    with c2:
        st.subheader("エッジ検出結果")
        st.image(edge, use_container_width=True)

    st.metric("異常スコア(%)", f"{score:.2f}")
    st.caption(f"エッジ強画素数: {bright}")

    result = judge_defect(score, threshold)
    if result == "要確認":
        st.error("判定: 要確認（しきい値超過）")
    else:
        st.success("判定: 許容範囲")

    st.markdown(
        "**ユーザ向け説明**: スコアが高いほど輪郭変化が多く、欠陥疑い箇所が多い可能性があります。"
    )
else:
    st.info("画像をアップロードすると解析が開始されます。")
