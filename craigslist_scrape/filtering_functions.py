# Acceptable Zip Codes by SQL Query results

def check_businesses(min_rank, summary_table_by_zipcodes):
    zips = []
    for zipcode, rank in summary_table_by_zipcodes['businesses'].items():
        if min_rank == None:
            zips.append(zipcode)
            continue
        if rank >= min_rank:
            zips.append(zipcode)
    if zips == []:
        zips == None
    return zips

def check_evictions(min_rank, summary_table_by_zipcodes):
    zips = []
    for zipcode, rank in summary_table_by_zipcodes['evictions'].items():
        if min_rank == None:
            zips.append(zipcode)
            continue
        if rank >= min_rank:
            zips.append(zipcode)
    if zips == []:
        zips == None
    return zips

def check_schools_k9(min_rank, summary_table_by_zipcodes):
    zips = []
    for zipcode, rank in summary_table_by_zipcodes['schools_k9'].items():
        if min_rank == None:
            zips.append(zipcode)
            continue
        if rank >= min_rank:
            zips.append(zipcode)
    if zips == []:
        zips == None
    return zips

def check_schools_hs(min_rank, summary_table_by_zipcodes):
    zips = []
    for zipcode, rank in summary_table_by_zipcodes['schools_hs'].items():
        if min_rank == None:
            zips.append(zipcode)
            continue
        if rank >= min_rank:
            zips.append(zipcode)
    if zips == []:
        zips == None
    return zips

def check_home_prices(min_rank, summary_table_by_zipcodes):
    zips = []
    for zipcode, rank in summary_table_by_zipcodes['home_prices'].items():
        if min_rank == None:
            zips.append(zipcode)
            continue
        if rank >= min_rank:
            zips.append(zipcode)
    if zips == []:
        zips == None
    return zips
