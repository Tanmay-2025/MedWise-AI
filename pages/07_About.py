import streamlit as st
from utils.helpers import page_footer

st.title("ℹ️ About MedWise AI")
st.subheader("AI-Based Antibiotic Misuse Awareness & Risk Checker")

st.info("""
MedWise AI is an educational web application developed to promote
**responsible antibiotic use** and increase awareness about
**Antimicrobial Resistance (AMR).**

The platform combines artificial intelligence, interactive learning,
and transparent risk assessment to educate the public.
""")
st.divider()

st.header("🌍 The Problem")

st.markdown("""
Antimicrobial Resistance (AMR) is recognized by the World Health Organization as one of the world's most significant public health challenges.

Common causes include:

• Self-medication

• Using antibiotics for viral illnesses

• Stopping treatment early

• Sharing antibiotics

• Reusing leftover medicines

These practices accelerate the development of resistant bacteria, making infections increasingly difficult to treat.
""")
st.divider()

# ==========================================
# Mission
# ==========================================

st.header("🎯 Our Mission")

st.markdown("""
MedWise AI aims to promote **Antibiotic Stewardship** by:

✅ Increasing public awareness of AMR

✅ Encouraging evidence-based antibiotic use

✅ Reducing common misconceptions

✅ Supporting informed healthcare decisions

✅ Making trusted health education accessible through AI
""")

st.divider()

# ==========================================
# Features
# ==========================================

st.header("✨ Key Features")

left, right = st.columns(2)

with left:

    st.success("""
### 🩺 Risk Assessment

✔ Multiple-choice behavioural assessment

✔ Transparent scoring engine

✔ Personalized recommendations

✔ PDF assessment report

✔ Visual risk dashboard
""")

    st.success("""
### 📚 Learning Hub

✔ Learn about AMR

✔ Myth vs Fact

✔ Educational Resources
""")

with right:

    st.info("""
### 🤖 AI Knowledge Assistant

✔ Google Gemini powered

✔ Uses a curated WHO–CDC–ICMR knowledge base

✔ Generates easy-to-understand explanations

✔ Prevents diagnosis and prescription requests
""")

    st.info("""
### 📝 Awareness Quiz

✔ Interactive questions

✔ Instant scoring

✔ Detailed explanations
""")

st.divider()

st.header("⭐ What Makes MedWise AI Different?")

points = [
    "AI responses are grounded in trusted public health guidance.",
    "Transparent risk scoring instead of black-box predictions.",
    "Interactive education through quizzes and myth-busting.",
    "Evidence-based recommendations from WHO, CDC, and ICMR.",
    "Designed specifically for public awareness rather than diagnosis."
]

for point in points:
    st.success(point)

st.divider()
# ==========================================
# Technology
# ==========================================

st.header("🛠 Technology Stack")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Frontend", "Streamlit")
col2.metric("Backend", "Python")
col3.metric("AI", "Gemini")
col4.metric("Visualization", "Plotly")

st.markdown("""
### Core Technologies

- Streamlit
- Python
- Google Gemini API
- Plotly
- ReportLab
- Pillow
- python-dotenv
""")

st.divider()

# ==========================================
# References
# ==========================================

st.header("📚 Trusted References")

st.markdown("""
- 🌍 World Health Organization (WHO)

- 🇺🇸 Centers for Disease Control and Prevention (CDC)

- 🇮🇳 Indian Council of Medical Research (ICMR)

- 💊 National Centre for Disease Control (NCDC)
""")

st.divider()

st.header("📚 Evidence-Based Knowledge")

st.markdown("""
MedWise AI's educational content is compiled from trusted public health organizations:

🌍 World Health Organization (WHO)

🇺🇸 Centers for Disease Control and Prevention (CDC)

🇮🇳 Indian Council of Medical Research (ICMR)

The AI assistant uses this curated knowledge base to generate educational responses while avoiding medical diagnosis or treatment recommendations.
""")
st.divider()

# ==========================================
# Future Scope
# ==========================================

st.header("🚀 Future Enhancements")

st.markdown("""
• 🌐 Multilingual educational support

• 📱 Mobile application

• 📈 Personalized learning progress

• 🏥 Integration with hospital awareness programs

• 👨‍⚕️ Healthcare professional dashboard

• 📊 Population-level awareness analytics

• 🌍 Community AMR awareness campaigns
""")

st.divider()

st.success("""
### 🌱 Together Against Antimicrobial Resistance

Every responsible decision—from completing prescribed antibiotics to avoiding self-medication—helps preserve these life-saving medicines for future generations.

Small actions today can make a significant impact on global health.
""")
st.divider()

# ==========================================
# Disclaimer
# ==========================================

st.warning("""
### ⚠ Educational Disclaimer

MedWise AI is developed **for educational and awareness purposes only.**

This application:

• Does **not diagnose diseases**

• Does **not prescribe medications**

• Does **not replace professional medical advice**

Always consult a qualified healthcare professional for diagnosis and treatment.
""")

page_footer()