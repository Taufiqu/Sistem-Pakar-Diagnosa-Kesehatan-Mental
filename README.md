# 🧠 Sistem Pakar Diagnosa Kesehatan Mental

Sebuah aplikasi web berbasis **Python Flask** yang dirancang sebagai platform skrining awal untuk kondisi kesehatan mental. Proyek ini memberikan evaluasi untuk **Depresi**, **Kecemasan**, dan **Stres** menggunakan logika pencocokan skor sederhana.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Taufiqu/Sistem-Pakar-Diagnosa-Kesehatan-Mental?style=social)](https://github.com/Taufiqu/Sistem-Pakar-Diagnosa-Kesehatan-Mental/stargazers)

---

## 🚀 Demo Langsung

https://sistem-pakar-diagnosa-kesehatan-men.vercel.app/

---

## 🌟 Fitur Utama

-   **Tes Depresi (PHQ-9)**: Skrining gejala depresi berdasarkan 9 kriteria klinis.
-   **Tes Kecemasan (GAD-7)**: Evaluasi tingkat kecemasan umum berdasarkan 7 item.
-   **Tes Stres (PSS-10)**: Pengukuran tingkat stres yang dirasakan pengguna.
-   **Hasil Real-time**: Dapatkan skor dan interpretasi diagnostik langsung di halaman.
-   **Desain Responsif**: Tampilan optimal di perangkat desktop maupun mobile.
-   **Backend Flask**: Logika aplikasi sepenuhnya ditangani oleh server Python Flask.

---

## 🛠️ Tumpukan Teknologi (Technology Stack)

-   **Frontend**:
    -   HTML5
    -   Tailwind CSS
    -   JavaScript
-   **Backend**:
    -   Python 3.11+
    -   Flask (sebagai web server dan framework)
    -   Pandas (untuk pemrosesan data dari file CSV)
-   **Deployment**:
    -   Dirancang untuk platform hosting seperti Replit, Railway, atau sejenisnya.

---

## 🏗️ Struktur Proyek

```
.
├── static/              # Aset statis (CSS, gambar, dll.)
├── templates/           # Template HTML yang di-render oleh Flask
├── Anxiety.csv          # Dataset untuk logika pencocokan
├── Depression.csv
├── Stress.csv
├── main.py              # Aplikasi utama Flask
├── requirements.txt     # Daftar dependensi Python
└── .replit              # File konfigurasi untuk deployment di Replit
```

---

## 🚀 Panduan Instalasi dan Menjalankan

Ikuti langkah-langkah ini untuk menjalankan aplikasi di lingkungan pengembangan lokal Anda.

1.  **Clone repositori:**
    ```bash
    git clone [https://github.com/Taufiqu/Sistem-Pakar-Diagnosa-Kesehatan-Mental.git](https://github.com/Taufiqu/Sistem-Pakar-Diagnosa-Kesehatan-Mental.git)
    cd Sistem-Pakar-Diagnosa-Kesehatan-Mental
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    # Windows
    python -m venv env
    .\env\Scripts\activate

    # macOS / Linux
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Instal semua dependensi yang diperlukan:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan aplikasi Flask:**
    ```bash
    python main.py
    ```
    Buka browser Anda dan kunjungi `http://127.0.0.1:5000` untuk melihat aplikasi berjalan.

---

## 📊 Skoring Penilaian

Skoring didasarkan pada standar instrumen psikologi yang umum digunakan.

| Tes         | Skor    | Interpretasi          |
| :---------- | :------ | :-------------------- |
| **Depresi** | 0-4     | Depresi Minimal       |
| (PHQ-9)     | 5-9     | Depresi Ringan        |
|             | 10-14   | Depresi Sedang        |
|             | 15-27   | Depresi Berat         |
| **Kecemasan** | 0-4     | Kecemasan Minimal     |
| (GAD-7)     | 5-9     | Kecemasan Ringan      |
|             | 10-14   | Kecemasan Sedang      |
|             | 15-21   | Kecemasan Berat       |
| **Stres** | 0-13    | Stres Rendah          |
| (PSS-10)    | 14-26   | Stres Sedang          |
|             | 27-40   | Stres Tinggi          |

---

## ⚠️ Penafian (Disclaimer)

Aplikasi ini adalah **alat skrining awal** dan ditujukan untuk **keperluan edukasi**. Hasil tes ini **tidak menggantikan diagnosis klinis** dari seorang profesional. Untuk diagnosis yang akurat dan penanganan yang tepat, sangat disarankan untuk berkonsultasi dengan psikolog atau psikiater.