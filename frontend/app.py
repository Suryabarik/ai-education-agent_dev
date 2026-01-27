import streamlit as st
import requests
import json

# -------- CONFIG --------
API_URL = "http://127.0.0.1:8000/generate-content"  # FastAPI endpoint

# -------- PAGE SETUP --------
st.set_page_config(
    page_title="AI Education Agent",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Education Content Generator")
st.markdown("Generate explanations, MCQs, and get reviewer feedback instantly!")

# -------- USER INPUT --------
with st.form("input_form"):
    grade = st.number_input("Grade (1-12)", min_value=1, max_value=12, value=4)
    topic = st.text_input("Topic", placeholder="Enter topic, e.g., Types of angles")
    submit_btn = st.form_submit_button("Generate Content")

if submit_btn:
    if not topic.strip():
        st.warning("Please enter a topic!")
    else:
        st.info("Generating content… Please wait.")
        payload = {"grade": grade, "topic": topic}

        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                data = response.json()

                # Generator Output
                st.subheader("✅ Generated Explanation & MCQs")
                gen = data.get("generator_output", {})
                st.markdown(f"**Explanation:** {gen.get('explanation', '')}")

                mcqs = gen.get("mcqs", [])
                for i, mcq in enumerate(mcqs, 1):
                    st.markdown(f"**Q{i}: {mcq.get('question', '')}**")
                    options = mcq.get("options", [])
                    for j, opt in zip(["A", "B", "C", "D"], options):
                        st.markdown(f"{j}. {opt}")
                    st.markdown(f"**Answer:** {mcq.get('answer', '')}")
                    st.markdown("---")

                # Reviewer Feedback
                st.subheader("📝 Reviewer Feedback")
                reviewer = data.get("reviewer_output", {})
                st.markdown(f"**Status:** {reviewer.get('status', '')}")
                feedback = reviewer.get("feedback", [])
                for point in feedback:
                    st.markdown(f"- {point}")

                # Refined Output
                st.subheader("🔄 Refined Explanation & MCQs")
                refined = data.get("refined_output", {})
                st.markdown(f"**Explanation:** {refined.get('explanation', '')}")
                mcqs_refined = refined.get("mcqs", [])
                for i, mcq in enumerate(mcqs_refined, 1):
                    st.markdown(f"**Q{i}: {mcq.get('question', '')}**")
                    options = mcq.get("options", [])
                    for j, opt in zip(["A", "B", "C", "D"], options):
                        st.markdown(f"{j}. {opt}")
                    st.markdown(f"**Answer:** {mcq.get('answer', '')}")
                    st.markdown("---")

            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
