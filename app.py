import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_prediction(data):
    output_example  = {
        "prediction": 140000,
        "error": "no error"
    }
    return output_example

def preprocess_data(data):
    return data

def get_expected_data_format():
    data_format = """{
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
        data = preprocess_data(data)
        prediction = get_prediction(data)
        return jsonify(prediction)
    
    # GET
    else:
        return get_expected_data_format()

port = int(os.environ.get("PORT", 5000))

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=port)