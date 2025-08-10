class IdEmitter:
    def __init__(self):
        self._owner_id = 0
        self._square_id = 0
        self._token_id = 0
        self._team_id = 0
        self._scout_report_id = 0
        self._arena_id = 0
        self._game_id = 0
        self._board_id = 0
        self._board_analysis_id = 0
        self._scout_analysis_id = 0
        self._engine_id = 0


    @property
    def owner_id(self) -> int:
        self._owner_id += 1
        return self._owner_id


    @property
    def square_id(self) -> int:
        self._square_id += 1
        return self._square_id


    @property
    def token_id(self) -> int:
        self._token_id += 1
        return self._token_id


    @property
    def team_id(self) -> int:
        self._team_id += 1
        return self._team_id

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

id_emitter = IdEmitter()