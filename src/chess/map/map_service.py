from typing import List, Optional, TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.element.square import Square
from chess.team.element.mobility_status import MobilityStatus

if TYPE_CHECKING:
    from chess.team.element.piece import ChessPiece


class MapService:
    from chess.map.map import Map
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

    def find_coordinates_reachable_from_chess_piece(
        self, chess_piece: 'ChessPiece'
    ) -> (ChessPiece, List[Coordinate]):

        destinations: List[Coordinate]
        origin = chess_piece.coordinate_stack.current_coordinate()

        for quadrant in chess_piece.rank.territories:
            results = self._map.coordinates_from_origin(origin, quadrant.delta)
            destinations.extend(results)

        return ChessPiece, destinations


    def squares_to_string(self) -> str:
        return str(self._map)

    def capture_square(self, piece: 'ChessPiece', from_coordinate: Coordinate, to_coordinate: Coordinate):
        """
        Moves a chess_piece from its origin to a destination square, handling captures.
        This method assumes the move has already been validated by the motion rank.
        It updates the board state and chess_piece coordinates/status.
        """
        origin_square = self.find_square_by_coordinate(from_coordinate)
        destination_square = self.find_square_by_coordinate(to_coordinate)

        if not origin_square or origin_square.occupant != piece:
            raise ValueError(f"GridService Error: {piece.label} not found at origin {from_coordinate}.")
        if not destination_square:
            raise ValueError(f"GridService Error: Destination square {to_coordinate} does not exist.")

        # Clear the origin square
        origin_square.set_occupant(None)

        # Handle potential capture at destination
        target_occupant = destination_square.occupant
        if target_occupant is not None:
            # This is a capture scenario
            captured_piece = target_occupant
            captured_piece.status = MobilityStatus.PRISONER  # Update status of captured chess_piece
            captured_piece.captor = piece  # Set the captor
            print(f"GridService: {piece.label} captured {captured_piece.label} at {to_coordinate}")
        else:
            # This is a move to an empty square
            print(f"GridService: {piece.label} moved to empty square {to_coordinate}")

        # Place the moving chess_piece on the destination square
        destination_square.set_occupant(piece)
        piece.coordinate_stack.push_coordinate(to_coordinate)  # Update chess_piece's coordinate stack
        print(f"GridService: {piece.label} now at {to_coordinate}")




