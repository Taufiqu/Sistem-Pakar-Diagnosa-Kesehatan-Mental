# 🧠 Sistem Pakar Diagnosa Kesehatan Mental

Platform AI berbasis web untuk screening awal kondisi kesehatan mental yang mencakup tes untuk **Depresi**, **Kecemasan**, dan **Stres**.

## 🌟 Fitur Utama

- **Tes Depresi (PHQ-9)** - Screening depresi berdasarkan kriteria klinis
- **Tes Kecemasan (GAD-7)** - Evaluasi tingkat kecemasan dan gangguan anxiety  
- **Tes Stres** - Pengukuran tingkat stress dan kemampuan coping
- **Responsive Design** - Optimized untuk desktop dan mobile
- **Real-time Results** - Hasil diagnosa langsung tanpa reload halaman

## 🚀 Demo Live

🌐 **[Lihat Demo](https://Taufiqu.github.io/Sistem-Pakar-Diagnosa-Kesehatan-Mental/)**

## 🛠️ Teknologi

- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)
- **Deployment**: GitHub Pages
- **Original Backend**: Python Flask, Scikit-learn, Pandas

## 📱 Screenshots

### Homepage
![Homepage](https://via.placeholder.com/800x400/4F46E5/FFFFFF?text=Mental+Health+Expert+System)

### Test Interface
![Test Interface](https://via.placeholder.com/800x400/10B981/FFFFFF?text=Interactive+Assessment)

## 🏗️ Struktur Project

```
├── docs/                   # GitHub Pages deployment
│   ├── index.html         # Homepage
│   ├── anxiety.html       # Tes Kecemasan
│   ├── depression.html    # Tes Depresi
│   ├── stress.html        # Tes Stres
│   └── static/           
│       └── css/
│           └── style.css  # Custom styles
├── templates/             # Original Flask templates
├── static/               # Static assets
├── *.csv                 # ML datasets
├── main.py              # Flask application
├── build_static.py      # Static site generator
└── requirements.txt     # Python dependencies
```

## 🚀 Quick Start

### For Development (Flask)
```bash
# Clone repository
git clone https://github.com/Taufiqu/Sistem-Pakar-Diagnosa-Kesehatan-Mental.git
cd Sistem-Pakar-Diagnosa-Kesehatan-Mental

# Setup virtual environment
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python main.py
```

### For Static Site (GitHub Pages)
```bash
# Build static site
python build_static_simple.py

# Files generated in docs/ directory
# Ready for GitHub Pages deployment
```

## 📊 Assessment Scoring

### Depresi (PHQ-9)
- **0-4**: Depresi Minimal
- **5-9**: Depresi Ringan  
- **10-14**: Depresi Sedang
- **15-27**: Depresi Berat

### Kecemasan (GAD-7)
- **0-4**: Kecemasan Minimal
- **5-9**: Kecemasan Ringan
- **10-14**: Kecemasan Sedang  
- **15-21**: Kecemasan Berat

### Stres
- **0-1**: Stres Rendah
- **2-3**: Stres Sedang
- **4-5**: Stres Tinggi
- **6+**: Stres Sangat Tinggi

## ⚠️ Disclaimer

Hasil tes ini hanya untuk **screening awal** dan **tujuan edukasi**. Tidak menggantikan diagnosis profesional. Untuk diagnosis akurat dan penanganan yang tepat, konsultasikan dengan **psikolog atau psikiater**.

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

Project ini dibuat untuk keperluan **edukasi** dan **pembelajaran**.

## 👨‍💻 Developer

Dikembangkan sebagai **Tugas Sistem Pakar** - Semester 5

---

### 🔧 Build Commands

```bash
# Build static site
python build_static_simple.py

# Install dependencies
pip install -r requirements.txt

# Run Flask development server
python main.py
```

**Made with ❤️ for Mental Health Awareness**