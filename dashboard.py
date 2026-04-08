import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

df = pd.read_csv("main_data.csv")
df['date'] = pd.to_datetime(df['date'])

weather_map = {
    1: "Clear",
    2: "Mist / Cloudy",
    3: "Light Rain / Snow",
    4: "Heavy Rain / Storm"
}

season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

weekday_map = {
    0: "Sunday", 1: "Monday", 2: "Tuesday",
    3: "Wednesday", 4: "Thursday",
    5: "Friday", 6: "Saturday"
}

df['weather_label'] = df['weather'].map(weather_map)
df['season_label'] = df['season'].map(season_map)
df['weekday_label'] = df['weekday'].map(weekday_map)

day_df = df[df['data_type'] == 'day']
hour_df = df[df['data_type'] == 'hour']

min_date = df['date'].min()
max_date = df['date'].max()

with st.sidebar:
    st.header("📊 Filter Data")

    start_date, end_date = st.date_input(
        "Pilih Rentang Waktu",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    weather_options = ["Clear", "Mist / Cloudy", "Light Rain / Snow", "Heavy Rain / Storm"]
    selected_weather = st.multiselect("Pilih Cuaca", weather_options, default=weather_options)

    season_options = ["Spring", "Summer", "Fall", "Winter"]
    selected_season = st.multiselect("Pilih Season", season_options, default=season_options)

day_filtered = day_df[
    (day_df['date'] >= pd.to_datetime(start_date)) &
    (day_df['date'] <= pd.to_datetime(end_date)) &
    (day_df['weather_label'].isin(selected_weather)) &
    (day_df['season_label'].isin(selected_season))
]

hour_filtered = hour_df[
    (hour_df['date'] >= pd.to_datetime(start_date)) &
    (hour_df['date'] <= pd.to_datetime(end_date)) &
    (hour_df['weather_label'].isin(selected_weather)) &
    (hour_df['season_label'].isin(selected_season))
]

st.title("🚲 Bike Sharing Dashboard")
st.caption("Analisis penggunaan sepeda 2011–2012")

col1, col2, col3 = st.columns(3)

col1.metric("Total Rentals", int(day_filtered['total_count'].sum()))
col2.metric("Rata-rata Harian", int(day_filtered['total_count'].mean()))
col3.metric("Max Rentals", int(day_filtered['total_count'].max()))

# ========================
# HANDLE DATA KOSONG
# ========================
if day_filtered.empty or hour_filtered.empty:
    st.warning("Data tidak tersedia untuk filter yang dipilih ⚠️")
    st.stop()

st.header("1. Pengaruh Cuaca terhadap Penyewaan")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.scatter(day_filtered['temp'], day_filtered['total_count'])
    ax.set_title("Temperature vs Total Rentals")
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Total Rentals")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    ax.scatter(day_filtered['humidity'], day_filtered['total_count'])
    ax.set_title("Humidity vs Total Rentals")
    ax.set_xlabel("Humidity")
    ax.set_ylabel("Total Rentals")
    st.pyplot(fig)

fig, ax = plt.subplots()
avg_weather = day_filtered.groupby('weather_label')['total_count'].mean().reindex(weather_options)
avg_weather.plot(kind='bar', ax=ax)
ax.set_title("Average Rentals by Weather")
st.pyplot(fig)

st.header("2. Pola Jam & Hari")

hour_pattern = hour_filtered.groupby(['hour', 'workingday'])['total_count'].mean().unstack()

fig, ax = plt.subplots()
hour_pattern.plot(ax=ax)
ax.set_title("Hourly Pattern (Workingday vs Weekend)")
st.pyplot(fig)

order_day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

fig, ax = plt.subplots()
avg_weekday = hour_filtered.groupby('weekday_label')['total_count'].mean().reindex(order_day)
avg_weekday.plot(kind='bar', ax=ax)
ax.set_title("Average Rentals by Weekday")
st.pyplot(fig)

st.header("3. Casual vs Registered Users")

user_hour = hour_filtered.groupby('hour')[['casual', 'registered']].mean()

fig, ax = plt.subplots()
user_hour.plot(ax=ax)
ax.set_title("Casual vs Registered per Hour")
st.pyplot(fig)

user_season = day_filtered.groupby('season_label')[['casual', 'registered']].mean().reindex(season_options)

fig, ax = plt.subplots()
user_season.plot(kind='bar', ax=ax)
ax.set_title("Casual vs Registered per Season")
st.pyplot(fig)

