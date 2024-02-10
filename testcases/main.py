# import requests
# import pandas as pd

# def get_elevation(lat, long):
#     query = ('https://api.open-elevation.com/api/v1/lookup?locations='+ f'{lat},{long}')
#     r = requests.get(query).json()  # json object, various ways you can extract value
#     elevations = [result['elevation'] for result in r['results']]
#     return elevations
    
# print(get_elevation(32.49446154936118, -103.6139956127073))

# def get_distance(lat, long):
    
    
for x in range(0, 10, 1):
    print(x)