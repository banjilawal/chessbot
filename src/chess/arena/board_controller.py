from typing import List

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.element.square import Square
from chess.map.map_service import MapService
from chess.motion.explorer import Explorer
from chess.team.element.piece import ChessPiece
from chess.team.team_service import TeamService


class BoardController:
    _team_service: TeamService
    _square_service: MapService

    def __init__(self, team_service: TeamService, square_service: MapService):
        self._team_service = team_service
        self._square_service = square_service


    @property
    def team_service(self) -> TeamService:
        return self._team_service


    @property
    def square_service(self) -> MapService:
        return self._square_service


    def move_chess_piece_by_id(self, chess_piece_id: int, destination: Coordinate):
        chess_piece = self._team_service.find_chess_piece_by_id(chess_piece_id)

        if chess_piece is  None:
            raise ValueError(f"ChessPiece with ID {chess_piece_id} not found.")
        origin = chess_piece.coordinate_stack.current_coordinate()

        if not chess_piece.rank.walk.is_walkable(origin, destination):
            raise ValueError(
                f"Destination {destination} is not reachable from {origin} by a "
                f"{chess_piece.rank.walk.__class__.__name__}"
            )
        self._square_service.capture_square(chess_piece, destination)


    def explore_team_frontier(self, team_id: int):
        team = self._team_service.find_team_by_id(id)

        if team is None:
            raise ValueError(f"Team with ID {id} not found.")

        tuples: List[(ChessPiece, List[Coordinate])] = []
        explorers = team.free_chess_pieces()

        for explorer in explorers:
            t = Explorer.discover_destinations(explorer, self._square_service)
            chess_piece: ChessPiece = t[0]
            destination_count = len(t[1])
            print(f"TUPLE: {chess_piece.name} destination_count={destination_count}")
            if destination_count > 0 and tuple not in tuples:
                tuples.append(Explorer.discover_destinations(explorer, self._square_service))
        return tuples


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
    #
    # def execute_move(self, piece_id: int, destination_coordinate: Coordinate):
    #     """
    #     Executes a chess chess_piece's move. This is the high-level entry point for moves.
    #     It orchestrates validation and obsolete_board state updates.
    #     """
    #     piece = self._team_service.find_chess_piece_by_id(piece_id)
    #     if not piece:
    #         raise ValueError(f"Move failed: ChessPiece with ID {piece_id} not found.")
    #
    #     origin_coordinate = piece.current_coordinate()
    #     if not origin_coordinate:
    #         raise ValueError(f"Move failed: {piece.label} has no current position.")
    #
    #     # 1. Validate the move using the chess_piece's motion rank
    #     print(
    #         f"BoardController: Validating move for {piece.label} from {origin_coordinate} to {destination_coordinate}")
    #     piece.rank.validate_and_check_move(piece, self._board_for_motion_logic, destination_coordinate)
    #     print(f"BoardController: Move for {piece.label} is valid.")
    #
    #     # 2. If validation passes, update the obsolete_board state via MapService
    #     print(f"BoardController: Executing move for {piece.label} via GridService.")
    #     self._grid_service.capture_square(piece, origin_coordinate, destination_coordinate)  # Renamed call
    #     print(f"BoardController: Move for {piece.label} executed successfully.")


