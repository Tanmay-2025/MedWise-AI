import streamlit as st
from utils.helpers import page_footer

st.title("📝 Antibiotic Awareness Quiz")
st.subheader("Test your knowledge of antibiotics and antimicrobial resistance")

st.info("""
Test your understanding of responsible antibiotic use and antimicrobial resistance (AMR).

The questions are based on educational guidance from the World Health Organization (WHO), Centers for Disease Control and Prevention (CDC), and the Indian Council of Medical Research (ICMR).

This quiz is intended for educational purposes only.
""")

st.divider()

questions = [

    {
        "question": "1. How should antibiotics ideally be obtained?",
        "options": [
            "Prescription from a qualified doctor",
            "From a friend or family member",
            "Using leftover antibiotics",
            "Buying without medical consultation"
        ],
        "answer": "Prescription from a qualified doctor",
        "explanation": "Antibiotics should only be taken when prescribed by a qualified healthcare professional."
    },

    {
        "question": "2. Antibiotics are effective against:",
        "options": [
            "Viruses",
            "Bacteria",
            "All infections",
            "Common cold and flu"
        ],
        "answer": "Bacteria",
        "explanation": "Antibiotics treat bacterial infections. They do not work against viruses."
    },

    {
        "question": "3. When should you stop taking antibiotics?",
        "options": [
            "When symptoms improve",
            "After two days",
            "Complete the prescribed course",
            "Whenever you feel better"
        ],
        "answer": "Complete the prescribed course",
        "explanation": "Stopping antibiotics early increases the risk of antimicrobial resistance."
    },

    {
        "question": "4. What should you do with leftover antibiotics?",
        "options": [
            "Keep them for future illnesses",
            "Share them with family",
            "Dispose of them safely",
            "Take them whenever you feel sick"
        ],
        "answer": "Dispose of them safely",
        "explanation": "Leftover antibiotics should not be reused or shared."
    },

    {
        "question": "5. Why is antibiotic misuse dangerous?",
        "options": [
            "It causes antimicrobial resistance",
            "It improves immunity",
            "It cures viral infections faster",
            "It has no effect"
        ],
        "answer": "It causes antimicrobial resistance",
        "explanation": "Misusing antibiotics allows bacteria to become resistant to treatment."
    },

    {
    "question": "6. Which illness usually does NOT require antibiotics?",
    "options": [
        "Common cold",
        "Bacterial pneumonia",
        "Urinary tract infection",
        "Strep throat"
    ],
    "answer": "Common cold",
    "explanation": "The common cold is caused by viruses. Antibiotics only treat bacterial infections."
},

{
    "question": "7. What is the safest action if you miss an antibiotic dose?",
    "options": [
        "Take two doses together",
        "Follow your healthcare professional's or medicine label's instructions",
        "Stop the medicine completely",
        "Take antibiotics only when symptoms return"
    ],
    "answer": "Follow your healthcare professional's or medicine label's instructions",
    "explanation": "If you miss a dose, follow the instructions provided with your medicine or consult your healthcare professional."
},

{
    "question": "8. Antibiotic resistance occurs when:",
    "options": [
        "Your body becomes resistant",
        "Bacteria become resistant",
        "Viruses become resistant",
        "Medicines expire"
    ],
    "answer": "Bacteria become resistant",
    "explanation": "Resistance develops in bacteria, making infections harder to treat."
},

{
    "question": "9. Which practice helps prevent antimicrobial resistance?",
    "options": [
        "Sharing antibiotics",
        "Stopping treatment early",
        "Using antibiotics only when prescribed",
        "Keeping leftover antibiotics"
    ],
    "answer": "Using antibiotics only when prescribed",
    "explanation": "Responsible antibiotic use is one of the most effective ways to slow antimicrobial resistance."
},

{
    "question": "10. Besides responsible antibiotic use, what also helps reduce antimicrobial resistance?",
    "options": [
        "Good hand hygiene and vaccination",
        "Taking antibiotics monthly",
        "Keeping leftover medicines",
        "Sharing prescriptions"
    ],
    "answer": "Good hand hygiene and vaccination",
    "explanation": "Preventing infections reduces the need for antibiotics and helps slow resistance."
}

]

with st.form("quiz_form"):

    answers = []

    for i, q in enumerate(questions):

        answer = st.radio(
            q["question"],
            q["options"],
            index=None,
            key=f"q{i}"
        )

        answers.append(answer)

        st.markdown("<br>", unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "🎯 Submit Quiz",
        use_container_width=True
    )

if submitted:

    if None in answers:

        st.error("Please answer every question before submitting.")

    else:

        score = 0

        for answer, question in zip(answers, questions):

            if answer == question["answer"]:

                score += 1

        percentage = round(score / len(questions) * 100)

        st.divider()

        st.header("📊 Your Quiz Result")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Score", f"{score}/{len(questions)}")

        with col2:
            st.metric("Percentage", f"{percentage}%")

        with col3:

            if percentage >= 80:
                level = "Excellent"
            elif percentage >= 60:
                level = "Good"
            else:
                level = "Needs work"

            st.metric("Performance", level)

        st.progress(percentage / 100)

        st.divider()

        if percentage >= 80:

            st.success("""
### 🏆 Excellent!

You have a strong understanding of responsible antibiotic use and antimicrobial resistance.
""")

        elif percentage >= 60:

            st.info("""
### 👍 Good Job!

You have good awareness, but reviewing the learning materials will strengthen your understanding.
""")

        else:

            st.warning("""
### 📚 Needs Work

Visit the **Learn AMR** page to improve your knowledge about responsible antibiotic use.
""")
        
        st.divider()

        st.header("📖 Review Your Answers")

        for i, q in enumerate(questions):

            correct = answers[i] == q["answer"]

            with st.expander(f"Question {i+1}"):

                if correct:
                    st.success("✅ Correct")
                else:
                    st.error("❌ Incorrect")

                st.write(f"**Your Answer:** {answers[i]}")
                st.write(f"**Correct Answer:** {q['answer']}")

                st.info(f"**Explanation:** {q['explanation']}")

st.divider()

st.divider()

st.header("📚 What You Learned")

learning_points = [
    "Antibiotics treat bacterial—not viral—infections.",
    "Never self-medicate with antibiotics.",
    "Never share or reuse leftover antibiotics.",
    "Antimicrobial resistance develops in bacteria.",
    "Good hygiene and vaccination help reduce the need for antibiotics."
]

for point in learning_points:
    st.success(point)

st.divider()

st.subheader("Continue Learning")

c1, c2 = st.columns(2)

with c1:
    if st.button("📚 Learn About AMR", use_container_width=True):
        st.switch_page("pages/04_Learn_AMR.py")

with c2:
    if st.button("💡 Myth vs Fact", use_container_width=True):
        st.switch_page("pages/05_Myth_vs_Fact.py")
st.warning("""
### Educational Disclaimer

This quiz evaluates awareness of responsible antibiotic use.

It does not diagnose illness, determine infection type, or replace advice from a qualified healthcare professional.
""")

st.caption(
    "Educational content adapted from WHO, CDC, and ICMR public guidance."
)

page_footer()