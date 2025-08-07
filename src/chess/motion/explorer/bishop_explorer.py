
from typing import List

from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.map_service import MapService
from chess.motion.explorer.explorer import Explorer
from chess.motion.walk.bishop_walk import BishopWalk
from chess.team.model.piece import ChessPiece


class BishopExplorer(Explorer):

    def discover_destinations(self, chess_piece: ChessPiece, map_service: MapService) -> List[Coordinate]:
        destinations: List[Coordinate] = []

        for quadrant in chess_piece.motion_controller.territories:
            destinations.extend(
                map_service.find_destinations_from_origin(
                    chess_piece.coordinate_stack.current_coordinate()
                )
            )
        return destinations

        # quadrants = piece.motion_controller.territories
        # print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")
        #
        # for quadrant in quadrants:
        #     delta = quadrant.delta
        #     current = origin.shift(delta)
        #
        #     while board.coordinate_is_valid(current):
        #         if not BishopWalk.is_walkable(origin, current):
        #             break
        #
        #         occupant = board.find_chess_piece(current)
        #         if occupant is None:
        #             destinations.append(current)
        #         elif piece.is_enemy(occupant):
        #             print(f"{piece.label} found enemy {occupant.label} at {current} adding the target")
        #             destinations.append(current)
        #             break
        #         else:
        #             print(f"{piece.label} cannot occupy {current} friendly {occupant.label} lives there")
        #             break  # Blocked by friendly chess_piece
        #
        #         next_row = current.row + delta.delta_row
        #         next_column = current.column + delta.delta_column
        #
        #         if 0 <= next_row < ROW_SIZE and 0 <=  next_column < COLUMN_SIZE:
        #             current = current.shift(delta)
        #         else:
        #             break
        #         current = current.shift(delta)
        # return destinations






