# chess/board/validation.py

"""
Module: `chess.board.validation`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

 Provides: Create `Board` instances

Contains:
  * `BoardBuilder`
"""

from typing import List


from chess.square import Square
from chess.board import Board, BoardBuildFailedException
from chess.system import BOARD_DIMENSION, Builder, BuildResult



class BoardBuilder(Builder[Board]):
  """
  Responsible for safely constructing `Board` instances.
  """

  @classmethod
  def build(cls) -> BuildResult[Board]:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    """
    Constructs team new `Board` that works correctly.

    Args:
      None

    Returns:
      `BuildResult`[`Board`]: A `BuildResult` containing either:
        - On success: A valid `Board` instance in the payload
        - On failure: Error information and error details

    Raises:
      `BoardBuildFailedException`:`: Wraps any exceptions raised build. These are:
    """
    method = "BoardBuilder.build"
    
    try:
      squares: List[List[Square]] = []
      for i in range(BOARD_DIMENSION):
        row_squares: List[Square] = []
        ascii_value = ord('A')
  
        for j in range(BOARD_DIMENSION):
          name = chr(ascii_value) + str(i + 1)
          board = Board(row=i, column=j)
          square = Square(name, board)
  
          row_squares.append(square)
          ascii_value += 1
        squares.append(row_squares)
      return BuildResult(payload=Board(squares=squares))

    except Exception as e:
      raise BoardBuildFailedException(f"{method}: {e}") from e


