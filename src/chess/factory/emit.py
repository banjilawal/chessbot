class IdEmitter:
    def __init__(self):
        self._player_id = 0
        self._coordinate_id = 0
        self._square_id = 0
        self._piece_id = 0
        self._turn_record_id = 0


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
    def turn_record_id(self) -> int:
        self._turn_record_id += 1
        return self._turn_record_id

id_emitter = IdEmitter()