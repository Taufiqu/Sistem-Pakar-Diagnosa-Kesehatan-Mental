from flask import Flask, request, render_template
import pandas as pd

# Load the DSM-5 Depression dataset
data = pd.read_csv("Depression.csv")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/diagnose", methods=["POST"])
def diagnose():
    # Get user input for gender, age, and all 9 questions
    gender = request.form.get("gender", "").strip()
    age = request.form.get("age", "").strip()
    q1 = int(request.form.get("q1", 0))
    q2 = int(request.form.get("q2", 0))
    q3 = int(request.form.get("q3", 0))
    q4 = int(request.form.get("q4", 0))
    q5 = int(request.form.get("q5", 0))
    q6 = int(request.form.get("q6", 0))
    q7 = int(request.form.get("q7", 0))
    q8 = int(request.form.get("q8", 0))
    q9 = int(request.form.get("q9", 0))

    # Calculate total PHQ-9 score from user input
    user_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9

    # Filter the dataset based on user input
    filtered_data = data
    if gender:
        filtered_data = filtered_data[filtered_data["2. Gender"].str.lower() == gender.lower()]
    if age:
        filtered_data = filtered_data[filtered_data["1. Age"] == age]

    # Find the closest Depression Value to the user's score
    filtered_data["score_diff"] = abs(filtered_data["Depression Value"] - user_score)
    closest_match = filtered_data.loc[filtered_data["score_diff"].idxmin()]  # Select the closest match

    # Convert the result to a dictionary
    result = closest_match.to_dict()

    # Render results page
    return render_template(
        'recommend.html', result=result, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9
    )
if __name__ == "__main__":
    app.run(debug=True)
