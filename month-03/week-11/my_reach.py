import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/wards_utm31.gpkg", layer="wards_utm31").to_crs(epsg=32631)
facilities = gpd.read_file(
    "data/processed/health-facilities_utm31.gpkg", layer="health-facilities_utm31"
).to_crs(epsg=32631)

wards["area_km2"] = wards.area/ 1_000_000

reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)
reach = reach.dissolve()
reach.to_file("data/processed/facility_buffer.gpkg", layer="facility_buffer")
print(gpd.list_layers("data/processed/facility_buffer.gpkg"))

uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area/ 1_000_000

gaps = uncovered[["wardname", "uncovered_km2"]]
result = wards.merge(gaps, on="wardname", how="left")
result["uncovered_km2"] = result["uncovered_km2"].fillna(0)
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(1)
print(result[["wardname", "area_km2", "uncovered_km2", "uncovered_pct"]].round(2))


fig, ax = plt.subplots(figsize=(7,8))
wards.plot(ax=ax, color = "#F2F9F9", edgecolor="#043A41" )
reach.plot(ax=ax, color = "#CD4ACD", edgecolor="#22041E", alpha= 0.4 )
facilities.plot(ax=ax, color="#E9F365", markersize=18)

ax.set_title("Buffers around health facilities in Lagos Mainland wards")
ax.set_axis_off()

fig.savefig("month-03/week-11/my_new_map.png", dpi=150, bbox_inches= "tight")
print("Map saved")