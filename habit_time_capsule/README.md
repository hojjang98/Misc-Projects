# 🧠 Habit Time Capsule — Data-Driven Future Self Simulator  

## 📌 Overview  
**Habit Time Capsule** was born from a daily idea-generation habit I maintain — see the original concept here: [habit_time_capsule.md](https://github.com/hojjang98/ideas/blob/main/self-insight/habit_time_capsule.md).  
Recently, after reading *Atomic Habits*, I was inspired to actually turn this idea into a working prototype.  

The goal is simple: give users a playful but data-driven way to **log daily habits** and **simulate their future self** (1/3/6/12 months).  

---

## 🚀 Features (MVP)  
- **Habit Logging**: Record habits with quick inputs (text/slider/number)  
- **Trend Visualization**: Plot daily values and moving averages  
- **Forecasting**: Extend trends into the future with a baseline + *what-if* slider  
- **Time Capsule**: Write a message to your future self and unlock it later  

---

## 🛠️ Tech Stack  
- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Backend/DB**: SQLite (auto-generated)  
- **Modeling**: Pandas, Numpy (moving averages & forecasts)  
- **Visualization**: Streamlit Charts, Matplotlib/Plotly  

---

## 📂 Project Structure  
```bash
habit_time_capsule/
├── app.py              # Main Streamlit app
├── habits.db           # SQLite database (auto-generated)
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── reports/            # (Optional) auto-generated PDF/PNG reports

⚡ Getting Started

git clone https://github.com/hojjang98/habit_time_capsule.git
cd habit_time_capsule

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

