# SLCSP problem
# From https://homework.adhoc.team/slcsp/
# Sarah Withee's solution

class Zips:

    zips: dict

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

    def __init__(self):
        self.zips = dict()

    def add(self, zipcode, state, county_code, name, rate_area):
        z = self.Single_Zip(zipcode, state, county_code, name, rate_area)
        self.zips[zipcode] = z

    def get_state_and_rate_area(self, zipcode):
        if zipcode not in self.zips:
            return None, None
        zip_data = self.zips[zipcode]
        return zip_data.state, zip_data.rate_area
