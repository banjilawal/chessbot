from chess.board.board import Board
from chess.game.record.turn_record import TurnRecord
from chess.team.team import Team


class Game:
    _board = Board
    _white_team = Team
    _black_team = Team
    _game_history: list[TurnRecord]

    def __init__(self, board, white_team, black_team):
        self._board = board
        self._white_team = white_team
        self._black_team = black_team

    @property
    def get_board(self):
        return self._board


    @property
    def get_white_team(self):
        return self._white_team


    @property
    def get_black_team(self):
        return self._black_team


    @property
    def get_game_history(self):
        return self._game_history