from dataclasses import field
from typing import Tuple, List, Optional

from chess.common.config import BOARD_DIMENSION
from chess.common.emitter import id_emitter
from chess.common.geometry import Square, Coordinate
from chess.common.piece import Piece, CaptivityStatus
from chess.game.record.capture_record import CaptureRecord
from chess.game.record.turn_record import TurnRecord


#@dataclass(frozen=True)
class Board:
    _chess_pieces: List[Piece]
    _squares: Tuple[Tuple[Square, ...], ...]# = field(init=False, repr=False)

    def __init__(self):
        self._chess_pieces = field(default_factory=list)
        self._squares = tuple(
            tuple(
                Square(
                    id=id_emitter.square_id_counter(),
                    coordinate=Coordinate(row=row, column=col)
                )
                for col in range(BOARD_DIMENSION)
            )
            for row in range(BOARD_DIMENSION)
        )
        # object.__setattr__(self, 'squares', squares)

    @property
    def chess_pieces(self) -> List[Piece]:
        return self._chess_pieces.copy()


    def get_chess_piece_by_coordinate(self, coordinate: Coordinate) -> Optional[Piece]:
        if not self.coordinate_is_valid(coordinate):
            print("The coordinate is not valid. Cannot find chess piece.")
            return None
        return self.squares[coordinate.row][coordinate.column].occupant


    def get_chess_piece_by_id(self, target_id: int) -> Optional[Piece]:
        for chess_piece in self.chess_pieces:
            print("Checking if ", chess_piece.name, " is mover with id ", target_id)
            if chess_piece.id == target_id:
                return chess_piece
        return None


    @property
    def squares(self) -> Tuple[Tuple[Square, ...], ...]:
        return self._squares


    def empty_squares(self) -> List[Square]:
        empty_squares = []
        for row in self.squares:
            for square in row:
                if square.occupant is None and square not in empty_squares:
                    empty_squares.append(square)
        return empty_squares


    def occupied_squares(self) -> List[Square]:
        occupied_squares = []
        for row in self.squares:
            for square in row:
                if square.occupant is not None and square not in occupied_squares:
                    occupied_squares.append(square)
        return occupied_squares


    def remove_chess_piece_from_board(self, chess_piece_id: int) -> Piece:
        chess_piece = self.get_chess_piece_by_id(chess_piece_id)
        if chess_piece is None:
            print("No chess piece with id", chess_piece_id, "is on the board. cannot remove a non-existent piece.")
            return None
        if chess_piece.coordinate is None:
            print("Cannot remove a chess piece from an empty square.")
            return None

        square = self.squares[chess_piece.coordinate.row][chess_piece.coordinate.column]
        square.occupant = None
        chess_piece.coordinate = None
        self.chess_pieces.remove(chess_piece)
        return chess_piece


    def add_chess_piece_to_board(self, chess_piece: Piece, coordinate: Coordinate) -> None:
        if chess_piece is None:
            raise ValueError("Cannot add a null chess piece")
        if not self.coordinate_is_valid(coordinate):
            raise ValueError("THe chess piece cannot be addd. The destination coordinate is out of range.")
        if self.squares[coordinate.row][coordinate.column].occupant is not None:
            raise ValueError("The chess piece cannot be added. The destination square is already occupied.")

        self.process_occupation(chess_piece, coordinate)


    def capture_square(self, chess_piece: Piece, coordinate: Coordinate) -> Optional[TurnRecord]:
        if chess_piece is None:
            print("Captor cannot be null. Aborting capture process.")
            return None
        if not self.coordinate_is_valid(coordinate):
            print("The destination coordinate is out of range. Aborting capture process.")
            return None

        turn_record = None
        capture_record = None
        previous_coordinate = chess_piece.current_position();
        square = self.squares[coordinate.row][coordinate.column]
        current_occupant = square.occupant
        if current_occupant is not None and not self.are_enemies(chess_piece, current_occupant ):
            print("A friendly is occupying the square. Aborting capture process.")
            return None

        if current_occupant is not None and chess_piece.is_enemy(current_occupant):
            prisoner = self.remove_chess_piece_from_board(current_occupant.id)
            prisoner.status = CaptivityStatus.PRISONER

            captor = self.remove_chess_piece_from_board(chess_piece)
            square.occupant = captor
            captor.coordinate = square.coordinate
            captor.add_position(coordinate)
            capture_record = CaptureRecord(
                id=id_emitter.capture_record_id_counter(),
                location=coordinate,
                captor=captor,
                prisoner=prisoner
            )
            return prisoner

        if current_occupant is None:
            new_occupant = self.remove_chess_piece_from_board(chess_piece.id)
            square.occupant = new_occupant
            new_occupant.coordinate = square.coordinate
            turn_record = TurnRecord(
                record_id=id_emitter.turn_record_id_counter(),
                moved_piece=new_occupant,
                departure_coordinate=previous_coordinate,
                arrival_coordinate=coordinate,
                capture_record=capture_record
            )
            return turn_record
        return None


    def coordinate_is_valid(self, coordinate: Coordinate):
        if coordinate is None:
            print("A null coordinate is not valid")
            return False
        if coordinate.row <= -1 or coordinate.row >= len(self._squares):
            print("The coordinate is not valid. Its row is out of range")
            return False
        if coordinate.column <= -1 or coordinate.column >= len(self._squares[0]):
            print("The coordinate is not valid. Its column is out of range")
            return False
        return True