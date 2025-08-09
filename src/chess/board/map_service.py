from typing import List, Optional, TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate
from chess.board.element.square import Square

if TYPE_CHECKING:
    from chess.token.piece import ChessPiece


class MapService:
    from chess.board.board import Map
    _map: Map

    def __init__(self, mao: Map):
        self._map = map

    def squares(self) -> List[List[Square]]:
        return self._map.squares


    def empty_squares(self) -> List[Square]:
        return self._map.empty_squares()


    def occupied_squares(self) -> List[Square]:
        return self._map.occupied_squares()

    def find_square_by_coordinate(self, coordinate: Coordinate) -> Optional[Square]:
        return self._map.find_square_by_coordinate(coordinate)


    def find_square_by_id(self, square_id) -> Optional[Square]:
        return self._map.find_square_by_id(square_id)


    def find_square_by_name(self, name:str) -> Optional[Square]:
        return self._map.find_square_by_name(name)


    def squares_to_string(self) -> str:
        return str(self._map)

    def capture_square(self, chess_piece: 'ChessPiece', destination: Coordinate):

        destination_square = self.find_square_by_coordinate(destination)
        target_occupant = destination_square.occupant

        if target_occupant is None or chess_piece.is_enemy(target_occupant):
            self._capture_helper(chess_piece, destination_square, target_occupant)
        else:
            print("The square is occupied by a friendly")
            chess_piece.add_obstruction(target_occupant)
            return


    def _capture_helper(
        self,
        chess_piece: 'ChessPiece',
        target_square: Square,
        enemy: Optional['ChessPiece']
    ):
        originating_square = self.find_square_by_coordinate(
            chess_piece.coordinate_stack.current_coordinate()
        )

        if not chess_piece.is_enemy(enemy):
            raise Exception(
                "Fatal error. A friendly should never be a self._capture_helper parameter."
            )

        if enemy is not None:
            chess_piece.capture_prisoner(enemy)

        originating_square.set_occupant(None)
        target_square.set_occupant(chess_piece)
        chess_piece.coordinate_stack.push_coordinate(target_square.coordinate)



