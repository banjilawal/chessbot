class IdGenerator:
    travel_request_id: int = 1
    travel_decision_id: int = 1

    def next_travel_request_id(self) -> int:
        """Generates the next travel request ID."""
        current_id = self.travel_request_id
        self.travel_request_id += 1
        return current_id

    def next_travel_decision_id(self) -> int:
        """Generates the next travel decision ID."""
        current_id = self.travel_decision_id
        self.travel_decision_id += 1
        return current_id
