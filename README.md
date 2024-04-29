# WSI-PeruDB [![DOI](https://zenodo.org/badge/747418826.svg)](https://zenodo.org/doi/10.5281/zenodo.10558511)
This package allows users to access the Water Stable Isotope Database in Peru. It includes 464 stations over Peru, updated until 2023, and provides an interactive map for exploring the spatial distribution of all the stations. Additionally, it offers features for technical validation and display temporal series for each station and department across Peru.

## How to use it 
First, users must install the package WSIPeruDB: 

```
pip install WSIPeruDB
```
After that, in order to view the spatial distribution of stable isotope stations, users must run the following command: 

```
import wsiperudb
wsiperudb.generate_map()
```
<div align="left">
    <img src="images/map.png" alt="map" width="500" height="500">
  </a>
    
To get information from every department, users must import the 'department_information' module. This allows them to check if the dataset is stored in the WSIPeruDB or in another database.
    
```
wsiperudb.department_information()
```

<div align="left">
    <img src="images/information.png" alt="map" width="300" height="200">
  </a>

In order to plot the Linear Meteoric Water Line (LMWL) for every station, department, and sample type, users must run the following command:

```
wsiperudb.plot_lmwl()
```
<div align="left">
    <img src="images/lmwl.png" alt="map" width="300" height="200">
  </a>

The temporal series for every station and histogram for all data in each department, users must run the following commnad: 

```
wsiperudb.analize_temporal_series()
```
<div align="left">
    <img src="images/histogram.png" alt="map" width="300" height="200">
  </a>
<div align="left">
    <img src="images/temporalseries.png" alt="map" width="300" height="200">
  </a>

WSIPeruDB offers users the ability to compare temporal series from every department and sample type, taking into account both summer and winter seasons:

```
wsiperudb.compare_departments()
```
<div align="left">
    <img src="images/comparing.png" alt="map" width="300" height="200">
  </a>

Users can download dataset information for each department or station, based on their respective sample types.

```
wsiperudb.download_dataset()
```
<div align="left">
    <img src="images/dataset_download.png" alt="map" width="300" height="200">
  </a>

Finally, users can download site information for each department or station, based on their respective sample types.

```
wsiperudb.download_site_information()
```
<div align="left">
    <img src="images/iteinformation_download.png" alt="map" width="500" height="500">
  </a>


## GeoJson 
To display comprehensive information about each station on an interactive map, we create a geojson called site_information.geojson file. Additionally, about the peru_departamental_simple.geojson file, we are using it from this [github](https://github.com/juaneladio/peru-geojson) 

## Add data
We encourage users to send their data to the following email address: japaestegui@igp.gob.pe, using the metadata template named 'WSI-PeruDB_template.xlsx' to add their station's information and dataset to the database. Additionally, please include the following details in the email:
- User's Name
- Institution or Company Name
- Country
- Email address

## Download Data
Users must fill the request through this google forms. This is necessary for us to maintain statistics about the database. 
