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
        
        # Find the closest match in the dataset
        depression_data["score_diff"] = abs(depression_data["Depression Value"] - user_score)
        closest_match = depression_data.loc[depression_data["score_diff"].idxmin()]
        
        # Render result
        result = closest_match.to_dict()

        return render_template('depresi/depresi.html',age=age, gender=gender, user_score=user_score, result=result)
    return render_template('depresi/depresi_form.html')

@app.route("/stress", methods=["GET", "POST"])
def stress_diagnosis():
    if request.method == "POST":
        age = request.form.get("age")
        gender = request.form.get("gender")

        # Get user input for stress scale
        scores = [int(request.form.get(f"q{i}", 0)) for i in range(1, 11)]
        user_score = sum(scores)
        
        # Find the closest match in the dataset
        stress_data["score_diff"] = abs(stress_data["Stress Value"] - user_score)
        closest_match = stress_data.loc[stress_data["score_diff"].idxmin()]
        
        # Render result
        result = closest_match.to_dict()
        return render_template('stres/stres.html',age=age, gender=gender,user_score=user_score, result=result)
    return render_template('stres/stres_form.html')

@app.route("/anxiety", methods=["GET", "POST"])
def anxiety_diagnosis():
    if request.method == "POST":

        age = request.form.get("age")
        gender = request.form.get("gender")

        # Get user input for anxiety scale
        scores = [int(request.form.get(f"q{i}", 0)) for i in range(1, 8)]
        user_score = sum(scores)
        
        # Find the closest match in the dataset
        anxiety_data["score_diff"] = abs(anxiety_data["Anxiety Value"] - user_score)
        closest_match = anxiety_data.loc[anxiety_data["score_diff"].idxmin()]
        
        # Render result
        result = closest_match.to_dict()
        return render_template('anxiety/anxiety.html', age=age, gender=gender, user_score=user_score, result=result)
    return render_template('anxiety/anxiety_form.html')

            
if __name__ == "__main__":
    app.run(debug=True)
