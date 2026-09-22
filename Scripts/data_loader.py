from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "Data" / "EduPro Online Platform.xlsx"


@st.cache_data
def load_data():
    teachers = pd.read_excel(DATA_PATH, sheet_name="Teachers")
    courses = pd.read_excel(DATA_PATH, sheet_name="Courses")
    transactions = pd.read_excel(DATA_PATH, sheet_name="Transactions")

    teachers["AgeCategory"] = pd.cut(
        teachers["Age"],
        bins=[0, 25, 35, 50, float("inf")],
        labels=["Young", "Adult", "Senior", "Veteran"],
        include_lowest=True
    )

    teachers["ExperienceCategory"] = pd.cut(
        teachers["YearsOfExperience"],
        bins=[-1, 2, 5, 10, float("inf")],
        labels=["Beginner", "Intermediate", "Experienced", "Expert"]
    )

    teachers["Performance"] = pd.cut(
        teachers["TeacherRating"],
        bins=[0, 3, 4, 5],
        labels=["Low Performing", "Average Performing", "Top Performing"],
        include_lowest=True
    )

    teacher_course = transactions.merge(
        courses[[
            "CourseID",
            "CourseName",
            "CourseCategory",
            "CourseType",
            "CourseLevel",
            "CoursePrice",
            "CourseDuration",
            "CourseRating"
        ]],
        on="CourseID",
        how="left"
    )

    teacher_course = teacher_course.merge(
        teachers[[
            "TeacherID",
            "TeacherName",
            "Age",
            "Gender",
            "Expertise",
            "YearsOfExperience",
            "TeacherRating",
            "AgeCategory",
            "ExperienceCategory",
            "Performance"
        ]],
        on="TeacherID",
        how="left"
    )

    return teachers, courses, transactions, teacher_course