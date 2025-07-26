class IdEmitter:
    def __init__(self):
        self._player_id = 0
        self._coordinate_id = 0
        self._square_id = 0
        self._piece_id = 0
        self._ascii_value = ord('a')
        self._column_name = chr(self._ascii_value)

        self._column_index = 0

    @property
    def player_id(self) -> int:
        self._player_id += 1
        return self._player_id

    @property
    def coordinate_id(self) -> int:
        self._coordinate_id += 1
        return self._coordinate_id

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
        print("1 col_index:", self._column_index," ", self._column_name)
        self._column_name = chr(self._ascii_value)
        self._ascii_value += 1
        if self._ascii_value > 7:
            self._ascii_value = 0
        return self._column_name
id_emitter = IdEmitter()