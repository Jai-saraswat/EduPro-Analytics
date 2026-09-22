import streamlit as st

from Scripts.data_loader import load_data
from Scripts.analysis import (
    filter_teacher_courses,
    performance_course_rating,
    performance_enrollment
)
from Scripts.charts import (
    performance_course_chart,
    performance_enrollment_chart
)
from Scripts.filters import (
    expertise_filter,
    category_filter,
    level_filter
)

st.title("Instructor Impact")

teachers, courses, transactions, teacher_course = load_data()

col1, col2, col3 = st.columns(3)

with col1:
    selected_expertise = expertise_filter(
        teachers,
        "impact_expertise"
    )

with col2:
    selected_category = category_filter(
        courses,
        "impact_category"
    )

with col3:
    selected_level = level_filter(
        courses,
        "impact_level"
    )

data = filter_teacher_courses(
    teacher_course,
    selected_expertise,
    selected_category,
    selected_level
)

if data.empty:
    st.warning("No records match the selected filters.")
    st.stop()

course_rating_data = performance_course_rating(data)
enrollment_data = performance_enrollment(data)

st.subheader("Instructor Performance vs Course Quality")

st.plotly_chart(
    performance_course_chart(course_rating_data),
    use_container_width=True
)

st.subheader("Instructor Performance vs Enrollment")

st.plotly_chart(
    performance_enrollment_chart(enrollment_data),
    use_container_width=True
)

st.caption(
    "Enrollment volume is measured using transaction records. "
    "Course ratings are calculated from unique instructor-course relationships."
)