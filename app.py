import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Nilai Ujian", layout="centered")

st.markdown("""
    <h1 style='text-align: center;'>SmartScore - Prediksi Nilai Ujian dengan Machine Learning 🎓</h1>
""", unsafe_allow_html=True)


st.markdown("""
Selamat datang di aplikasi prediksi nilai siswa! 🖐️  

Sistem prediksi ini menganalisis berbagai variabel akademik dan non-akademik yang mempengaruhi prestasi siswa. 
Data kebiasaan belajar, kondisi kesehatan, dan faktor lingkungan akan diproses menggunakan model machine learning untuk menghasilkan estimasi nilai ujian. 
Hasil prediksi ini dapat digunakan sebagai acuan untuk identifikasi dini dan perbaikan metode belajar
""")

st.markdown("Silahkan isi kebiasaan dan informasi siswa di bawah ini lalu tekan tombol **Prediksi**.")


st.markdown("""
<style>
.stButton>button {
    background-color: #FF4B4B;
    color: white;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load('models/lasso_model.pkl')  # atau model lain
scaler = joblib.load('models/column_scaler.pkl')  # ColumnTransformer
feature_columns = joblib.load('models/feature_columns.pkl')  # List kolom final


# From Input
st.subheader("🧠 Kondisi Mental dan Gaya Hidup")
mental_health_rating = st.slider("Rating kesehatan mental (1-10)", 1, 10, 5)
age = st.slider("Usia", 10, 24, 17)
sleep_hours = st.slider("Jam tidur per hari", 3, 10, 7)
olahraga = st.slider("Frekuensi olahraga per minggu", 0, 6, 2)

diet = st.selectbox("Kualitas Diet", ['Poor', 'Fair', 'Good'])
diet_map = {'Poor': 0, 'Fair': 1, 'Good': 2}
diet_encoded = diet_map[diet]

internet = st.selectbox("Kualitas Internet", ['Poor', 'Average', 'Good'])
internet_map = {'Poor': 0, 'Average': 1, 'Good': 2}
internet_encoded = internet_map[internet]

st.subheader("🎓 Aktivitas Akademik")
belajar = st.slider("Jam belajar per hari", 0, 8, 4)
attendance = st.slider("Persentase kehadiran (%)", 56.0, 98.0, 90.0, step=0.5)
netflix = st.slider("Jam nonton Netflix per hari", 0, 5, 2)
medsos = st.slider("Jam main media sosial", 0, 7, 3)

st.subheader("Data Demografis")
gender = st.radio("Jenis Kelamin", ['Female', 'Male', 'Other'])
gender_female = 1 if gender == 'Female' else 0
gender_male = 1 if gender == 'Male' else 0
gender_other = 1 if gender == 'Other' else 0

job = st.radio("Punya kerja part-time?", ['Yes', 'No'])
job_yes = 1 if job == 'Yes' else 0
job_no = 1 if job == 'No' else 0

eksul = st.radio("Ikut ekstrakurikuler?", ['Yes', 'No'])
eksul_yes = 1 if eksul == 'Yes' else 0
eksul_no = 1 if eksul == 'No' else 0


edu = st.selectbox("Pendidikan Orang Tua", ['High School', 'Bachelor', 'Master'])
edu_map = {'Unknown':-1,'High School': 0, 'Bachelor': 1, 'Master': 2}
parental_encoded = edu_map[edu]


# --- BENTUK DATAFRAME SESUAI FITUR TRAINING ---
input_df = pd.DataFrame([{
    
    'mental_health_rating': mental_health_rating,
    'age': age,
    'sleep_hours': sleep_hours,
    'attendance_percentage': attendance,
    'netflix_hours': netflix,
    'social_media_hours': medsos,
    'study_hours_per_day': belajar,
    'exercise_frequency': olahraga,
    'gender_Female': gender_female,
    'gender_Male': gender_male,
    'gender_Other': gender_other,
    'part_time_job_No': job_no,
    'part_time_job_Yes': job_yes,
    'extracurricular_participation_No': eksul_no,
    'extracurricular_participation_Yes': eksul_yes,
    'diet_quality_encoded': diet_encoded,
    'parental_education_encoded': parental_encoded,
    'internet_quality_encoded': internet_encoded
}])

# Urutkan kolom agar cocok dengan model
input_df = input_df[feature_columns]

# --- TOMBOL PREDIKSI ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔍 Prediksi Sekarang", use_container_width=True):
        with st.spinner("⏳ Sedang memproses prediksi..."):
            # Transform dan prediksi
            input_scaled = scaler.transform(input_df)
            prediction = model.predict(input_scaled)[0]
            prediction = max(min(prediction, 100), 0)

        # Tampilkan hasil
        st.subheader("📘 Hasil Prediksi")
        st.success(f"Berikut ini adalah prediksi nilai ujian berdasarkan data kebiasaan siswa: **{prediction:.2f}**")

        # ⛔ Tampilkan warning jika nilainya rendah
        if prediction < 60:
            st.warning("⚠️ Nilai masih di bawah standar. Mungkin perlu evaluasi waktu belajar atau kebiasaan lain.")
