from typing import TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate

if TYPE_CHECKING:
    from chess.token.chess_piece import ChessPiece


class Obstruction:
    _friend_id: int
    _blocked_coordinate:Coordinate


    def __init__(self, friend: 'ChessPiece'):
        self._friend_id = friend.id
        self._blocked_coordinate = friend.positions.current_coordinate()

    @property
    def friend_id(self) -> int:
        return self._friend_id

    @property
    def blocked_coordinate(self) -> Coordinate:
        return self._blocked_coordinate