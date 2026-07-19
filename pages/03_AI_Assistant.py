import streamlit as st
from utils.ai_service import ask_ai
from utils.helpers import page_footer
allowed_keywords = [
    "antibiotic",
    "antibiotics",
    "amr",
    "antimicrobial",
    "resistance",
    "infection",
    "bacteria",
    "virus",
    "viral",
    "doctor",
    "prescription",
    "dose",
    "medicine",
    "who",
    "cdc",
    "icmr"
]

st.title("🤖 MedWise AI Assistant")
st.subheader("AI-Powered Antibiotic Awareness")

st.info("""
Ask educational questions about antibiotics, antimicrobial resistance (AMR),
and responsible antibiotic use.

⚠ This assistant provides educational information only.
""")
st.success("""
### 🧠 How MedWise AI Answers Your Questions

✅ Searches a local knowledge base built from WHO, CDC and ICMR guidance

✅ Uses AI to explain the information in simple language

✅ Provides educational responses only (no diagnosis or prescriptions)
""")
st.divider()

# ==========================================
# Suggested Questions
# ==========================================

st.subheader("💡 Frequently Asked Questions")

questions = [

    "What is antimicrobial resistance (AMR)?",

    "Why should antibiotics not be used for viral infections?",

    "What causes antibiotic resistance?",

    "What should I do if I miss an antibiotic dose?",

    "Can I stop antibiotics once I feel better?",

    "How should leftover antibiotics be disposed of?",

    "Can I use antibiotics without a prescription?",

    "How can I help prevent antimicrobial resistance?"
]

cols = st.columns(2)

if "selected_question" not in st.session_state:
    st.session_state.selected_question = ""

for i, q in enumerate(questions):

    with cols[i % 2]:

        if st.button(q, use_container_width=True):
            st.session_state.selected_question = q

st.divider()

# ==========================================
# User Question
# ==========================================

st.subheader("✍️ Ask Your Question")

user_question = st.text_area(
    "",
    value=st.session_state.selected_question,
    height=140,
    placeholder="Example: Why shouldn't antibiotics be taken for viral infections?"
)

search = st.button(
    "🔍 Generate Answer",
    use_container_width=True
)

# ==========================================
# AI Response
# ==========================================

if search:

    if user_question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching WHO • CDC • ICMR knowledge base..."):

            try:
                

                if not any(word in user_question.lower() for word in allowed_keywords):
                    st.warning(
        "Please ask a question related to antibiotics, antimicrobial resistance, infections, or responsible antibiotic use."
    )
                    st.stop()
                answer = ask_ai(user_question)

                st.divider()

                st.subheader("📖 AI Explanation")

                with st.container(border=True):
                    st.markdown(answer)
                st.success(
    "✅ Response generated using MedWise AI's curated WHO, CDC, and ICMR educational knowledge base."
)

                st.caption(
    "Educational sources: World Health Organization (WHO), Centers for Disease Control and Prevention (CDC), and Indian Council of Medical Research (ICMR)."
)
                with st.expander("📚 Learn More"):

                    st.write("""
This answer is generated using a curated educational knowledge base
built from publicly available WHO, CDC and ICMR resources.

MedWise AI simplifies trusted health information using AI while
avoiding diagnosis or treatment recommendations.
""")
                
            except Exception as e:

                st.error("Unable to generate a response.")

                st.code(str(e))

st.divider()

st.subheader("🔗 Continue Learning")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("📚 Learn AMR"):
        st.switch_page("pages/04_Learn_AMR.py")

with c2:
    if st.button("💡 Myth vs Fact"):
        st.switch_page("pages/05_Myth_vs_Fact.py")

with c3:
    if st.button("📝 Quiz"):
        st.switch_page("pages/06_Quiz.py")

# ==========================================
# Educational Disclaimer
# ==========================================

st.warning("""
### Educational Disclaimer

• This assistant provides educational information only.

• It does **not diagnose diseases**.

• It does **not prescribe medicines**.

• Always consult a qualified healthcare professional for medical advice.
""")

page_footer()