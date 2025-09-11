class KingPiece(Piece):

    def __init__(self, piece_id: int, name: str, rank: 'Rank', side: 'Team'):
        super().__init__(piece_id, name, rank, side)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, KingPiece):
            return self.id == other.id