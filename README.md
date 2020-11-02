# House_3D_API

## 1. Purpose and project objectives 

### Purpose
- [x] To model a house in 3D from lidar satellite images (geoTIFFs file) by only entering a home address

### Pitch of the project 
Put yourself in the shoes of a company, active in the Geospatial industy and whose purpose is to use lidar satellite image data to launch a new branch in the insurrance business. With this respect, the company needs you to build a solution with these data to model buildings in 3D with by only entering a home address.

What is LIDAR ? LIDAR stands for Light Detection and Ranging and is a remote sensing method used to examine the surface of the Earth. LIDAR is a remote sensing method that uses light in the form of a pulsed laser to measure ranges (variable distances) to the Earth. The device will illuminate a target with a laser light and a sensor will measure the reflection. Differences in wavelength and return times will be used to get 3D representations of an area.

### Objectives
- [x] Consolidate the knowledge in Python, specifically in : NumPy, Pandas, Matplotlib
- [x] To be able to search and implement new librairies
- [x] To be able to read and use shapefiles
- [x] To be able to read and use geoTIFFs
- [x] To be able to render a 3D plot
- [x] To be able to construct the project with object-oriented programming (OOP)
- [x] To be able to implement the whole project - and make it functioning -  through an API
- [x] To be able to present a final product

### Features 
#### Must-have 
- [x] 3D lookup of houses

#### Nice-to-Have
- [x] Optimize your solution to have the result as fast as possible.
- [x] Better visualization
- [x] 3D Belgium's monuments i.e church, etc.

## 2. The project 
### Working plan and steps 
#### 1. Research 
- [x] Research and understand the term, concept and requirement of the project.
- [x] Discover new libraries that can serve the project purposes 
  - geopy - convert physical addresses to Geographic locations
  - folium - plot address on a map
  - rasterio - read and write GEOTIFF format file
  - pyproj - performs cartographic transformations and geodetic computations
  - rioarray - rasterio xarray extension (xarray - working with labelled multi-dimensional arrays)
  - matplotlib (mpl_toolkits.mplot3d Axes3D) - plot 3D objects on a 2D matplotlib figure
  - open3d - a modern library for 3D data processing
  - shapefile - provide read and write support for Shapefile (.shp) format
  - geopandas - make working with geospatial data in python easier and extends the datatypes used by pandas to allow spatial operations on geometric types
  - earthpy - make it easier to plot and work with spatial raster and vector data using open source tools
  - fiona - provide read and write support to real-world data using multi-layered GIS formats and integrates readily with other Python GIS packages such as pyproj and Shapely
  - cartopy - designed for geospatial data processing in order to produce maps and other geospatial data analyses
  - shapely - provide support for manipulation and analysis of planar geometric objects
  - gdal - translator library for raster and vector geospatial data formats

#### 2. Data collection 
- [x] [DTM file for Flandre including Brussels](http://bit.ly/DTM_Flandre)
- [x] [DSM file for Flandre including Brussels](http://bit.ly/DSM_Flandre)
- [x] [Shapefiles with cadastral maps and parcels](https://eservices.minfin.fgov.be/myminfin-web/pages/cadastral-plans?_ga=2.167466685.225309318.1604313780-388788923.1602907232)

#### 3. Python procedural programming 
- [x] Programming python command and function for each step of the process flow, i.a.:
  - Returning CRS coordinates (epsg: WSG84 and 31370) from address input command 
  - Identifying right .tif or shp. from CRS coordinates
  - Locate property from CRS coordinates
  - Cropping .tif file with self-made shapes (e.g. polygon) or with cadastral .shp file geometries 
  - Constructing 3D point cloud files from cropped .tif file
  - Using various algorithms (i.a. poisson, pall-pivoting,...) to generate 3D meshes from point clouds or to improve 3D visualization  

- [x] Testing and fine-tuning code for improving readability, effacy and/or execution speed

see, [notebooks with single commands and functions](https://github.com/jcmeunier77/House_3D_API/tree/master/notebooks%20with%20single%20commands%20and%20functions), for further details 

#### 4. Python object-oriented programming
- [x] Deploying each single procedural commands into four coherent and consistent objects : 
    - [a_addres_to_crs.py](https://github.com/jcmeunier77/House_3D_API/blob/master/api/src/utils/a_addres_to_crs.py) : returns CRS coordinates from input address
    - [b_crs_to_tif.py](https://github.com/jcmeunier77/House_3D_API/blob/master/api/src/utils/b_crs_to_tif.py) : uses encoded CRS coordinate to locate the right .tif or .shp file
    - [c_file_to_pix.py](https://github.com/jcmeunier77/House_3D_API/blob/master/api/src/utils/c_file_to_pix.py) : return 3D visualization from cropped .tif files
    - [d_target_to_map.py](https://github.com/jcmeunier77/House_3D_API/blob/master/api/src/utils/d_target_to_map.py) : save a folium map as .html file from CRS coordinates
 - [x] Constructing a 'meta' object for dispatching commands to base objects
 - [x] Designing a Flask API for linking an .html interface to project objects 
    - with 2 routes : one for opening the address form (see next section) and one for render folium map .html template
    - rem: the 3d visualization being open as a separate open3D object  
 
 #### 5. Designing user friendly interface with form and buttons 
 - [x] Using CSS/HTML and adapted from available [bootstrap](https://v5.getbootstrap.com/) templates and codes  
 - [x] Form :
    - for encoding address
 - [x] Buttons :
    - 'Locate building on map' : opens folium .html map in new window  
    - 'View 3D reconstruction' : opens the open3D object in a separate object 
   
#### 6. Wrapping up things 
- [x] Linking the .html interface with the API with some javascript code 
    - by clicking on the interface buttons the interface communicates with the API for lauching the desired commands 
- [x] Linking each blocks of the project and ensuring an efficient communication between them 

### Project structure and process flow

to incorporate : flowshart with process flow 

### Project output 
#### Screenshot of the .html interface 

<p align="center">
    <img src="https://github.com/jcmeunier77/House_3D_API/blob/master/screenshots/main-index%20page%20.png">
</p>

#### Screenshot of the folium map 

<p align="center">
    <img src="https://github.com/jcmeunier77/House_3D_API/blob/master/screenshots/map%20output.png">
</p>

#### Screenshot of the 3D reconstruction 
<p align="center">
    <img src="https://github.com/jcmeunier77/House_3D_API/blob/master/screenshots/3d%20output.png">
</p>

### Pending 

- [x] To host the data on an online server.
- [x] To develop web application allowing client to type in any address in Belgium to view 3D houses.
- [x] To obtain latest LIDAR images so that new houses after 2014 can be rendered.
- [x] To incorporate cadastral plan of each property in the 3D rendering so that only the requested house is rendered.
- [x] To explore other 3D plotting libraries

  
