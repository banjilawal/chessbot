from typing import List

from chess.geometry.board import ChessBoard
from chess.piece.piece import ChessPiece
from chess.game.record.turn_record import TurnRecord
from chess.player.player import Player


class Game:
    _board = ChessBoard
    _white_player: Player
    _blck_player: Player
    _pieces: List[ChessPiece]
    _game_history: list[TurnRecord]

    def __init__(self, board, white_player: Player, black_player: Player):
        self._board = board

    @property
    def get_board(self):
        return self._board

    @property
    def get_game_history(self):
        return self._game_history