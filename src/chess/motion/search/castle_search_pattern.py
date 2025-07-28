from typing import TYPE_CHECKING

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.geometry.quadrant import Quadrant
from chess.motion.search.search_pattern import SearchPattern




class CastleSearchPattern(SearchPattern):

    @staticmethod
    def search(rank, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        if not SearchPattern.check_basic_conditions(rank, origin, board):
            return destinations

        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            x_delta = quadrant.x_delta
            y_delta = quadrant.y_delta
            next_coord = origin.shift(x_delta, y_delta)

            while board.coordinate_is_valid(next_coord):
                if board.coordinate_is_occupied(next_coord):
                    # Can capture enemy but not move beyond
                    occupant = board.get_chess_piece_by_coordinate(next_coord)
                    if occupant and occupant.player != rank.members[0].player:
                        destinations.append(next_coord)
                    break  # blocked
                destinations.append(next_coord)
                next_coord = next_coord.shift(x_delta, y_delta)

        return destinations
