# Data notes

## GRID3 NGA - Operational Wards v1.0 
- Source : https://data.grid3.org
- Downloaded:9/12/2026 9:58 PM
- 9410 features, polygons
- Columns : wardname(text), wardcode (text), lganame (text), lgacode (numeric), statename (text), statecode (text), status(text), source(text), urban (text)
- Covers my LGA fully
 ### Quality check
  - COMPLETENESS: wards are complete
  - CURRENCY: Last edit 2025
  - POSITIONAL: Operational ward boundaries align with just slight deviation. 
  - ATTRIBUTE: Attributes are suffient for analysis
  - FITNESS: Data is adequate for spatial analysis as computed areas of ward line up with public figure
 



## GRID3 NGA - Health Facilities v2.0 
- Source : https://data.grid3.org
- Downloaded: 9/13/2026 6:07 PM
- 51022 feaures, points
- Columns : state (text), lga (text), ward (text), facility_name (text), facility_name_source (text), ownership (text), ownership_type (text), facility_level (text)
- Covers my LGA fully
### Quality check
- COMPLETENESS: all health facility points are accurately recorded. 
- CURRENCY: Last edit 2024. Up to date
- POSITIONAL: slight spatial deviation of some points
- ATTRIBUTE: All columns are complete and accounted for. no missing attributes
- FITNESS: It would also be sufficient for analysis



## OSM road, extracted via QuickOSM
- Query: highway =* within Lagos Mainland Extent
- Extracted: 9/13/2026
- 2493 features, lines
- Coverage looks good. But relatively sparse in the ward with wardcode LASLMD02
### Quality check
- COMPLETENESS:All main roads are recorded , good in built-up areas
- CURRENCY: up to date
- POSITIONAL: the roads line up perfectly with satelite imagery
- ATTRIBUTE: scarcity in terms of road/street names, number of lanes or crossing markings and crossing
- FITNESS: Adequate for access analysis in built up area

## CRS and Reprojection 
- All source layers arrived in EPSG:4326
- Study area Lagos Mainland extracted from NGA Operational Wards
- All layers clipped to study area, then reprojected to EPSG:32631 UTM 31N
- Area check matches public figure, summed area of wards to give a value of 20.18 squaredkilometers for the entirety of Lagos Mainland which coincides with recorded published figure of ~20 squaredkilometers  
- Working files in data/processed, raw files left untouched.