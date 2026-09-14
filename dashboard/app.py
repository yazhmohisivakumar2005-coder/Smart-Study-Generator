import streamlit as st

st.set_page_config(
    page_title="Smart Study Generator",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Smart Study Generator")
st.subheader("AI-Powered Personalized Study Dashboard")

st.write(
    "Track your study progress, identify weak areas, "
    "and prepare efficiently for exams."
)

# Student Progress
st.header("📊 Study Progress")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Overall Progress", "72%")

with col2:
    st.metric("Topics Completed", "18 / 25")

with col3:
    st.metric("Quiz Score", "82%")

with col4:
    st.metric("Study Streak", "5 Days 🔥")

# Progress bar
st.progress(0.72)

# Important Topics
st.header("⭐ Topic Performance")

topics = {
    "Operating Systems": 85,
    "Computer Networks": 72,
    "DBMS": 65,
    "Data Structures": 90,
    "Algorithms": 55
}

for topic, progress in topics.items():
    st.write(f"**{topic} — {progress}%**")
    st.progress(progress / 100)

# Weak Areas
st.header("⚠️ Weak Areas")

st.warning("Algorithms — needs more revision")
st.warning("DBMS — revise normalization and transactions")

# Study Plan
st.header("📅 Personalized Study Plan")

day1, day2, day3 = st.tabs(["Day 1", "Day 2", "Day 3"])

with day1:
    st.write("### 🔴 High Priority")
    st.write("- Algorithms")
    st.write("- DBMS")
    st.write("Revision: Practice important questions")

with day2:
    st.write("### 🟡 Medium Priority")
    st.write("- Computer Networks")
    st.write("- Operating Systems")
    st.write("Revision: Review key concepts and flashcards")

with day3:
    st.write("### 🟢 Revision Day")
    st.write("- Data Structures")
    st.write("- Full syllabus quick revision")
    st.write("Revision: Attempt practice quiz")

# Quiz Performance
st.header("📝 Quiz Performance")

st.write("Recent Quiz Score")

st.bar_chart({
    "Quiz 1": 65,
    "Quiz 2": 72,
    "Quiz 3": 78,
    "Quiz 4": 82
})

# Agent Recommendations
st.header("🤖 AI Agent Recommendations")

st.info(
    "1. Focus on Algorithms because it currently has the lowest progress."
)

st.info(
    "2. Revise DBMS concepts and practice exam questions."
)

st.info(
    "3. Continue daily revision to maintain your study streak."
)

st.success("🎯 Keep studying consistently — you are making good progress!")