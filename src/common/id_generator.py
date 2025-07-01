class IdGenerator:
    def __init__(self):
        self.travel_request_id = 1
        self.travel_decision_id = 1

    def next_travel_request_id(self) -> int:
        current_id = self.travel_request_id
        self.travel_request_id += 1
        return current_id

    def next_travel_decision_id(self) -> int:
        current_id = self.travel_decision_id
        self.travel_decision_id += 1
        return current_id

global_id_generator = IdGenerator()
