import xlrd
import random
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import mapclassify
import shapely

sns.set_style('whitegrid')
# DATA_PATH               = './data/data2.xlsx'
SHAPE_PATH              = "./shapefiles/Europe.shp"
map_df                  = gpd.read_file(SHAPE_PATH)
map_df.head()

map_df['DATA'] = np.random.randint(1, 600, map_df.shape[0])





merged = map_df.set_index('NAME')
merged = merged.drop('Germany')


unique_list = merged.index.unique()
unique_list = [x for x in unique_list]


# merged = merged.drop(merged[merged['NAME'] == 'Germany'].index[0])

fig, ax = plt.subplots(1, figsize=(15,10))
ax.set_xticks([])
ax.set_yticks([])

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list('trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),cmap(np.linspace(minval, maxval, n)))
    return new_cmap

cmap = plt.get_cmap('RdPu')
new_cmap = truncate_colormap(cmap, 0.3, 1)

merged.plot(column='DATA',
            cmap=new_cmap,
            scheme='QUANTILES', k=10,
            linewidth=0.9,
            ax=ax,
            edgecolor='1',
            legend=True, 
            # missing_kwds={"color": "lightgrey", "label": "Missing values",},
            legend_kwds={'loc': 'center left', 'bbox_to_anchor':(1,0.5)}
            )


merged['coords'] = merged['geometry'].apply(lambda x: x.representative_point().coords[:])
merged['coords'] = [coords[0] for coords in merged['coords']]
for index, row in merged.iterrows():
    plt.annotate(text=index, xy=row['coords'], horizontalalignment='center', size=5, color='black')


plt.title('öoghbögubh Title', loc='left', size="10")
plt.xlabel('source:  https://www.lfd.uci.edu/~gohlke/pythonlibs/', loc="left", size="8")
plt.savefig('result.png')


