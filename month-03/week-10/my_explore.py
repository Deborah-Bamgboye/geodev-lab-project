import geopandas as gpd 
print(gpd.list_layers("data/processed/wards_utm31.gpkg"))

wards = gpd.read_file("data/processed/wards_utm31.gpkg", layer = "wards_utm31")
print(wards.head())
print("Rows and Column:", wards.shape)
print(wards.geom_type.value_counts())
print("Wards CRS:", wards.crs)
print("Bounds:", wards.total_bounds)