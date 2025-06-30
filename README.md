# SmartScore - Prediksi Nilai Ujian dengan Machine Learning🎓

## Deskripsi Proyek

Proyek ini adalah aplikasi web interaktif berbasis Streamlit yang dirancang untuk memprediksi nilai ujian akhir siswa dengan menganalisis lebih dari 15 variabel penting, seperti:

- Jam belajar  
- Pola tidur  
- Penggunaan media sosial  
- Kualitas diet  
- Kesehatan mental  
- dan faktor kebiasaan lainnya

Aplikasi ini memanfaatkan algoritma **machine learning** — termasuk **Linear Regression**, **Lasso**, dan **Ridge Regression** untuk memberikan prediksi nilai akhir sekaligus mengungkap faktor-faktor kebiasaan yang paling memengaruhi performa akademik siswa.

> 🔍 *Apa sebenarnya yang membuat nilai ujian seorang siswa rendah meski sudah belajar keras?*  
> Atau sebaliknya — *mengapa ada siswa yang tampak santai tapi justru mendapat nilai tinggi?*

Aplikasi ini hadir untuk menjawab pertanyaan-pertanyaan tersebut melalui pendekatan berbasis data. Cocok digunakan oleh:

- **Siswa**, untuk mengevaluasi kebiasaan belajarnya  
- **Guru**, untuk memahami pola belajar siswa secara lebih mendalam  
- **Orang tua**, untuk mendukung perkembangan akademik anak secara lebih strategis


## Struktur Repositori
```
academic-performance-prediction/
├── .streamlit/
│ └── config.toml # Konfigurasi tema dan layout untuk Streamlit
├── data/
│ ├── external/ # Data mentah dari sumber eksternal (belum diproses)
│ └── processed/ # Data yang telah dibersihkan dan siap digunakan untuk modeling
├── models/
│ ├── column_scaler.pkl # Objek scaler untuk normalisasi/standardisasi fitur
│ ├── feature_columns.pkl # Daftar kolom fitur yang digunakan dalam model
│ ├── lasso_model.pkl # Model Lasso Regression yang telah dilatih
│ ├── linear_model.pkl # Model Linear Regression yang telah dilatih
│ └── ridge_model.pkl # Model Ridge Regression yang telah dilatih
├── notebooks/
│ ├── 01_exploratory_analysis.ipynb # Notebook untuk eksplorasi awal data
│ └── 02_model_experimentation.ipynb # Notebook untuk eksperimen dan evaluasi model
├── app.py # Kode utama untuk menjalankan aplikasi Streamlit
├── requirements.txt # Daftar dependensi Python yang dibutuhkan
└── README.md # Dokumentasi proyek (file ini)
```
## Cara Menjalankan Proyek
Ikuti langkah-langkah di bawah ini untuk mengatur lingkungan dan menjalankan aplikasi di mesin lokal.

1. Kloning Repositori
Buka terminal atau Git Bash Anda dan jalankan perintah berikut:
```
git clone https://github.com/NamaPenggunaAnda/nama-repositori-anda.git
cd nama-repositori-anda
```
2. Buat dan Aktifkan Lingkungan Virtual (Direkomendasikan)

```
python -m venv venv
```
3. Instal Dependensi
Setelah lingkungan virtual aktif, instal semua pustaka Python yang diperlukan dari ```requirements.txt```:
```
pip install -r requirements.txt
```
4. Jalankan Aplikasi Streamlit
```
streamlit run app.py
```

## Dataset

Dataset ini adalah kumpulan data simulasi yang dirancang untuk meneliti hubungan antara kebiasaan hidup sehari-hari dengan prestasi akademik mahasiswa. 
Dataset berisi 1.000 catatan mahasiswa sintetis dengan lebih dari 15 variabel yang mencakup jam belajar, pola tidur, penggunaan media sosial, kualitas diet, kesehatan mental, dan nilai ujian akhir. 
Data ini dibuat menggunakan pola yang realistis namun sepenuhnya artifisial untuk tujuan edukasi dan latihan. Dataset sangat cocok digunakan untuk berbagai proyek analisis data seperti machine learning (terutama untuk prediksi nilai), 
analisis regresi (mencari korelasi antar variabel), clustering (pengelompokan mahasiswa berdasarkan pola kebiasaan), dan visualisasi data. 

#### 🧾 Deskripsi Fitur Dataset

| Feature Name                      | Data Type   | Description                                            | Encoding Info                                              |
|----------------------------------|-------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| `student_id`                     | object      | ID unik untuk setiap siswa                                                  | -                                                           |
| `age`                            | int64       | Usia siswa                                                                  | -                                                           |
| `gender`                         | object      | Jenis kelamin siswa                                                         | Perempuan → `0`, Laki-laki → `1`                            |
| `study_hours_per_day`           | float64     | Rata-rata jam belajar siswa per hari                                        | -                                                           |
| `social_media_hours`            | float64     | Jumlah jam per hari menggunakan media sosial                                | -                                                           |
| `netflix_hours`                 | float64     | Jumlah jam per hari menonton Netflix atau platform streaming lainnya        | -                                                           |
| `part_time_job`                 | object      | Status siswa memiliki pekerjaan paruh waktu atau tidak                      | Ya → `0`, Tidak → `1`                                       |
| `attendance_percentage`         | float64     | Persentase kehadiran kelas (0–100%)                                         | -                                                           |
| `sleep_hours`                   | float64     | Rata-rata jam tidur siswa per hari                                          | -                                                           |
| `diet_quality`                  | object      | Kualitas pola makan harian siswa                                            | Buruk → `0`, Cukup → `1`, Baik → `2`                        |
| `exercise_frequency`            | int64       | Jumlah hari dalam seminggu siswa berolahraga                                | -                                                           |
| `parental_education_level`      | object      | Tingkat pendidikan tertinggi orang tua siswa                                | Tidak Diketahui → `-1`, SMA → `0`, S1 → `1`, S2 → `2`       |
| `internet_quality`              | object      | Kualitas koneksi internet yang digunakan siswa                              | Buruk → `0`, Cukup → `1`, Baik → `2`                        |
| `mental_health_rating`          | int64       | Penilaian kesehatan mental siswa (skala 1–10)                               | -                                                           |
| `extracurricular_participation` | object      | Partisipasi siswa dalam kegiatan ekstrakurikuler                            | Ya → `0`, Tidak → `1`                                       |
| `exam_score`                    | float64     | Nilai ujian akhir siswa (skala 0–100)                                       | -                                                           |

## Model Machine Learning
Proyek ini memanfaatkan beberapa model regresi untuk memprediksi nilai ujian akhir siswa dengan menganalisis lebih dari 15 variabel penting:

- Linear Regression: Sebuah model dasar yang memodelkan hubungan linear antara fitur input dan harga properti.
- Lasso Regression: Regresi linear dengan regularisasi L1, berguna untuk seleksi fitur dan mencegah overfitting dengan mengempeskan koefisien fitur yang kurang penting menjadi nol.
- Ridge Regression: Regresi linear dengan regularisasi L2, yang membantu mengatasi masalah multikolinearitas dan mengurangi kompleksitas model.

Model-model ini, bersama dengan ```column_scaler``` (untuk penskalaan fitur) dan ```feature_columns``` (untuk memastikan konsistensi fitur), telah dilatih dan disimpan dalam format ```.pkl``` di folder ```models/```.

## Hasil dan Analisis


## Kontak

