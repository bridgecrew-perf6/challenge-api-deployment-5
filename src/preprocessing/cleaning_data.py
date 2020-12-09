import json
import jsonschema

import numpy as np


def validate_JSON(json_to_test: dict, json_schema_filepath: str) -> tuple:
    """Validates a JSON according to a specified schema
    Args:
        json_to_test: dictionnary representing the JSON to test
        json_schema_filepath: filepath to a JSON object representing to schema to validate against
    Returns:
        Tuple whose 1st element is True if the JSON is in the right format, False otherwise
        and whose 2d element is either None if 1st element is True and a string explaining
        the error if False
    """
    with open(json_schema_filepath, "r") as file:
        schema = json.load(file)

    try:
        jsonschema.validate(json_to_test, schema)
    except Exception as valid_err:
        return (False, valid_err)
    else:
        return (True, None)


def to_region(postcode: str) -> str:
    """Converts a Belgian postal code to the corresponding region
    Args:
        postcode: Belgian postal code
    Returns:
        Letter corresponding to the region
    """
    # casting: 'str' -> 'int' if necessary
    postcode = int(postcode)
    # 'B' -> Brussels-Capital Region
    # 'W' -> Walloon Region
    # 'F' -> Flemish Region
    if 1000 <= postcode and postcode <= 1299:
        region = 'B'
    elif (1300 <= postcode and postcode <= 1499) or (4000 <= postcode and postcode <= 7999):
        region = 'W'
    else:
        region = 'F'
    return region

def preprocess(data: dict) -> (np.ndarray, bool):
    """Preprocesses the property features
    Args:
        data: feature of a real estate property already verified to be correctly formatted
    Returns:
        array containing the processed features
         
    """
    property_data = data['data']

    final_features = np.empty(10)

    #final_features[0] => house_is
    final_features[0] = np.float64(0) if property_data['property-type'] != 'HOUSE' else np.float64(1)
    #final_features[1] => rooms_number
    final_features[1] = np.float64(property_data['rooms-number'])
    #final_features[2] => area 
    final_features[2] = np.float64(property_data['area'])
    #final_features[4] => B
    #final_features[5] => F
    #final_features[6] => W 
    region = to_region(property_data['zip-code'])
    if region == 'B':
        final_features[4] = np.float64(1)
        final_features[5] = np.float64(0)
        final_features[6] = np.float64(0)
    elif region == 'F':
        final_features[4] = np.float64(0)
        final_features[5] = np.float64(1)
        final_features[6] = np.float64(0)
    else:
        final_features[4] = np.float64(0)
        final_features[5] = np.float64(0)
        final_features[6] = np.float64(1)
    
    # checking if optionnal 'equipped-kitchen' was given before using it
    if 'equipped-kitchen' in property_data:
        # final_features[3] => equipped_kitchen_has
        final_features[3] = np.float64(1) if property_data['equipped-kitchen'] else np.float64(0)
    else:
        # we tag a non given optionial features with np.nan
        final_features[3] = np.nan
    
    # checking if optionnal 'building-state' was given before using it
    # final_features[7] => good
    # final_features[8] => renovated
    # final_features[9] => to_renovate
    if 'building-state' in property_data:
        if property_data['building-state'] == 'GOOD':
            final_features[7] = np.float64(1)
            final_features[8] = np.float64(0)
            final_features[9] = np.float64(0)
        elif property_data['building-state'] == 'TO RENOVATE' or property_data['building-state'] == 'TO REBUILD':
            final_features[7] = np.float64(0)
            final_features[8] = np.float64(0)
            final_features[9] = np.float64(1)
        # elif property_data['building-state'] == 'JUST RENOVATED' or property_data['building-state'] == 'NEW':
        else:
            final_features[7] = np.float64(0)
            final_features[8] = np.float64(1)
            final_features[9] = np.float64(0)
    
    return final_features
