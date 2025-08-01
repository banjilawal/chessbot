
from typing import List, Optional, TYPE_CHECKING


from chess.geometry.board.coordinate import Coordinate
from chess.square.model import Square

from chess.piece.piece import ChessPiece
from chess.transaction.failure import Failure
from chess.transaction.transaction_result import TransactionResult
from chess.validator.coordinate_validator import CoordinateValidator
from chess.validator.piece_validator import ChessPieceValidator

if TYPE_CHECKING:
    pass


class ChessBoard:
    _chess_pieces: List[ChessPiece]
    _grid: List[List[Square]]


    def __init__(self, grid: List[List[Square]]):
        self._chess_pieces = []
        self._grid = grid


    @property
    def chess_pieces(self) -> List[ChessPiece]:
        return self._chess_pieces


    @property
    def grid(self) -> List[List[Square]]:
        return self._grid

    def find_chess_piece(self, coordinate: Coordinate) -> Optional[ChessPiece]:
        coordinate_validation_result = CoordinateValidator.coordinate_exists(coordinate, self)
        if coordinate_validation_result.is_failure:
            print("Cannot find chess_piece at invalid coordinate")
            return None
        return self._grid[coordinate.row][coordinate.column].occupant


    def find_square(self, coordinate: Coordinate) -> Optional[Square]:

        coordinate_validation_result = CoordinateValidator.coordinate_exists(coordinate, self)
        if coordinate_validation_result.is_failure:
            print("Cannot find model at invalid coordinate")
            return None
        return self.grid[coordinate.row][coordinate.column]


    def empty_squares(self) -> List[Square]:
        empty_squares = []
        for square in self._grid:
            if square.occupant is None and square not in empty_squares:
                print(f"Empty model name:{square}")
                empty_squares.append(square)
        return empty_squares


    def occupied_squares(self) -> List[Square]:
        occupied_squares = []
        for square in self._grid:
            occupant = square.occupant
            if occupant is not None and square not in occupied_squares:
                print(f"Occupied model name:{square} occupant label:{occupant.label}")
                occupied_squares.append(square)
        return occupied_squares


    def place_chess_piece_on_board(self, chess_piece: ChessPiece, coordinate: Coordinate) -> TransactionResult:
        method = "ChessBoard.add_new_piece"

        # Validate chess_piece presence
        # chess_piece_not_null_result = ChessPieceValidator.is_not_null(chess_piece)
        # if chess_piece_not_null_result.is_failure:
        #     return chess_piece_not_null_result

        can_add_chess_piece_result = ChessPieceValidator.can_place_on_board(chess_piece)
        if can_add_chess_piece_result.is_failure:
            return can_add_chess_piece_result

        # Validate coordinate on chess_board
        coordinate_validation_result = CoordinateValidator.coordinate_exists(coordinate, self)
        if coordinate_validation_result.is_failure:
            return coordinate_validation_result

        # Check if the destination model is free
        square = self.find_square(coordinate)
        if square.occupant is None:
            return TransactionResult(
                method,
                Failure(f"Square not found at f{coordinate} {chess_piece.label} to the board.")
            )

        return square.occupy(chess_piece)


    def capture_square(self, chess_piece: ChessPiece, destination: Coordinate) -> TransactionResult:
        method = "ChessBoard.capture_square"

        can_move_chess_piece_result = ChessPieceValidator.can_be_moved(chess_piece)
        if can_move_chess_piece_result.is_failure:
            return can_move_chess_piece_result

        # 2. Validate the destination coordinate on the chess_board
        coord_validation_result = CoordinateValidator.coordinate_exists(destination, self)
        if coord_validation_result.is_failure:
            return TransactionResult(method, Failure("The coordinate is not valid"))

        # 3. Get the squares
        square_to_leave = self.find_square(chess_piece.current_coordinate())
        destination_square = self.find_square(destination)

        # 4. Attempt to occupy the model
        occupation_result = destination_square.occupy(chess_piece)

        # 5. If successful, make the chess_piece leave its previous model (if any)
        if occupation_result.is_success:
            return square_to_leave.leave(chess_piece)

        return occupation_result  # failed occupation outcome

        # def capture_square(self, chess_piece: ChessPiece, coordinate: Coordinate):
        #     if chess_piece is None:
        #         raise ValueError("Captor cannot be null. Aborting capture process.")
        #         # return None
        #     if not self.coordinate_is_valid(coordinate):
        #         raise ValueError("The destination coord is out of range. Aborting capture process.")
        #         # return None
        #
        #     turn_record = None
        #     capture_record = None
        #     model = self._grid[coordinate.row][coordinate.column]
        #     current_occupant = model.occupant
        #     print("The model at ", coordinate, " is ", model, " it contains ", current_occupant)
        #     if current_occupant is not None and not chess_piece.is_enemy(current_occupant):
        #         print("A friendly is occupying the model. Aborting capture process.")
        #         return None
        #
        # if current_occupant is not None and chess_piece.is_enemy(current_occupant):
        #     print("The current occupant is an enemy on ")
        #     prisoner = current_occupant
        #     model.occupant = None
        #     prisoner.coordinate = None
        #
        #     captor = chess_piece
        #     # prisoner = self.remove_piece_from_board(current_occupant.id)
        #     prisoner.status = MobilityStatus.PRISONER
        #
        #     print("prisoner=", prisoner, " captor=", captor, "")
        #
        #
        #     # captor = self.remove_piece_from_board(chess_piece)
        #     model.occupant = captor
        #     # captor.coord = model.coord
        #     # captor.add_position(coord)
        #     self._killed_pieces.append(prisoner)
        #
        # if current_occupant is None:
        #     print("The current occupant is None. The chess_piece is free to move to the destination model.")
        #     print(f"Square {model} has occupant {current_occupant} and chess_piece {chess_piece} is free to move to the destination model.")
        #     model.occupant = chess_piece
        #     chess_piece.coordinate = model.coordinate


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
