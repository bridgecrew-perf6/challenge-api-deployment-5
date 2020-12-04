import numpy as np

mandatory_features = ['property-type', 'area', 'rooms-number', 'zip-code']
optional_features = ['land-area', 'garden', 'garden-area', 'equipped-kitchen',
    'full-address', 'swimmingpool', 'furnished', 'open-fire', 'terrace',
    'terrace-area', 'facades-number', 'building-state']


def all_mandatory_features_there(property_data, mandatory_features):
    all_there = True
    for feature in mandatory_features:
        all_there = all_there and feature in property_data
    return all_there

def to_region(postcode):
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

def preprocess(property_data):
    #shape (1,2) is expected by the prediction model
    final_features = np.empty(10).reshape(1,-1)

    #final_features[0][0] => house_is
    final_features[0][0] = np.float64(0) if property_data['property-type'] != 'HOUSE' else np.float64(1)
    #final_features[1] => rooms_number
    final_features[0][1] = np.float64(property_data['rooms-number'])
    #final_features[0][2] => area 
    final_features[0][2] = np.float64(property_data['area'])
    #final_features[0][3] => equipped_kitchen_has
    final_features[0][3] = np.float64(1) if property_data['equipped-kitchen'] else np.float64(0)
    #final_features[0][4] => B
    #final_features[0][5] => F
    #final_features[0][6] => W 
    region = to_region(property_data['zip-code'])
    if region == 'B':
        final_features[0][4] = np.float64(1)
        final_features[0][5] = np.float64(0)
        final_features[0][6] = np.float64(0)
    elif region == 'F':
        final_features[0][4] = np.float64(0)
        final_features[0][5] = np.float64(1)
        final_features[0][6] = np.float64(0)
    else:
        final_features[0][4] = np.float64(0)
        final_features[0][5] = np.float64(0)
        final_features[0][6] = np.float64(1)
    #final_features[0][7] => good
    #final_features[0][8] => renovated
    #final_features[0][9] => to_renovate
    if property_data['building-state'] == 'GOOD':
        final_features[0][7] = np.float64(1)
        final_features[0][8] = np.float64(0)
        final_features[0][9] = np.float64(0)
    elif property_data['building-state'] == 'TO RENOVATE' or property_data['building-state'] == 'TO REBUILD':
        final_features[0][7] = np.float64(0)
        final_features[0][8] = np.float64(0)
        final_features[0][9] = np.float64(1)
    #elif property_data['building-state'] == 'JUST RENOVATED' or property_data['building-state'] == 'NEW':
    else:
        final_features[0][7] = np.float64(0)
        final_features[0][8] = np.float64(1)
        final_features[0][9] = np.float64(0)
    
    return final_features