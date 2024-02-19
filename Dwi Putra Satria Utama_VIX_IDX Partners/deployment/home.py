import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


# st.set_page_config(page_title='Prediksi Risiko Kredit Pada Debitur', layout='wide', initial_sidebar_state='expanded')

def run():
    # Membuat Sub Header
    st.title('Prediksi Risiko Kredit Pada Debitur')

    # Menambahkan Deskripsi
    st.write('Dashboard ini dibuat untuk final project saya sebagai Data Scientist Intern di ID/X Partners. Fokus utama proyek ini adalah membangun model prediksi risiko kredit menggunakan dataset yang disediakan oleh perusahaan tersebut. Dataset ini mencakup informasi tentang pinjaman. Tujuan akhirnya adalah menyediakan solusi teknologi yang dapat membantu perusahaan dalam mengambil keputusan yang lebih baik terkait dengan penilaian risiko kredit.')

    st.write('Created by: [Dwi Putra Satria Utama](https://www.linkedin.com/in/dwiputra3500/)')

    st.markdown('---')

    st.subheader("Rangkuman Project")

    st.markdown('**Tujuan Project:**')
    st.write("""
             Membangun model prediksi untuk mengidentifikasi risiko kredit calon debitur berdasarkan 
             informasi pada saat pengajuan pinjaman.
            """)
    
    st.markdown('**Transformasi Data:**')
    st.write("""
            1. Penghapusan kolom tertentu yang tidak relevan.
            2. Konversi format tanggal.
            3. Ekstraksi nilai numerik dari kolom 'term'.
            4. Penambahan kolom 'loan_category' berdasarkan kategori risiko pinjaman.
            """)
    
    st.markdown('**Insight EDA:**')
    st.write("""
            1. Profil High Risk: Term=36 bulan, Kepemilikan rumah rent/mortgage, tujuan untuk debt consolidation, status di CA.
            2. Analisis Pendapatan: Kategori "non-risk" memiliki pendapatan rata-rata lebih tinggi.
            3. Analisis DTI: Kategori "non-risk" memiliki Debt-to-Income rata-rata yang lebih rendah.
            4. Analisis Penggunaan Kredit: Kategori "high risk" memiliki tingkat penggunaan kredit yang lebih tinggi.
            """)
    
    st.markdown('**Penanganan Missing Value:**')
    st.write("""
             - Dilakukan penghapusan pada data yang hilang karena termasuk dalam MCAR.
            """)

    st.markdown('**Penanganan Imbalance Data:**')
    st.write("""
            - Undersampling dilakukan untuk menyamakan jumlah data pada kedua kelas target dan untuk efisiensi komputasi.
            """)
    
    st.markdown('**Penanganan Outlier:**')
    st.write("""
             - Menggunakan metode IQR Winsorization untuk mempertahankan distribusi asli data.
            """)

    st.markdown('**Pemodelan:**')
    st.write("""
            1. **Logistic Regression:**
               - Performa baik.

            2. **Decision Tree:**
               - Performa setara dengan Logistic Regression dan Neural Network with Keras (Sequential)  tetapi komputasi lebih cepat.
               - Dipilih sebagai model utama untuk deployment.

            3. **Neural Network with Keras (Sequential):**
               - Menggunakan aktivasi Selu, inisialisasi HeNormal, regularisasi L2, dan dropout.
               - Performa baik.
            """)

    st.markdown('**Kesimpulan:**')
    st.write("""
             Model decision tree dipilih sebagai model utama untuk prediksi risiko kredit karena komputasi yang lebih efisien dengan nilai akurasi yang serupa dengan Model Logictic Regression dan Model Neural Network with Keras (Sequential). Model ini siap untuk di-deploy dalam sistem pencegahan risiko kredit pada institusi keuangan.
            """)

    st.markdown('**Link Deployment:** [Hugging Face Dwi Putra Satria Utama](https://huggingface.co/spaces/dwiputra3500/Dwi-Putra-Satria-Utama_VIX_IDX-Partners)')

if __name__ == '__main__':
    run()
