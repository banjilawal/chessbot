from chess.token.model.base import Piece


class King(Piece):
    def __init__(self, token_id: int, name: str, rank: 'Rank', team: 'Team'):
        super().__init__(token_id, name, rank, team)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, King):
            return self.id == other.id