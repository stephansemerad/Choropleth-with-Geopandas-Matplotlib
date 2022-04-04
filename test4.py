import xlrd
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import mapclassify
import warnings
import shapely
import libpysal

# from shapely.errors import ShapelyDeprecationWarning
# warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 
# # https://www.lfd.uci.edu/~gohlke/pythonlibs/

    
sns.set_style('whitegrid')
DATA_PATH               = './data/data2.xlsx'
SHAPE_PATH              = "./shapefiles/Comuna.shp"
df                      = pd.read_excel(DATA_PATH)
map_df                  = gpd.read_file(SHAPE_PATH)

merged = map_df.set_index('NOM_COMUNA').join(df.set_index('NOM_COMUNA'))
fig, ax = plt.subplots(1, figsize=(15,10))

# ax.axis('off')
ax.set_xticks([])
ax.set_yticks([])




def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list('trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),cmap(np.linspace(minval, maxval, n)))
    return new_cmap

cmap = plt.get_cmap('RdPu')
new_cmap = truncate_colormap(cmap, 0.3, 1)

merged.plot(column='INMIGRANTES',
            cmap=new_cmap,
            scheme='QUANTILES', k=8,
            # linewidth=0.9,
            ax=ax,
            # edgecolor='1',
            legend=True, 
            missing_kwds={"color": "lightgrey", "label": "Missing values",},
            legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1,0.5)}
            
            )


merged.plot(column='INMIGRANTES',
            cmap=new_cmap,
            scheme='QUANTILES', k=10,
            # linewidth=0.9,
            ax=ax,
            # edgecolor='1',
            # legend=True, 
            missing_kwds={"color": "lightgrey", "label": "Missing values",},
            # legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1,0.5)}
            
            )


data = merged.index
districts = [i.title() for i in data]


merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
merged['coords'] = [coords[0] for coords in merged['coords']]
for index, row in merged.iterrows():
    plt.annotate(text=index, xy=row['coords'], horizontalalignment='center', size=5, color='black')


plt.title('öoghbögubh Title', loc='left', size="10")
plt.xlabel('source:  https://www.lfd.uci.edu/~gohlke/pythonlibs/', loc="left", size="8")
plt.savefig('result.png')


