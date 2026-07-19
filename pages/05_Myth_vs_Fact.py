import streamlit as st
from utils.helpers import load_myths, page_footer

st.title("💡 Myth vs Fact")
st.subheader("Separate common misconceptions from scientific facts")

st.info("""
Many people unknowingly misuse antibiotics because of common myths.

Understanding the facts helps reduce antimicrobial resistance (AMR) and promotes responsible antibiotic use.
""")

st.divider()

myths = load_myths()

for i, item in enumerate(myths, start=1):

    with st.expander(f"🧠 Myth {i}", expanded=False):

        st.error(f"❌ **Myth**\n\n{item['myth']}")

        st.markdown("---")

        st.success(f"✅ **Fact**\n\n{item['fact']}")

st.divider()

st.header("🧩 Quick Myth Check")

question = st.radio(
    "Antibiotics should be taken for the common cold.",
    ["Myth", "Fact"],
    index=None
)

if question == "Myth":
    st.success("✅ Correct! The common cold is caused by viruses, so antibiotics are not effective.")

elif question == "Fact":
    st.error("❌ Incorrect. Antibiotics do not treat viral infections like the common cold.")

st.divider()

st.header("📖 What Health Organizations Recommend")

recommendations = [
    "Use antibiotics only when prescribed by a qualified healthcare professional.",
    "Never demand antibiotics for viral illnesses.",
    "Follow the prescribed dose and schedule.",
    "Never share or reuse leftover antibiotics.",
    "Help prevent infections through vaccination and good hygiene."
]

for rec in recommendations:
    st.success(rec)

st.divider()
st.header("📌 Key Takeaways")

left, right = st.columns(2)

with left:

    st.success("""
### ✅ Always Remember

✔ Antibiotics treat bacterial infections.

✔ Complete the full prescribed course.

✔ Follow your doctor's advice.

✔ Dispose of leftover medicines safely.
""")

with right:

    st.error("""
### ❌ Avoid These Practices

✖ Self-medication

✖ Sharing antibiotics

✖ Using leftover antibiotics

✖ Taking antibiotics for colds or flu
""")

st.divider()

st.header("🌍 Why Correct Information Matters")

col1, col2 = st.columns(2)

with col1:
    st.metric("Safer Treatment", "✔")

    st.metric("Reduced AMR", "✔")

with col2:
    st.metric("Better Patient Outcomes", "✔")

    st.metric("Protects Future Antibiotics", "✔")

st.divider()

st.info("""
### 💡 Did You Know?

According to WHO, CDC, and ICMR guidance:

• Antibiotics are among the most valuable medicines in modern healthcare.

• Misuse accelerates antimicrobial resistance.

• Everyone has a role in preserving their effectiveness through responsible use.
""")

st.divider()
st.warning("""
### Educational Disclaimer

This information is intended for educational purposes only.

Always consult a qualified healthcare professional for diagnosis and treatment.
""")

st.caption(
    "Sources: World Health Organization (WHO), CDC, Indian Council of Medical Research (ICMR)"
)

page_footer()