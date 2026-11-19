import geopandas as gpd

wards = gpd.read_file("data/processed/wards_utm31.gpkg", layer="wards_utm31").to_crs(epsg=32631)
facilities= gpd.read_file(
    "data/processed/health-facilities_utm31.gpkg", layer="health-facilities_utm31"
).to_crs(epsg=32631)

# count facilities per ward
joined = gpd.sjoin(
    facilities, wards[["wardname", "geometry"]], how="inner", predicate="within"
)
counts = joined.groupby("wardname").size().rename("facility_count").reset_index()
wards = wards.merge(counts, on="wardname", how="left")
wards["facility_count"] = wards["facility_count"].fillna(0).astype(int)
print(wards[["wardname", "facility_count"]])
print("Total counted:", wards["facility_count"].sum(), "of", len(facilities))
