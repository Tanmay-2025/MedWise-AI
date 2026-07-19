import streamlit as st
from utils.helpers import page_footer

st.title("🌐 Trusted Resources")
st.subheader("Reliable sources for antibiotic awareness and AMR education")

st.info("""
Continue learning from internationally recognized healthcare organizations.

These resources provide accurate, evidence-based information about
antibiotics, antimicrobial resistance (AMR), infection prevention,
and responsible medicine use.
""")

st.success("""
### 📚 What You Can Learn

These trusted organizations provide guidance on:

✔ Appropriate antibiotic use

✔ Antimicrobial Resistance (AMR)

✔ Infection prevention

✔ Antibiotic stewardship

✔ Patient safety

✔ Public health recommendations
""")
st.divider()

# ==========================================================
# Trusted Organizations
# ==========================================================

st.header("🏥 Trusted Healthcare Organizations")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 🌍 World Health Organization (WHO)

The WHO leads global efforts to combat Antimicrobial Resistance (AMR).

Key topics include:

• Global Action Plan on AMR

• Antibiotic stewardship

• Infection prevention and control

• Public awareness campaigns

• World AMR Awareness Week
""")

    st.link_button(
        "Visit WHO",
        "https://www.who.int/health-topics/antimicrobial-resistance",
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.success("""
### 🇮🇳 Indian Council of Medical Research (ICMR)

ICMR develops evidence-based national guidance for antibiotic use in India.

Resources include:

• Antimicrobial stewardship

• Treatment guidelines

• Hospital infection control

• National AMR surveillance
""")

    st.link_button(
        "Visit ICMR",
        "https://www.icmr.gov.in/",
        use_container_width=True
    )

with col2:

    st.info("""
### 🇺🇸 Centers for Disease Control and Prevention (CDC)

The CDC promotes responsible antibiotic use through its 'Be Antibiotics Aware' campaign.

Resources include:

• Appropriate antibiotic use

• Viral vs bacterial infections

• Safe prescribing practices

• Patient education materials
""")

    st.link_button(
        "Visit CDC",
        "https://www.cdc.gov/antibiotic-use/",
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info("""
### 🇮🇳 National Centre for Disease Control (NCDC)

NCDC supports India's public health system through:

• Disease surveillance

• Infection prevention

• Outbreak response

• National AMR initiatives
""")

    st.link_button(
        "Visit NCDC",
        "https://ncdc.mohfw.gov.in/",
        use_container_width=True
    )

st.divider()

st.header("📌 Key Messages from Trusted Health Authorities")

messages = [

    "Antibiotics should only be used when prescribed by a qualified healthcare professional.",

    "Antibiotics do not treat viral illnesses such as colds or influenza.",

    "Always complete the prescribed antibiotic course unless advised otherwise by your healthcare provider.",

    "Never share antibiotics with others.",

    "Never use leftover antibiotics for a future illness.",

    "Good hand hygiene and vaccination help reduce infections and antibiotic use.",

    "Responsible antibiotic use helps slow Antimicrobial Resistance (AMR)."

]

for message in messages:
    st.success(message)

st.divider()

# ==========================================================
# Quick Learning Tips
# ==========================================================

st.header("💊 Responsible Antibiotic Use")

tips = [

    "Take antibiotics only when prescribed by a qualified healthcare professional.",

    "Follow the prescribed dose and schedule carefully.",

    "Complete the entire prescribed course unless your doctor advises otherwise.",

    "Never request antibiotics for viral illnesses such as the common cold or flu.",

    "Never share antibiotics or reuse leftover medicines.",

    "Return unused medicines through safe disposal programs where available.",

    "Prevent infections through vaccination, hand hygiene, safe food preparation, and clean water."

]

for tip in tips:

    st.success(f"✅ {tip}")

st.divider()

st.header("🦠 Viral vs Bacterial Infections")

left, right = st.columns(2)

with left:

    st.error("""
### ❌ Usually Viral

• Common cold

• Influenza (flu)

• Most sore throats

• Most coughs

Antibiotics do NOT work.
""")

with right:

    st.success("""
### ✅ May Require Antibiotics

• Some bacterial pneumonia

• Urinary tract infections

• Strep throat

• Certain skin infections

Only after professional evaluation.
""")
st.divider()

# ==========================================================
# Additional Learning
# ==========================================================

st.header("🎓 Continue Learning")

st.markdown("""
After exploring these trusted resources, continue your learning through:

• 📚 Learn About AMR

• 💡 Myth vs Fact

• 📝 Antibiotic Awareness Quiz

• 🤖 AI Knowledge Assistant

• 🩺 Antibiotic Misuse Risk Checker
""")

st.info("""
Use the **Learn AMR**, **Myth vs Fact**, **Quiz**, and **AI Assistant**
pages to strengthen your understanding of responsible antibiotic use.
""")

st.divider()

# ==========================================================
# Disclaimer
# ==========================================================
st.success("""
### 🌱 Antibiotic Stewardship Starts With Everyone

Responsible antibiotic use protects you today and helps preserve these life-saving medicines for future generations.

Every informed decision contributes to slowing antimicrobial resistance.
""")
st.divider()
st.warning("""
### ⚠ Educational Disclaimer

The websites listed above are trusted public health resources.

MedWise AI provides educational information only and does **not**
diagnose diseases or prescribe medications.

Always consult a qualified healthcare professional for medical advice.
""")

page_footer()