import streamlit as st

from Scripts.data_loader import load_data
from Scripts.analysis import (
    filter_teacher_courses,
    unique_teacher_courses
)
from Scripts.charts import (
    experience_teacher_scatter,
    experience_course_scatter
)
from Scripts.filters import (
    expertise_filter,
    category_filter,
    level_filter
)

st.title("Experience & Ratings")

teachers, courses, transactions, teacher_course = load_data()

col1, col2, col3 = st.columns(3)

with col1:
    selected_expertise = expertise_filter(
        teachers,
        "experience_expertise"
    )

with col2:
    selected_category = category_filter(
        courses,
        "experience_category"
    )

with col3:
    selected_level = level_filter(
        courses,
        "experience_level"
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

course_data = unique_teacher_courses(data)

teacher_ids = course_data["TeacherID"].unique()

teacher_data = teachers[
    teachers["TeacherID"].isin(teacher_ids)
]

teacher_corr = teacher_data[
    ["YearsOfExperience", "TeacherRating"]
].corr().iloc[0, 1]

course_corr = course_data[
    ["YearsOfExperience", "CourseRating"]
].corr().iloc[0, 1]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Experience ↔ Teacher Rating",
        f"{teacher_corr:.3f}"
    )
    st.caption(f"Sample size: {len(teacher_data)} instructors")

with col2:
    st.metric(
        "Experience ↔ Course Rating",
        f"{course_corr:.3f}"
    )
    st.caption(f"Sample size: {len(course_data)} instructor-course pairs")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        experience_teacher_scatter(teacher_data),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        experience_course_scatter(course_data),
        use_container_width=True
    )

if abs(teacher_corr) < 0.1:
    teacher_text = "There is essentially no linear relationship between experience and teacher rating."
elif teacher_corr > 0:
    teacher_text = "More teaching experience is associated with higher teacher ratings."
else:
    teacher_text = "More teaching experience is associated with lower teacher ratings."

if abs(course_corr) < 0.1:
    course_text = "There is essentially no linear relationship between experience and course rating."
elif course_corr > 0:
    course_text = "More teaching experience is associated with higher course ratings."
else:
    course_text = "More teaching experience is associated with lower course ratings."

st.subheader("Interpretation")

st.write(teacher_text)
st.write(course_text)
st.caption(
    "Correlation measures association, not causation."
)