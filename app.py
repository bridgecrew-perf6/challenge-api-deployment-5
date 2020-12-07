import os
from flask import Flask, request, jsonify

from sklearn.preprocessing import MinMaxScaler, RobustScaler

from src.preprocessing import cleaning_data
from src.model.modeling import Polynomial_regression_model

app = Flask(__name__)

def get_expected_data_format():
    data_format = """Please make a POST request with a JSON object of this format:
    {
        "data": {
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
            "  terrace": Optional[bool],
            "terrace-area": Optional[int],
            "facades-number": Optional[int],
            "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
        }
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

        if 'data' not in data:
            response = jsonify(error='formatting_error')
        
        else:
            property_data = data['data']

            processed_features, featuresMissing = cleaning_data.preprocess(property_data)

            if featuresMissing:
                response = jsonify(error='features_missing')

            else:
                predicted_price = model.predict_single_point(processed_features)
                prediction = {
                    'price': predicted_price,
                    'r2_score': model.get_test_r2_score()
                }
                
                response = jsonify(prediction=prediction)
    
    # GET
    else:
        response = get_expected_data_format()
    
    return response

if __name__ == '__main__':
    model = Polynomial_regression_model('src/model/dataset.csv', RobustScaler(), 3)

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)