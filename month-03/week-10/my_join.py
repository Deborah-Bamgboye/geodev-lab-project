import pandas as pd
import geopandas as gpd

wards = gpd.read_file("data/processed/wards_utm31.gpkg", layer= "wards_utm31")
pop = pd.read_csv("data/processed/ward_population.csv")

first_try = wards.merge(pop, left_on="wardname", right_on="wardname", how="left")
matched = first_try["population"].notna().sum()
print("Matched on first try: ", matched, "of", len(wards))

# def clean_name(name):
#     return name.strip().upper().replace("-", " ")
# wards["join_key"] = wards["wardname"].apply(clean_name)
# pop["join_key"] = pop["ward"].apply(clean_name)
# joined = wards.merge(pop, on="join_key", how= "left")
# matched = joined["population"].notna().sum()
# print("Matched after cleaning:", matched, "of", len(wards))
# print(joined[["wardname", "population"]])