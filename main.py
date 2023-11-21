from flask import Flask, render_template, request
from joblib import load


app = Flask(__name__)

# Load the saved model
loaded_model = load('best_decision_model_water_treatment.joblib')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve values entered by the user
        pH = request.form['pH']
        hardness = request.form['Hardness']
        total_dissolved_solids = request.form['Total Dissolved Solids']
        chloramines = request.form['Chloramines']
        sulfate = request.form['Sulfate']
        conductivity = request.form['Conductivity']
        organic_carbon = request.form['Organic Carbon']
        trihalomethanes = request.form['Trihalomethanes']
        turbidity = request.form['Turbidity']

        # Print the values (you can process or use them as needed)
        print("pH:", pH)
        print("Hardness:", hardness)
        print("Total Dissolved Solids:", total_dissolved_solids)
        print("Chloramines:", chloramines)
        print("Sulfate:", sulfate)
        print("Conductivity:", conductivity)
        print("Organic Carbon:", organic_carbon)
        print("Trihalomethanes:", trihalomethanes)
        print("Turbidity:", turbidity)

        entered_values = [[pH,hardness,total_dissolved_solids,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]]
        prediction = loaded_model.predict(entered_values)[0]
        print(prediction)
        if prediction == 0:
            prediction_result = "Unsafe"
        else:
            prediction_result = "Safe"

        result = f"As per the quality of water entered , the sample of water is {prediction_result} for drinking purpose"
        # You can perform further processing or return a response as needed
        return render_template('home.html', prediction_result=prediction_result)

    # Handle other cases or errors here
    return "An error occurred."

if __name__ == '__main__':
    app.run(debug=True)
