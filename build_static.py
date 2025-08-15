import os
import json
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import shutil

def create_docs_structure():
    """Create docs directory structure for GitHub Pages"""
    if os.path.exists('docs'):
        shutil.rmtree('docs')
    
    os.makedirs('docs', exist_ok=True)
    os.makedirs('docs/static', exist_ok=True)
    os.makedirs('docs/static/css', exist_ok=True)
    os.makedirs('docs/static/js', exist_ok=True)
    print("✅ Created docs directory structure")

def copy_static_files():
    """Copy CSS and JS files"""
    try:
        if os.path.exists('static'):
            shutil.copytree('static', 'docs/static', dirs_exist_ok=True)
            print("✅ Copied static files")
        else:
            print("⚠️ No static directory found, creating basic CSS")
            with open('docs/static/css/style.css', 'w') as f:
                f.write("""
body { font-family: 'Inter', sans-serif; }
.container { max-width: 1200px; margin: 0 auto; padding: 20px; }
.card { background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.btn { padding: 12px 24px; border-radius: 6px; text-decoration: none; display: inline-block; }
.btn-primary { background: #3b82f6; color: white; }
.btn-success { background: #10b981; color: white; }
.btn-danger { background: #ef4444; color: white; }
.text-center { text-align: center; }
.mb-8 { margin-bottom: 2rem; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
""")
    except Exception as e:
        print(f"⚠️ Error copying static files: {e}")

def build_prediction_models():
    """Build and train ML models"""
    models = {}
    
    try:
        # Anxiety Model
        if os.path.exists('Anxiety.csv'):
            anxiety_data = pd.read_csv('Anxiety.csv')
            print(f"✅ Loaded anxiety data: {len(anxiety_data)} rows")
            
            # Simple model training
            X = anxiety_data.drop(['Anxiety_Level'], axis=1, errors='ignore')
            if 'Anxiety_Level' in anxiety_data.columns:
                y = anxiety_data['Anxiety_Level']
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model = LogisticRegression(random_state=42, max_iter=1000)
                model.fit(X_train, y_train)
                models['anxiety'] = {
                    'model': model,
                    'feature_names': list(X.columns),
                    'accuracy': model.score(X_test, y_test)
                }
                print(f"✅ Anxiety model trained with accuracy: {models['anxiety']['accuracy']:.2f}")
        
        # Depression Model
        if os.path.exists('Depression.csv'):
            depression_data = pd.read_csv('Depression.csv')
            print(f"✅ Loaded depression data: {len(depression_data)} rows")
            
            X = depression_data.drop(['Depression_Level'], axis=1, errors='ignore')
            if 'Depression_Level' in depression_data.columns:
                y = depression_data['Depression_Level']
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model = LogisticRegression(random_state=42, max_iter=1000)
                model.fit(X_train, y_train)
                models['depression'] = {
                    'model': model,
                    'feature_names': list(X.columns),
                    'accuracy': model.score(X_test, y_test)
                }
                print(f"✅ Depression model trained with accuracy: {models['depression']['accuracy']:.2f}")
                
    except Exception as e:
        print(f"⚠️ Error building models: {e}")
    
    return models

def create_index_html():
    """Create main index.html"""
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem Pakar Diagnosa Kesehatan Mental</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="static/css/style.css" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <header class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-bold text-gray-800 mb-4">
                <i class="fas fa-brain text-blue-600 mr-3"></i>
                Sistem Pakar Diagnosa Kesehatan Mental
            </h1>
            <p class="text-xl text-gray-600">Platform AI untuk screening awal kondisi kesehatan mental</p>
        </header>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            <!-- Depression Card -->
            <div class="bg-white rounded-xl shadow-lg p-8 hover:shadow-xl transition-shadow duration-300">
                <div class="text-center">
                    <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-brain text-2xl" style="color: #2563eb !important;"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-gray-800 mb-3">Tes Depresi</h3>
                    <p class="text-gray-600 mb-6">Screening untuk mendeteksi gejala depresi berdasarkan kriteria klinis</p>
                    <a href="depression.html" class="btn btn-primary inline-block" style="background-color: #2563eb !important; color: white !important;">
                        Mulai Diagnosa
                    </a>
                </div>
            </div>
            
            <!-- Anxiety Card -->
            <div class="bg-white rounded-xl shadow-lg p-8 hover:shadow-xl transition-shadow duration-300">
                <div class="text-center">
                    <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-heart text-2xl" style="color: #dc2626 !important;"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-gray-800 mb-3">Tes Kecemasan</h3>
                    <p class="text-gray-600 mb-6">Evaluasi tingkat kecemasan dan gangguan anxiety</p>
                    <a href="anxiety.html" class="btn btn-danger inline-block" style="background-color: #dc2626 !important; color: white !important;">
                        Mulai Diagnosa
                    </a>
                </div>
            </div>
            
            <!-- Stress Card -->
            <div class="bg-white rounded-xl shadow-lg p-8 hover:shadow-xl transition-shadow duration-300">
                <div class="text-center">
                    <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-shield-alt text-2xl" style="color: #16a34a !important;"></i>
                    </div>
                    <h3 class="text-2xl font-bold text-gray-800 mb-3">Tes Stres</h3>
                    <p class="text-gray-600 mb-6">Pengukuran tingkat stress dan kemampuan coping</p>
                    <a href="stress.html" class="btn btn-success inline-block" style="background-color: #16a34a !important; color: white !important;">
                        Mulai Diagnosa
                    </a>
                </div>
            </div>
        </div>
        
        <footer class="text-center mt-16 text-gray-600">
            <p>&copy; 2024 Sistem Pakar Kesehatan Mental. Dikembangkan untuk keperluan edukasi.</p>
            <p class="text-sm mt-2">⚠️ Hasil diagnosa bersifat screening awal, konsultasi dengan profesional kesehatan mental untuk diagnosis akurat.</p>
        </footer>
    </div>
</body>
</html>"""
    
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ Created index.html")

def create_anxiety_page():
    """Create anxiety test page"""
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tes Kecemasan - Sistem Pakar</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <nav class="mb-8">
            <a href="index.html" class="text-blue-600 hover:text-blue-800">&larr; Kembali ke Beranda</a>
        </nav>
        
        <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <h1 class="text-3xl font-bold text-center mb-8 text-gray-800">Tes Kecemasan (GAD-7)</h1>
            
            <form id="anxietyForm" class="space-y-6">
                <div class="space-y-4">
                    <div class="question-group">
                        <p class="font-medium mb-3">1. Merasa gugup, cemas, atau tegang</p>
                        <div class="space-y-2">
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="0" class="mr-2"> Tidak sama sekali
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="1" class="mr-2"> Beberapa hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="2" class="mr-2"> Lebih dari setengah hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="3" class="mr-2"> Hampir setiap hari
                            </label>
                        </div>
                    </div>
                    
                    <div class="question-group">
                        <p class="font-medium mb-3">2. Tidak dapat menghentikan atau mengendalikan kekhawatiran</p>
                        <div class="space-y-2">
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="0" class="mr-2"> Tidak sama sekali
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="1" class="mr-2"> Beberapa hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="2" class="mr-2"> Lebih dari setengah hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="3" class="mr-2"> Hampir setiap hari
                            </label>
                        </div>
                    </div>
                    
                    <!-- Add more questions as needed -->
                </div>
                
                <button type="submit" class="w-full bg-red-600 text-white py-3 px-6 rounded-lg hover:bg-red-700 transition-colors">
                    Lihat Hasil Diagnosa
                </button>
            </form>
            
            <div id="results" class="mt-8 hidden">
                <div class="bg-blue-50 border border-blue-200 rounded-lg p-6">
                    <h3 class="text-lg font-bold mb-2">Hasil Tes Kecemasan</h3>
                    <p id="anxietyLevel" class="text-gray-700"></p>
                    <div id="recommendation" class="mt-4 p-4 rounded-lg"></div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('anxietyForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Calculate anxiety score
            let score = 0;
            for (let i = 1; i <= 2; i++) {
                const answer = document.querySelector(`input[name="q${i}"]:checked`);
                if (answer) {
                    score += parseInt(answer.value);
                }
            }
            
            // Determine anxiety level
            let level, color, recommendation;
            if (score <= 4) {
                level = "Kecemasan Minimal";
                color = "bg-green-100 border-green-200";
                recommendation = "Tingkat kecemasan Anda dalam batas normal. Pertahankan gaya hidup sehat.";
            } else if (score <= 9) {
                level = "Kecemasan Ringan";
                color = "bg-yellow-100 border-yellow-200";
                recommendation = "Anda mengalami kecemasan ringan. Pertimbangkan teknik relaksasi dan manajemen stres.";
            } else if (score <= 14) {
                level = "Kecemasan Sedang";
                color = "bg-orange-100 border-orange-200";
                recommendation = "Anda mengalami kecemasan sedang. Disarankan untuk berkonsultasi dengan profesional kesehatan mental.";
            } else {
                level = "Kecemasan Berat";
                color = "bg-red-100 border-red-200";
                recommendation = "Anda mengalami kecemasan berat. Sangat disarankan untuk segera berkonsultasi dengan profesional kesehatan mental.";
            }
            
            // Show results
            document.getElementById('anxietyLevel').textContent = `Skor: ${score} - ${level}`;
            document.getElementById('recommendation').textContent = recommendation;
            document.getElementById('recommendation').className = `mt-4 p-4 rounded-lg ${color}`;
            document.getElementById('results').classList.remove('hidden');
        });
    </script>
</body>
</html>"""
    
    with open('docs/anxiety.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ Created anxiety.html")

def create_depression_page():
    """Create depression test page"""
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tes Depresi - Sistem Pakar</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <nav class="mb-8">
            <a href="index.html" class="text-blue-600 hover:text-blue-800">&larr; Kembali ke Beranda</a>
        </nav>
        
        <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <h1 class="text-3xl font-bold text-center mb-8 text-gray-800">Tes Depresi (PHQ-9)</h1>
            
            <form id="depressionForm" class="space-y-6">
                <div class="space-y-4">
                    <div class="question-group">
                        <p class="font-medium mb-3">1. Sedikit tertarik atau tidak menikmati aktivitas</p>
                        <div class="space-y-2">
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="0" class="mr-2"> Tidak sama sekali
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="1" class="mr-2"> Beberapa hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="2" class="mr-2"> Lebih dari setengah hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="3" class="mr-2"> Hampir setiap hari
                            </label>
                        </div>
                    </div>
                    
                    <div class="question-group">
                        <p class="font-medium mb-3">2. Merasa sedih, depresi, atau putus asa</p>
                        <div class="space-y-2">
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="0" class="mr-2"> Tidak sama sekali
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="1" class="mr-2"> Beberapa hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="2" class="mr-2"> Lebih dari setengah hari
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="3" class="mr-2"> Hampir setiap hari
                            </label>
                        </div>
                    </div>
                </div>
                
                <button type="submit" class="w-full bg-blue-600 text-white py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors">
                    Lihat Hasil Diagnosa
                </button>
            </form>
            
            <div id="results" class="mt-8 hidden">
                <div class="bg-blue-50 border border-blue-200 rounded-lg p-6">
                    <h3 class="text-lg font-bold mb-2">Hasil Tes Depresi</h3>
                    <p id="depressionLevel" class="text-gray-700"></p>
                    <div id="recommendation" class="mt-4 p-4 rounded-lg"></div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('depressionForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            let score = 0;
            for (let i = 1; i <= 2; i++) {
                const answer = document.querySelector(`input[name="q${i}"]:checked`);
                if (answer) {
                    score += parseInt(answer.value);
                }
            }
            
            let level, color, recommendation;
            if (score <= 4) {
                level = "Depresi Minimal";
                color = "bg-green-100 border-green-200";
                recommendation = "Tingkat depresi Anda dalam batas normal. Pertahankan aktivitas positif dan gaya hidup sehat.";
            } else if (score <= 9) {
                level = "Depresi Ringan";
                color = "bg-yellow-100 border-yellow-200";
                recommendation = "Anda mengalami gejala depresi ringan. Pertimbangkan untuk meningkatkan aktivitas sosial dan olahraga.";
            } else if (score <= 14) {
                level = "Depresi Sedang";
                color = "bg-orange-100 border-orange-200";
                recommendation = "Anda mengalami depresi sedang. Disarankan untuk berkonsultasi dengan psikolog atau psikiater.";
            } else {
                level = "Depresi Berat";
                color = "bg-red-100 border-red-200";
                recommendation = "Anda mengalami depresi berat. Sangat disarankan untuk segera mencari bantuan profesional kesehatan mental.";
            }
            
            document.getElementById('depressionLevel').textContent = `Skor: ${score} - ${level}`;
            document.getElementById('recommendation').textContent = recommendation;
            document.getElementById('recommendation').className = `mt-4 p-4 rounded-lg ${color}`;
            document.getElementById('results').classList.remove('hidden');
        });
    </script>
</body>
</html>"""
    
    with open('docs/depression.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ Created depression.html")

def create_stress_page():
    """Create stress test page"""
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tes Stres - Sistem Pakar</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8">
        <nav class="mb-8">
            <a href="index.html" class="text-blue-600 hover:text-blue-800">&larr; Kembali ke Beranda</a>
        </nav>
        
        <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
            <h1 class="text-3xl font-bold text-center mb-8 text-gray-800">Tes Tingkat Stres</h1>
            
            <form id="stressForm" class="space-y-6">
                <div class="space-y-4">
                    <div class="question-group">
                        <p class="font-medium mb-3">1. Seberapa sering Anda merasa kewalahan dengan tanggung jawab?</p>
                        <div class="space-y-2">
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="0" class="mr-2"> Tidak pernah
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="1" class="mr-2"> Jarang
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="2" class="mr-2"> Kadang-kadang
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q1" value="3" class="mr-2"> Sering
                            </label>
                        </div>
                    </div>
                    
                    <div class="question-group">
                        <p class="font-medium mb-3">2. Seberapa sering Anda merasa sulit berkonsentrasi?</p>
                        <div class="space-y-2">
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="0" class="mr-2"> Tidak pernah
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="1" class="mr-2"> Jarang
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="2" class="mr-2"> Kadang-kadang
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="q2" value="3" class="mr-2"> Sering
                            </label>
                        </div>
                    </div>
                </div>
                
                <button type="submit" class="w-full bg-green-600 text-white py-3 px-6 rounded-lg hover:bg-green-700 transition-colors">
                    Lihat Hasil Diagnosa
                </button>
            </form>
            
            <div id="results" class="mt-8 hidden">
                <div class="bg-blue-50 border border-blue-200 rounded-lg p-6">
                    <h3 class="text-lg font-bold mb-2">Hasil Tes Stres</h3>
                    <p id="stressLevel" class="text-gray-700"></p>
                    <div id="recommendation" class="mt-4 p-4 rounded-lg"></div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.getElementById('stressForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            let score = 0;
            for (let i = 1; i <= 2; i++) {
                const answer = document.querySelector(`input[name="q${i}"]:checked`);
                if (answer) {
                    score += parseInt(answer.value);
                }
            }
            
            let level, color, recommendation;
            if (score <= 1) {
                level = "Stres Rendah";
                color = "bg-green-100 border-green-200";
                recommendation = "Tingkat stres Anda rendah. Pertahankan keseimbangan hidup yang sehat.";
            } else if (score <= 3) {
                level = "Stres Sedang";
                color = "bg-yellow-100 border-yellow-200";
                recommendation = "Anda mengalami stres sedang. Pertimbangkan teknik manajemen stres seperti meditasi atau olahraga.";
            } else if (score <= 5) {
                level = "Stres Tinggi";
                color = "bg-orange-100 border-orange-200";
                recommendation = "Anda mengalami stres tinggi. Disarankan untuk mencari cara mengurangi beban dan berkonsultasi dengan ahli.";
            } else {
                level = "Stres Sangat Tinggi";
                color = "bg-red-100 border-red-200";
                recommendation = "Anda mengalami stres sangat tinggi. Sangat disarankan untuk segera mencari bantuan profesional.";
            }
            
            document.getElementById('stressLevel').textContent = `Skor: ${score} - ${level}`;
            document.getElementById('recommendation').textContent = recommendation;
            document.getElementById('recommendation').className = `mt-4 p-4 rounded-lg ${color}`;
            document.getElementById('results').classList.remove('hidden');
        });
    </script>
</body>
</html>"""
    
    with open('docs/stress.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ Created stress.html")

def main():
    """Main build function"""
    print("🚀 Building static site for GitHub Pages...")
    
    try:
        create_docs_structure()
        copy_static_files()
        build_prediction_models()
        create_index_html()
        create_anxiety_page()
        create_depression_page()
        create_stress_page()
        
        print("\n✅ Static site build completed!")
        print("📁 Files created in 'docs' directory:")
        print("   - index.html")
        print("   - anxiety.html")
        print("   - depression.html") 
        print("   - stress.html")
        print("   - static/css/style.css")
        print("\n🚀 Ready for GitHub Pages deployment!")
        
    except Exception as e:
        print(f"❌ Build failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()