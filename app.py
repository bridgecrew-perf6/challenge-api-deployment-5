import os
from flask import Flask, request, jsonify

from sklearn.preprocessing import MinMaxScaler

from src.preprocessing import cleaning_data
from src.model.modeling import Polynomial_regression_model

app = Flask(__name__)

model = Polynomial_regression_model('src/model/dataset.csv', MinMaxScaler(), 3)

def get_prediction(data):
    output_example  = {
        "prediction": 140000,
        "error": "no error"
    }
    return output_example

def preprocess_data(data):
    return data

def get_expected_data_format():
    data_format = """Please make a POST request with a JSON object of this format:
    {
        "area": int,
        "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
        "rooms-number": int,
        "zip-code": int,
        "land-area": Optional[int],
        "garden": Optional[bool],
        "garden-area": Optional[int],
        "equipped-kitchen": Optional[bool],
        "full-address": Optional[str],
        "swimmingpool": Optional[bool],
        "furnished": Optional[bool],
        "open-fire": Optional[bool],
        "terrace": Optional[bool],
        "terrace-area": Optional[int],
        "facades-number": Optional[int],
        "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
    }"""
    return data_format

@app.route('/', methods = ['GET'])
def alive():
    return 'alive'

@app.route('/predict', methods = ['POST', 'GET'])
def login():
    # POST
    if request.method == 'POST':
        data = request.get_json()

        processed_features = cleaning_data.preprocess(data)
        prediction = model.predict(processed_features)

        return jsonify(prediction = prediction[0])
    
    # GET
    else:
        return get_expected_data_format()

if __name__=='__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)