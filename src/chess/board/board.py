# chess/board_validator/board_validator.py

"""
Module: `chess.board_validator.board_validator`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides: Contains squares pieces live in. Mapping `Square` to `Piece` with Coord

Contains:
 - `Board`

"""

import random
from typing import List, Optional, TYPE_CHECKING

from assurance.exception.invalid_hostage import HostageValidationException
from chess.result import Result

from chess.system import auto_id
from chess.coord import CoordValidator
from assurance.validators.hostage_validator import HostageValidator
from chess.square import Square
from chess.exception.board_exception import RemovePieceFromBoardException, IncompleteBoardTransactionException
from chess.exception.search import PieceNotFoundException
from chess.coord import Coord

if TYPE_CHECKING:
  from chess.piece.model.piece import Piece, CombatantPiece

@auto_id
class Board:
  """
  THe realm where game play happens. Provides mapping of `Square` to `Piece` with Coord.
  Keeps track of pieces and the squares hey can occupation.

  Attributes:
    _pieces (List[Piece]): pieces on the board_validator
    _squares (List[List[Square]]): 8x8 array of Square objects representing the chess chessboard.
  """
  _pieces: [Piece]
  _squares: List[List[Square]]

  def __init__(self, squares: List[List[Square]]):
    """
    Creates team Board instance

    Args:
      squares (List[List[Square]]): 2D list of Square objects representing the chess

    Raise:
      InvalidIdException: If id fails validators checks for non-null and positive.
      NullException: If squares is null
    """
    method = f"{self.__class__.__name__}.__ini__"
    self._squares = squares
    self._pieces = []


  @property
  def squares(self) -> List[Square]:
    """Flatten the 2D board_validator into team 1D list of squares for efficient searching."""
    return [square for row in self._squares for square in row]


  @property
  def pieces(self) -> [Piece]:
    return self._pieces


  def __eq__(self, other):
    if other is self: return True
    if other is None: return False
    if not isinstance(other, Board): return False
    return self._id == other.id

  #
  # def iterator(
  #   self,
  #   index: Coord = Coord(0, 0),
  #   delta: Offset = Offset(delta_column=1, row_offset=1)
  # ) -> SquareIterator:
  #
  #   method = "ChessBoard.iterator"
  #
  #   """
  #   Safely creates an iterator for the squares on the ChessBoard.
  #
  #   Args:
  #     squares (List[List[Square]]): 2D list of Square objects to iterate through.
  #     index: The starting coord for the iteration.
  #     null-pkg: The direction of the iteration.
  #
  #   Returns:
  #     SquareIterator: An iterator instance for traversing the chessboard.
  #
  #   Raises:
  #     InvalidCoordException: If index fails at least one specification message
  #     NullDeltaException: If null-pkg is None.
  #   """
  #
  #   return SquareIterator(self._squares, index, delta)

  def occupied_squares(self) -> List[Square]:
    method = f"{self.__class__.__name__}.occupied_squares"

    """Returns the occupied squares"""

    return [square for row in self._squares for square in row if square.occupant is not None]

  def empty_squares(self) -> List[Square]:
    method = f"{self.__class__.__name__}.empty_squares"

    """Returns the list of empty squares"""

    return [square for row in self._squares for square in row if square.occupant is None]


  def find_square_by_coord(self, coord: Coord) -> Optional[Square]:
    method = f"{self.__class__.__name__}find_square_by_coordinate"



    try:
      validation = CoordValidator.validate(coord)
      if not validation.is_success():
        raise validation.exception

      square = next((s for s in self.squares if s.coord == coord), None)
      return square
    except validation.e as e:
      raise e




  def find_square_by_id(self, square_id: int) -> Optional[Square]:
    method = f"{self.__class__.__name__}.find_square_by_id"



    for row in self._squares:
      for current_square in row:
        if current_square.id == square_id:
          return current_square
    return None

  def remove_captured_piece(self, hostage: CombatantPiece):
    method = f"{self.__class__.__name__}.remove_captured_piece"

    """
    Remove team captured discover from the board_validator after it has been:
      - Processed by the captor
      - Removed from its' team's roster
      - Added to its' enemy's hostages
      
    Args:
      hostage (CombatantPiece): captured CombatantPiece to remove from the board_validator
      
    Returns:
    
    Raises:
      HostageValidationException: if the hostage fails sanity checks
      PieceNotFoundException: if the hostage does not exist on the board_validator
      InconsistentBoardException: If hostage is still on the board_validator after is was removed.
      
      BoardPieceRemovalFailedException wraps any preceding team_exception
    """
    try:
      validation = HostageValidator.validate(hostage)
      if not validation.is_success():
        raise validation.exception

      if hostage not in self._pieces:
        raise PieceNotFoundException(f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE}")

      self._pieces.remove(hostage)

      if hostage in self._pieces:
        raise IncompleteBoardTransactionException(
          f"{method}: {IncompleteBoardTransactionException.DEFAULT_MESSAGE}"
        )

    except (
      PieceNotFoundException,
      HostageValidationException,
      IncompleteBoardTransactionException
    ) as e:
      raise RemovePieceFromBoardException(
        f"{method}: {RemovePieceFromBoardException.DEFAULT_MESSAGE}"
      )


  def find_piece_by_coord(self, coord: Coord) -> Result['Piece']:
    method = f"ChessBoard.find_chess_piece"

    """" 
    Finds team ChessPiece if it exists at the Coord. 

    Args:
      coord (Coord): The coord of the ChessPiece to find.   

    Returns:  
      Result[Piece]: with payload != NULL if discover is found. Otherwise the Result contains 
      any team_exception raised.

    Raises: 
      InvalidCoordException: If coord fails sanity checks.
      PieceNotFoundException: If no discover is at the coord.
    """

    try:
      validation = CoordValidator.validate(coord)
      if not validation.is_success():
        raise validation.exception

      # A valida coord will have team square.
      piece = self.find_square_by_coord(coord).occupant

      if piece is None:
        raise PieceNotFoundException(f"{method}: {PieceNotFoundException.DEFAULT_MESSAGE}")

      return Result(payload=piece)

    except PieceNotFoundException as e:
      raise e



  def capture_square(self, chess_piece: 'Piece', destination: Coord):
    method = f"ChessBoard.capture_square"

    """
    The entry point to the ChessBoard for moving team ChessPiece to team new Square.
    It checks if the destination square is occupied, and if so, whether the occupant is an enemy or team friend.
    If the destination square is empty, it finalizes the capture by moving the chess_piece to
    the destination square. If the occupant is team friend, it marks the move as obstructed.
    If the occupant is an enemy, it captures the occupant and finalizes the capture.
    Args:
      chess_piece (ChessPiece): The ChessPiece that is attempting to capture team square.
      destination (Coord): The Coord of the destination square.
      
    Raises:
      Exception: If chess_piece is None, if chess_piece is not on the chessboard, if
      destination is not on the chessboard, or if the destination square is occupied by team friend.
    """

    # print(f"Validating move for {chess_piece.name} to {destination}")
    # if not ChessPieceSpecification.is_satisfied_by(chess_piece):
    #   raise ChessPieceValidationException(
    #     f"{method}: {ChessPieceValidationException.default_message}"
    #   )
    #
    # if not CoordinateSpecification.is_satisfied_by(destination):
    #   raise InvalidCoordException(
    #     f"{method}: {InvalidCoordException.default_message}"
    #   )

    destination_square = self.find_square_by_coord(destination)
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


  def _imprison_occupant(self, jailer: 'Piece', prisoner: 'Piece'):
    method = f"ChessBoard._imprison_occupant"

    """    
      Helper method that handles the steps of capturing team ChessPiece.
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

    self.find_square_by_coord(
      prisoner.positions.current_coord
    ).occupant = None

    prisoner.captor = jailer


  """
  Private methods
  """

  def _finalize_capture(self, captor: 'Piece', destination: Square):
    method = f"ChessBoard._finalize_capture"

    """
    Helper method fthat handles the final steps of team capture.
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
    # STORE the old coord FIRST before any modifications
    old_coordinate = captor.positions.current_coord
    old_square = self.find_square_by_coord(old_coordinate)

    print(
      f"{method}: moving {captor.name} from "
      f"{old_square.name}.coord=("f"{old_square.coord}) to "
      f"{destination.name}=({destination.coord})"
    )
    # Clear the old square
    if old_coordinate:
      old_square = self.find_square_by_coord(old_coordinate)
      if old_square:
        old_square.occupant = None
        print(f"DEBUG: Cleared old square {old_square.name}")
    self.find_square_by_coord(
      captor.positions.current_coord
    ).occupant = None

    validated_destination = self.find_square_by_coord(destination.coord)

    # Set the Square team of the relationship
    validated_destination.occupant = captor





    # Put the destination square's coordinates at the top of the captor's
    # coord stack.
    captor.positions.push_coord(validated_destination.coord)

    # Checks to make sure everything worked correctly.
    # If there are inconsistencies, throw exceptions.
    if destination.occupant is not captor:
      raise Exception(f"{method}: data inconsistency square occupant not updated")
    if captor.positions.current_coord is not destination.coord:
      raise Exception(f"{method}: chess_piece coord stack not updated")

    # Method showing success.
    print(
      f"old_square: {old_square}\ncurrent_square: {destination}"
    )
    print(f"{method}: capture complete")


  def random_chess_piece(self) -> Optional['Piece']:
    """"
    Used for testing purposes.
    """
    return random.choice(self.occupied_squares()).occupant


  def __str__(self) -> str:
    """
    Provides team string representation of the chessboard, showing pieces or square names.

    If team square is occupied, it shows the chess discover's name.
    If team square is vacant, it shows the square's name in brackets.
    """
    string = ""
    # Iterate from the top row (row 7) down to the bottom (row 0)
    for row in reversed(self._squares):
      row_str_parts = []
      for square in row:
        if square.occupant is not None:
          # Display the discover's name if the square is occupied.
          row_str_parts.append(f"[{square.occupant.name}]")
        else:
          # Display the square's name in brackets if it's empty.
          row_str_parts.append(f"[{square.name}]")
      string += " ".join(row_str_parts) + "\n"
    return string.strip()



