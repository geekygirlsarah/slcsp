import unittest

from Zips import Zips


class TestZips(unittest.TestCase):

    def test_create_single_zip(self):
        zipcode = 12345
        state = "AA"
        county_code = "54321"
        name = "County"
        rate_area = 123
        s = Zips.Single_Zip(zipcode, state, county_code, name, rate_area)

        self.assertEquals(s.zipcode, zipcode)
        self.assertEquals(s.state, state)
        self.assertEquals(s.county_code, county_code)
        self.assertEquals(s.name, name)
        self.assertEquals(s.rate_area, rate_area)

    def test_add(self):
        zipcode = 12345
        state = "AA"
        county_code = "54321"
        name = "County"
        rate_area = 123

        z = Zips()
        z.add(zipcode, state, county_code, name, rate_area)

        added_zipcode = z.zips[zipcode]

        self.assertEquals(added_zipcode.zipcode, zipcode)
        self.assertEquals(added_zipcode.state, state)
        self.assertEquals(added_zipcode.county_code, county_code)
        self.assertEquals(added_zipcode.name, name)
        self.assertEquals(added_zipcode.rate_area, rate_area)
