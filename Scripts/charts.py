import plotly.express as px


def rating_distribution(data):
    return px.histogram(
        data,
        x="TeacherRating",
        nbins=10,
        title="Instructor Rating Distribution",
        labels={"TeacherRating": "Teacher Rating"}
    )


def age_distribution(data):
    counts = (
        data["AgeCategory"]
        .value_counts()
        .reindex(["Young", "Adult", "Senior", "Veteran"])
        .reset_index()
    )

    counts.columns = ["AgeCategory", "Count"]

    return px.bar(
        counts,
        x="AgeCategory",
        y="Count",
        title="Instructor Age Distribution"
    )


def experience_distribution(data):
    counts = (
        data["ExperienceCategory"]
        .value_counts()
        .reindex(
            ["Beginner", "Intermediate", "Experienced", "Expert"]
        )
        .reset_index()
    )

    counts.columns = ["ExperienceCategory", "Count"]

    return px.bar(
        counts,
        x="ExperienceCategory",
        y="Count",
        title="Instructor Experience Distribution"
    )


def expertise_distribution(data):
    counts = (
        data["Expertise"]
        .value_counts()
        .sort_values(ascending=False)
        .reset_index()
    )

    counts.columns = ["Expertise", "Count"]

    return px.bar(
        counts,
        x="Count",
        y="Expertise",
        orientation="h",
        title="Instructor Expertise Distribution"
    )


def experience_teacher_scatter(data):
    return px.scatter(
        data,
        x="YearsOfExperience",
        y="TeacherRating",
        hover_data=["TeacherName", "Expertise"],
        title="Experience vs Teacher Rating",
        labels={
            "YearsOfExperience": "Years of Experience",
            "TeacherRating": "Teacher Rating"
        }
    )


def experience_course_scatter(data):
    return px.scatter(
        data,
        x="YearsOfExperience",
        y="CourseRating",
        hover_data=["TeacherName", "CourseName", "Expertise"],
        title="Experience vs Course Rating",
        labels={
            "YearsOfExperience": "Years of Experience",
            "CourseRating": "Course Rating"
        }
    )


def category_rating_chart(data):
    return px.bar(
        data,
        x="CourseCategory",
        y="CourseRating",
        title="Average Course Rating by Category",
        labels={
            "CourseCategory": "Course Category",
            "CourseRating": "Average Course Rating"
        }
    )


def level_rating_chart(data):
    return px.bar(
        data,
        x="CourseLevel",
        y="CourseRating",
        title="Average Course Rating by Level",
        labels={
            "CourseLevel": "Course Level",
            "CourseRating": "Average Course Rating"
        }
    )


def category_level_heatmap(data):
    return px.imshow(
        data,
        text_auto=".2f",
        aspect="auto",
        title="Course Rating by Category and Level",
        labels={
            "x": "Course Level",
            "y": "Course Category",
            "color": "Course Rating"
        }
    )


def gender_level_chart(data):
    return px.bar(
        data,
        x="CourseLevel",
        y="CourseRating",
        color="Gender",
        barmode="group",
        title="Course Rating by Gender and Course Level",
        labels={
            "CourseLevel": "Course Level",
            "CourseRating": "Average Course Rating"
        }
    )


def performance_course_chart(data):
    return px.bar(
        data,
        x="Performance",
        y="CourseRating",
        title="Course Rating by Instructor Performance",
        labels={
            "Performance": "Instructor Performance",
            "CourseRating": "Average Course Rating"
        }
    )


def performance_enrollment_chart(data):
    return px.bar(
        data,
        x="Performance",
        y="Enrollments",
        title="Enrollment Volume by Instructor Performance",
        labels={
            "Performance": "Instructor Performance",
            "Enrollments": "Enrollment Count"
        }
    )