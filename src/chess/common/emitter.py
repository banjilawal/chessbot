class IdEmitter:
    def __init__(self):
        self.square_id_counter = 0
        self.chess_piece_counter = 0

    def square_id(self) -> int:
        self.square_id_counter += 1
        return self.square_id_counter

    def chess_piece_id(self) -> int:
        self.chess_piece_id_counter += 1
        return self.chess_id_counter
id_emitter = IdEmitter()