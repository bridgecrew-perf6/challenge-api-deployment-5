mandatory_features = ['property-type', 'area', 'rooms-number', 'zip-code']
optional_features = ['land-area', 'garden', 'garden-area', 'equipped-kitchen',
    'full-address', 'swimmingpool', 'furnished', 'open-fire', 'terrace',
    'terrace-area', 'facades-number', 'building-state']


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

# def preprocess(house_data):
#     return processed_features