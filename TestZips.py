# SLCSP problem
# From https://homework.adhoc.team/slcsp/
# Sarah Withee's solution

import unittest

from Zips import Zips


class TestZips(unittest.TestCase):

    def test_create_single_zip(self):
        zipcode = 12345
        state = "AA"
        county_code = "54321"
        name = "County"
        rate_area = 123

        # Make single object with the data
        s = Zips.Single_Zip(zipcode, state, county_code, name, rate_area)

        # Assert the expected data is in the object
        self.assertEqual(s.zipcode, zipcode)
        self.assertEqual(s.state, state)
        self.assertEqual(s.county_code, county_code)
        self.assertEqual(s.name, name)
        self.assertEqual(s.rate_area, rate_area)

    def test_add(self):
        zipcode = 12345
        state = "AA"
        county_code = "54321"
        name = "County"
        rate_area = 123

        # Create object and add info to it
        z = Zips()
        z.add(zipcode, state, county_code, name, rate_area)

        # Get actual data from within class
        added_zipcode = z.zips[zipcode]

        # Assert all data in object matches what was added
        self.assertEqual(added_zipcode.zipcode, zipcode)
        self.assertEqual(added_zipcode.state, state)
        self.assertEqual(added_zipcode.county_code, county_code)
        self.assertEqual(added_zipcode.name, name)
        self.assertEqual(added_zipcode.rate_area, rate_area)

    def test_get_state_and_rate_area(self):
        zipcode = 12345
        state = "AA"
        county_code = "54321"
        name = "County"
        rate_area = 123

        # Make new Zips object, add zip to it
        z = Zips()
        z.add(zipcode, state, county_code, name, rate_area)

        # Get direct object we're expecting
        added_zipcode = z.zips[zipcode]

        # Assert function result is same as object we're expecting
        result_state, result_rate_area = z.get_state_and_rate_area(zipcode)

        self.assertEqual(result_state, state)
        self.assertEqual(result_rate_area, rate_area)

    def test_check_invalid_zipcode(self):
        zipcode = 12345
        state = "AA"
        county_code = "54321"
        name = "County"
        rate_area = 123

        # Make new Zips object, add zip to it
        z = Zips()
        z.add(zipcode, state, county_code, name, rate_area)

        result_state, result_rate_area = z.get_state_and_rate_area(00000)

        # Assert that invalid zip code returns None instead
        self.assertIsNone(result_state)
        self.assertIsNone(result_rate_area)
