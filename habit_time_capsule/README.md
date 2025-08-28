# 🧠 Habit Time Capsule — Data-Driven Future Self Simulator  

## 📌 Overview  
**Habit Time Capsule** started as a daily idea-generation exercise (see the original draft [here](https://github.com/hojjang98/ideas/blob/main/self-insight/habit_time_capsule.md)).  
After reading *Atomic Habits*, I decided to actually build it — not just as a concept, but as something I could use myself every day.  

The app is simple: log your habits, visualize trends, and leave notes to your “future self.”  
I built this mainly for **my own daily tracking**, but it also became a fun project to explore how small behaviors accumulate into long-term change.  

---

## 🚀 Features  
- **Habit Logging**  
  - Quick forms for recording habits (name, value, date)  
  - Categories to organize habits more clearly  

- **Visualization**  
  - Daily habit trends with moving averages  
  - Forecasting (next 7 days) based on recent data  

- **Time Capsule**  
  - Write a message to your future self  
  - Unlock it at a chosen future date  

- **Personal Use Case**  
  - I use this instead of plain notes to track small habits daily  
  - It doubles as a reflection tool — “if I keep this up, what kind of person will I be?”  

---

## 🛠️ Tech Stack  
- **Frontend/UI**: [Streamlit](https://streamlit.io/)  
- **Database**: SQLite (auto-generated, lightweight)  
- **Analysis**: Pandas, Numpy (moving averages & simple forecasts)  
- **Visualization**: Streamlit native charts + Matplotlib  

---

## 📂 Project Structure  
```bash
habit_time_capsule/
├── app.py              # Main Streamlit app
├── habits.db           # SQLite database (auto-generated)
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── reports/            # Time capsule messages (saved here)

⚡ Getting Started

git clone https://github.com/hojjang98/habit_time_capsule.git
cd habit_time_capsule

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

💡 Reflections

This project is not a polished product — it’s something I made to solve my own need.
But that’s also why it feels meaningful: I actually use it.

- Instead of just writing habits in a notepad, I can track them, visualize progress, and even forecast trends.

- The “time capsule” feature makes it fun — I leave notes to my future self to see how much I’ve changed.

For me, this is a reminder that even small coding projects can be powerful if they fit into your daily life.