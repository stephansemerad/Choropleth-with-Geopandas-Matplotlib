
import pandas as pd
import numpy as np
import seaborn as sns
import shapefile as shp
import matplotlib.pyplot as plt
import os
os.system('cls')




if __name__ == '__main__':
    
    # 1. SETUP and DATA
    sns.set(style='whitegrid', palette='pastel', color_codes=True)
    
    sns.mpl.rc('figure', figsize=(10,6))
    
    df = pd.read_excel('./data/data2.xlsx')
    df_total = df.shape

    data    = df.INM_PERC          # know_english_csv 
    names   = df.NOM_COMUNA       # states_csv 

    shp_path = "./shapefiles/Comuna.shp"
    sf = shp.Reader(shp_path)