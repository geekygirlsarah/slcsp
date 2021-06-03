# SLCSP problem
# From https://homework.adhoc.team/slcsp/
# Sarah Withee's solution

class SilverPlans:
    def __init__(self):
        self.prices_by_area = dict()

    def add(self, plan_id, state, metal_level, rate, rate_area):
        # plan_id isn't used. I'm leaving it in because it makes sense to pass in
        # all data into this object and let it choose what it keeps or not. If I
        # was going for super-optimzied, I'd leave it out. If I knew it'd
        # expand more later, I'd keep it in

        # Only storing silver plans in here. This could always expand if needed
        # (add GoldPlans object, or rename this to Plans and add tracking for
        # the other plans)
        if metal_level.lower() != "silver":
            return

        # Store all plan rates under state+area. makes for quick (linear) searching later
        search_key = state + str(rate_area)
        if search_key not in self.prices_by_area:
            self.prices_by_area[search_key] = []
        self.prices_by_area[search_key].append(float(rate))

    def get_all_plan_rates(self, state, rate_area):
        search_key = state + str(rate_area)

        # If it's not in there, it returns a KeyError. This check avoids that
        if search_key not in self.prices_by_area:
            return []
        # Remove redundancies
        prices = set(self.prices_by_area[search_key])
        # Get them sorted ascending
        results = sorted(prices)

        return results
