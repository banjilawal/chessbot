from typing import List, Optional

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.model.square import Square



class GridService:
    from chess.map.repo.grid_repo import GridRepo
    _repo: GridRepo

    def __init__(self, repo: GridRepo):
        self._repo = repo


    def squares(self) -> List[List[Square]]:
        return self._repo.squares


    def empty_squares(self) -> List[Square]:
        return self._repo.empty_squares()


    def occupied_squares(self) -> List[Square]:
        return self._repo.occupied_squares()

    def find_square_by_coordinate(self, coordinate: Coordinate) -> Optional[Square]:
        return self._repo.find_square_by_coordinate(coordinate)


    def find_square_by_id(self, square_id) -> Optional[Square]:
        return self._repo.find_square_by_id(square_id)


    def find_square_by_name(self, name:str) -> Optional[Square]:
        return self._repo.find_square_by_name(name)


    def squares_to_string(self) -> str:
        return str(self._repo)

    def capture_square(self, piece: 'ChessPiece', from_coordinate: Coordinate, to_coordinate: Coordinate):
        """
        Moves a piece from its origin to a destination square, handling captures.
        This method assumes the move has already been validated by the motion controller.
        It updates the board state and piece coordinates/status.
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
            captured_piece.status = MobilityStatus.PRISONER  # Update status of captured piece
            captured_piece.captor = piece  # Set the captor
            print(f"GridService: {piece.label} captured {captured_piece.label} at {to_coordinate}")
        else:
            # This is a move to an empty square
            print(f"GridService: {piece.label} moved to empty square {to_coordinate}")

        # Place the moving piece on the destination square
        destination_square.set_occupant(piece)
        piece.coordinate_stack.push_coordinate(to_coordinate)  # Update piece's coordinate stack
        print(f"GridService: {piece.label} now at {to_coordinate}")




