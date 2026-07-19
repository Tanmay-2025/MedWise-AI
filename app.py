import streamlit as st
import os
# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="MedWise AI",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load Custom CSS
# -------------------------------
css_path = os.path.join("styles", "style.css")

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------
# Sidebar Logo
# -------------------------------
logo_path = os.path.join("assets", "logo.png")

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=160)

# -------------------------------
# Sidebar Title
# -------------------------------
st.sidebar.title("💊 MedWise AI")

st.sidebar.markdown(
    """
### AI-Based Antibiotic Misuse Awareness & Risk Checker

Educating users about responsible antibiotic use and
Antimicrobial Resistance (AMR).
"""
)

st.sidebar.divider()

st.sidebar.info("""
📌 Educational AI Platform

Built using

• Streamlit
• Python
• Google Gemini AI
• Plotly
""")

st.sidebar.divider()

st.sidebar.success(
    "✅ Educational Tool\n\nNot a substitute for professional medical advice."
)

# -------------------------------
# Main Welcome Screen
# -------------------------------
st.title("💊 Welcome to MedWise AI")

st.markdown(
    """
### AI-Based Antibiotic Misuse Awareness & Risk Checker

Use the **navigation menu on the left** to explore the application.

### Available Modules

- 🏠 Home
- 🩺 Risk Checker
- 🤖 AI Assistant
- 📚 Learn About AMR
- 💡 Myth vs Fact
- 📝 Awareness Quiz
- ℹ️ About
- 🌐 Resources

---

### ⚠ Disclaimer

This application is developed for educational purposes only.

It does **NOT** diagnose diseases,
recommend medicines,
or replace professional healthcare advice.

Always consult a qualified healthcare professional for medical concerns.
"""
)

st.divider()

st.caption(
    "© 2026 MedWise AI | Built for Bio-Hackathon | References: WHO • CDC • ICMR"
)