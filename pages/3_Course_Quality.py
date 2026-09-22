import streamlit as st

from Scripts.data_loader import load_data
from Scripts.analysis import (
    filter_teacher_courses,
    category_course_rating,
    level_course_rating,
    category_level_rating,
    gender_level_rating
)
from Scripts.charts import (
    category_rating_chart,
    level_rating_chart,
    category_level_heatmap,
    gender_level_chart
)
from Scripts.filters import (
    expertise_filter,
    category_filter,
    level_filter
)

st.title("Course Quality")

teachers, courses, transactions, teacher_course = load_data()

col1, col2, col3 = st.columns(3)

with col1:
    selected_category = category_filter(
        courses,
        "quality_category"
    )

with col2:
    selected_level = level_filter(
        courses,
        "quality_level"
    )

with col3:
    selected_expertise = expertise_filter(
        teachers,
        "quality_expertise"
    )

data = filter_teacher_courses(
    teacher_course,
    selected_expertise,
    selected_category,
    selected_level
)

if data.empty:
    st.warning("No courses match the selected filters.")
    st.stop()

category_data = category_course_rating(data)
level_data = level_course_rating(data)
heatmap_data = category_level_rating(data)
gender_data = gender_level_rating(data)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        category_rating_chart(category_data),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        level_rating_chart(level_data),
        use_container_width=True
    )

st.plotly_chart(
    category_level_heatmap(heatmap_data),
    use_container_width=True
)

st.plotly_chart(
    gender_level_chart(gender_data),
    use_container_width=True
)