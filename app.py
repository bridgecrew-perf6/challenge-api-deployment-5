from flask import Flask, jsonify
from flask import redirect, url_for, request

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
        "swimmingpool": Opional[bool],
        "furnished": Opional[bool],
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

if __name__ == '__main__':
    app.run(debug = True) 