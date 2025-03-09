import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("merged_air_quality.csv")

df = load_data()

# Title
st.title("Dashboard Analisis Data Kualitas Udara")

# Sidebar untuk memilih analisis
menu = st.sidebar.selectbox("Pilih Analisis", [
    "Tren Polusi Udara", "Stasiun dengan Polusi Tertinggi/Terendah", "Perbandingan Polusi Berdasarkan Waktu"
])

# 1️⃣ Analisis Tren Polusi Udara
df['Tahun'] = pd.to_datetime(df['date']).dt.year
if menu == "Tren Polusi Udara":
    st.subheader("Tren Polusi Udara dari Waktu ke Waktu")
    polutan = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    fig, axes = plt.subplots(len(polutan), 1, figsize=(10, 20))
    for i, pol in enumerate(polutan):
        df_grouped = df.groupby('Tahun')[pol].mean()
        axes[i].plot(df_grouped.index, df_grouped.values, marker='o', linestyle='-', color='b')
        axes[i].set_title(f"Tren Rata-rata {pol} per Tahun")
        axes[i].set_xlabel("Tahun")
        axes[i].set_ylabel("Konsentrasi")
    st.pyplot(fig)

# 2️⃣ Stasiun dengan Polusi Tertinggi/Terendah
elif menu == "Stasiun dengan Polusi Tertinggi/Terendah":
    st.subheader("Stasiun dengan Polusi Udara Tertinggi dan Terendah")
    polutan = st.selectbox("Pilih Polutan", ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])
    df_station = df.groupby('station')[polutan].mean().reset_index()
    top_station = df_station.nlargest(5, polutan)
    bottom_station = df_station.nsmallest(5, polutan)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Stasiun dengan Polusi Tertinggi")
        st.write(top_station)
    with col2:
        st.write("### Stasiun dengan Polusi Terendah")
        st.write(bottom_station)

# 3️⃣ Perbandingan Polusi Berdasarkan Waktu
elif menu == "Perbandingan Polusi Berdasarkan Waktu":
    st.subheader("Perbandingan Polusi Udara pada Pagi, Siang, dan Malam")
    df['Jam'] = pd.to_datetime(df['date']).dt.hour
    df['Waktu'] = df['Jam'].apply(lambda x: 'Pagi' if 5 <= x < 12 else ('Siang' if 12 <= x < 18 else 'Malam'))
    polutan = st.selectbox("Pilih Polutan untuk Perbandingan Waktu", ['PM2.5', 'PM10', 'CO'])
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='Waktu', y=polutan, data=df, palette='coolwarm', ax=ax)
    ax.set_title(f"Polusi {polutan} Berdasarkan Waktu")
    ax.set_xlabel("Waktu")
    ax.set_ylabel(f"Konsentrasi {polutan}")
    st.pyplot(fig)

st.write("Sumber Data: Dataset Kualitas Udara")

