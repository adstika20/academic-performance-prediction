# Student Habits vs Academic Performance📊

Dataset ini adalah kumpulan data simulasi yang dirancang untuk meneliti hubungan antara kebiasaan hidup sehari-hari dengan prestasi akademik mahasiswa. 
Dataset berisi 1.000 catatan mahasiswa sintetis dengan lebih dari 15 variabel yang mencakup jam belajar, pola tidur, penggunaan media sosial, kualitas diet, kesehatan mental, dan nilai ujian akhir. 
Data ini dibuat menggunakan pola yang realistis namun sepenuhnya artifisial untuk tujuan edukasi dan latihan. Dataset sangat cocok digunakan untuk berbagai proyek analisis data seperti machine learning (terutama untuk prediksi nilai), 
analisis regresi (mencari korelasi antar variabel), clustering (pengelompokan mahasiswa berdasarkan pola kebiasaan), dan visualisasi data. 

## Data Understanding

## 🧾 Deskripsi Fitur Dataset

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
