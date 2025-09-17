from typing import Generic, TypeVar, Optional, cast

from chess.square import Square
from chess.rank.queen import Queen
from chess.piece.piece import Piece

T = TypeVar('T')


class Directive(Generic[T]):
    """A data-holding object representing an`actor`'s intent to perform a
    state changing operation  on a `target`. An `Action` can change state of:

    The Directive is handled by an Executor who carry out the directive

    * Its `actor` who initiates and performs the activity
    * The `target` which the operation is performed upon.

    ## Possible State Changes:
    - If the actor wants to change its state then target is a resource `actor` needs.
    - If `actor` wants to change `target` state then the `actor' state might not be affected

    Attributes:
        _id (`int`): A unique identifier for an `operation`.
        _actor (`T`): The entity performing the state-changing activity
        _target (`T`): The `target` can either
    """
    _id: int
    _actor: T
    _target: Optional[T]


    def __init__(self, directive_id: int, actor: T, target: Optional[T]=None):
        self._id = directive_id
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