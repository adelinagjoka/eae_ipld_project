# Data Apps with Python & Streamlit

![Python](https://img.shields.io/badge/Python-3.11+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-app-red) ![Pandas](https://img.shields.io/badge/Pandas-data-150458)

A multi-page web application built with Python and Streamlit that brings together three small data projects: image processing, exploratory data analysis, and an interactive dashboard.

Final project for the course **Introduction to Programming Languages for Data**, part of the **Master in Big Data & Analytics** at EAE Business School, Barcelona (2025–2026).

🔗 **Live app:** [adelinagjoka94.streamlit.app](https://adelinagjoka94.streamlit.app/)

![App overview](ipld_project_overview.png)

---

## What's inside

The app has a home page with a short profile and three project pages, each first developed in a Jupyter Notebook and then turned into an interactive web page.

### 1. Image Cropper
Loads an image as a NumPy array and crops it by slicing pixel ranges, showing how images are stored and manipulated as numerical data.

### 2. Netflix Data Analysis
Exploratory analysis of the Netflix titles dataset (adapted from Kaggle):
- **Key metrics:** earliest and latest release years, titles with a missing director, number of unique countries, and average title length.
- **Top 10 producing countries** for a year chosen by the user (interactive pie chart).
- **Average movie duration over the years**, after cleaning duration text such as "90 min" into numbers (line chart).

### 3. Temperatures Dashboard
Interactive dashboard of daily average temperatures for 10 major cities worldwide (2000–2010, adapted from Kaggle):
- Select up to **4 cities** and a **date range** to compare.
- **Line chart** of temperature trends and **histogram** of the temperature distribution.
- Record **minimum and maximum** temperatures across the dataset.

---

## Skills demonstrated

- **Data cleaning and transformation** with Pandas (missing values, text-to-number conversion, filtering, grouping)
- **Numerical computing** with NumPy (array slicing for image processing)
- **Data visualization** with Matplotlib
- **Interactive web apps** with Streamlit (widgets, multi-page layout)
- **From notebook to product:** prototyping logic in Jupyter, then turning it into a deployed app
- **Version control** with Git and GitHub

## Tech stack

Python · Pandas · NumPy · Matplotlib · Streamlit · Jupyter · Git

---

## Project structure

```
eae_ipld_project/
├── home.py                 # home page of the app
├── pages/                  # the three project pages
│   ├── 01_image_cropper.py
│   ├── 02_netflix_data_analysis.py
│   └── 03_temperatures_dashboard.py
├── development/            # Jupyter notebooks where the logic was built
├── data/                   # datasets
└── requirements.txt
```

## How to run it locally

```bash
git clone https://github.com/adelinagjoka/eae_ipld_project.git
cd eae_ipld_project
python -m venv venv
venv\Scripts\activate          # Windows  (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
streamlit run home.py
```

The app opens in your browser at `http://localhost:8501`.

---

## Credits

Project template and course by [Enric Domingo](https://github.com/enricd). The analysis, notebooks and app pages were completed by me as part of the course.

## Author

**Adelina Gjoka**: Data Analyst | BI, Data Governance & AI Automation | Insurance & Banking

[LinkedIn](https://www.linkedin.com/in/adelina-gjoka11) · [GitHub](https://github.com/adelinagjoka)
