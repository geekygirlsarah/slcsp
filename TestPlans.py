import unittest
from Plans import Plans


class TestPlans(unittest.TestCase):

    def test_create_single_plan(self):
        plan_id = "123ABC456DEF"
        state = "AA"
        metal_level = "Brass"
        rate = 123.45
        rate_area = 123
        p = Plans.Single_Plan(plan_id, state, metal_level, rate, rate_area)

        self.assertEquals(p.plan_id, plan_id)
        self.assertEquals(p.state, state)
        self.assertEquals(p.metal_level, metal_level)
        self.assertEquals(p.rate, rate)
        self.assertEquals(p.rate_area, rate_area)

    def test_add(self):
        plan_id = "123ABC456DEF"
        state = "AA"
        metal_level = "Brass"
        rate = 123.45
        rate_area = 123

        p = Plans()
        p.add(plan_id, state, metal_level, rate, rate_area)
        key = state + str(rate_area)

        added_plan = p.plans[key]

        self.assertEquals(added_plan.plan_id, plan_id)
        self.assertEquals(added_plan.state, state)
        self.assertEquals(added_plan.metal_level, metal_level)
        self.assertEquals(added_plan.rate, rate)
        self.assertEquals(added_plan.rate_area, rate_area)
