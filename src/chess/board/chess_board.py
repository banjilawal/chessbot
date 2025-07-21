from dataclasses import dataclass, field
from typing import Tuple, List, Optional, cast

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
            raise ValueError("No chess piece with id", chess_piece_id,
                             " is on the board. cannot remove a non-existent figure.")
        return self.process_withdrawal(chess_piece)

    def add_chess_piece(self, chess_piece: ChessPiece, coordinate: Coordinate) -> None:
        if chess_piece is None:
            raise ValueError("Cannot add a null chess piece")
        if not self.is_valid_coordinate(coordinate):
            raise ValueError("THe chess piece cannot be addd. The destination coordinate is out of range.")
        if self.squares[coordinate.row][coordinate.column].occupant is not None:
            raise ValueError("The chess piece cannot be added. The destination square is already occupied.")

        self.process_occupation(chess_piece, coordinate)

    def move_chess_piece(self, chess_piece: ChessPiece, destination: Coordinate) -> Optional[ChessPiece]:
        if chess_piece is None:
            print("Cannot move a null chess piece.")
            return None
        if not self.is_valid_coordinate(destination):
            print("Cannot move the chess piece. The destination coordinate is out of range.")
            return None

        square = self.squares[destination.row][destination.column]
        if square.occupant is not None:
            return process_capture(chess_piece, square.occupant)

        self.process_occupation(chess_piece, destination)
        return None

    # change tthe signature and name to capture_square then it can deal with all the cases
    def process_capture(self, captor: ChessPiece, prisoner: ChessPiece) -> ChessPiece:
        if captor is None or prisoner is None:
            print("Captor cannot be null. Aborting capture process.")
            return None
        if prisoner is not None and not self.are_enemies(captor, prisoner):
            print("A friendly is occupying the square. Aborting capture process.")
            return None

        if prisoner is not None and self.are_enemies(captor, prisoner):
            square = self.squares[prisoner.row][prisoner.column]
            recorded_prisoner = self.remove_chess_piece(prisoner)
            square.occupant = captor
            captor.coordinate = square.coordinate
            return recorded_prisoner

        if prisoner is None:
            print("No prisoner. Captor occupying square")
            self.process_occupation(captor)
            return None




    def process_occupation(self, occupant: ChessPiece, destination: Coordinate) -> None:
        if occupant is None or not self.is_valid_coordinate(destination):
            raise ValueError("Cannot process an occupation. A null figure is specified.")
            return None

        self.squares[destination.row][destination.column].occupant = occupant
        occupant.coordinate = destination

    def process_withdrawal(self, ex_occupant: ChessPiece) -> ChessPiece:
        if ex_occupant is None:
            raise ValueError("Cannot process a withdrawal. A null figure is specified.")
            return None
        if ex_occupant.coordinate is None:
            raise ValueError("Cannot process a withdrawal. The occupant does not have a coordinate.")
            return None

        self.squares[ex_occupant.coordinate.row][ex_occupant.coordinate.column].occupant = None
        ex_occupant.coordinate = None
        return ex_occupant

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