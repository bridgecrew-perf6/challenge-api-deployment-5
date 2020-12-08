import numpy as np

import jsonschema

# definitions of mandatory and optional features names
mandatory_features = ['property-type', 'area', 'rooms-number', 'zip-code']
optional_features = ['land-area', 'garden', 'garden-area', 'equipped-kitchen',
    'full-address', 'swimmingpool', 'furnished', 'open-fire', 'terrace',
    'terrace-area', 'facades-number', 'building-state']


def all_mandatory_features_there(property_data: dict , mandatory_features: list) -> bool:
    """Checks if no mandatory feature is ommitted
    Args:
        property_data: the features of a property
        mandatory_features: the names of the mandatory features for the prediction
    Returns:
        True if all the mandatory features are there, False otherwise
    """
    all_there = True
    for feature in mandatory_features:
        all_there = all_there and feature in property_data
    return all_there

def to_region(postcode: str) -> str:
    """Converts a Belgian postal code to the corresponding region
    Args:
        postcode (str): Belgian postal code
    Returns:
        Letter corresponding to the region
    """
    #casting: 'str' -> 'int' if necessary
    postcode = int(postcode)
    #'B' -> Brussels-Capital Region
    #'W' -> Walloon Region
    #'F' -> Flemish Region
    if 1000 <= postcode and postcode <= 1299:
        region = 'B'
    elif (1300 <= postcode and postcode <= 1499) or (4000 <= postcode and postcode <= 7999):
        region = 'W'
    else:
        region = 'F'
    return region

def preprocess(property_data: dict) -> (np.ndarray, bool):
    """Preprocesses the property features
    Args:
        property_data: feature of a real estate property
    Returns:
        array containing the processed features
         
    """
    final_features = np.empty(10)
    featuresMissing = False

    if all_mandatory_features_there(property_data, mandatory_features):
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
        #final_features[7] => good
        #final_features[8] => renovated
        #final_features[9] => to_renovate
        if property_data['building-state'] == 'GOOD':
            final_features[7] = np.float64(1)
            final_features[8] = np.float64(0)
            final_features[9] = np.float64(0)
        elif property_data['building-state'] == 'TO RENOVATE' or property_data['building-state'] == 'TO REBUILD':
            final_features[7] = np.float64(0)
            final_features[8] = np.float64(0)
            final_features[9] = np.float64(1)
        #elif property_data['building-state'] == 'JUST RENOVATED' or property_data['building-state'] == 'NEW':
        else:
            final_features[7] = np.float64(0)
            final_features[8] = np.float64(1)
            final_features[9] = np.float64(0)
        
        if 'equipped-kitchen' in property_data:
            #final_features[3] => equipped_kitchen_has
            final_features[3] = np.float64(1) if property_data['equipped-kitchen'] else np.float64(0)
        else:
            # we tag a non given optionial features with np.nan
            final_features[3] = np.nan
    
    else:
        featuresMissing = True
    
    return final_features, featuresMissing

# def validateJSON(JSONschema_filepath):
