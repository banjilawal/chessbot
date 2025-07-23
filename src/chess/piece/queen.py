from chess.piece.chess_piece import Piece


class Queen(Piece):
    def __init__(self, chess_piece_id: int, name: str, team: 'Team', rank: 'Rank'):
        super().__init__(chess_piece_id, name, team, rank)