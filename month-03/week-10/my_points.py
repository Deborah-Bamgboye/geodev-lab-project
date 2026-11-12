import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/wards_utm31.gpkg", layer= "wards_utm31")
table = pd.read_csv("Lagos-Mainland-health-facilities.csv")
print(table.head(3))

facilities = gpd.GeoDataFrame(
 table,
 geometry= gpd.points_from_xy(table["longitude"], table["latitude"]),
 crs="EPSG:4326",
)
print(facilities.head(3))
print(facilities.crs)

facilities.to_file("data/processed/health-facilities.gpkg", layer="health-facilities")
print("saved", len(facilities), "facilities")

facilities = facilities.to_crs(wards.crs)
fig, ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color = "#F2F9F9", edgecolor="#043A41" )
facilities.plot(ax=ax, color="#E9F365", markersize=18)
ax.set_title("Health facilities in Lagos Mainland")
ax.set_axis_off()

fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches= "tight")
print("Map saved")