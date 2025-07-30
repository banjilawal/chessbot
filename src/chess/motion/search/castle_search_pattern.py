from typing import TYPE_CHECKING, List

from chess.geometry.coordinate import Coordinate
from chess.geometry.board import Board
from chess.geometry.quadrant import Quadrant
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import ChessPiece


class CastleSearchPattern(SearchPattern):
    def __init__(self):
        super().__init__()

    def _perform_search(self, piece: ChessPiece, board: Board) -> List[Coordinate]:
        origin = piece.current_position()
        destinations: List[Coordinate] = []
        quadrants = piece.rank.territories
        print(f"{piece.label} at {origin} will search {len(quadrants)} quadrants for potential destinations")

        for quadrant in quadrants:
            delta = quadrant.delta
            current = origin

            while True:
                try:
                    current= current.shift(delta)
                except ValueError:
                    # Went off the board — stop searching in this direction
                    break

                occupant = board.find_piece(current)
                if occupant is None:
                    destinations.append(current)
                elif piece.is_enemy(occupant):
                    print(f"{piece.label} found enemy {occupant.label} at {current} adding the target")
                    destinations.append(current)
                    break
                else:
                    print(f"{piece.label} cannot occupy {current} friendly {occupant.label} lives there")
                    break  # Blocked by friendly piece

        return destinations



