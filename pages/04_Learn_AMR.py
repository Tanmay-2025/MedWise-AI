import streamlit as st
from utils.helpers import page_footer

st.title("📚 Learn About Antimicrobial Resistance (AMR)")
st.subheader("Understand why responsible antibiotic use matters")

st.info("""
### 🦠 What is Antimicrobial Resistance (AMR)?

Antimicrobial Resistance (AMR) occurs when microorganisms—especially bacteria—change over time and no longer respond effectively to antibiotics.

As a result, infections become harder to treat, increasing the risk of severe illness, prolonged hospital stays, and higher healthcare costs.

Responsible antibiotic use helps slow the development of resistance and protects these life-saving medicines for future generations.
""")

st.divider()

# ==================================================
# Key Statistics
# ==================================================

st.header("📊 Why Should We Care?")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Global Health Threat", "Yes 🌍")

with c2:
    st.metric("Can It Be Prevented?", "Partially ✅")

with c3:
    st.metric("Public Awareness", "Essential 📚")

st.divider()

# ==================================================
# How AMR Happens
# ==================================================

st.header("🔬 How Does Antibiotic Resistance Develop?")

steps = [
    "🦠 A bacterial infection occurs.",
    "💊 Antibiotics kill susceptible bacteria.",
    "🛡️ Naturally resistant bacteria survive.",
    "📈 Resistant bacteria multiply and spread.",
    "⚠ Future infections become more difficult to treat."
]

for step in steps:
    st.write(step)
st.divider()
# ==================================================
# Good vs Bad Practices
# ==================================================

st.header("✅ Safe Practices vs ❌ Unsafe Practices")

left, right = st.columns(2)

with left:

    st.success("""
### ✅ Responsible Antibiotic Use

✔ Take antibiotics only when prescribed

✔ Complete the full course

✔ Follow dosage instructions

✔ Ask healthcare professionals when unsure

✔ Dispose of unused medicines properly
""")

with right:

    st.error("""
### ❌ Antibiotic Misuse

✖ Self-medication

✖ Stopping treatment early

✖ Sharing antibiotics

✖ Using leftover medicines

✖ Taking antibiotics for viral infections
""")

st.divider()


st.header("🩺 When Are Antibiotics Needed?")

left, right = st.columns(2)

with left:

    st.success("""
### Usually Needed

✔ Strep throat (bacterial)

✔ Certain urinary tract infections

✔ Some bacterial pneumonia

✔ Certain skin infections
""")

with right:

    st.error("""
### Usually NOT Needed

✖ Common cold

✖ Influenza (Flu)

✖ Most coughs

✖ Most sore throats caused by viruses
""")
# ==================================================
# Consequences
# ==================================================

st.header("⚠ Consequences of Antibiotic Misuse")

a, b, c, d = st.columns(4)

with a:
    st.metric("Longer Illness", "↑")

with b:
    st.metric("Hospital Stay", "↑")

with c:
    st.metric("Treatment Cost", "↑")

with d:
    st.metric("Drug Resistance", "↑")

st.divider()


st.header("🏥 What is Antibiotic Stewardship?")

st.success("""
Antibiotic stewardship means using antibiotics only when necessary,
choosing the correct medicine, dose, and duration.

It helps:

• Improve patient outcomes

• Reduce unnecessary antibiotic use

• Slow antimicrobial resistance

• Preserve antibiotic effectiveness
""")

# ==================================================
# Myth vs Reality
# ==================================================

st.header("💡 Did You Know?")

st.info("""
💊 **Antibiotics only work against bacterial infections.**

They do **NOT** cure:

• Common Cold

• Flu

• Most sore throats caused by viruses

• Viral fever
""")

st.divider()

# ==================================================
# Prevention Tips
# ==================================================

st.header("🛡 How Can We Prevent AMR?")

tips = [

    "Take antibiotics only when prescribed by a qualified healthcare professional.",

    "Follow the prescribed dose and schedule exactly as instructed.",

    "Complete the full course unless your healthcare professional advises otherwise.",

    "Never buy antibiotics without a prescription where regulations require one.",

    "Never share antibiotics with anyone.",

    "Do not keep leftover antibiotics for future illnesses.",

    "Wash your hands regularly to prevent infections.",

    "Stay up to date with recommended vaccinations.",

    "Help spread awareness about responsible antibiotic use."
]

for i, tip in enumerate(tips, start=1):
    st.success(f"**{i}.** {tip}")

st.divider()

# ==================================================
# Summary
# ==================================================


st.header("📝 Quick Knowledge Check")

q = st.radio(
    "Antibiotics are effective against:",
    [
        "Viruses",
        "Bacteria",
        "Both"
    ],
    index=None
)

if q == "Viruses":
    st.error("Incorrect. Antibiotics do not treat viral infections.")

elif q == "Both":
    st.error("Incorrect. Antibiotics work only against bacterial infections.")

elif q == "Bacteria":
    st.success("Correct! Responsible antibiotic use helps prevent AMR.")
st.divider()
st.header("🎯 Key Takeaways")

st.success("""
✔ Antibiotics treat bacterial infections—not viral illnesses.

✔ Never use antibiotics without professional medical advice.

✔ Always follow the prescribed dose and duration.

✔ Never share or reuse leftover antibiotics.

✔ Responsible antibiotic use helps protect everyone from antimicrobial resistance.
""")

st.warning("""
### Educational Disclaimer

This information is provided for educational purposes only.

MedWise AI does **not** diagnose illnesses or prescribe medications.

Always consult a qualified healthcare professional for medical advice.
""")

st.caption("""
Educational content adapted from publicly available guidance issued by:

• World Health Organization (WHO)

• Centers for Disease Control and Prevention (CDC)

• Indian Council of Medical Research (ICMR)

This page is intended for awareness and educational purposes only.
""")

page_footer()