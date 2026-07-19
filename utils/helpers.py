import json
import streamlit as st


def load_questions():
    """Load questionnaire from JSON."""
    with open("data/questions.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_recommendations():
    """Load recommendation data."""
    with open("data/recommendations.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_myths():
    """Load myths and facts."""
    with open("data/myths.json", "r", encoding="utf-8") as file:
        return json.load(file)


def page_footer():
    st.divider()

    st.caption(
        "💊 MedWise AI | Educational Project | References: WHO • CDC • ICMR"
    )

def load_knowledge():

    with open(
        "data/knowledge_base.json",
        encoding="utf-8"
    ) as f:

        return json.load(f)