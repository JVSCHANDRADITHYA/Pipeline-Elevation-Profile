
import zipfile
import matplotlib.pyplot as plt
import os

def extract_kml_from_kmz(kmz_file, output_dir):
    with zipfile.ZipFile(kmz_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

if __name__ == '__main__' :
    # Example usage
    kmz_file_path = 'E:\\project_pipline\\resources\\OIL 4 STEEL MOC Red Stag.kmz'
    output_dir = 'E:\\project_pipline\\resources'

    extract_kml_from_kmz(kmz_file_path, output_dir)


