class IdFactory:
    def __init__(self):
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
global_id_generator = IdFactory()