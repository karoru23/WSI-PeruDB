from setuptools import setup, find_packages

setup(
    name='WSIPeruDB',
    version='0.1.0.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'folium',
        'scikit-learn',
        'plotly_express',
        'ipywidgets',
        'geopandas',
        'openpyxl'
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    author='Carol Romero',
    author_email='romeroroldancarol@gmail.com',
    description='Water Stable Isotope Database in Peru',
    long_description='This package allows users to access the Water Stable Isotope Database in Peru. Provides an interactive map for exploring the spatial distribution of all the stations. Additionally, it offers features for technical validation and display temporal series for each station and department across Peru',
    url='https://github.com/karoru23/WSI-PeruDB',
)
