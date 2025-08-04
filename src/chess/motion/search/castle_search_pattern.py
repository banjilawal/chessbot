from typing import List

from chess.geometry.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.search.search_pattern import SearchPattern
from chess.piece.piece import ChessPiece


class CastleSearchPattern(SearchPattern):
    def __init__(self):
        super().__init__()

    def _perform_search(self, piece: ChessPiece, board: ChessBoard) -> List[Coordinate]:
        origin = piece.current_coordinate()
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
                    # Went off the chess_board — stop searching in this direction
                    break

                occupant = board.find_chess_piece(current)
                if occupant is None:
                    destinations.append(current)
                elif piece.is_enemy(occupant):
                    print(f"{piece.label} found enemy {occupant.label} at {current} adding the target")
                    destinations.append(current)
                    break
                else:
                    print(f"{piece.label} cannot occupy {current} friendly {occupant.label} lives there")
                    break  # Blocked by friendly chess_piece

        return destinations



