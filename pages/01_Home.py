import streamlit as st
from utils.helpers import page_footer

st.title("💊 MedWise AI")
st.image("assets/hero.png", use_container_width=True)
st.subheader("AI-Based Antibiotic Misuse Awareness & Risk Checker")

st.warning(
    """
⚠ **Educational Tool**

This application helps users understand safe antibiotic practices.
It **does not diagnose diseases** or prescribe medicines.
"""
)

st.divider()

# Hero Section
left, right = st.columns([2, 1])

with left:
    st.markdown("""
## Protect Antibiotics. Protect Lives.

Antibiotic misuse is one of the leading causes of **Antimicrobial Resistance (AMR)**.

MedWise AI helps you:

- 🩺 Assess your antibiotic use
- 🤖 Learn through an AI assistant
- 📚 Understand AMR
- 💡 Correct common misconceptions
- 📝 Test your knowledge
""")

with right:
    st.info("""
### 📊 Quick Facts

🌍 AMR is a global health challenge.

💊 Antibiotics do not treat viral infections.

✅ Responsible antibiotic use helps save lives.
""")

st.divider()

st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 🩺 Antibiotic Risk Checker

✔ Detect unsafe habits

✔ Transparent scoring

✔ Personalized recommendations
""")

    st.success("""
### 📚 Learn About AMR

✔ Simple explanations

✔ Prevention tips

✔ WHO-based awareness
""")

with col2:

    st.info("""
### 🤖 AI Assistant

✔ Educational answers

✔ Safe antibiotic guidance

✔ Easy language
""")

    st.info("""
### 📝 Awareness Quiz

✔ Interactive learning

✔ Improve your knowledge

✔ Instant score
""")

st.divider()

st.header("📈 Dashboard")

a, b, c, d = st.columns(4)

a.metric("Questions", "5")
b.metric("Learning Pages", "4")
c.metric("Quiz", "5 MCQs")
d.metric("AI Assistant", "Ready")

st.divider()

st.header("🚀 Start Here")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🩺 Risk Assessment"):
        st.switch_page("pages/02_Risk_Checker.py")

with col2:
    if st.button("🤖 AI Assistant"):
        st.switch_page("pages/03_AI_Assistant.py")

with col3:
    if st.button("📚 Learn AMR"):
        st.switch_page("pages/04_Learn_AMR.py")

page_footer()