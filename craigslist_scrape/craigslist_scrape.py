import filtering_functions

# Sample Inputs from user
max_rent = 2000
min_rent = 1000
category = 'apa'
min_rank_businesses = None
min_rank_evictions = 8
min_rank_schools_k9 = 8
min_rank_schools_hs = None
min_rank_home_prices = 5
distance_to_bike_parking = "Short"      # Short, Medium, Long
distance_to_bike_share = "Short"        # Short, Medium, Long
density_of_parking_spots_500m = "Low"   # Low, Medium, High Density within 500m
density_of_SFPD_Incidents = "Low"       # Low, Medium, High Density in 2016
density_of_trees_100m = "High"          # Low, Medium, High Density within 500m


def scrape_craigslist(max_rent= None, min_rent = None, cat = category):

    from craigslist import CraigslistHousing
    import filtering_functions
    import zip_lookup

    cl = CraigslistHousing(site='sfbay', area='sfc', category= cat,
                             filters={'max_price': max_rent, 'min_price': min_rent})

    results = cl.get_results(sort_by='newest', geotagged=True, limit=100) #do we need to set a reasonable limit?
    tentative_rental = []
    valid_rentals = []
    for result in results:

        # assign geotag if it is a part of the rental ad
        if result['geotag'] is not None:
            geotag = result['geotag']
        else:
            continue #skip for now

        zipcode = zip_lookup.zip_lookup(geotag)
        tentative_rental.append(result)



        ### # OF BUSINESSES FILTER
        if zipcode not in filtering_functions.check_businesses(min_rank_businesses, zip_query):
            continue

        ### NEARBY SCHOOLS FILTER
        if zipcode not in filtering_functions.check_evictions(min_rank_evictions, zip_query):
            continue



        # Made it to the end of the filters intact? Rental is Valid for this User's Query!
        valid_rentals.append(result)
        tentative_rental = [] # reset the tentative rental, continue loop

        print(result["area"], result["price"], result["name"], result["url"])
    return valid_rentals

# Example Raw Scrape Data
#{'id': '6060895324', 'has_map': True, 'price': '$1600', 'url': 'http://sfbay.craigslist.org/sfc/apa/6060895324.html', 'name': 'Furnished Room', 'has_image': True, 'datetime': '2017-03-26 09:33', 'where': 'nob hill', 'geotag': (37.790788, -122.419036)}
