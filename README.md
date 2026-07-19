# 💊 MedWise AI

## AI-Based Antibiotic Misuse Awareness & Risk Checker

MedWise AI is an educational web application developed to promote responsible antibiotic use and increase awareness about Antimicrobial Resistance (AMR). The platform combines AI, interactive learning, and transparent risk assessment to help users understand safe antibiotic practices.

---

## ✨ Features

### 🩺 Antibiotic Misuse Risk Checker
- Interactive questionnaire
- Transparent risk scoring
- Personalized recommendations
- Risk dashboard with charts
- Downloadable PDF report

### 🤖 AI Educational Assistant
- Powered by Google Gemini
- Uses a local knowledge base built from WHO, CDC, and ICMR guidance
- Answers educational questions about antibiotics and AMR
- Does not provide diagnosis or prescriptions

### 📚 Learn About AMR
- What AMR is
- How antibiotic resistance develops
- Safe vs unsafe antibiotic practices
- Prevention strategies

### 💡 Myth vs Fact
- Common misconceptions about antibiotics
- Evidence-based facts from trusted health organizations

### 📝 Awareness Quiz
- Interactive multiple-choice quiz
- Instant scoring
- Explanations for every answer

### 🌐 Trusted Resources
- WHO
- CDC
- ICMR
- NCDC

---

## 🛠 Technology Stack

- Python
- Streamlit
- Google Gemini API
- Plotly
- ReportLab
- Pillow

---

## 📂 Project Structure

```text
MedWise-AI/
│
├── assets/
├── data/
├── pages/
├── utils/
├── app.py
├── style.css
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Tanmay-2025/MedWise-AI.git
```

Move into the project:

```bash
cd MedWise-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 📚 Knowledge Sources

This project uses educational information based on guidance from:

- World Health Organization (WHO)
- Centers for Disease Control and Prevention (CDC)
- Indian Council of Medical Research (ICMR)
- National Centre for Disease Control (NCDC)

---

## ⚠ Disclaimer

MedWise AI is intended for educational and awareness purposes only.

It does not diagnose diseases, prescribe medications, or replace professional medical advice. Always consult a qualified healthcare professional regarding diagnosis and treatment.

---

## 👨‍💻 Developer

Developed as a Bio-Hackathon project to promote responsible antibiotic use and public awareness of antimicrobial resistance.