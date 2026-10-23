import csv
def inspect_column(filename,column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    values =[]
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        
        values.append(float(raw))
    return {
        "Smallest": min(values),
        "Largest": max(values),
        "Count": len(values),
    }
area_result = inspect_column("Lagos_Mainland-Wards.csv", "area_km2")
ward_id_result = inspect_column("Lagos_Mainland-Wards.csv", "uniq_id")
print("Area: ", area_result)
print("Ward-ID: ", ward_id_result)
    # print("Number of rows: ", len(rows))
    # print("Columns: ", list(rows[0].keys()))