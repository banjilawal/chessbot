from dataclasses import field
from typing import Tuple, List, Optional, TYPE_CHECKING

from chess.factory.emit import id_emitter

from chess.game.record.turn_record import TurnRecord
from chess.geometry.coordinate import Coordinate
from chess.geometry.square import Square
from chess.piece.captivity_status import CaptivityStatus
from chess.piece.piece import Piece

if TYPE_CHECKING:
    from chess.game.record.capture_record import CaptureRecord


class Board:
    _pieces: List[Piece]
    _killed_pieces: List[Piece]
    _grid: List[List[Square]]


    def __init__(self, grid: List[List[Square]]):
        self._pieces = []
        self._killed_pieces = []
        self._grid = grid

    @property
    def pieces(self) -> List[Piece]:
        return self._pieces


    def get_piece_by_coordinate(self, coordinate: Coordinate) -> Optional[Piece]:
        print("Checking for coordinate", coordinate, "")
        if not self.coordinate_is_valid(coordinate):
            raise ValueError("The coordinate is not valid. Cannot find chess piece.")
            return None
        square = self._grid[coordinate.row][coordinate.column]
        print("The square at ", coordinate, " is ", square, " it contains ", square.occupant, "")
        return self.grid[coordinate.row][coordinate.column].occupant


    def get_piece_by_id(self, target_id: int) -> Optional[Piece]:
        print("Searching for chess piece with id ", target_id, " on the board.")
        for chess_piece in self._pieces:
            print("Checking if ", chess_piece.name, " is mover with id ", target_id)
            print("checking against ", chess_piece.id, " and ", target_id, "")
            if chess_piece.id == target_id:

                return chess_piece
        return None


    @property
    def grid(self) -> List[List[Square]]:
        return self._grid


    def empty_squares(self) -> List[Square]:
        empty_squares = []
        for square in self._grid:
            if square.occupant is None and square not in empty_squares:
                print(f"Empty square name:{square}")
                empty_squares.append(square)
        return empty_squares


    def occupied_squares(self) -> List[Square]:
        occupied_squares = []
        for square in self._grid:
            occupant = square.occupant
            if occupant is not None and square not in occupied_squares:
                print(f"Occupied square name:{square} occupant label:{occupant.label}")
                occupied_squares.append(square)
        return occupied_squares


    def remove_piece_from_board(self, piece_id: int) -> Piece:
        piece = self.get_piece_by_id(piece_id)
        if piece is None:
            raise ValueError("No chess piece with id", piece_id, "is on the board. cannot remove a non-existent piece.")
        if piece.coordinate is None:
            raise ValueError("Cannot remove a chess piece from an empty square.")

        print(f"Found piece with id {piece.id} at coordinate {piece.coordinate} to remove.")
        square = self.grid[piece.coordinate.row][piece.coordinate.column]
        print(f"the square at {piece.coordinate} is {square}.")
        square.occupant = None
        piece.coordinate = None
        self.pieces.remove(piece)
        return piece


    def add_piece_to_board(self, chess_piece: Piece, coordinate: Coordinate) -> None:
        if chess_piece is None:
            raise ValueError("Cannot add a null chess piece")
        if not self.coordinate_is_valid(coordinate):
            raise ValueError("THe chess piece cannot be addd. The destination coordinate is out of range.")
        if self.grid[coordinate.row][coordinate.column].occupant is not None:
            raise ValueError("The chess piece cannot be added. The destination square is already occupied. by ", gt)

        print("Calling capture_square with ", chess_piece, " and ", coordinate, "")
        self.capture_square(chess_piece, coordinate)


    def capture_square(self, piece: Piece, coordinate: Coordinate) -> TurnRecord:
        if piece is None:
            raise ValueError("Captor cannot be null. Aborting capture process.")
            # return None
        if not self.coordinate_is_valid(coordinate):
            raise ValueError("The destination coordinate is out of range. Aborting capture process.")
            # return None

        turn_record = None
        capture_record = None
        square = self._grid[coordinate.row][coordinate.column]
        current_occupant = square.occupant
        print("The square at ", coordinate, " is ", square, " it contains ", current_occupant)
        if current_occupant is not None and not self.are_enemies(piece, current_occupant):
            print("A friendly is occupying the square. Aborting capture process.")
            return None

        if current_occupant is not None and piece.is_enemy(current_occupant):
            print("The current occupant is an enemy on ")
            prisoner = current_occupant
            square.occupant = None
            prisoner.coordinate = None

            captor = piece
            # prisoner = self.remove_piece_from_board(current_occupant.id)
            prisoner.status = CaptivityStatus.PRISONER

            print("prisoner=", prisoner, " captor=", captor, "")


            # captor = self.remove_piece_from_board(piece)
            square.occupant = captor
            # captor.coordinate = square.coordinate
            captor.add_position(coordinate)
            capture_record = CaptureRecord(
                id=id_emitter.capture_record_id_counter(),
                location=coordinate,
                captor=captor,
                prisoner=prisoner
            )
            self._killed_pieces.append(prisoner)

        if current_occupant is None:
            square.occupant = piece
            piece.add_position(coordinate)
            piece.coordinate = square.coordinate
            turn_record = TurnRecord(
                record_id=id_emitter.turn_record_id,
                moved_piece=piece,
                arrival_coordinate=coordinate,
                capture_record=capture_record
            )
            return turn_record
        return None


    def coordinate_is_valid(self, coordinate: Coordinate):
        if coordinate is None:
            print("A null coordinate is not valid")
            return False
        if coordinate.row <= -1 or coordinate.row >= len(self._grid):
            print("The coordinate is not valid. Its row is out of range")
            return False
        if coordinate.column <= -1 or coordinate.column >= len(self._grid[0]):
            print("The coordinate is not valid. Its column is out of range")
            return False
        return True

    def __str__(self) -> str:
        board_str = ""
        for row_index in reversed(range(len(self._grid))):  # start from top row (8) to bottom (1)
            row_squares = self._grid[row_index]
            row_str = " ".join(f"[{square.name}]" for square in row_squares)
            board_str += row_str + "\n"
        return board_str.strip()
