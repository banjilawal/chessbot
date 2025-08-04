class PlcementChart(Enum):
    def __new__(
        obj = object.__new__(cls)
        obj._acronym = acronym
        obj._player_order = player_order
        obj._acronym = acronym
        obj._game_color = game_color
        obj._back_row_index = back_row_index
        obj._pawn_row_index = pawn_row_index
        return obj