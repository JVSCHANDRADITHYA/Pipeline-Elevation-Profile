# Pipeline-Elevation-Profile
 The Pipeline Elevation Profile Mapping Project aims to create a comprehensive and visually intuitive representation of the elevation profile along a pipeline route. This project leverages Geographic Information System (GIS) technologies to generate detailed elevation profiles, which are then saved and shared in the Keyhole Markup Language (KMZ) file format.

![alt text](image-1.png)

OIL Pipeline project for Indian Reservation in Stanfield


RUN THIS REPO :

Clone this repository onto your local machine:
```bash
git clone https://github.com/JVSCHANDRADITHYA/Pipeline-Elevation-Profile.git
cd Pipeline-Elevation-Profile
```
Execute the following command to install the required dependencies:
``` bash
 python -r req.txt
```
For optimal isolation, it is recommended to create a conda environment with a minimum Python version of 3.11 (optional step):
``` bash
 conda create -n project_pipeline python=3.11
```

Run the main script with the specified parameters:
```bash
 python main.py --dataroot (FILE PATH) --interval (interval value)
