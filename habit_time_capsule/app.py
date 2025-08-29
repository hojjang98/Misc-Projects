import streamlit as st
import sqlite3
import pandas as pd
import datetime
import os
import altair as alt

# -----------------------------
# 1. Initialize Database
# -----------------------------
DB_PATH = os.path.join(os.path.dirname(__file__), "workouts.db")

def init_db():
    """DB 없으면 새로 생성"""
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS workout_sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            exercise TEXT NOT NULL,
            set_num INTEGER,
            reps INTEGER,
            weight REAL,
            note TEXT
        )
        """)
        conn.commit()
        conn.close()

init_db()

# -----------------------------
# 2. DB Functions
# -----------------------------
def log_set(exercise: str, set_num: int, reps: int, weight: float, note: str, date: str = None):
    """운동 세트 기록 저장"""
    if date is None:
        date = datetime.date.today().isoformat()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO workout_sets (date, exercise, set_num, reps, weight, note) VALUES (?, ?, ?, ?, ?, ?)",
                (date, exercise, set_num, reps, weight, note))
    conn.commit()
    conn.close()

def load_data():
    """전체 데이터 로드"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM workout_sets", conn)
    conn.close()
    return df

# -----------------------------
# 3. Predefined Categories
# -----------------------------
EXERCISE_CATEGORY = {
    "Bench Press": "Chest",
    "Incline Dumbbell Press": "Chest",
    "Dips": "Chest/Triceps",
    "Pull-ups": "Back",
    "Barbell Row": "Back",
    "Bicep Curl": "Biceps",
    "Squat": "Legs",
    "Deadlift": "Back/Legs",
    "Overhead Press": "Shoulders",
    "Lateral Raises": "Shoulders",
    "Tricep Pushdown": "Triceps",
    "Lunges": "Legs",
    "Leg Press": "Legs",
    "Running": "Cardio",
    "Cycling": "Cardio",
    "Burpees": "Cardio",
    "Jump Rope": "Cardio",
}

# -----------------------------
# 4. UI
# -----------------------------
st.title("🏋️ Workout Tracker Dashboard")

df = load_data()
if not df.empty:
    df["volume"] = df["reps"] * df["weight"]

# Tabs
tab1, tab2, tab3 = st.tabs(["Dashboard", "Log Workout", "Records"])

# ---- Dashboard ----
with tab1:
    st.header("📊 Dashboard")

    if not df.empty:
        # 날짜 관련 파생
        today = datetime.date.today()
        this_week = today.isocalendar()[1]
        this_month = today.month

        df["date"] = pd.to_datetime(df["date"])
        df["week"] = df["date"].dt.isocalendar().week
        df["month"] = df["date"].dt.month

        weekly_volume = df[df["week"] == this_week]["volume"].sum()
        monthly_volume = df[df["month"] == this_month]["volume"].sum()

        # 목표 예시
        goal_weekly = 10000
        progress = min(weekly_volume / goal_weekly, 1.0) * 100

        st.metric("Weekly Volume", f"{weekly_volume:.0f} kg")
        st.progress(progress/100, text=f"{progress:.1f}% of {goal_weekly}kg goal")

        # PR Tracking
        st.subheader("🏆 Personal Records")
        pr_df = df.groupby("exercise")["weight"].max().reset_index()
        st.dataframe(pr_df)

        # Category Analysis
        st.subheader("📈 Category Breakdown")
        df["category"] = df["exercise"].map(EXERCISE_CATEGORY).fillna("Other")
        cat_summary = df.groupby("category")["volume"].sum().reset_index()

        cat_chart = alt.Chart(cat_summary).mark_bar().encode(
            x="category",
            y="volume",
            tooltip=["category", "volume"]
        )
        st.altair_chart(cat_chart, use_container_width=True)

    else:
        st.info("No records yet. Log your first workout!")

# ---- Log Workout ----
with tab2:
    st.header("📝 Log a Workout")

    date = st.date_input("Date", datetime.date.today())

    all_exercises = list(EXERCISE_CATEGORY.keys())
    exercise = st.selectbox("Exercise name", [""] + all_exercises)
    if exercise == "":
        exercise = st.text_input("Or enter custom exercise")

    num_sets = st.number_input("How many sets?", min_value=1, max_value=10, step=1, value=3)

    set_data = []
    with st.form("set_form"):
        for i in range(1, num_sets+1):
            cols = st.columns(3)
            reps = cols[0].number_input(f"Set {i} - Reps", min_value=0, step=1, key=f"reps_{i}")
            weight = cols[1].number_input(f"Weight (kg)", min_value=0.0, step=2.5, key=f"weight_{i}")
            note = cols[2].text_input("Note", key=f"note_{i}")
            set_data.append((i, reps, weight, note))

        submitted = st.form_submit_button("Save Workout")

        if submitted and exercise:
            for s in set_data:
                log_set(exercise, s[0], s[1], s[2], s[3], date.isoformat())
            st.success(f"Saved {exercise} with {num_sets} sets on {date}")
            st.experimental_rerun()  # 저장 후 새로고침
        elif submitted:
            st.error("Please enter an exercise name!")

# ---- Records ----
with tab3:
    st.header("📒 Workout Records")
    if not df.empty:
        st.subheader("Recent Records (last 10)")
        st.dataframe(df.tail(10))

        st.subheader("Summary by Exercise")
        summary = df.groupby("exercise").agg(
            total_sets=("set_num", "count"),
            total_reps=("reps", "sum"),
            total_volume=("volume", "sum")
        ).reset_index()
        st.dataframe(summary)

        st.subheader("Visualization")
        chart1 = alt.Chart(summary).mark_bar().encode(
            x="exercise",
            y="total_volume",
            tooltip=["exercise", "total_volume"]
        ).properties(title="Total Training Volume by Exercise")
        st.altair_chart(chart1, use_container_width=True)

        daily = df.groupby("date")["volume"].sum().reset_index()
        chart2 = alt.Chart(daily).mark_line(point=True).encode(
            x="date:T",
            y="volume:Q",
            tooltip=["date", "volume"]
        ).properties(title="Total Training Volume Over Time")
        st.altair_chart(chart2, use_container_width=True)
    else:
        st.info("No records yet.")