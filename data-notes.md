# Data notes

## GRID3 NGA - Operational Wards v1.0 
- Source : https://data.grid3.org
- Downloaded:9/12/2026 9:58 PM
- 9410 features, polygons
- Columns : wardname(text), wardcode (text), lganame (text), lgacode (numeric), statename (text), statecode (text), status(text), source(text), urban (text)
- Covers my LGA fully
 



## GRID3 NGA - Health Facilities v2.0 
- Source : https://data.grid3.org
- Downloaded: 9/13/2026 6:07 PM
- 51022 feaures, points
- Columns : state (text), lga (text), ward (text), facility_name (text), facility_name_source (text), ownership (text), ownership_type (text), facility_level (text)
- Covers my LGA fully



## OSM road, extracted via QuickOSM
- Query: highway =* within Lagos Mainland Extent
- Extracted: 9/13/2026
- 2493 features, lines
- Coverage looks good. But relatively sparse in the ward with wardcode LASLMD02

## CRS and Reprojection 
- All source layers arrived in EPSG:4326
- Study area Lagos Mainland extracted from NGA Operational Wards
- All layers clipped to study area, then reprojected to EPSG:32631 UTM 31N
- Area check matches public figure 
- Working files in data/processed, raw files left untouched.