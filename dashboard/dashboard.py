import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "merged_air_quality.csv")
    return pd.read_csv(file_path)

df = load_data()

# Buat kolom datetime dari year, month, day, dan hour
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

# Ambil tahun dari kolom datetime
df['Tahun'] = df['datetime'].dt.year

# Manual Grouping berdasarkan Binning
bins = [0, 9, 14, 18, 23]  # Rentang jam
labels = ["Pagi", "Siang", "Sore", "Malam"]  # Label waktu
df['Waktu'] = pd.cut(df['datetime'].dt.hour, bins=bins, labels=labels, right=True)

# Title
st.title("Dashboard Analisis Data Kualitas Udara")

# Sidebar untuk memilih analisis
menu = st.sidebar.selectbox("Pilih Analisis", [
    "Tren Polusi Udara", "Stasiun dengan Polusi Tertinggi/Terendah", "Perbandingan Polusi Berdasarkan Waktu"
])

# 1️⃣ Analisis Tren Polusi Udara
if menu == "Tren Polusi Udara":
    st.subheader("Tren Polusi Udara dari Waktu ke Waktu")
    polutan = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3']
    fig, axes = plt.subplots(len(polutan), 1, figsize=(10, 30), constrained_layout=True)
    for i, pol in enumerate(polutan):
        df_grouped = df.groupby('Tahun')[pol].mean()
        axes[i].plot(df_grouped.index, df_grouped.values, marker='o', linestyle='-', color='b')
        axes[i].set_title(f"Tren Rata-rata {pol} per Tahun")
        axes[i].set_xlabel("Tahun")
        axes[i].set_ylabel("Konsentrasi")
    st.pyplot(fig)
    
    st.write("### Kesimpulan:")
    st.write("Tren tahunan menunjukkan adanya fluktuasi dalam konsentrasi polutan udara. Sebagian besar polutan seperti PM2.5, PM10, NO2, SO2, CO, dan O3 mengalami penurunan sekitar tahun 2014 hingga 2016, namun kemudian menunjukkan peningkatan kembali pada tahun 2017. Ini menunjukkan adanya faktor-faktor eksternal yang mempengaruhi tingkat polusi udara, mungkin saja adanya peningkatan aktivitas industri dan transportasi.")

# 2️⃣ Stasiun dengan Polusi Tertinggi/Terendah
elif menu == "Stasiun dengan Polusi Tertinggi/Terendah":
    st.subheader("Stasiun dengan Polusi Udara Tertinggi dan Terendah")
    # Pilih polutan
    polutan = st.selectbox("Pilih Polutan", ['PM2.5', 'PM10', 'CO'])
    
    # Data stasiun tertinggi & terendah
    df_station = df.groupby('station')[polutan].mean().reset_index()
    top_station = df_station.nlargest(5, polutan)
    bottom_station = df_station.nsmallest(5, polutan)

    # Tampilkan tabel
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Stasiun dengan Polusi Tertinggi")
        st.write(top_station)
    with col2:
        st.write("### Stasiun dengan Polusi Terendah")
        st.write(bottom_station)

    # **Visualisasi Barplot Stasiun dengan Polusi Sesuai Pilihan**
    fig, ax = plt.subplots(figsize=(10, 5))
    station_avg = df.groupby('station')[polutan].mean().sort_values()
    sns.barplot(x=station_avg.index, y=station_avg.values, hue=station_avg.index, palette="coolwarm", ax=ax, legend=False)
    
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_xlabel('Stasiun')
    ax.set_ylabel(f'Rata-rata {polutan}')
    ax.set_title(f'Rata-rata {polutan} di Setiap Stasiun')

    st.pyplot(fig)

    st.write("### Kesimpulan:")
    st.write(
        "Dari hasil analisis, ditemukan bahwa beberapa stasiun memiliki tingkat polusi yang jauh lebih tinggi dibandingkan yang lain. "
        "Hal ini bisa disebabkan oleh faktor lokasi, tingkat lalu lintas, aktivitas industri, atau kondisi geografis. "
        "Sementara itu, beberapa stasiun memiliki kualitas udara yang lebih baik, mungkin karena lokasinya lebih jauh dari sumber polusi utama."
    )

# 3️⃣ Perbandingan Polusi Berdasarkan Waktu
elif menu == "Perbandingan Polusi Berdasarkan Waktu":
    st.subheader("Perbandingan Polusi Udara Berdasarkan Waktu")
    polutan = st.selectbox("Pilih Polutan untuk Analisis", ['PM2.5', 'PM10', 'CO'])

    # 📌 **Boxplot untuk Distribusi Polusi**
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='Waktu', y=polutan, data=df, palette='coolwarm', ax=ax)
    ax.set_title(f"Distribusi {polutan} Berdasarkan Waktu")
    ax.set_xlabel("Waktu")
    ax.set_ylabel(f"Konsentrasi {polutan}")
    st.pyplot(fig)

    # 📌 **Heatmap untuk Visualisasi Polusi Berdasarkan Stasiun dan Waktu**
    df_grouped = df.groupby(["station", "Waktu"])[polutan].mean().reset_index()
    df_pivot = df_grouped.pivot(index="station", columns="Waktu", values=polutan)

    plt.figure(figsize=(12, 6))
    sns.heatmap(df_pivot, cmap="coolwarm", annot=True, fmt=".1f", linewidths=0.5)
    plt.title(f"Heatmap Rata-rata {polutan} Berdasarkan Stasiun dan Waktu")
    plt.xlabel("Waktu")
    plt.ylabel("Stasiun")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # **Kesimpulan**
    st.write("### Kesimpulan:")
    st.write(
        f"Dari hasil analisis distribusi polutan {polutan} berdasarkan waktu (Pagi, Siang, Sore, dan Malam), terlihat adanya pola tertentu dalam tingkat polusi. "
        "Distribusi polusi bervariasi antar waktu, dengan kemungkinan peningkatan polusi di waktu tertentu akibat aktivitas manusia dan kondisi atmosfer."
    )

st.write("Sumber Data: [Dataset Kualitas Udara](https://github.com/marceloreis/HTI/tree/master)")
st.write("© Copyright by Heriswaya")
