### NEIGHBOURHOOD IDENTIFIER, to be used in the craigslist scraper as a filter (if required)

# Check which neighbourhood the listing is in (by geotag)
geotag = result["geotag"]
area_found = False
area = ""
for a, coords in neighbourhood_lookup.BOXES.items():
    if neighbourhood_lookup.in_box(geotag, coords):
        area = a
        area_found = True

# Check which neighbourhood the listing is in (by name, backup)
location = result["where"]
for hood in neighbourhood_lookup.NEIGHBORHOODS:
    if hood in location.lower():
        area = hood
result["area"] = area
