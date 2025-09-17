from typing import cast

from chess.piece import Piece
from chess.square import Square
from chess.operation import Directive


class OccupationDirective(Directive):

    def __init__(self, directive_id: int, actor: Piece, target: Square):
        super().__init__(directive_id=directive_id, actor=actor, target=target)

    @property
    def id(self):
        return self._id

    @property
    def piece(self):
        return cast(Piece, self.target)

    @property
    def square(self):
        return cast(self._target, Square)

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if isinstance(other, OccupationDirective):
            return self._id == other.id