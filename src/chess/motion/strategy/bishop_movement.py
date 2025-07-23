from chess.board.chess_board import ChessBoard
from chess.common.geometry import Coordinate
from chess.motion.diagonal import DiagonalMove
from chess.motion.strategy.movement_strategy import MovementStrategy


class BishopMovement(MovementStrategy):

    def __init__(self, rules=[DiagonalMove]):
        super().__init__(rules)


    def possible_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        pass



    def get_quadrant_one_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        positions = []
        for column in (origin.column, board.dimension - 1):
            for row in (origin.row, board.dimension - 1):
                positions.append(Coordinate(row=row, colum=column))
        return positions

    def get_quadrant_two_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        positions = []
        for column in (0, origin.column):
            for row in (origin.row, board.dimension - 1):
                positions.append(Coordinate(row=row, colum=column))
        return positions

    def get_quadrant_three_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        positions = []
        for column in (0, origin.column):
            for row in (0, origin.row):
                positions.append(Coordinate(row=row, colum=column))
        return positions

    def get_quadrant_four_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        positions = []
        for column in (origin.column, board.colums - 1):
            for row in (0, origin.row):
                positions.append(Coordinate(row=row, colum=column))
        return positions