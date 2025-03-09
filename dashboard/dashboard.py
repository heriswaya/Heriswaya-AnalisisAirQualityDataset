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
    
    st.write("### Kesimpulan:")
    st.write("Dari hasil analisis, ditemukan bahwa stasiun Gucheng dan Dongsi sering mencatatkan konsentrasi polutan yang lebih tinggi dibandingkan dengan stasiun lainnya. Kemungkinan bahwa wilayah sekitar stasiun tersebut memiliki aktivitas industri atau lalu lintas yang lebih padat. Sebaliknya, stasiun Huairou dan Dingling menunjukkan tingkat polusi yang relatif lebih rendah, yang kemungkinan disebabkan oleh kondisi lingkungan yang lebih baik atau lebih sedikit sumber polusi di sekitarnya.")

# 3️⃣ Perbandingan Polusi Berdasarkan Waktu
elif menu == "Perbandingan Polusi Berdasarkan Waktu":
    st.subheader("Perbandingan Polusi Udara pada Pagi, Siang, dan Malam")
    df['Jam'] = df['datetime'].dt.hour
    df['Waktu'] = df['Jam'].apply(lambda x: 'Pagi' if 5 <= x < 12 else ('Siang' if 12 <= x < 18 else 'Malam'))
    polutan = st.selectbox("Pilih Polutan untuk Perbandingan Waktu", ['PM2.5', 'PM10', 'CO'])
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='Waktu', y=polutan, data=df, palette='coolwarm', ax=ax)
    ax.set_title(f"Polusi {polutan} Berdasarkan Waktu")
    ax.set_xlabel("Waktu")
    ax.set_ylabel(f"Konsentrasi {polutan}")
    st.pyplot(fig)
    
    st.write("### Kesimpulan:")
    st.write("Dari hasil analisis distribusi polutan berdasarkan waktu (pagi, siang, dan malam), terlihat bahwa tidak terdapat perbedaan yang signifikan dalam distribusi polusi PM2.5, PM10, dan CO sepanjang hari. Konsentrasi polusi cenderung seragam dengan beberapa nilai outlier yang cukup tinggi. Hal ini menunjukkan bahwa faktor utama yang mempengaruhi tingkat polusi bukan hanya waktu dalam sehari, tetapi juga kondisi lingkungan lainnya seperti cuaca, kelembapan, serta intensitas aktivitas manusia dan industri.")

st.write("Sumber Data: [Dataset Kualitas Udara](https://github.com/marceloreis/HTI/tree/master)")
st.write("© Copyright by Heriswaya")
