from flask import Flask, request, jsonify, render_template_string
import pandas as pd

# Load the dataset
data = pd.read_csv("tourism.csv")

# Preprocess the data (e.g., handle missing values)
data = data.fillna({'Price': 0, 'Time_Minutes': 0, 'Rating': 0})

# Initialize the Flask app
app = Flask(__name__)

# HTML Template for the Home Page
home_page_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Tourism Expert System</title>
</head>
<body>
    <h1>Welcome to the Tourism Expert System</h1>
    <form action="/recommend" method="POST">
        <label for="category">Category:</label>
        <input type="text" id="category" name="category" placeholder="e.g., Taman Hiburan"><br><br>
        
        <label for="city">City:</label>
        <input type="text" id="city" name="city" placeholder="e.g., Jakarta"><br><br>
        
        <label for="max_price">Maximum Price:</label>
        <input type="number" id="max_price" name="max_price" placeholder="e.g., 100000"><br><br>
        
        <button type="submit">Get Recommendations</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(home_page_html)

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
