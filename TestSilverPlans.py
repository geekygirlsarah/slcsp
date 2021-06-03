# SLCSP problem
# From https://homework.adhoc.team/slcsp/
# Sarah Withee's solution

import unittest
from SilverPlans import SilverPlans


class TestSilverPlans(unittest.TestCase):

    def test_add_silver_plan(self):
        plan_id = "123ABC456DEF"
        state = "AA"
        metal_level = "Silver"
        rate = 123.45
        rate_area = 123

        # Create object, add plan to it
        p = SilverPlans()
        p.add(plan_id, state, metal_level, rate, rate_area)

        # Get raw data out of object
        key = state + str(rate_area)
        self.assertIn(key, p.prices_by_area)
        added_plan = p.prices_by_area[key]

        # Assert object is as expected
        self.assertIsNotNone(added_plan)
        self.assertNotEquals(added_plan, [])
        self.assertIn(123.45, added_plan)
        self.assertNotIn(543.21, added_plan)
        self.assertEquals(len(p.prices_by_area), 1)

    def test_add_non_silver_plan(self):
        plan_id = "123ABC456DEF"
        state = "AA"
        metal_level = "Brass"
        rate = 123.45
        rate_area = 123

        # Create object, add plan to it
        p = SilverPlans()
        p.add(plan_id, state, metal_level, rate, rate_area)

        # Look for raw data but a brass plan shouldn't be in there
        key = state + str(rate_area)
        self.assertEquals(len(p.prices_by_area), 0)
        self.assertNotIn(key, p.prices_by_area)

    def test_get_all_plan_rates(self):
        plan_id1 = "123ABC456DEF"
        state = "AA"
        metal_level = "Silver"
        rate1 = 123.45
        rate_area = 123

        # Create object and add plan to it
        p = SilverPlans()
        p.add(plan_id1, state, metal_level, rate1, rate_area)

        # Add second plan
        plan_id2 = "456DEF123ABC"
        rate2 = 654.32
        p.add(plan_id2, state, metal_level, rate2, rate_area)

        # Get all results
        results = p.get_all_plan_rates(state, rate_area)

        # Assert both values are in there
        self.assertIn(rate1, results)
        self.assertIn(rate2, results)
        # Assert only those two items in there
        self.assertEquals(len(results), 2)
