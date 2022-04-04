# easy_choroplet_map | Create Chloreplath Maps in minutes.

I always liked Choropleth Maps, they can easy show you distributions of countries for a given dataset.I built this module for myself to explore what could be done in Python.

# Links

[https://github.com/stephansemerad/Choropleth-with-Geopandas-Matplotlib](https://github.com/stephansemerad/Choropleth-with-Geopandas-Matplotlib)

<!--
# Install -->

<!-- ```bash
pip install pln-fx
``` -->

# How To Use

```python
from easy_choroplet_map import EasyChoroplethMap

if __name__ == '__main__':
    easy = EasyChoroplethMap()

    # Use random data
    # --------------------------------
    easy.random_data()
    easy.title      = 'Random Data'
    easy.subtitle   = '(2020)'
    easy.source     = 'https://www.random.org/'
    easy.create_map(file_path='./imgs/result.png')

```

![](https://github.com/stephansemerad/Choropleth-with-Geopandas-Matplotlib/master/imgs/result.png)
