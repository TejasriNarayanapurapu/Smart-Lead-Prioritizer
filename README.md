# 🚀 Smart Lead Prioritizer – Caprae Capital Internship Challenge

This project was developed as part of the AI-Readiness Prework Challenge by **Caprae Capital Partners**. It is designed to demonstrate how AI-driven tools can streamline lead generation and prioritization for acquisition and outreach teams.

## 📌 Project Objective

To replicate and enhance aspects of [SaaSquatchLeads](https://www.saasquatchleads.com/) within a strict 5-hour build window — showcasing practical AI/ML/heuristic tools for prioritizing B2B leads.

## 💡 What It Does

Upload a CSV of raw leads and instantly receive a scored, ranked list that highlights the most promising leads. Each lead is scored based on:

| Feature     | Score |
|-------------|-------|
| Email       | +2    |
| LinkedIn    | +3    |
| Company     | +2    |
| Website     | +1    |

Final output is downloadable and ranked by score.

## 🔧 Features

- 📥 CSV Upload (Streamlit file uploader)
- ✅ Automatic scoring based on completeness
- 📊 Top 3 leads preview
- 💾 Downloadable CSV of scored leads
- 🎯 No ML required – heuristic-based, fast, reliable

## 📽️ Project Walkthrough Video

🎥 I created a short 2-minute walkthrough explaining the logic, features, and usage of the Lead Prioritizer app.  
Watch it here 👉 [https://drive.google.com/file/d/14CeZXgJSYTzhLyC-CEBxfXVBoAF07EXV/view?usp=drive_link]

> In the video, I demonstrate how the Streamlit app works, how the CSV leads are scored based on business criteria, and how users can download the prioritized leads — all within a clean and intuitive UI.
  

## 🧪 How to Run

```bash
git clone https://github.com/yourusername/lead-prioritizer.git
cd lead-prioritizer
pip install -r requirements.txt
streamlit run app.py




