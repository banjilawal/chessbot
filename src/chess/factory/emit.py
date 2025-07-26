class IdEmitter:
    def __init__(self):
        self._player_id = 0
        self._square_id = 0
        self._piece_id = 0

    @property
    def player_id(self) -> int:
        self._player_id += 1
        return self._player

    @property
    def square_id(self) -> int:
        self._square_id += 1
        return self._square_id

    @property
    def piece_id(self) -> int:
        self._piece_id += 1
        return self._piece_id
id_emitter = IdEmitter()