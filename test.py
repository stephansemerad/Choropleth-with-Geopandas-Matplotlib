import pandas as pd
import numpy as np
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

import pdb
import os; os.system('cls')

def read_shapefile(sf):
    print('read_shapefile')
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df

if __name__ == '__main__':
    BLUE                    = '#30ACE8'
    LINE_COLOR              = '#FFFFFF'# '#808081'
    BACKGROUND_COLOR        = '#F7F7F7'
    MISSING_VALUES_COLOR    = 'lightgrey'
    TITLE                   = 'This is a test'
    DATA_PATH               = './data/data2.xlsx'
    SHAPE_PATH              = "./shapefiles/Comuna.shp"
    COLORS                  = [ '#FFC0CB','#FFB6C1','#FF69B4','#FF1493','#DB7093','#C71585',]
    COLORS                  = ['#30ace8','#2b9ad0','#2689b9','#2178a2','#1c678b','#185674','#13445c','#0e3345','#09222e']


    sns.set_style('whitegrid')

    sf      = shp.Reader(SHAPE_PATH)
    
    sf_df   = read_shapefile(sf)
    df      = pd.read_excel(DATA_PATH)

    data        = df.INMIGRANTES
    districts   = df.NOM_COMUNA
    
    color_allocation, bins = pd.qcut(data, len(COLORS), retbins=True, labels=list(range(0,len(COLORS))))
    color_list = [COLORS[val] for val in color_allocation]


    
    i = 'LAS CONDES'
    sf_df[sf_df.NOM_COMUNA == i].index[0]

    district_ids = []
    for i in districts:
        try:
            district_ids.append(sf_df[sf_df.NOM_COMUNA == i].index[0])
        except:
            print(f'not found: {i}')
            

    
    
    fig, ax = plt.subplots(figsize = (11,9))
    ax.set_title('Information title', fontdict={'fontsize': '15', 'fontweight' : '3'})
    
    # district lines
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, LINE_COLOR, linewidth=0.1)
            
            
    for id in district_ids:
        print('filling id: ', id)
        shape_ex = sf.shape(id)
        
        x_lon = np.zeros((len(shape_ex.points),1))
        y_lat = np.zeros((len(shape_ex.points),1))
        
        for ip in range(len(shape_ex.points)):
            x_lon[ip] = shape_ex.points[ip][0]
            y_lat[ip] = shape_ex.points[ip][1]
        
        # fill od the color
        ax.fill(x_lon,y_lat, color_list[district_ids.index(id)])
        
        x0 = np.mean(x_lon)
        y0 = np.mean(y_lat)
        
        
        title = sf_df.iloc[id]['NOM_COMUNA']

        plt.text(x0, y0, title, fontsize=10)
        # if print_id != False:

    
    fig.savefig("result2.png", dpi=100)
    plt.legend(loc="upper left")

    plt.axis('off')
    plt.tick_params(axis='both', left='off', top='off', right='off', bottom='off', labelleft='off', labeltop='off', labelright='off', labelbottom='off')
    plt.savefig('foo.png', dpi=100, bbox_inches='tight', pad_inches=0.0)
    plt.show()



    # OPTIONAL
    # sns.set(style='whitegrid')