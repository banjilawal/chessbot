from typing import Generic, TypeVar, Optional, cast

from chess.board.square import Square
from chess.rank.queen import Queen
from chess.token.model import Piece

T = TypeVar('T')


class Command(Generic[T]):
    _id: int
    _client: T
    _resource: Optional[T]


    def __init__(self, req_id: int, client: T, resource: Optional[T]=None):
        self._id = req_id
        self._client = client
        self._resource = resource


    @property
    def id(self) -> int:
        return self._id


    @property
    def client(self) -> T:
        return self._client


    @property
    def resource(self) -> Optional[T]:
        return self._resource


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Command):
            return False
        return self._id == other.id


class OccupySquare(Command):

    def __init__(self, req_id: int, piece: Piece, square: Square):
        super().__init__(req_id=req_id, client=piece, resource=square)


    @property
    def id(self):
        return self._id


    @property
    def piece(self):
        return cast(self._client, Piece)


    @property
    def square(self):
        return cast(self._resource, Square)


    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        if isinstance(other, OccupySquare):
            return self._id == other.id


class Promote(Command):

    def __init__(self, req_id: int, piece: Piece, rank: Queen = Queen()):
        super().__init__(req_id=req_id, client=piece, resource=rank)


    @property
    def id(self):
        return self._id


    @property
    def piece(self) -> Piece:
        return cast(self._client, Piece)


    @property
    def rank(self) -> Queen:
        return cast(self._client, Queen)


    def __eq__(self, other):

        if not super().__eq__(other):
            return False

        if isinstance(other, Promote):
            return self._id == other.id