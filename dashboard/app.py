import streamlit as st

st.set_page_config(
    page_title="Smart Study Generator",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------

st.title("📚 Smart Study Generator")
st.subheader("AI-Powered Personalized Study Dashboard")

st.write(
    "Transform your study progress into personalized revision priorities, "
    "study plans, and recommendations."
)

# -----------------------------
# STUDENT INPUT
# -----------------------------

st.sidebar.header("👤 Student Information")

student_name = st.sidebar.text_input(
    "Student Name",
    "Student"
)

subject = st.sidebar.selectbox(
    "Select Subject",
    [
        "Data Structures",
        "Operating Systems",
        "Computer Networks",
        "DBMS",
        "Algorithms"
    ]
)

study_hours = st.sidebar.slider(
    "Today's Study Hours",
    0,
    12,
    3
)

topics_completed = st.sidebar.slider(
    "Topics Completed",
    0,
    25,
    18
)

quiz_score = st.sidebar.slider(
    "Latest Quiz Score (%)",
    0,
    100,
    82
)

confidence = st.sidebar.select_slider(
    "Overall Confidence",
    options=["Low", "Medium", "High"],
    value="Medium"
)

# -----------------------------
# CALCULATIONS
# -----------------------------

overall_progress = int((topics_completed / 25) * 100)

if quiz_score < 60:
    performance = "Needs Improvement"
elif quiz_score < 80:
    performance = "Good"
else:
    performance = "Excellent"

# -----------------------------
# STUDENT WELCOME
# -----------------------------

st.header(f"👋 Welcome, {student_name}!")

st.write(
    f"Your selected subject is **{subject}**. "
    f"Based on your current inputs, here is your personalized study overview."
)

# -----------------------------
# METRICS
# -----------------------------

st.header("📊 Study Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Overall Progress",
        f"{overall_progress}%"
    )

with col2:
    st.metric(
        "Topics Completed",
        f"{topics_completed}/25"
    )

with col3:
    st.metric(
        "Quiz Score",
        f"{quiz_score}%"
    )

with col4:
    st.metric(
        "Study Hours",
        f"{study_hours} hrs"
    )

st.progress(overall_progress / 100)

# -----------------------------
# PERFORMANCE
# -----------------------------

st.header("🎯 Performance Analysis")

if performance == "Excellent":
    st.success(
        "Excellent performance! Continue revision and practice regularly."
    )
elif performance == "Good":
    st.info(
        "Good performance. Focus on weaker topics to improve further."
    )
else:
    st.warning(
        "Your quiz score indicates that additional revision is recommended."
    )

st.write(f"**Performance Level:** {performance}")
st.write(f"**Confidence Level:** {confidence}")

# -----------------------------
# TOPIC PERFORMANCE
# -----------------------------

st.header("📚 Topic Performance")

topic_data = {
    "Data Structures": 90,
    "Operating Systems": 85,
    "Computer Networks": 72,
    "DBMS": 65,
    "Algorithms": 55
}

for topic, score in topic_data.items():

    st.write(f"**{topic} — {score}%**")

    st.progress(score / 100)

# -----------------------------
# WEAK AREAS
# -----------------------------

st.header("⚠️ Weak Areas")

weak_topics = [
    topic for topic, score in topic_data.items()
    if score < 70
]

if weak_topics:

    for topic in weak_topics:
        st.warning(
            f"🔴 {topic} — requires additional revision"
        )

else:

    st.success(
        "No major weak areas detected."
    )

# -----------------------------
# REVISION PRIORITY
# -----------------------------

st.header("🔥 Revision Priority")

priority_topics = sorted(
    topic_data.items(),
    key=lambda x: x[1]
)

for index, (topic, score) in enumerate(priority_topics):

    if score < 60:
        priority = "HIGH"
    elif score < 75:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    st.write(
        f"{index + 1}. **{topic}** — "
        f"{priority} priority ({score}%)"
    )

# -----------------------------
# PERSONALIZED STUDY PLAN
# -----------------------------

st.header("📅 Personalized 3-Day Study Plan")

day1, day2, day3 = st.tabs(
    ["Day 1", "Day 2", "Day 3"]
)

with day1:

    st.subheader("🔴 High Priority Topics")

    st.write("- Algorithms")
    st.write("- DBMS")

    st.write(
        "**Activity:** Understand concepts and practice important questions."
    )

with day2:

    st.subheader("🟡 Medium Priority Topics")

    st.write("- Computer Networks")
    st.write("- Operating Systems")

    st.write(
        "**Activity:** Revise concepts and practice flashcards."
    )

with day3:

    st.subheader("🟢 Final Revision")

    st.write("- Data Structures")
    st.write("- Complete syllabus quick revision")

    st.write(
        "**Activity:** Attempt a practice quiz and review mistakes."
    )

# -----------------------------
# QUIZ PERFORMANCE
# -----------------------------

st.header("📝 Quiz Performance")

quiz_data = {
    "Quiz 1": 65,
    "Quiz 2": 72,
    "Quiz 3": 78,
    "Quiz 4": quiz_score
}

st.bar_chart(quiz_data)

# -----------------------------
# AI RECOMMENDATIONS
# -----------------------------

st.header("🤖 AI Study Recommendations")

recommendations = [
    "Focus first on topics with scores below 70%.",
    "Practice exam questions after completing each topic.",
    "Use flashcards for quick revision before the exam.",
    "Maintain consistent daily study hours.",
    "Take another quiz after completing the revision plan."
]

for recommendation in recommendations:

    st.info(
        f"💡 {recommendation}"
    )

# -----------------------------
# STUDY STREAK
# -----------------------------

st.header("🔥 Study Streak")

if study_hours >= 3:

    st.success(
        "🔥 Great! You completed at least 3 study hours today."
    )

else:

    st.warning(
        "Try to study for at least 3 hours today."
    )

# -----------------------------
# FOOTER
# -----------------------------

st.divider()

st.caption(
    "Smart Study Generator Agent | Built with Langflow + Google Gemini + Streamlit"
)