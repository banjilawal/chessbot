class IdEmitter:
    def __init__(self):
        self._person_id = 0
        self._bot_id = 0
        self._square_id = 0
        self._piece_id = 0
        self._side_id = 0
        self._scout_report_id = 0
        self._arena_id = 0
        self._game_id = 0
        self._board_id = 0
        self._board_analysis_id = 0
        self._scout_analysis_id = 0
        self._engine_id = 0
        self._occupy_id = 0
        self._promote_id = 0
        self._outcome_id = 0


    @property
    def person_id(self) -> int:
        self._person_id += 1
        return self._person_id


    @property
    def bot_id(self) -> int:
        self._bot_id += 1
        return self._bot_id


    @property
    def square_id(self) -> int:
        self._square_id += 1
        return self._square_id


    @property
    def piece_id(self) -> int:
        self._piece_id += 1
        return self._piece_id


    @property
    def side_id(self) -> int:
        self._side_id += 1
        return self._side_id

    @property
    def scout_report_id(self) -> int:
        self._scout_report_id += 1
        return self._scout_report_id

    @property
    def arena_id(self) -> int:
        self._arena_id += 1
        return self._arena_id

    @property
    def game_id(self) -> int:
        self._game_id += 1
        return self._game_id

    @property
    def board_id(self) -> int:
        self._board_id += 1
        return self._board_id


    @property
    def scout_analysis_id(self) -> int:
        self._scout_analysis_id += 1
        return self._scout_analysis_id

    @property
    def board_analysis_id(self) -> int:
        self._board_analysis_id += 1
        return self._board_analysis_id

    @property
    def engine_id(self) -> int:
        self._engine_id += 1
        return self._engine_id


    @property
    def occupy_id(self) -> int:
        self._occupy_id += 1
        return self._occupy_id


    @property
    def promote_id(self) -> int:
        self._promote_id += 1
        return self._promote_id


    @property
    def outcome_id(self) -> int:
        self._outcome_id += 1
        return self._outcome_id

id_emitter = IdEmitter()