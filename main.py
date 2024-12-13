from flask import Flask, request, jsonify, render_template
import pandas as pd

# Load the dataset
data = pd.read_csv("tourism.csv")

# Preprocess the data (e.g., handle missing values)
data = data.fillna({'Price': 0, 'Time_Minutes': 0, 'Rating': 0})

# Initialize the Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/recommend", methods=["POST"])
def recommend():
    # Get user input from the form
    category = request.form.get("category", "")
    city = request.form.get("city", "")
    max_price = request.form.get("max_price", float('inf'))
    
    # Ensure max_price is converted to a number
    try:
        max_price = float(max_price)
    except ValueError:
        max_price = float('inf')

    # Filter data based on user input
    filtered_data = data[
        (data["Category"].str.contains(category, case=False, na=False)) &
        (data["City"].str.contains(city, case=False, na=False)) &
        (data["Price"] <= max_price)
    ]

    # Sort by rating (descending)
    filtered_data = filtered_data.sort_values(by="Rating", ascending=False)

    # Prepare response
    recommendations = filtered_data.head(5).to_dict(orient="records")
    
    # Convert recommendations to HTML for display
    results_html = "<h2>Recommendations</h2><ul>"
    for rec in recommendations:
        results_html += f"<li>{rec['Place_Name']} - {rec['Category']} - {rec['City']} - {rec['Price']} - {rec['Rating']}</li>"
    results_html += "</ul>"
    return results_html

if __name__ == "__main__":
    app.run(debug=True)
