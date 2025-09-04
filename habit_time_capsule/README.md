# 🧠 Habit Time Capsule — Data-Driven Future Self Simulator  

## 🔍 Summary
A personal project that started as an idea-generation exercise, later built into a working app.  
Habit Time Capsule lets users **log daily habits**, **visualize progress**, and leave **messages to their future selves**.  
Inspired by *Atomic Habits*, this tool helps track small behaviors that accumulate into long-term change.  

---

## 🎯 Objectives
- Replace plain notetaking with structured habit tracking  
- Visualize habit trends and forecast future progress  
- Add a playful element with a “time capsule” feature  

---

## 🚀 Features
- **Habit Logging**: Quick forms, categories for organization  
- **Visualization**: Daily trends, moving averages, 7-day forecasts  
- **Time Capsule**: Leave notes to future self, unlock later  
- **Personal Use Case**: Daily use for reflection and behavior tracking  

---

## 🛠️ Tech Stack
- **Frontend/UI**: Streamlit  
- **Database**: SQLite  
- **Analysis**: Pandas, Numpy  
- **Visualization**: Streamlit charts, Matplotlib  

---

## 📂 Project Structure
```bash
habit_time_capsule/
├── app.py              # Main Streamlit app
├── habits.db           # SQLite database (auto-generated)
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── reports/            # Time capsule messages
```

---

⚡ Getting Started

git clone https://github.com/hojjang98/habit_time_capsule.git
cd habit_time_capsule

pip install -r requirements.txt
streamlit run app.py

## 📊 Results
- Implemented a fully working habit tracking system with daily visualization  
- Integrated a simple 7-day forecasting method to estimate future trends  
- Time capsule feature successfully tested — messages can be written and unlocked later  
- Used daily in practice, replacing plain notepad-style habit logs  

---

## 🚀 Next Steps
- Add export/import functionality for habit logs  
- Explore advanced forecasting (Prophet, ARIMA, or ML models)  
- Improve UI/UX with custom components for easier habit input  
- Extend visualization options (weekly/monthly aggregates)  

---

## 💡 Reflections
This project started as a personal experiment but quickly became something meaningful in my daily routine.  
Even though it’s small and simple, it proves that coding projects don’t need to be “big” to be impactful —  
as long as they fit into your life, they can bring real value.
