from typing import List

from chess.geometry.coordinate.coordinate import Coordinate
from chess.grid.model.square import Square
from chess.grid.service.grid_service import GridService
from chess.team.team_service import TeamService


class BoardController:
    _team_service: TeamService
    _square_service: GridService

    def __init__(self, team_service: TeamService, square_service: GridService):
        self._team_service = team_service
        self._square_service = square_service

    @property
    def team_service(self) -> TeamService:
        return self._team_service

    @property
    def square_service(self) -> GridService:
        return self._square_service

    def _create_motion_board_adapter(self) -> List[List[Square]]:
        adapter = self._square_service.squares()
        adapter.coordinate_is_valid = self._grid_service.find_square_by_coordinate
        adapter.coordinate_is_occupied = lambda coord: self._grid_service.find_square_by_coordinate(
            coord) is not None and \
                                                       self._grid_service.find_square_by_coordinate(
                                                           coord).occupant is not None
        adapter.get_square_occupant = lambda coord: self._grid_service.find_square_by_coordinate(coord).occupant if \
            self._grid_service.find_square_by_coordinate(coord) else None
        return adapter

    def execute_move(self, piece_id: int, destination_coordinate: Coordinate):
        """
        Executes a chess piece's move. This is the high-level entry point for moves.
        It orchestrates validation and board state updates.
        """
        piece = self._team_service.find_chess_piece_by_id(piece_id)
        if not piece:
            raise ValueError(f"Move failed: ChessPiece with ID {piece_id} not found.")

        origin_coordinate = piece.current_coordinate()
        if not origin_coordinate:
            raise ValueError(f"Move failed: {piece.label} has no current position.")

        # 1. Validate the move using the piece's motion controller
        print(
            f"BoardController: Validating move for {piece.label} from {origin_coordinate} to {destination_coordinate}")
        piece.motion_controller.validate_and_check_move(piece, self._board_for_motion_logic, destination_coordinate)
        print(f"BoardController: Move for {piece.label} is valid.")

        # 2. If validation passes, update the board state via GridService
        print(f"BoardController: Executing move for {piece.label} via GridService.")
        self._grid_service.capture_square(piece, origin_coordinate, destination_coordinate)  # Renamed call
        print(f"BoardController: Move for {piece.label} executed successfully.")


