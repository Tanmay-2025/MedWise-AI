import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils.helpers import (
    load_questions,
    load_recommendations,
    page_footer,
)

from utils.risk_engine import calculate_risk
from utils.pdf_generator import generate_pdf


# ---------------- PAGE ---------------- #

st.title("🩺 Antibiotic Misuse Risk Assessment")

st.markdown("""
Evaluate your antibiotic usage habits and awareness.

This educational assessment estimates your likelihood of **antibiotic misuse**
using guidance adapted from **WHO, CDC and ICMR**.

⚠ **This is NOT a medical diagnosis.**
""")

questions = load_questions()
recommendations = load_recommendations()

MAX_SCORE = 13

st.divider()

# ---------------- FORM ---------------- #

with st.form("risk_form"):

    st.subheader("Answer the following questions")

    answers = {}

    for q in questions:

        if q["type"] == "radio":

            answers[q["id"]] = st.radio(
                q["question"],
                q["options"],
                index=None,
                key=f"q_{q['id']}"
            )

        else:

            answers[q["id"]] = st.selectbox(
                q["question"],
                ["Select an option"] + q["options"],
                key=f"q_{q['id']}"
            )

    submitted = st.form_submit_button(
        "🔍 Assess My Risk",
        use_container_width=True
    )

# ---------------- VALIDATION ---------------- #

if submitted:

    invalid = False

    for value in answers.values():

        if value is None or value == "Select an option":

            invalid = True

    if invalid:

        st.error("Please answer every question before submitting.")

    else:

        result = calculate_risk(answers)

        risk = recommendations[result["level"]]

        st.divider()

        st.header("📊 Assessment Results")

        # ---------------- RISK BADGE ---------------- #

        if result["level"] == "Low":

            st.markdown("""
<div style="
background:#E8F5E9;
padding:18px;
border-radius:12px;
font-size:24px;
font-weight:bold;
color:#2E7D32;
text-align:center;
border-left:8px solid #2E7D32;">
🟢 LOW RISK
</div>
""", unsafe_allow_html=True)

        elif result["level"] == "Moderate":

            st.markdown("""
<div style="
background:#FFF8E1;
padding:18px;
border-radius:12px;
font-size:24px;
font-weight:bold;
color:#F9A825;
text-align:center;
border-left:8px solid #F9A825;">
🟡 MODERATE RISK
</div>
""", unsafe_allow_html=True)

        else:

            st.markdown("""
<div style="
background:#FFEBEE;
padding:18px;
border-radius:12px;
font-size:24px;
font-weight:bold;
color:#C62828;
text-align:center;
border-left:8px solid #C62828;">
🔴 HIGH RISK
</div>
""", unsafe_allow_html=True)

        st.write(risk["message"])

        st.divider()

        # ---------------- DASHBOARD ---------------- #

        st.subheader("📈 Risk Dashboard")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Risk Score",
                f"{result['score']} / {MAX_SCORE}"
            )

        with c2:
            st.metric(
                "Unsafe Habits",
                len(result["flags"])
            )

        with c3:
            st.metric(
                "Risk Level",
                result["level"]
            )

        # ---------------- GAUGE ---------------- #

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=result["score"],
                title={"text": "Risk Score"},
                gauge={
                    "axis": {"range": [0, MAX_SCORE]},
                    "bar": {"color": "#1565C0"},
                    "steps": [
                        {"range": [0,4], "color":"#C8E6C9"},
                        {"range": [4,8], "color":"#FFE082"},
                        {"range": [8,13], "color":"#EF9A9A"},
                    ]
                }
            )
        )

        gauge.update_layout(height=320)

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

        st.markdown("""
### Risk Scale

🟢 **0–3** → Low Risk

🟡 **4–7** → Moderate Risk

🔴 **8–13** → High Risk
""")
        
        # ---------------- DONUT CHART ---------------- #

        st.divider()

        st.subheader("📊 Antibiotic Usage Overview")

        TOTAL_QUESTIONS = len(questions)

        unsafe = len(result["flags"])
        safe = TOTAL_QUESTIONS - unsafe

        fig = px.pie(
            names=["Safe Practices", "Unsafe Practices"],
            values=[safe, unsafe],
            hole=0.65,
            color=["Safe Practices", "Unsafe Practices"],
            color_discrete_map={
                "Safe Practices": "#4CAF50",
                "Unsafe Practices": "#F44336"
            }
        )

        fig.update_traces(
            textinfo="percent+label"
        )

        fig.update_layout(
            showlegend=False,
            height=420,
            margin=dict(l=10, r=10, t=20, b=10)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ---------------- PERSONALIZED SUMMARY ---------------- #

        st.divider()

        st.subheader("🩺 Personalized Summary")

        if result["level"] == "Low":

            st.success("""
Your responses indicate **responsible antibiotic practices**.

Continue following medical advice, complete prescribed treatments,
and avoid unnecessary antibiotic use.
""")

        elif result["level"] == "Moderate":

            st.warning("""
Your responses suggest **some habits that may increase the risk of
antibiotic misuse**.

Review the recommendations below to improve safe antibiotic use.
""")

        else:

            st.error("""
Your responses indicate **multiple behaviours associated with
antibiotic misuse**.

Learning about responsible antibiotic use can help reduce the risk
of antimicrobial resistance (AMR).
""")

        # ---------------- UNSAFE HABITS ---------------- #

        st.divider()

        st.subheader("🚩 Unsafe Habits Identified")

        if result["flags"]:

            for flag in result["flags"]:

                st.markdown(f"""
<div style="
background:#FFF8E1;
padding:15px;
border-left:6px solid #FB8C00;
border-radius:12px;
margin-bottom:10px;">

⚠ <b>{flag}</b>

</div>
""", unsafe_allow_html=True)

        else:

            st.success("Excellent! No unsafe antibiotic practices were identified.")

        # ---------------- GOOD PRACTICES ---------------- #

        st.divider()

        st.subheader("✅ Positive Practices")

        good = []

        if answers.get("source") == "Prescription from a doctor":
            good.append("Obtained antibiotics through a healthcare professional.")

        if answers.get("completed") == "Yes":
            good.append("Completed the prescribed antibiotic course.")

        if answers.get("shared") == "No":
            good.append("Did not share antibiotics with others.")

        if answers.get("leftover") == "No":
            good.append("Did not store or reuse leftover antibiotics.")

        if len(good):

            for item in good:
                st.success(item)

        else:

            st.info("Keep following safe antibiotic practices.")

        # ---------------- RECOMMENDATIONS ---------------- #

        st.divider()

        st.subheader("💡 Personalized Recommendations")

        for rec in risk["recommendations"]:

            st.markdown(f"""
<div style="
background:#E8F5E9;
padding:15px;
border-left:6px solid #2E7D32;
border-radius:12px;
margin-bottom:12px;">

✅ {rec}

</div>
""", unsafe_allow_html=True)

        # ---------------- WHY IT MATTERS ---------------- #

        st.divider()

        st.subheader("📘 Why These Habits Matter")

        explanations = {

            "Self-medication":
            "Taking antibiotics without medical advice increases the chance of unnecessary antibiotic use and contributes to antimicrobial resistance.",

            "Possible self-medication":
            "Using antibiotics without professional evaluation may result in inappropriate treatment.",

            "Used leftover antibiotics":
            "Leftover antibiotics may not be appropriate for your current illness and should never be reused.",

            "Stored leftover antibiotics":
            "Keeping leftover antibiotics encourages self-medication in the future.",

            "Shared leftover antibiotics":
            "Sharing leftover medicines may delay proper diagnosis and treatment.",

            "Shared antibiotics":
            "Antibiotics should never be shared because treatments differ depending on the infection and patient.",

            "Used antibiotics from another person":
            "Medicines prescribed for someone else may not be appropriate for you.",

            "Stopped antibiotic course early":
            "Stopping treatment before completing the prescribed course may contribute to antimicrobial resistance.",

            "Used antibiotics for viral infection":
            "Antibiotics do not work against viral illnesses such as colds and influenza.",

            "Uncertain antibiotic use":
            "Patients should understand why antibiotics are prescribed before taking them."
        }

        if result["flags"]:

            for flag in result["flags"]:

                with st.expander(flag):

                    st.write(explanations.get(flag))

                    st.caption("Reference: WHO • CDC • ICMR")

        # ---------------- LEARN MORE ---------------- #

        st.divider()

        st.subheader("📚 Learn More")

        st.info("""
### WHO, CDC & ICMR Recommendations

✔ Take antibiotics **only when prescribed** by a qualified healthcare professional.

✔ Never use antibiotics for viral illnesses like the common cold or flu.

✔ Follow the prescribed dose and duration.

✔ Never share antibiotics.

✔ Never reuse leftover antibiotics.

✔ Prevent infections through vaccination, hand hygiene and healthy practices.

Responsible antibiotic use protects both you and future generations.
""")

        # ---------------- REPORT ---------------- #

        st.divider()

        st.subheader("📄 Assessment Report")

        pdf = generate_pdf(
            result,
            risk["recommendations"]
        )

        st.download_button(
            "⬇ Download My Assessment Report",
            pdf,
            file_name="MedWise_AI_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        st.success(
            "Your report contains your risk level, identified habits and personalized recommendations."
        )

        # ---------------- NEXT STEPS ---------------- #

        st.divider()

        st.subheader("🚀 Continue Learning")

        c1, c2, c3 = st.columns(3)

        with c1:
            if st.button("📚 Learn AMR", use_container_width=True):
                st.switch_page("pages/04_Learn_AMR.py")

        with c2:
            if st.button("🤖 Ask AI", use_container_width=True):
                st.switch_page("pages/03_AI_Assistant.py")

        with c3:
            if st.button("📝 Take Quiz", use_container_width=True):
                st.switch_page("pages/06_Quiz.py")

st.divider()

st.info(
    """
⚠ Disclaimer

This assessment is intended for educational purposes only.

Always consult a qualified healthcare professional regarding
medical diagnosis or treatment.
"""
)

page_footer()