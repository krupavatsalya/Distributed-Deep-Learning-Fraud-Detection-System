from flask import Flask, render_template, request, jsonify, redirect, url_for
from tensorflow.keras.models import load_model
import numpy as np
import random

app = Flask(__name__)
model = load_model('my_model.keras')

@app.route('/')
def home():
    return redirect(url_for('predict'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "GET":
        print("GET request to /predict")
        return render_template("predict.html")
    if request.method == "POST":
        search_input = request.form['search']
        search_input = float(search_input) / 172788
        data = np.array([[search_input] + [round(random.uniform(0, 1), 6)] * 29])
        prediction = model.predict(data)
        prediction = round(prediction[0][0], 2)
        print("Prediction:", prediction)
        if prediction == 0.0:
            return jsonify({'prediction': "Transaction at this time is not Fraud"})
        else:
            return jsonify({'prediction': "Transaction at this time Fraud"})

if __name__ == '__main__':
    app.run(debug=True)
