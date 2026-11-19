# Week 11: Coordinate reference systems and spatial operations in code
## what this folder contains
- area_wrong_and_right.py
- clip_dissove.py
- coverage_gap.py
- fix_geometry.py
- nearest.py
- one_point.py
- README.md
- set_vs_to.py
- spatial_ops.py
## How to run it
From the repository root:
uv run month-03/week-11/clip_dissolve.py

## What I found
- I chose the epsg32361 because it's best suited for area measurements
## what went wrong and how I tried to fix it
 for my_validity.py there were no invalid geometries to fix with make_valid

## limitations of the coverage method chosen

The coverage gap method measures straight-line distance, not travel distance. A 2 km buffer ignores the road network, one-way systems, traffic, the lagoon and bridge bottlenecks, so it overstates how accessible a facility really is, and any ward it flags as uncovered is a best-case result. The method also treats every facility as equal and every point inside a buffer as equally served. It ignores facility type, capacity, opening hours and quality, and it does not account for how many residents live in each part of a ward, so a large uncovered area that is mostly empty weighs the same as a small one that is densely populated. The 2 km threshold is a judgement call, and the results are sensitive to it: a small change in distance can shift which wards are flagged. Results also depend on the completeness of the facilities layer. Missing or misplaced points, especially unmapped private clinics, will create gaps that do not exist on the ground, while facilities outside the LGA must be kept in the buffer or edge wards will be wrongly penalised. Finally, the output is area-based, so it shows where coverage is missing but not how many people are affected, and a population layer would be needed to answer that.