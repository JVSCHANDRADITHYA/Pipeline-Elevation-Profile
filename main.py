import xml.etree.ElementTree as ET
import zipfile
import requests
import pandas as pd
from geopy.distance import geodesic

start = []

def range1(initial, final, step):
    return range(initial, final + step, step)



def get_elevation(lat, long):
    query = ('https://api.open-elevation.com/api/v1/lookup?locations='+ f'{lat},{long}')
    # print(query)
    r = requests.get(query).json()  # json object, various ways you can extract value
    elevations = [result['elevation'] for result in r['results']]
    # print(elevation)
    return elevations

def extract_coordinates_from_kmz(kmz_file_path, interval=300):
    # Open the KMZ file and extract the KML content
    with open(kmz_file_path, 'rb') as kmz_file:
        with zipfile.ZipFile(kmz_file) as kmz:
            kml_file_name = [name for name in kmz.namelist() if name.endswith('.kml')][0]
            with kmz.open(kml_file_name) as kml_file:
                kml_content = kml_file.read()

    root = ET.fromstring(kml_content)
    
    # Find the coordinates in the KML file
    coordinates = []

    for coordinates_elem in root.iter('{http://www.opengis.net/kml/2.2}coordinates'):
        coordinates.extend(coordinates_elem.text.strip().split())
    
    # Extract starting and ending points
    start_point = coordinates[0].split(',')
    start.append(start_point)
    end_point = coordinates[-1].split(',')
    print(start_point, end_point)
    start_longitude, start_latitude, start_altitude = map(float, start_point)
    end_longitude, end_latitude, end_altitude = map(float, end_point)

    interpolated_coordinates = []
    interpolated_elevations = []

    for distance in range1(0, int(geodesic((start_latitude, start_longitude), (end_latitude, end_longitude)).meters), interval):
        fraction = distance / geodesic((start_latitude, start_longitude), (end_latitude, end_longitude)).meters
        interpolated_latitude = start_latitude + fraction * (end_latitude - start_latitude)
        interpolated_longitude = start_longitude + fraction * (end_longitude - start_longitude)
        interpolated_coordinates.append((interpolated_latitude, interpolated_longitude))

        # Interpolate elevations
        interpolated_elevation = get_elevation(interpolated_latitude, interpolated_longitude)
        interpolated_elevations.append(interpolated_elevation)

    return {
        'interpolated_coordinates': interpolated_coordinates,
        'interpolated_elevations': interpolated_elevations
    }

# Example usage
kmz_file_path =                                 # GIVE YOUR PATHH
interval = 300                                  # change this for the desired value
result = extract_coordinates_from_kmz(kmz_file_path, interval)

start_lat = start[0][1]
start_long =  start[0][0]


print(f"Interpolated Coordinates and Elevations every {interval} meters:")
for i, (coord, elevations) in enumerate(zip(result['interpolated_coordinates'], result['interpolated_elevations'])):
    print(f"Point {i + 1}: Latitude: {coord[0]}, Longitude: {coord[1]}, Elevations: {elevations}, DISTANCE : {geodesic((start_lat, start_long), (coord[0], coord[1]))}")
