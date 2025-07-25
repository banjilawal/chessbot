from chess.common.piece import Piece


class Knight(Piece):
    def __init__(self, piece_id: int, label: str, team: 'Team', rank: 'Rank'):
        super().__init__(piece_id, label, team, rank)