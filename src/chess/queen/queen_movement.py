from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.search import SearchPattern



class QueenMovement(SearchPattern):
    def search(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        pass