import geopandas as gpd

wards = gpd.read_file("data/processed/wards_utm31.gpkg", layer="wards_utm31")
print("CRS:", wards.crs)


print("Suggested UTM: ", wards.estimate_utm_crs())
wards_utm = wards.to_crs(epsg=32631)
wards_utm["area_km2"] = wards_utm.area/ 1_000_000
print(wards_utm[["wardname", "area_km2"]].head(3))
print("Lagos Mainland total:", round(wards_utm["area_km2"].sum(), 1), "km2")
