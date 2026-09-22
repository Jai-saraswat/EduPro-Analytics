import streamlit as st


def expertise_filter(teachers, key="expertise"):
    options = sorted(teachers["Expertise"].dropna().unique())

    return st.multiselect(
        "Instructor Expertise",
        options,
        key=key
    )


def category_filter(courses, key="category"):
    options = sorted(courses["CourseCategory"].dropna().unique())

    return st.multiselect(
        "Course Category",
        options,
        key=key
    )


def level_filter(courses, key="level"):
    options = sorted(courses["CourseLevel"].dropna().unique())

    return st.multiselect(
        "Course Level",
        options,
        key=key
    )


def age_filter(teachers, key="age"):
    options = [
        x for x in teachers["AgeCategory"].dropna().unique()
    ]

    return st.multiselect(
        "Age Group",
        options,
        key=key
    )


def experience_filter(teachers, key="experience"):
    options = [
        x for x in teachers["ExperienceCategory"].dropna().unique()
    ]

    return st.multiselect(
        "Experience Group",
        options,
        key=key
    )


def rating_filter(key="rating"):
    return st.slider(
        "Teacher Rating Range",
        min_value=1.0,
        max_value=5.0,
        value=(1.0, 5.0),
        step=0.1,
        key=key
    )