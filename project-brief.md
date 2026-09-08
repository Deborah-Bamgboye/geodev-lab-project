# My project brief

## The questions

Which wards in Lagos Mainland local government area are more than 5 km from a health facility?

## Why it matters.

Lagos Mainland is incredibly dense, and heavy traffic congestion means that physical distance to a clinic can easily become a critical barrier during an emergency. Mapping these specific spatial gaps provides actionable data to highlight exactly which residential clusters are underserved. This can help local authorities and NGOs pinpoint exactly where mobile clinics, new primary care centers, or better emergency routing are needed most urgently.

## The data I need.

* Lagos Mainland ward boundaries: Polygon boundaries with ward names.
* Health facilities: Point locations of health facilities.
* Road network: Road centerlines covering Lagos Mainland.

## The data Source

* Ward boundaries – GRID3 Data Hub – https://data.grid3.org
* Health facilities – GRID3 Data Hub – https://data.grid3.org
* Road network – OpenStreetMap via Geofabrik – https://download.geofabrik.de/africa/nigeria.html

## What I would build.

I will build an interactive, web-based dashboard that processes and visualizes this spatial data. The application will allow users to filter Lagos Mainland wards and dynamically flag the specific residential zones that fall outside the 5km safety net, serving as a functional piece of civic tech for urban planning.