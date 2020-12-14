import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from sklearn.preprocessing import MinMaxScaler, RobustScaler

from src.preprocessing import cleaning_data
from src.model.modeling import Polynomial_regression_model

app = Flask(__name__)
CORS(app)


def get_expected_data_format() -> str:
    """Returns the expected format of the POST method input
    Returns:
        The expected format
    """
    data_format = """Please make a POST request with a JSON object of this format:
    {
        "data": {
            "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
            "area": int,
            "rooms-number": int,
            "zip-code": int,
            "garden": Optional[bool],
            "garden-area": Optional[int],
            "terrace": Optional[bool],
            "terrace-area": Optional[int],
            "facades-number": Optional[int],
            "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"],
            "equipped-kitchen": Optional[bool],
            "furnished": Optional[bool],
            "open-fire": Optional[bool],
            "swimmingpool": Optional[bool],
            "land-area": Optional[int],
            "full-address": Optional[str]
        }
    }"""
    return data_format

@app.route('/', methods = ['GET'])
def alive():
    """'/' route function
    Returns:
        'alive'
    """
    return 'alive'

@app.route('/predict', methods = ['POST', 'GET'])
def prediction():
    """'/predict' route function for the 'POST' and 'GET'
    Args:
        postcode (str): Belgian postal code
    Returns:
        JSON object and HTTP status code as the output of the 'POST' request 
        or the expected format of the 'POST' input for the 'GET' request
    """
    # POST
    if request.method == 'POST':
        data = request.get_json()

        input_valid = cleaning_data.validate_JSON(data, "./assets/input_schema.json")

        if not input_valid[0]:
            # modification of error string to make it readable in one line
            error_message = str(input_valid[1])
            error_message = error_message.replace('\n\n', '    ')
            error_message = error_message.replace('\n', ' ')

            response = jsonify(error=error_message), 400

        else:
            processed_features = cleaning_data.preprocess(data)

            predicted_price = model.predict_single_point(processed_features)
            prediction = {
                'price': predicted_price,
                'r2_score': model.get_test_r2_score()
            }
            
            response = jsonify(prediction=prediction), 200
    

        return response
    
    # GET
    else:
        return get_expected_data_format()

if __name__ == '__main__':
    model = Polynomial_regression_model('src/model/dataset.csv', RobustScaler(), 3)

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)