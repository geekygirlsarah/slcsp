class Plans:

    plans: dict

    class Single_Plan:
        plan_id: str
        state: str
        metal_level: str
        rate: float
        rate_area: int

        def __init__(self, plan_id, state, metal_level, rate, rate_area):
            self.plan_id = plan_id
            self.state = state
            self.metal_level = metal_level
            self.rate = rate
            self.rate_area = rate_area

    def __init__(self):
        self.plans = dict()

    def add(self, plan_id, state, metal_level, rate, rate_area):
        p = Plans.Single_Plan(plan_id, state, metal_level, rate, rate_area)
        key = state + str(rate_area)
        self.plans[key] = p

