# Bike Sharing ✨

## Project Overview

Project ini bertujuan untuk menganalisis pola penggunaan layanan bike sharing berdasarkan faktor cuaca, waktu, serta tipe pengguna (casual vs registered) pada periode tahun 2011–2012.

Dashboard interaktif dibuat menggunakan **Streamlit** untuk mempermudah eksplorasi data dan pengambilan insight secara visual.

---

## Business Questions

1. Bagaimana pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda?
2. Pada jam berapa dan hari apa permintaan penyewaan sepeda paling tinggi?
3. Apakah terdapat perbedaan pola penggunaan antara casual users dan registered users?

---

## Key Insights

* Penyewaan sepeda tertinggi terjadi pada kondisi cuaca cerah dan menurun pada cuaca buruk.
* Terdapat pola jam sibuk yang berbeda antara working day dan weekend.
* Registered users mendominasi penggunaan sepeda dengan pola yang lebih stabil dibanding casual users.

---

## Project Structure

```
submission
├── dashboard
│   ├── main_data.csv
│   └── dashboard.py
├── data
│   ├── data_1.csv
│   └── data_2.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Setup Environment

### Anaconda

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Shell / Terminal

```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## Run Streamlit App

Pastikan berada di folder `dashboard`, lalu jalankan:

```
streamlit run dashboard.py
```

Dashboard akan terbuka di browser secara otomatis.

---

## 🧠 Tools & Libraries

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit

