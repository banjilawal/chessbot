class IdEmitter:
    def __init__(self):
        self.square_id_counter = 0
        self.piece_id_counter = 0


    def square_id(self) -> int:
        self.square_id_counter += 1
        return self.square_id_counter

    def piece_id(self) -> int:
        self.piece_id_counter += 1
        return self.piece_id_counter
id_emitter = IdEmitter()