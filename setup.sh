# # idea from 
# https://medium.com/@barua.aindriya/visualize-data-on-a-choropleth-map-with-geopandas-and-matplotlib-924cedd8e9cb

# 1. Set Up Virtual Env
python -m venv venv      
venv\scripts\activate

# 2. Installations 
# has to download pipwin since some stuff works terrible on windows. 
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal 

pip install xlrd
pip install pandas
pip install seaborn 
pip install matplotlib
pip install numpy
pip install descartes
pip install pyshp

pip install wheel

pip install pipwin

pipwin install gdal
pipwin install fiona
pipwin install geopandas


# 3. test
python 
import xlrd
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import geopandas as gpd

# 4 - create requirments.txt
pip freeze > requirements.txt

# 5 - deactivate
deactivate


# 6 - get date from 

https://map.igismap.com/share-map/export-layer/Indian_States/06409663226af2f3114485aa4e0a23b4