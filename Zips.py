class Single_Zip:
    zipcode: str
    state: str
    county_code: str
    name: str
    rate_area: int

    def __init__(self, zipcode, state, county_code, name, rate_area):
        self.zipcode = zipcode
        self.state = state
        self.county_code = county_code
        self.name = name
        self.rate_area = rate_area


class Zips:

    zips: dict

    def __init__(self):
        self.zips = dict()

    def add(self, zipcode, state, county_code, name, rate_area):
        z = Single_Zip(zipcode, state, county_code, name, rate_area)
        self.zips[zipcode] = z
