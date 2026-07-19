import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

from utils.prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")


# ==========================================
# Load Local Knowledge Base
# ==========================================

def load_knowledge():

    with open(
        "data/knowledge_base.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


# ==========================================
# Retrieve Relevant Information
# ==========================================

def retrieve_context(question):

    knowledge = load_knowledge()

    question = question.lower()

    context = []

    for item in knowledge:

        for keyword in item["keywords"]:

            if keyword.lower() in question:

                context.append(
                    f"[{item['source']}] {item['content']}"
                )

                break

    return "\n".join(context)


# ==========================================
# AI Function
# ==========================================

def ask_ai(question):

    try:

        context = retrieve_context(question)

        if context == "":

            context = (
                "No directly matching information was found in the local "
                "knowledge base. Use general WHO, CDC and ICMR educational "
                "guidelines only."
            )

        prompt = f"""
{SYSTEM_PROMPT}

You are MedWise AI.

Your primary source of information is the embedded knowledge base below.

Never contradict it.

Never diagnose diseases.

Never prescribe medicines.

Always encourage consulting a qualified healthcare professional.

-----------------------------------

Embedded Knowledge

{context}

-----------------------------------

User Question

{question}

"""

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error: {e}"