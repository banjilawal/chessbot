from chess.board.board import Board
from chess.common.piece import Piece


class Bishop(Piece):
    def __init__(self, piece_id: int, label: str, team: 'Team', rank: 'Rank'):
        super().__init__(piece_id, label, team, rank)

    def move(self, destination: 'Coordinate', board: Board):
        if self
