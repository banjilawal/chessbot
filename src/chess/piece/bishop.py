from chess.board.board import Board
from chess.piece.piece import Piece


class Bishop(Piece):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)

    def move(self, destination: 'Coordinate', board: Board):
        if self.rank.
