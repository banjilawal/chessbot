from typing import Generic, TypeVar, Optional, cast

from chess.square import Square
from chess.rank.queen import Queen
from chess.piece.piece import Piece

T = TypeVar('T')


class Action(Generic[T]):
    _id: int
    _actor: T
    _target: Optional[T]


    def __init__(self, action_id: int, actor: T, target: Optional[T]=None):
        self._id = action_id
        self._actor = actor
        self._target = target


    @property
    def id(self) -> int:
        return self._id


    @property
    def actor(self) -> T:
        return self._actor


    @property
    def target(self) -> Optional[T]:
        return self._target


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Action):
            return False
        return self._id == other.id


class OccupySquare(Action):

    def __init__(self, action_id: int, piece: Piece, square: Square):
        super().__init__(action_id=action_id, actor=piece, target=square)


    @property
    def id(self):
        return self._id


    @property
    def piece(self):
        return cast(self._actor, Piece)


    @property
    def square(self):
        return cast(self._target, Square)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if isinstance(other, OccupySquare):
            return self._id == other.id


class Promote(Action):

    def __init__(self, action_id: int, piece: Piece, rank: Queen = Queen()):
        super().__init__(action_id=action_id, actor=piece, target=rank)


    @property
    def id(self):
        return self._id


    @property
    def piece(self) -> Piece:
        return cast(self._actor, Piece)


    @property
    def rank(self) -> Queen:
        return cast(self._actor, Queen)


    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        if isinstance(other, Promote):
            return self._id == other.id