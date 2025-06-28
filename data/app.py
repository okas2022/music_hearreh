
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="청능재활 데모", layout="centered")

st.title("🎧 청능 뇌훈련: 좌우뇌 자극 프로그램")
st.markdown("매일 언어와 음악을 활용해 좌우뇌를 자극해보세요!")

# 세션 상태 초기화
if "language_score" not in st.session_state:
    st.session_state.language_score = 0
if "music_score" not in st.session_state:
    st.session_state.music_score = 0

# --- 언어 훈련 콘텐츠 ---
one_syllable_words = ["눈", "물", "불", "밥", "차", "꽃", "집", "산"]
training_words = ["학교", "사랑", "소리", "건강", "친구", "기쁨"]
training_sentences = [
    "오늘은 날씨가 맑고 기분이 좋아요.",
    "친구와 함께 영화를 봤어요.",
    "보청기를 착용하면 소리가 더 잘 들려요.",
    "매일 꾸준히 연습하면 청력이 좋아져요."
]

# --- 언어 훈련 (좌뇌) ---
st.header("📝 언어 훈련 (좌뇌)")
task_type = st.radio("훈련 유형을 선택하세요:", ["1음절 단어", "일반 단어", "문장"])

if task_type == "1음절 단어":
    sample = random.choice(one_syllable_words)
    st.markdown("**아래 단어를 소리 내어 발음해보세요:**")
    st.image("brain_left_basic.png", caption="좌뇌 기본 언어영역 자극")
    st.info(sample)
elif task_type == "일반 단어":
    sample = random.choice(training_words)
    st.markdown("**아래 단어를 소리 내어 발음해보세요:**")
    st.image("brain_left_word.png", caption="브로카 영역 자극")
    st.info(sample)
else:
    sample = random.choice(training_sentences)
    st.markdown("**아래 문장을 소리 내어 읽어보세요:**")
    st.image("brain_left_sentence.png", caption="좌반구 언어 통합영역 자극")
    st.info(sample)

if st.button("음성 평가 시뮬레이션"):
    with st.spinner("음성을 분석하는 중입니다..."):
        time.sleep(2)
    score = np.random.randint(60, 100)
    st.session_state.language_score = score
    st.success(f"언어 인식 정확도 점수: {score}/100")

# --- 음악 훈련 (우뇌) ---
st.header("🎵 음악 훈련 (우뇌)")
st.markdown("**화면에 나오는 리듬을 따라 손뼉 치듯이 Space 키를 눌러보세요.**")
st.text("(이곳에서는 시뮬레이션으로 진행됩니다)")
st.image("brain_right_music.png", caption="우측 청각피질 자극")

if st.button("리듬 감각 분석 시뮬레이션"):
    with st.spinner("리듬 분석 중입니다..."):
        time.sleep(2)
    score = np.random.randint(60, 100)
    st.session_state.music_score = score
    st.success(f"리듬 감각 점수: {score}/100")

# --- 좌우뇌 자극 점수 시각화 ---
st.header("📊 좌우뇌 자극 점수")
labels = ['언어 (좌뇌)', '음악 (우뇌)']
scores = [st.session_state.language_score, st.session_state.music_score]
colors = ['skyblue', 'salmon']

fig, ax = plt.subplots()
ax.bar(labels, scores, color=colors)
ax.set_ylim([0, 100])
ax.set_ylabel("점수")
ax.set_title("오늘의 뇌 자극 현황")
st.pyplot(fig)

# --- 피드백 메시지 ---
if st.session_state.language_score and st.session_state.music_score:
    avg = (st.session_state.language_score + st.session_state.music_score) / 2
    st.success(f"오늘의 훈련 평균 점수는 {avg:.1f}점입니다. 잘하셨어요!")
