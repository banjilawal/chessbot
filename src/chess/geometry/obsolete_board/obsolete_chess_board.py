
from typing import List, Optional, TYPE_CHECKING








if TYPE_CHECKING:
    from chess.token.model import Piece
    from chess.board.square import Square
    from chess.geometry.coord import Coordinate


class ObsoleteChessBoard:
    _chess_pieces: List['Piece']
    _grid: List[List['Square']]


    def __init__(self, grid: List[List['Square']]):
        self._chess_pieces = []
        self._grid = grid


    @property
    def chess_pieces(self) -> List['Piece']:
        return self._chess_pieces


    @property
    def grid(self) -> List[List['Square']]:
        return self._grid

    def find_chess_piece(self, coordinate: 'Coordinate') -> Optional['Piece']:
        return self._grid[coordinate.row][coordinate.column].occupant


    def find_square(self, coordinate: 'Coordinate') -> Optional['Square']:
        return self.grid[coordinate.row][coordinate.column]


    def empty_squares(self) -> List['Square']:
        empty_squares = []
        for square in self._grid:
            if square.occupant is None and square not in empty_squares:
                print(f"Empty model name:{square}")
                empty_squares.append(square)
        return empty_squares


    def occupied_squares(self) -> List['Square']:
        occupied_squares = []
        for square in self._grid:
            occupant = square.occupant
            if occupant is not None and square not in occupied_squares:
                print(f"Occupied model name:{square} occupant label:{occupant.label}")
                occupied_squares.append(square)
        return occupied_squares

    #
    #    def capture_square(self, captor: ChessPiece, coordinate: Coordinate):
    #         if captor is None:
    #             raise ValueError("Captor cannot be null. Aborting capture process.")
    #             # return None
    #         if not self.coordinate_is_valid(coordinate):
    #             raise ValueError("The destination coord is out of range. Aborting capture process.")
    #             # return None
    #
    #         turn_record = None
    #         capture_record = None
    #         square = self._grid[coordinate.row][coordinate.column]
    #         current_occupant = square.occupant
    #         print("The square at ", coordinate, " is ", square, " it contains ", current_occupant)
    #         if current_occupant is not None and not captor.is_enemy(current_occupant):
    #             print("A friendly is occupying the square. Aborting capture process.")
    #             return None
    #
    #     if current_occupant is not None and captor.is_enemy(current_occupant):
    #         print("The current occupant is an enemy on ")
    #         prisoner = current_occupant
    #         square.occupant = None
    #         prisoner.coordinate = None
    #
    #         captor = captor
    #         # prisoner = self.remove_piece_from_board(current_occupant.id)
    #         prisoner.test_outcome = MobilityStatus.PRISONER
    #
    #         print("prisoner=", prisoner, " captor=", captor, "")
    #
    #
    #         # captor = self.remove_piece_from_board(captor)
    #         square.occupant = captor
    #         # captor.coord = square.coord
    #         # captor.add_position(coord)
    #         self._killed_pieces.append(prisoner)
    #
    #     if current_occupant is None:
    #         print("The current occupant is None. The captor is free to move to the destination square.")
    #         print(f"Square {square} has occupant {current_occupant} and captor {captor} is free to move to the destination square.")
    #         square.occupant = captor
    #         captor.coordinate = square.coordinate
    #
    #
    # def capture_square(self, captor: 'ChessPiece', destination: 'Coordinate'):
    #     method = "ObsoleteChessBoard.capture_square"
    #
    #     # 3. Get the squares
    #     square_to_leave = self.find_square(captor.current_coordinate())
    #     destination = self.find_square(destination)
    #     destination.occupy(captor)
    #     square_to_leave.leave(captor)




    # def coordinate_is_valid(self, coordinate: Coordinate):
    #     if coordinate is None:
    #         print("A null coord is not valid")
    #         return False
    #     print("chekcing coord ", coordinate, " for validity.")
    #     if coordinate.row < 0 or coordinate.row >= len(self._grid):
    #         raise ValueError("The coord is not valid. Its row is out of range")
    #     if coordinate.column < 0 or coordinate.column >= len(self._grid[0]):
    #         print("The coord is not valid. Its column is out of range")
    #         return False
    #     return True

    def __str__(self) -> str:
        board_str = ""
        for row_index in reversed(range(len(self._grid))):  # start from top row (8) to bottom (1)
            row_squares = self._grid[row_index]
            row_str = " ".join(f"[{square.name}]" for square in row_squares)
            board_str += row_str + "\n"
        return board_str.strip()
