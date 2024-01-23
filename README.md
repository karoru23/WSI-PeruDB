# WSI-PeruDB
This Jupyter notebook with Python coding allows users to access the Water Stable Isotope Database in Peru. It includes 464 stations over Peru, updated until 2023, and provides an interactive map for exploring the spatial distribution of all the stations. Additionally, it offers features for technical validation and display temporal series for each station and department across Peru.

## Installation of Libraries
Before running WSI-PeruDB script it is necessary to install these libraries using [pip](https://pip.pypa.io/en/stable/): 

1. [MySQL Connector](https://pypi.org/project/mysql-connector-python/) for connecting to the database on the freeMySQLhosting platform:
```bash
pip install mysql-connector-python
```
2. Install [Pandas](https://pypi.org/project/pandas/):
```bash
pip install pandas
```
3. Install [Numpy](https://pypi.org/project/numpy/): 
```bash
pip install numpy
```
4. For an interactive map [Folium](https://pypi.org/project/folium/):
```bash
pip install folium
```
5. For the exploratory analysis [Scikit-Learn](https://pypi.org/project/scikit-learn/):
```bash
pip install scikit-learn
```
6. For graphics [Matplotlib](https://pypi.org/project/matplotlib/): 
```bash
pip install matplotlib
```
7. For interactive graphics [Plotly-Express](https://pypi.org/project/plotly-express/):
```bash
pip install plotly_express
```
8. For improved visualization of the stations' information [ipywidgets](https://pypi.org/project/ipywidgets/):
```bash
pip install ipywidgets
```
9. Install [Geopandas](https://pypi.org/project/geopandas/)
```bash
pip install geopandas
```
## GeoJson 
To display comprehensive information about each station on an interactive map, we create a geojson called site_information.geojson file. Additionally, about the peru_departamental_simple.geojson file, we are using it from this [github](https://github.com/juaneladio/peru-geojson) 

## Add data
We encourage users to send their data to the following email address: japaestegui@igp.gob.pe, using the metadata template named 'WSI-PeruDB_template.xlsx' to add their station's information and dataset to the database. Additionally, please include the following details in the email:
- User's Name
- Institution or Company Name
- Country
- Email address

## Download Data
Users must send an email to the following email address: japaestegui@igp.gob.pe, including the same email details mentioned earlier, to download the dataset. This is necessary for us to maintain statistics about the database. 
