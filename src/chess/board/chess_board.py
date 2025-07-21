from dataclasses import dataclass, field
from typing import Tuple, List, Optional, cast
from wsgiref.validate import check_errors

from chess.common.emitter import id_emitter
from chess.common.geometry import ChessSquare, Coordinate
from chess.figure.chess_piece import ChessPiece

DIMENSION = 8



@dataclass
class ChessBoard:
    chess_pieces: List[ChessPiece] = field(default_factory=list)
    squares: Tuple[Tuple[ChessSquare, ...], ...] = field(init=False, repr=False)

    def __post_init__(self):
        squares = tuple(
            tuple(
                ChessSquare(
                    id=id_emitter.square_id_counter(),
                    coordinate=Coordinate(row=row, column=col)
                )
                for col in range(DIMENSION)
            )
            for row in range(DIMENSION)
        )
        object.__setattr__(self, 'squares', squares)

    def get_chess_piece_by_id(self, target_id: int) -> Optional[ChessPiece]:
        for chess_piece in self.chess_pieces:
            print("Checking if ", chess_piece.name, " is mover with id ", target_id)
            if chess_piece.id == target_id:
                return chess_piece
        return None

    def get_all_occupants(self) -> List[ChessPiece]:
        return self.chess_pieces

    def get_empty_squares(self) -> List[ChessSquare]:
        empty_squares = []
        for row in self.squares:
            for square in row:
                if square.occupant is None and square not in empty_squares:
                    empty_squares.append(square)
        return empty_squares

    def get_occupied_squares(self) -> List[ChessSquare]:
        occupied_squares = []
        for row in self.squares:
            for square in row:
                if square.occupant is not None and square not in occupied_squares:
                    occupied_squares.append(square)
        return occupied_squares

    def remove_chess_piece(self, chess_piece_id: int) -> ChessPiece:
        chess_piece = self.get_chess_piece_by_id(chess_piece_id)
        if chess_piece is None:
            print("No chess piece with id", chess_piece_id, "is on the board. cannot remove a non-existent figure.")
            return None
        if chess_piece.coordinate is None:
            print("Cannot remove a chess piece from an empty square.")
            return None


        square = self.squares[chess_piece.coordinate.row][chess_piece.coordinate.column]
        square.occupant = None
        chess_piece.coordinate = None
        self.chess_pieces.remove(chess_piece)

        return chess_piece

    def add_new_chess_piece(self, chess_piece: ChessPiece, coordinate: Coordinate) -> None:
        if chess_piece is None:
            raise ValueError("Cannot add a null chess piece")
        if not self.is_valid_coordinate(coordinate):
            raise ValueError("THe chess piece cannot be addd. The destination coordinate is out of range.")
        if self.squares[coordinate.row][coordinate.column].occupant is not None:
            raise ValueError("The chess piece cannot be added. The destination square is already occupied.")

        self.process_occupation(chess_piece, coordinate)

    def capture_square(self, chess_piece: ChessPiece, coordinate: Coordinate) -> Optional[ChessPiece]:
        if chess_piece is None:
            print("Captor cannot be null. Aborting capture process.")
            return None
        if not self.is_valid_coordinate(coordinate):
            print("The destination coordinate is out of range. Aborting capture process.")
            return None

        square = self.squares[coordinate.row][coordinate.column]
        current_occupant = square.occupant
        if current_occupant is not None and not self.are_enemies(chess_piece, current_occupant ):
            print("A friendly is occupying the square. Aborting capture process.")
            return None

        if current_occupant is not None and self.are_enemies(chess_piece, current_occupant):
            prisoner = self.remove_chess_piece(current_occupant.id)
            captor = self.remove_chess_piece(chess_piece)
            square.occupant = captor
            captor.coordinate = square.coordinate
            return prisoner

        if current_occupant is None:
            future_occupant = self.remove_chess_piece(chess_piece.piece_id)
            square.occupant = future_occupant
            future_occupant.coordinate = square.coordinate
            return None
        return None


    def are_enemies(self, a: ChessPiece, b: ChessPiece):
        return a.team.color == b.team.color

    def is_valid_coordinate(self, coordinate: Coordinate):
        if coordinate is None:
            print("A null coordinate is not valid")
            return False
        if coordinate.row <= -1 or coordinate.row >= DIMENSION:
            print("The coordinate is not valid. Its row is out of range")
            return False
        if coordinate.column <= -1 or coordinate.column >= DIMENSION:
            print("The coordinate is not valid. Its column is out of range")
            return False
        return True