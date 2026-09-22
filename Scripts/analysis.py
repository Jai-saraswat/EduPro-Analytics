import pandas as pd


def unique_teacher_courses(teacher_course):
    return teacher_course.drop_duplicates(
        subset=["TeacherID", "CourseID"]
    ).copy()


def filter_teacher_courses(
    teacher_course,
    expertise=None,
    category=None,
    level=None
):
    data = teacher_course.copy()

    if expertise:
        data = data[data["Expertise"].isin(expertise)]

    if category:
        data = data[data["CourseCategory"].isin(category)]

    if level:
        data = data[data["CourseLevel"].isin(level)]

    return data


def filter_teachers(
    teachers,
    expertise=None,
    age_category=None,
    experience_category=None,
    rating_range=None
):
    data = teachers.copy()

    if expertise:
        data = data[data["Expertise"].isin(expertise)]

    if age_category:
        data = data[data["AgeCategory"].isin(age_category)]

    if experience_category:
        data = data[
            data["ExperienceCategory"].isin(experience_category)
        ]

    if rating_range:
        data = data[
            data["TeacherRating"].between(
                rating_range[0],
                rating_range[1]
            )
        ]

    return data


def get_experience_correlations(teachers, teacher_course):
    teacher_corr = teachers[
        ["YearsOfExperience", "TeacherRating"]
    ].corr().iloc[0, 1]

    course_data = unique_teacher_courses(teacher_course)

    course_corr = course_data[
        ["YearsOfExperience", "CourseRating"]
    ].corr().iloc[0, 1]

    return teacher_corr, course_corr


def category_course_rating(data):
    return (
        unique_teacher_courses(data)
        .groupby("CourseCategory", as_index=False)["CourseRating"]
        .mean()
        .sort_values("CourseRating", ascending=False)
    )


def level_course_rating(data):
    return (
        unique_teacher_courses(data)
        .groupby("CourseLevel", as_index=False)["CourseRating"]
        .mean()
    )


def category_level_rating(data):
    return (
        unique_teacher_courses(data)
        .pivot_table(
            index="CourseCategory",
            columns="CourseLevel",
            values="CourseRating",
            aggfunc="mean"
        )
    )


def gender_level_rating(data):
    return (
        unique_teacher_courses(data)
        .groupby(["Gender", "CourseLevel"], as_index=False)["CourseRating"]
        .mean()
    )


def performance_course_rating(data):
    return (
        unique_teacher_courses(data)
        .groupby("Performance", observed=True, as_index=False)["CourseRating"]
        .mean()
    )


def performance_enrollment(data):
    return (
        data.groupby("Performance", observed=True)
        .size()
        .reset_index(name="Enrollments")
    )


def instructor_leaderboard(teachers):
    columns = [
        "TeacherID",
        "TeacherName",
        "Expertise",
        "Age",
        "YearsOfExperience",
        "TeacherRating",
        "Performance"
    ]

    return teachers[columns].sort_values(
        "TeacherRating",
        ascending=False
    )