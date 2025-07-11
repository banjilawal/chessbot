class IdGenerator:
    def __init__(self):
        self.travel_request_id = 1
        self.travel_decision_id = 1
        self.board_id = 1
        self.vault_id = 1
        self.travel_server_id = 1
        self.portal_id = 1
        self.crate_id = 1
        self.rack_id = 1
        self.vault_group_id = 1
        self.cell_id = 1
        self.mover_id = 1

    def next_cell_id(self) -> int:
        current_id = self.cell_id
        self.cell_id += 1
        return current_id

    def next_mover_id(self) -> int:
        current_id = self.mover_id
        self.mover_id += 1
        return current_id

    def next_portal_id(self) -> int:
        current_id = self.portal_id
        self.portal_id += 1
        return current_id

    def next_travel_server_id(self) -> int:
        current_id = self.travel_server_id
        self.travel_server_id += 1
        return current_id

    def next_board_id(self) -> int:
        current_id = self.board_id
        self.board_id += 1
        return current_id

    def next_crate_id(self) -> int:
        current_id = self.crate_id
        self.crate_id += 1
        return current_id

    def next_rack_id(self) -> int:
        current_id = self.rack_id
        self.rack_id += 1
        return current_id

    def next_vault_id(self) -> int:
        current_id = self.vault_id
        self.vault_id += 1
        return current_id

    def next_vault_group__id(self) -> int:
        current_id = self.vault_group_id
        self.vault_group_id += 1
        return current_id

    def next_travel_request_id(self) -> int:
        current_id = self.travel_request_id
        self.travel_request_id += 1
        return current_id

    def next_travel_decision_id(self) -> int:
        current_id = self.travel_decision_id
        self.travel_decision_id += 1
        return current_id

global_id_generator = IdGenerator()
