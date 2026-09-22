# EduPro Analytics

EduPro Analytics is a Streamlit dashboard for analyzing instructor performance and course quality in an online learning platform.

## Features

- **Instructor Performance**: Explore instructor ratings, age groups, experience groups, expertise distribution, and leaderboard rankings.
- **Experience & Ratings**: Analyze relationships between years of experience, instructor ratings, and course ratings with correlation insights.
- **Course Quality**: Compare average course ratings by category, level, and gender-level combinations.
- **Instructor Impact**: Evaluate how instructor performance levels relate to course quality and enrollment volume.

## Project Structure

```text
EduPro-Analytics/
├── app.py
├── requirements.txt
├── Data/
│   └── EduPro Online Platform.xlsx
├── Scripts/
│   ├── analysis.py
│   ├── charts.py
│   ├── data_loader.py
│   └── filters.py
└── pages/
    ├── 1_Instructor_Performance.py
    ├── 2_Experience_Ratings.py
    ├── 3_Course_Quality.py
    └── 4_Instructor_Impact.py
```

## Requirements

- Python 3.9+
- The dataset file at `Data/EduPro Online Platform.xlsx`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

From the repository root:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## Data Notes

The app reads three Excel sheets (`Teachers`, `Courses`, and `Transactions`) and creates derived categories for:

- Age group
- Experience group
- Performance level
