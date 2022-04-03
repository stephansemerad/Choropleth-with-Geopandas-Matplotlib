import xlrd
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import shapefile
import os

os.system('cls')


def read_shapefile(sf):
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df


df      = pd.read_excel('./data/data2.xlsx')
title   = 'Population Distrubution on Santiago Metropolitan Region'
data    = df.PERSONAS
names   = df.NOM_COMUNA
sf = shapefile.Reader("./shapefiles/comuna.shp")
color_options =  ['#dadaebFF','#bcbddcF0','#9e9ac8F0', '#807dbaF0','#6a51a3F0','#54278fF0']; 
new_data, bins = pd.qcut(data, 6, retbins=True, labels=list(range(6)))
color_ton = [] # TODO List Comprehension
for val in new_data: color_ton.append(color_options[val]) 
figsize = (11,9)
plt.figure(figsize = figsize)
fig, ax = plt.subplots(figsize = figsize)
fig.suptitle(title, fontsize=16)

for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')



plot_comunas_data(sf, title, names, data, 2, True)

plot_map_fill_multiples_ids_tone(sf, title, [], 
                                     false, 
                                     color_ton, 
                                     bins, 
                                     x_lim = None, 
                                     y_lim = None, 
                                     figsize = (11,9));

df = read_shapefile(sf)

plt.show()


# sns.set_style('whitegrid')
# sns.set(style='whitegrid', palette='pastel', color_codes=True)
# sf = shapefile.Reader("./shapefiles/comuna.shp")
# len(sf.shapes())


# def read_shapefile(sf):
#     fields = [x[0] for x in sf.fields][1:]
#     records = sf.records()
#     shps = [s.points for s in sf.shapes()]
#     df = pd.DataFrame(columns=fields, data=records)
#     df = df.assign(coords=shps)
#     return df

# def plot_shape(id, s=None):
#     """ PLOTS A SINGLE SHAPE """
#     plt.figure()
#     ax = plt.axes()
#     ax.set_aspect('equal')
#     shape_ex = sf.shape(id)
#     x_lon = np.zeros((len(shape_ex.points),1))
#     y_lat = np.zeros((len(shape_ex.points),1))
#     for ip in range(len(shape_ex.points)):
#         x_lon[ip] = shape_ex.points[ip][0]
#         y_lat[ip] = shape_ex.points[ip][1]
#     plt.plot(x_lon,y_lat) 
#     x0 = np.mean(x_lon)
#     y0 = np.mean(y_lat)
#     plt.text(x0, y0, s, fontsize=10)
#     # use bbox (bounding box) to set plot limits
#     plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
#     return x0, y0

# def plot_map(sf, x_lim = None, y_lim = None, figsize = (11,9)):
#     '''
#     Plot map with lim coordinates
#     '''
#     plt.figure(figsize = figsize)
#     id=0
#     for shape in sf.shapeRecords():
#         x = [i[0] for i in shape.shape.points[:]]
#         y = [i[1] for i in shape.shape.points[:]]
#         plt.plot(x, y, 'k')
        
#         if (x_lim == None) & (y_lim == None):
#             x0 = np.mean(x)
#             y0 = np.mean(y)
#             plt.text(x0, y0, id, fontsize=10)
#         id = id+1
    
#     if (x_lim != None) & (y_lim != None):     
#         plt.xlim(x_lim)
#         plt.ylim(y_lim)

# def plot_map2(id, sf, x_lim = None, y_lim = None, figsize=(11,9)):
#     '''
#     Plot map with lim coordinates
#     '''
   
#     plt.figure(figsize = figsize)
#     for shape in sf.shapeRecords():
#         x = [i[0] for i in shape.shape.points[:]]
#         y = [i[1] for i in shape.shape.points[:]]
#         plt.plot(x, y, 'k')
        
#     shape_ex = sf.shape(id)
#     x_lon = np.zeros((len(shape_ex.points),1))
#     y_lat = np.zeros((len(shape_ex.points),1))
#     for ip in range(len(shape_ex.points)):
#         x_lon[ip] = shape_ex.points[ip][0]
#         y_lat[ip] = shape_ex.points[ip][1]
#     plt.plot(x_lon,y_lat, 'r', linewidth=3) 
    
#     if (x_lim != None) & (y_lim != None):     
#         plt.xlim(x_lim)
#         plt.ylim(y_lim)


# def show_one_comuna():
#     df = read_shapefile(sf)
#     comuna = 'SANTIAGO'
#     com_id = df[df.NOM_COMUNA == comuna].index[0]
#     plot_shape(com_id, comuna)
#     plt.show()


# def show_map():
#     df = read_shapefile(sf)
#     y_lim = (-33.7,-33.3) # latitude 
#     x_lim = (-71, -70.25) # longitude
#     plot_map(sf, x_lim, y_lim)
#     plt.show()

# def show_map_highlight():
#     df = read_shapefile(sf)
#     y_lim = (-33.7,-33.3) # latitude 
#     x_lim = (-71, -70.25) # longitude
#     plot_map2(25, sf, x_lim, y_lim)
#     plt.show()


# def calc_color(data):
#     color_sq = ['#dadaebFF','#bcbddcF0','#9e9ac8F0','#807dbaF0','#6a51a3F0','#54278fF0']; 
#     colors = 'Purples';
#     new_data, bins = pd.qcut(data, 6, retbins=True, labels=list(range(6)))
#     color_ton = []
#     for val in new_data: color_ton.append(color_sq[val]) 
#     return color_ton, bins;


# def plot_map_fill_multiples_ids_tone(sf, title, comuna,  
#                                      print_id, color_ton, 
#                                      bins, 
#                                      x_lim = None, 
#                                      y_lim = None, 
#                                      figsize = (11,9)):
#     '''
#     Plot map with lim coordinates
#     '''
        
#     plt.figure(figsize = figsize)
#     fig, ax = plt.subplots(figsize = figsize)
#     fig.suptitle(title, fontsize=16)
#     for shape in sf.shapeRecords():
#             x = [i[0] for i in shape.shape.points[:]]
#             y = [i[1] for i in shape.shape.points[:]]
#             ax.plot(x, y, 'k')
                
#             for id in comuna:
#                 shape_ex = sf.shape(id)
#                 x_lon = np.zeros((len(shape_ex.points),1))
#                 y_lat = np.zeros((len(shape_ex.points),1))
#                 for ip in range(len(shape_ex.points)):
#                     x_lon[ip] = shape_ex.points[ip][0]
#                     y_lat[ip] = shape_ex.points[ip][1]
#                 ax.fill(x_lon,y_lat, color_ton[comuna.index(id)])
#                 if print_id != False:
#                     x0 = np.mean(x_lon)
#                     y0 = np.mean(y_lat)
#                     plt.text(x0, y0, id, fontsize=10)
#             if (x_lim != None) & (y_lim != None):     
#                 plt.xlim(x_lim)
#                 plt.ylim(y_lim)
            



# def plot_comunas_data(sf, title, comunas, data=None, color=None, print_id=False):
#     color_ton, bins = calc_color(data)
#     df = read_shapefile(sf)
#     comuna_id = []
#     for i in comunas:
#         i = conv_comuna(i).upper()
#         comuna_id.append(df[df.NOM_COMUNA == i.upper()].index.get_values()[0])
    
#     plot_map_fill_multiples_ids_tone(sf, title, comuna_id, 
#                                      print_id, 
#                                      color_ton, 
#                                      bins, 
#                                      x_lim = None, 
#                                      y_lim = None, 
#                                      figsize = (11,9));



# df = read_shapefile(sf)
# df.shape
# df[df.NOM_COMUNA == 'SANTIAGO']
# df.NOM_COMUNA

# I . Load the Census dataset





# Read the first sheet from the Excel File

# csv_df = pd.read_csv('./data/data.csv')
# columns = csv_df.columns


# states_csv = csv_df[columns[0]].tolist()
# know_english_csv = csv_df[columns[1]].tolist()

# reading the state wise shapefile of India in a GeoDataFrame and preview it


# fields = [x[0] for x in sf.fields][1:]
# records = [y[:] for y in sf.records()]
# shps = [s.points for s in sf.shapes()]
# map_df = pd.DataFrame(columns=fields, data=records)
# map_df = map_df.assign(coords=shps)

# map_df['coords'] = [Polygon(map_df['coords'])]


# map2_df = gpd.read_file(fp)
# map2_df.head()

# states_and_ut = map_df['st_nm'].tolist()
# print(type(map_df))

# # Plot the default map
# map_df.plot()

# # Join both the DataFrames by state names
# merged = map_df.set_index('st_nm').join(csv_df.set_index('State'))

# # Detect missing values. Return a boolean same-sized object indicating if the values are NA
# merged.isna().sum()

# # Summary to get the max and min and other statistical data on the dataset
# merged.describe()

# def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
#     new_cmap = colors.LinearSegmentedColormap.from_list(
#         'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
#         cmap(np.linspace(minval, maxval, n)))
#     return new_cmap

# arr = np.linspace(0, 50, 100).reshape((10, 10))
# fig, ax = plt.subplots(ncols=2)

# cmap = plt.get_cmap('RdPu')
# new_cmap = truncate_colormap(cmap, 0.3, 1)

# ax[0].imshow(arr, interpolation='nearest', cmap=cmap)
# ax[1].imshow(arr, interpolation='nearest', cmap=new_cmap)
# # plt.show()

# # create figure and axes for Matplotlib and set the title
# fig, ax = plt.subplots(1, figsize=(10, 6))
# ax.axis('off')
# ax.set_title('Percent of responders who know English', fontdict={'fontsize': '15', 'fontweight' : '3'})

# # plot the figure
# merged.plot(column='Percent of responders who know english', 
#             cmap= new_cmap, 
#             linewidth=0.9, 
#             ax=ax, 
#             edgecolor='1',
#             legend=True
#           )


# fig.savefig("result.png", dpi=100)
# plt.show()