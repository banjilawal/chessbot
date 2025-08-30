from typing import TYPE_CHECKING

from chess.geometry.coordinate.coord import Coordinate

if TYPE_CHECKING:
    from chess.token.model import Piece


class Obstruction:
    _friend_id: int
    _blocked_position:Coordinate


    def __init__(self, friend: 'Piece'):
        self._friend_id = friend.id
        self._blocked_position = friend.current_coordinate


    @property
    def friend_id(self) -> int:
        return self._friend_id


    @property
    def blocked_position(self) -> Coordinate:
        return self._blocked_position

