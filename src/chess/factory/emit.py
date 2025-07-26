class IdEmitter:
    def __init__(self):
        self._player_id = 0
        self._square_id = 0
        self._piece_id = 0
        self._column_name = ord('a')  # Start at 'a'

    @property
    def player_id(self) -> int:
        self._player_id += 1
        return self._player_id

    @property
    def square_id(self) -> int:
        self._square_id += 1
        return self._square_id

    @property
    def piece_id(self) -> int:
        self._piece_id += 1
        return self._piece_id

    @property
    def column_name(self) -> str:
        current = chr(self._column_name)
        self._column_name += 1
        return current

id_emitter = IdEmitter()