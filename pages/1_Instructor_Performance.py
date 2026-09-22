import streamlit as st

from Scripts.data_loader import load_data
from Scripts.analysis import filter_teachers, instructor_leaderboard
from Scripts.charts import (
    rating_distribution,
    age_distribution,
    experience_distribution,
    expertise_distribution
)
from Scripts.filters import (
    expertise_filter,
    age_filter,
    experience_filter,
    rating_filter
)

st.title("Instructor Performance")

teachers, courses, transactions, teacher_course = load_data()

col1, col2 = st.columns(2)

with col1:
    selected_expertise = expertise_filter(
        teachers,
        "performance_expertise"
    )

    selected_age = age_filter(
        teachers,
        "performance_age"
    )

with col2:
    selected_experience = experience_filter(
        teachers,
        "performance_experience"
    )

    selected_rating = rating_filter(
        "performance_rating"
    )

data = filter_teachers(
    teachers,
    selected_expertise,
    selected_age,
    selected_experience,
    selected_rating
)

if data.empty:
    st.warning("No instructors match the selected filters.")
    st.stop()

st.subheader("Instructor Rating Distribution")
st.plotly_chart(
    rating_distribution(data),
    use_container_width=True
)

st.subheader("Instructor Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(
        age_distribution(data),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        experience_distribution(data),
        use_container_width=True
    )

with col3:
    st.plotly_chart(
        expertise_distribution(data),
        use_container_width=True
    )

st.subheader("Instructor Performance Leaderboard")

leaderboard = instructor_leaderboard(data)

st.dataframe(
    leaderboard,
    use_container_width=True,
    hide_index=True
)