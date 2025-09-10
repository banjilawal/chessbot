from typing import Optional


class CombatantPiece(Piece):
    _captor: Optional[Piece]

    def __init__(self, piece_id: int, name: str, rank: 'Rank', side: 'Side'):
        super().__init__(piece_id, name, rank, side)
        self._captor = None


    @property
    def captor(self) -> Optional[Piece]:
        return self._captor


    @captor.setter
    def captor(self, captor: Piece):
        method = "Captor.@setter.captor"

        if captor is None:
            raise SetCaptorNullException(f"{method}: {SetCaptorNullException.DEFAULT_MESSAGE}")

        if self._captor is not None:
            raise PrisonerReleaseException(f"{method}: {PrisonerReleaseException.DEFAULT_MESSAGE}")

        self._captor = captor


    def __eq__(self, other):
        if not super().__eq__(other):
            return False

        if isinstance(other, CombatantPiece):
            return self.id == other.id


#
#
# def main():
#     from chess.rank.pawn_rank import Pawn
#     piece = CombatantPiece(piece_id=id_emitter.piece_id, name="BB-1", side=SideBuilder.build().payload, rank=Pawn())
#     print(piece)
#
#
# if __name__ == "__main__":
#     main()
