# ----- Libraries -----
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ----- Sidebar -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.write(
        "Interactive Project to load a dataset with information about the daily temperatures of 10 cities around the world, "
        "extract some insights using Pandas and displaying them with Matplotlib."
    )
    st.write(
        "Data extracted from: https://www.kaggle.com/datasets/sudalairajkumar/daily-temperature-of-major-cities (cleaned)."
    )

# ----- Page Title -----
st.title("🌦️ Temperatures Dashboard")
st.divider()

# ----- Load Dataset -----
@st.cache_data
def load_data():
    data_path = "data/cities_temperatures.csv"
    df = pd.read_csv(data_path, index_col=0)
    df["Date"] = pd.to_datetime(df["Date"]).dt.date
    df["AvgTemperatureCelsius"] = (df["AvgTemperatureFahrenheit"] - 32) * 5 / 9
    # Remove duplicate columns if any
    df = df.loc[:, ~df.columns.duplicated()]
    return df

temps_df = load_data()

# Display the dataset
with st.expander("Check the complete dataset:"):
    st.dataframe(temps_df)

# ----- Basic Information -----
unique_cities_list = temps_df["City"].unique().tolist()
min_date = temps_df["Date"].min()
max_date = temps_df["Date"].max()

# Safely get min/max temperature rows
min_temp_row = temps_df.loc[temps_df["AvgTemperatureCelsius"] == temps_df["AvgTemperatureCelsius"].min()].iloc[0]
max_temp_row = temps_df.loc[temps_df["AvgTemperatureCelsius"] == temps_df["AvgTemperatureCelsius"].max()].iloc[0]

# Convert to Python floats for Streamlit
min_temp = float(min_temp_row["AvgTemperatureCelsius"])
min_temp_city = min_temp_row["City"]
min_temp_date = min_temp_row["Date"]

max_temp = float(max_temp_row["AvgTemperatureCelsius"])
max_temp_city = max_temp_row["City"]
max_temp_date = max_temp_row["Date"]

# ----- Display Metrics -----
st.header("Basic Information")

cols1 = st.columns([4, 1, 6])

# Cities list
cols1[0].dataframe(pd.Series(unique_cities_list, name="Cities"), width="content")

# Min temperature
cols1[2].write("#")
min_temp_text = f"""
### ☃️ Min Temperature: {min_temp:.1f}°C  
*{min_temp_city} on {min_temp_date}*
"""
cols1[2].write(min_temp_text)

# Max temperature
cols1[2].write("#")
max_temp_text = f"""
### 🏜️ Max Temperature: {max_temp:.1f}°C  
*{max_temp_city} on {max_temp_date}*
"""
cols1[2].write(max_temp_text)

# ----- Temperature Comparison -----
st.header("Comparing the Temperatures of the Cities")

selected_cities = st.multiselect(
    "Select the cities to compare:",
    unique_cities_list,
    default=["Buenos Aires", "Dakar"],
    max_selections=4
)

if selected_cities:
    start_date = st.date_input(
        "Select the start date:", pd.to_datetime("2000-01-01").date()
    )
    end_date = st.date_input(
        "Select the end date:", pd.to_datetime("2010-12-31").date()
    )

    if start_date > end_date:
        st.warning("Start date is after end date. Swapping automatically.")
        start_date, end_date = end_date, start_date

    # ----- Line plot -----
    fig, ax = plt.subplots(figsize=(10, 5))

    for city in selected_cities:
        city_df = temps_df[temps_df["City"] == city]
        city_df_period = city_df[
            (city_df["Date"] >= start_date) &
            (city_df["Date"] <= end_date)
        ]
        ax.plot(
            city_df_period["Date"],
            city_df_period["AvgTemperatureCelsius"],
            label=city
        )

    ax.set_title("Temperature Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Avg Temperature (°C)")
    ax.legend()
    fig.autofmt_xdate()
    st.pyplot(fig)

    # ----- Histogram -----
    fig2, ax2 = plt.subplots(figsize=(10, 5))

    for city in selected_cities:
        city_df = temps_df[temps_df["City"] == city]
        city_df_period = city_df[
            (city_df["Date"] >= start_date) &
            (city_df["Date"] <= end_date)
        ]
        ax2.hist(
            city_df_period["AvgTemperatureCelsius"],
            bins=20,
            alpha=0.5,
            label=city
        )

    ax2.set_title("Temperature Distribution")
    ax2.set_xlabel("Avg Temperature (°C)")
    ax2.set_ylabel("Frequency")
    ax2.legend()
    st.pyplot(fig2)
