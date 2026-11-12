# Week 10: GeoPandas, layer as tables

## What this folder contains
- csv_to_points.py
- explore_layer.py
- explore_pandas.py
- facilities_map.png
- filter_sort.py
- geom_props.py
- join-population.py
- make_map.py
- my_explore.py
- my_join.py
- my_map.png
- my_points.py
- save_outputs.py
- table.csv

## How to run it 
From the repository root:
uv run month-03/week-10/ join_population.py
## what I found
 my_join.py worked on first try as population data was extracted as a raster file from world.pop and determined using  Zonal statistics on the otiginal wards laye, so the namings match.

 ## What went wrong and how I fixed it
 when I was running my_points.py, I noticed an error and figured out it was because the facilities layer I had just made was in the CRS : EPSG:4326 which was different from the polygon's CRS so i used :
 ```python
 facilities = facilities.to_crs(wards.crs)
```
to make them the same.
