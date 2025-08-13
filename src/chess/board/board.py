import random
from typing import List, Optional, TYPE_CHECKING

from assurance.validation.chess_piece_specification import ChessPieceSpecification
from assurance.validation.coordinate_specification import CoordinateSpecification
from assurance.validation.validation_exception import CoordinateValidationException, ChessPieceValidationException
from chess.exception.negative_id_exception import ChessException
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.creator.team_placement_manager import PlacementException
from chess.geometry.coordinate.coordinate import Coordinate, Delta
from chess.board.square_iterator import SquareIterator
from chess.board.square import Square

if TYPE_CHECKING:
    from chess.token.chess_piece import ChessPiece




class ChessBoard:
    _id: int
    _squares: List[List[Square]]

    """
    ChessBoard is responsible for managing the movement of ChessPieces on the chessboard. Squares and 
    ChessPieces are data-holding objects referenced by a Coordinate. The class
    - Maintain the relationship between a ChessPiece and Square.
    - Performs bounds checking.. ChessBoard does not know directly about a ChessPiece. All
    

    Attributes:
        _idw (int): id of ChessBoard.
        _squares (List[List[Square]]): 8x8 array of Square objects representing the chess chessboard.
    """

    def __init__(self, board_id: int, squares: List[List[Square]]):
        method = "ChessBoard.__init__()"

        """
        Creates a Board instance

        Args:
            board_id (int): Unique identifier for the ChessBoard.
            squares (List[List[Square]]): 2D list of Square objects representing the chess

        Raise:
            IdValidationException: If id fails validation checks for non-null and positive.
            NullException: If squares is null
        """

        self._id = board_id
        self._squares = squares


    @property
    def id(self) -> int:
        return self._id


    @property
    def squares(self) -> List[List[Square]]:
        return self._squares


    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if not isinstance(other, ChessBoard): return False
        return self._id == other.id


    def iterator(
        self,
        index: Coordinate = Coordinate(0, 0),
        delta: Delta = Delta(column_delta=1, row_delta=1)
     ) -> SquareIterator:

        method = "ChessBoard.iterator"

        """
        Safely creates an iterator for the squares on the ChessBoard.

        Args:
            squares (List[List[Square]]): 2D list of Square objects to iterate through.
            index: The starting coordinate for the iteration.
            delta: The direction of the iteration.
            
        Returns:
            SquareIterator: An iterator instance for traversing the chessboard.
            
        Raises:
            CoordinateValidationException: If index fails at least one specification message
            NullDeltaException: If delta is None.
        """

        return SquareIterator(self._squares, index, delta)

    def occupied_squares(self) -> List[Square]:
        method = "ChessBoard.occupied_squares"

        return [square for row in self._squares for square in row if square.occupant is not None]

    def empty_squares(self) -> List[Square]:
        method = "ChessBoard.empty_squares"

        return [square for row in self._squares for square in row if square.occupant is None]


    def find_square_by_coordinate(self, coordinate: Coordinate) -> Optional[Square]:
        method = "ChessBoard.find_square_by_coordinate"

        """" 
        Finds a square on the ChessBoard by its coordinate. If coordinate is neither not null
        or its columns are rows are out of bounds 
        
        Args:
            coordinate (Coordinate): The coordinate of the square to find.      
            
        Returns:    
            Optional[Square]: The Square object if found, otherwise None.
            
        Raises: 
            CoordinateValidationException: If coordinate is fails any validation checks.
        """

        if not CoordinateSpecification.is_satisfied_by(coordinate):
            raise CoordinateValidationException(CoordinateValidationException.default_message)
        return self._squares[coordinate.row][coordinate.column]


    def find_square_by_name(self, name: str) -> Optional[Square]:
        if name is None:
            raise Exception(f"Cannot find a square with a null name")

        for row in self._squares:
            for current_square in row:
                if current_square.name.upper() == name.upper():
                    return current_square
        return None

    def find_square_by_id(self, square_id: int) -> Optional[Square]:
        if square_id is None:
            raise Exception(f"Cannot find a square with a null id")

        if square_id < 0:
            raise Exception(f"find_square_by_id: square_id {square_id} is negative")

        for row in self._squares:
            for current_square in row:
                if current_square.id == square_id:
                    return current_square
        return None


    def find_chess_piece(self, coordinate: Coordinate) -> Optional['ChessPiece']:
        method = f"ChessBoard.find_chess_piece"

        """" 
        Finds a ChessPiece if it exists at the Coordinate. 

        Args:
            coordinate (Coordinate): The coordinate of the ChessPiece to find.      

        Returns:    
            Optional[ChessPiece] The ChessPiece if found at the coordinate otherwise None.

        Raises: 
            CoordinateValidationException: If coordinate is fails any validation checks.
        """

        return  self.find_square_by_coordinate(coordinate).occupant



    def capture_square(self, chess_piece: 'ChessPiece', destination: Coordinate):
        method = f"ChessBoard.capture_square"

        """
        The entry point to the ChessBoard for moving a ChessPiece to a new Square.
        It checks if the destination square is occupied, and if so, whether the occupant is an enemy or a friend.
        If the destination square is empty, it finalizes the capture by moving the chess_piece to
        the destination square. If the occupant is a friend, it marks the move as obstructed.
        If the occupant is an enemy, it captures the occupant and finalizes the capture.
        Args:
            chess_piece (ChessPiece): The ChessPiece that is attempting to capture a square.
            destination (Coordinate): The Coordinate of the destination square.
            
        Raises:
            Exception: If chess_piece is None, if chess_piece is not on the chessboard, if
            destination is not on the chessboard, or if the destination square is occupied by a friend.
        """

        # print(f"Validating move for {chess_piece.name} to {destination}")
        # if not ChessPieceSpecification.is_satisfied_by(chess_piece):
        #     raise ChessPieceValidationException(
        #         f"{method}: {ChessPieceValidationException.default_message}"
        #     )
        #
        # if not CoordinateSpecification.is_satisfied_by(destination):
        #     raise CoordinateValidationException(
        #         f"{method}: {CoordinateValidationException.default_message}"
        #     )

        destination_square = self.find_square_by_coordinate(destination)
        target_occupant = destination_square.occupant

        if target_occupant is None:
            print(
                f"{method}: "
                f"destination square {destination_square.name}"
                f" is empty calling ChessBoard._finalize_capture"
            )
            self._finalize_capture(chess_piece, destination_square)
            print(
                f""
            )
            return

        if not chess_piece.is_enemy(target_occupant):
            print(
                f"{method}: "
                f"destination square {destination_square.name}"
                f" is occupied by friend{target_occupant.name} "
                f"mark as obstruction"
            )
            chess_piece.add_obstruction(target_occupant)
            return


        if chess_piece.is_enemy(target_occupant):
            print(
                f"current occupant {target_occupant.name} "
                f"is being captured by its enemy {chess_piece.name} "
                f"calling ChesBoard.take_prisoner"
            )
            self._imprison_occupant(chess_piece, target_occupant)
            self._finalize_capture(chess_piece, destination_square)
            return
            # print(f"From BAORD.capture_square destination square is {destination}")
            # self._capture_helper(captor, destination, target_occupant)


    def _imprison_occupant(self, jailer: 'ChessPiece', prisoner: 'ChessPiece'):
        method = f"ChessBoard._imprison_occupant"

        """        
            Helper method that handles the steps of capturing a ChessPiece.
            Sets the captor as the resident of the square, adds the square's coordinates to the captor's
            stack, and sets the captor's old resident as empty.
            Also sets the prisoner.captor to the captor.
      .
        Args:
            jailer (ChessPiece): The ChessPiece that is capturing the prisoner.
            prisoner (ChessPiece): The ChessPiece that is being captured.
        Raises:
            ChessBoardException: If the prisoner is None or if the prisoner is already captured.
            
        """

        self.find_square_by_coordinate(
            prisoner.coordinate_stack.current_coordinate()
        ).occupant = None

        prisoner.captor = jailer


    """
    Private methods
    """

    def _finalize_capture(self, captor: 'ChessPiece', destination: Square):
        method = f"ChessBoard._finalize_capture"

        """
        Helper method fthat handles the final steps of a capture.
        Sets the captor as the resident and adds square's coordinates to the captor's
        stack. Sets the captor's old resident as empty.
        
        Args:
            captor (ChessPiece): The ChessPiece that is capturing the destination.
            destination (Square): The Square that is being captured.
            
        Raises:
            ChessBoardException: If the destination is None or if the captor is None.
        """



        # Remove the captor from their old square. I think its easier to understand
        # because there is less code than if I got the coords first to find the square
        # then deleted it.
        # STORE the old coordinate FIRST before any modifications
        old_coordinate = captor.coordinate_stack.current_coordinate()
        old_square = self.find_square_by_coordinate(old_coordinate)

        print(
            f"{method}: moving {captor.name} from "
            f"{old_square.name}.coord=("f"{old_square.coordinate}) to "
            f"{destination.name}=({destination.coordinate})"
        )
        # Clear the old square
        if old_coordinate:
            old_square = self.find_square_by_coordinate(old_coordinate)
            if old_square:
                old_square.occupant = None
                print(f"DEBUG: Cleared old square {old_square.name}")
        self.find_square_by_coordinate(
            captor.coordinate_stack.current_coordinate()
        ).occupant = None

        validated_destination = self.find_square_by_coordinate(destination.coordinate)

        # Set the Square side of the relationship
        validated_destination.occupant = captor





        # Put the destination square's coordinates at the top of the captor's
        # coordinate stack.
        captor.coordinate_stack.push_coordinate(validated_destination.coordinate)

        # Checks to make sure everything worked correctly.
        # If there are inconsistencies, throw exceptions.
        if destination.occupant is not captor:
            raise Exception(f"{method}: data inconsistency square occupant not updated")
        if captor.coordinate_stack.current_coordinate() is not destination.coordinate:
            raise Exception(f"{method}: chess_piece coordinate stack not updated")

        # Method showing success.
        print(
            f"old_square: {old_square}\ncurrent_square: {destination}"
        )
        print(f"{method}: capture complete")


    def random_chess_piece(self) -> Optional['ChessPiece']:
        """"
        Used for testing purposes.
        """
        return  random.choice(self.occupied_squares()).occupant



    def __str__(self) -> str:
        """
        Provides a string representation of the chessboard, showing pieces or square names.

        If a square is occupied, it shows the chess piece's name.
        If a square is vacant, it shows the square's name in brackets.
        """
        string = ""
        # Iterate from the top row (row 7) down to the bottom (row 0)
        for row in reversed(self._squares):
            row_str_parts = []
            for square in row:
                if square.occupant is not None:
                    # Display the piece's name if the square is occupied.
                    row_str_parts.append(f"[{square.occupant.name}]")
                else:
                    # Display the square's name in brackets if it's empty.
                    row_str_parts.append(f"[{square.name}]")
            string += " ".join(row_str_parts) + "\n"
        return string.strip()



