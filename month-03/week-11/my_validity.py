import geopandas as gpd

wards = gpd.read_file("data/processed/wards_utm31.gpkg", layer="wards_utm31")

print("Invalid before:", (~wards.is_valid).sum())
wards["geometry"] = wards.make_valid()
print("Invalid after:", (~wards.is_valid).sum())