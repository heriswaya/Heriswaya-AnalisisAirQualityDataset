# Dashboard Analisis Data Kualitas Udara

## 📌 Deskripsi
Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data kualitas udara berdasarkan berbagai parameter seperti PM2.5, PM10, NO2, SO2, CO, dan O3. Dashboard ini menyediakan tiga jenis analisis utama:

1. **Tren Polusi Udara** - Menampilkan tren polusi udara dari waktu ke waktu.
2. **Stasiun dengan Polusi Tertinggi/Terendah** - Membandingkan rata-rata polusi di berbagai stasiun pemantauan.
3. **Perbandingan Polusi Berdasarkan Waktu** - Menganalisis polusi berdasarkan waktu dalam sehari (Pagi, Siang, Malam).

---

## 📂 Struktur Proyek
```
📁 heriswaya-analisisairqualitydataset/
 ├── 📁 dashboard/
 │   ├── dashboard.py
 │   └── merged_air_quality.csv
 ├── 📁 data/
 │   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
 │   ├── PRSA_Data_Changping_20130301-20170228.csv
 │   ├── PRSA_Data_Dingling_20130301-20170228.csv
 │   ├── PRSA_Data_Dongsi_20130301-20170228.csv
 │   ├── PRSA_Data_Guanyuan_20130301-20170228.csv
 │   ├── PRSA_Data_Gucheng_20130301-20170228.csv
 │   ├── PRSA_Data_Huairou_20130301-20170228.csv
 │   ├── PRSA_Data_Nongzhanguan_20130301-20170228.csv
 │   ├── PRSA_Data_Shunyi_20130301-20170228.csv
 │   ├── PRSA_Data_Tiantan_20130301-20170228.csv
 │   ├── PRSA_Data_Wanliu_20130301-20170228.csv
 │   └── PRSA_Data_Wanshouxigong_20130301-20170228.csv
 ├── 📄 requirements.txt
 ├── 📄 Proyek_Analisis_Data.ipynb
 ├── 📄 url.txt
 └── 📄 README.md  👈 (Dokumen ini)
```

---

## 🚀 Cara Menjalankan Dashboard (Jika menggunakan VS Code)
Pastikan kamu telah menginstal **Python 3.8+** dan **pip**. Ikuti langkah-langkah berikut:

1. **Clone repository ini** (jika belum ada):
   ```bash
   git clone https://github.com/username/heriswaya-analisisairqualitydataset.git
   cd heriswaya-analisisairqualitydataset/dashboard
   ```

2. **Buat virtual environment (opsional tetapi disarankan)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk macOS/Linux
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit**:
   ```bash
   streamlit run dashboard.py
   ```

Setelah menjalankan perintah di atas, buka browser dan akses **http://localhost:----/** untuk melihat dashboard.

---

## 📊 Dataset
Dataset yang digunakan dalam analisis ini adalah `merged_air_quality.csv`, yang memiliki kolom berikut:
- `year`, `month`, `day`, `hour` → Informasi waktu pengukuran.
- `PM2.5`, `PM10`, `SO2`, `NO2`, `CO`, `O3` → Konsentrasi polutan udara.
- `TEMP`, `PRES`, `DEWP`, `RAIN`, `wd`, `WSPM` → Data cuaca.
- `station` → Lokasi stasiun pemantauan.

---

## 🛠 Deployment di Streamlit Cloud
Untuk meng-host aplikasi ini di **Streamlit Cloud**, ikuti langkah berikut:

1. **Upload proyek ke GitHub** (pastikan `dashboard.py`, `requirements.txt`, dan dataset sudah ada).
2. **Buka Streamlit Cloud** → [https://share.streamlit.io](https://share.streamlit.io)
3. **Buat aplikasi baru** dan masukkan link repository GitHub kamu.
4. **Tentukan file utama**: `dashboard/dashboard.py`
5. **Tunggu proses build selesai**, lalu aplikasi siap digunakan! 🎉

---

## 📜 Lisensi
Proyek ini dibuat untuk tujuan edukasi dan dapat digunakan serta dimodifikasi sesuai kebutuhan.

---

## ✨ Kontributor
- **Heriswaya** - [GitHub](https://github.com/heriswaya)

Jika ada saran atau pertanyaan, silakan buat **issue** atau **pull request** di repository ini! 🚀

