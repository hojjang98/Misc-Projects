import streamlit as st
import sqlite3
import pandas as pd
import datetime
import matplotlib.pyplot as plt

# -----------------------------
# 1. Initialize Database
# -----------------------------
def init_db():
    conn = sqlite3.connect("habits.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit TEXT NOT NULL,
        value INTEGER,
        date TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# 2. DB Functions
# -----------------------------
def log_habit(habit: str, value: int, date: str = None):
    if date is None:
        date = datetime.date.today().isoformat()
    conn = sqlite3.connect("habits.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO habits (habit, value, date) VALUES (?, ?, ?)",
                (habit, value, date))
    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect("habits.db")
    df = pd.read_sql("SELECT * FROM habits", conn)
    conn.close()
    return df

# -----------------------------
# 3. UI - Habit Logging
# -----------------------------
st.title("🧠 Habit Time Capsule")

st.header("Log a Habit")
with st.form("habit_form"):
    habit = st.text_input("Habit name", "")
    value = st.number_input("Value", min_value=0, step=1)
    date = st.date_input("Date", datetime.date.today())
    submitted = st.form_submit_button("Save")

    if submitted and habit:
        log_habit(habit, int(value), date.isoformat())
        st.success(f"Saved: {habit} - {value} on {date}")

# -----------------------------
# 4. View Habit Records
# -----------------------------
st.header("Habit Records")
df = load_data()
if not df.empty:
    st.dataframe(df)
else:
    st.info("No habit records yet. Add one above!")

# -----------------------------
# 5. Trend Visualization
# -----------------------------
st.header("Habit Trends")
if not df.empty:
    df["date"] = pd.to_datetime(df["date"])
    daily_trends = df.groupby(["date", "habit"])["value"].sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 5))
    for habit_name in daily_trends["habit"].unique():
        subset = daily_trends[daily_trends["habit"] == habit_name]
        ax.plot(subset["date"], subset["value"], marker="o", label=habit_name)

    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.set_title("Habit Trends Over Time")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("No data to visualize yet.")

# -----------------------------
# 6. Forecasting
# -----------------------------
st.header("Forecast Example")
if not df.empty:
    habit_choice = st.selectbox("Choose a habit to forecast", df["habit"].unique())
    subset = df[df["habit"] == habit_choice].copy().sort_values("date")
    subset["date"] = pd.to_datetime(subset["date"])

    subset["ma"] = subset["value"].rolling(window=3, min_periods=1).mean()

    last_date = subset["date"].max()
    future_dates = [last_date + datetime.timedelta(days=i) for i in range(1, 8)]
    last_ma = subset["ma"].iloc[-1]
    future_values = [last_ma] * len(future_dates)

    forecast_df = pd.DataFrame({"date": future_dates, "forecast": future_values})

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(subset["date"], subset["value"], marker="o", label="Actual")
    ax.plot(subset["date"], subset["ma"], linestyle="--", label="Moving Avg")
    ax.plot(forecast_df["date"], forecast_df["forecast"], linestyle=":", marker="x", label="Forecast")

    ax.set_title(f"{habit_choice} Forecast (Next 7 Days)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()
    st.pyplot(fig)
else:
    st.info("No data available for forecasting.")

# -----------------------------
# 7. Time Capsule
# -----------------------------
st.header("Time Capsule")
capsule_message = st.text_area("Write a message to your future self")
unlock_date = st.date_input("Unlock date", datetime.date.today())

if st.button("Save Capsule"):
    import os
    os.makedirs("reports", exist_ok=True)
    with open("reports/time_capsule.txt", "a", encoding="utf-8") as f:
        f.write(f"{unlock_date}: {capsule_message}\n")
    st.success("Time capsule saved! (check reports/time_capsule.txt)")