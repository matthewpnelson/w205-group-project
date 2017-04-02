# Rental Lookup Script

# Use this script to take inputs from a user on preferences for certain Rental
# criteria and return a list of rentals from craiglist which match those criteria.

import sys
from craigslist_scrape import scrape_craigslist



# Initial Filtering criteria (to be input at cmd line?)
max_rent = 2000
min_rent = 1000

# Scrape defaults are:
# max_rent= None, min_rent = None, cat = 'apa'

# Scrape Craigslist for rentals
scrape_craigslist(max_rent = max_rent, min_rent = min_rent)
