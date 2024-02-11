# Pipeline-Elevation-Profile
 The Pipeline Elevation Profile Mapping Project aims to create a comprehensive and visually intuitive representation of the elevation profile along a pipeline route. This project leverages Geographic Information System (GIS) technologies to generate detailed elevation profiles, which are then saved and shared in the Keyhole Markup Language (KMZ) file format.

![alt text](image-1.png)

OIL Pipeline project for Indian Reservation in Stanfield


Pipeline Elevation Profile
Overview

This repository contains a Python script for extracting coordinates and elevations from a KMZ file, generating an elevation profile along a pipeline route.
Usage
Prerequisites

    Python 3.11
    Git

Clone Repository

bash

git clone https://github.com/JVSCHANDRADITHYA/Pipeline-Elevation-Profile.git
cd Pipeline-Elevation-Profile

Set Up Environment

bash

# (Optional) Create a conda environment
conda create -n project_pipeline python=3.11
conda activate project_pipeline

Install Dependencies

bash

pip install -r requirements.txt

Run Main Script

bash

python main.py --kmz_file_path (KMZ FILE PATH) --interval (INTERVAL VALUE)

Replace (KMZ FILE PATH) with the path to your KMZ file and (INTERVAL VALUE) with the desired interval value.
