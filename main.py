from flask import Flask, request, render_template
import pandas as pd

depression_data = pd.read_csv("Depression.csv")
stress_data = pd.read_csv("Stress.csv")
anxiety_data = pd.read_csv("Anxiety.csv")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template('index.html')

@app.route("/depression", methods=["GET", "POST"])
def depression_diagnosis():
    if request.method == "POST":
        age = request.form.get("age")
        gender = request.form.get("gender")

        # Get user input for PHQ-9
        scores = [int(request.form.get(f"q{i}", 0)) for i in range(1, 10)]
        user_score = sum(scores)
        
        # Salin dataframe agar tidak mengubah data asli
        search_data = depression_data.copy()

        # 1. Hitung selisih skor (prioritas utama)
        search_data['score_diff'] = abs(search_data['Depression Value'] - user_score)

        # 2. Beri penalti jika gender tidak cocok
        search_data['gender_penalty'] = (search_data['2. Gender'] != gender) * 100

        # 3. Beri penalti jika usia tidak cocok
        search_data['age_penalty'] = (search_data['1. Age'] != age) * 100

        # 4. Hitung total "jarak" atau perbedaan
        search_data['total_diff'] = search_data['score_diff'] + search_data['gender_penalty'] + search_data['age_penalty']

        # 5. Cari baris dengan total_diff yang paling kecil
        closest_match = search_data.loc[search_data['total_diff'].idxmin()]
        
        # Render result
        result = closest_match.to_dict()

        return render_template('depresi/depresi.html',age=age, gender=gender, user_score=user_score, result=result)
    return render_template('depresi/depresi_form_new.html')

@app.route("/stress", methods=["GET", "POST"])
def stress_diagnosis():
    if request.method == "POST":
        age = request.form.get("age")
        gender = request.form.get("gender")

        # Get user input for stress scale
        scores = [int(request.form.get(f"q{i}", 0)) for i in range(1, 11)]
        user_score = sum(scores)
        
        # Salin dataframe agar tidak mengubah data asli
        search_data = stress_data.copy()
        
        # 1. Hitung selisih skor (prioritas utama)
        search_data['score_diff'] = abs(search_data['Stress Value'] - user_score)

        # 2. Beri penalti jika gender tidak cocok
        search_data['gender_penalty'] = (search_data['2. Gender'] != gender) * 100

        # 3. Beri penalti jika usia tidak cocok
        search_data['age_penalty'] = (search_data['1. Age'] != age) * 100

        # 4. Hitung total "jarak" atau perbedaan
        search_data['total_diff'] = search_data['score_diff'] + search_data['gender_penalty'] + search_data['age_penalty']

        # 5. Cari baris dengan total_diff yang paling kecil
        closest_match = search_data.loc[search_data['total_diff'].idxmin()]
        
        # Render result
        result = closest_match.to_dict()
        return render_template('stres/stres.html',age=age, gender=gender,user_score=user_score, result=result)
    return render_template('stres/stres_form_new.html')

@app.route("/anxiety", methods=["GET", "POST"])
def anxiety_diagnosis():
    if request.method == "POST":

        age = request.form.get("age")
        gender = request.form.get("gender")

        # Get user input for anxiety scale
        scores = [int(request.form.get(f"question_{i}", 0)) for i in range(1, 8)]
        user_score = sum(scores)
        
        search_data = anxiety_data.copy()

        # 1. Hitung selisih skor (prioritas utama)
        search_data['score_diff'] = abs(search_data['Anxiety Value'] - user_score)

        # 2. Beri penalti jika gender tidak cocok
        # Jika gender data TIDAK SAMA DENGAN gender input, beri penalti. Jika sama, penaltinya 0.
        # Penalti ini (angka 100) harus lebih besar dari rentang skor (0-21) agar ketidakcocokan gender sangat dihindari
        search_data['gender_penalty'] = (search_data['2. Gender'] != gender) * 100

        # 3. Beri penalti jika usia tidak cocok
        search_data['age_penalty'] = (search_data['1. Age'] != age) * 100

        # 4. Hitung total "jarak" atau perbedaan
        search_data['total_diff'] = search_data['score_diff'] + search_data['gender_penalty'] + search_data['age_penalty']

        # 5. Cari baris dengan total_diff yang paling kecil
        closest_match = search_data.loc[search_data['total_diff'].idxmin()]
        
        # Render result
        result = closest_match.to_dict()
        return render_template('anxiety/anxiety_result.html', age=age, gender=gender, user_score=user_score, result=result)
    return render_template('anxiety/anxiety_form_new.html')

if __name__ == "__main__":
    app.run(debug=True)
