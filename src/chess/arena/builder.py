# chess/arena/validation.py

"""
Module: `chess.arena.validation`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

 Provides: Create `Arena` instances
Contains:
  ArenadBuilder
"""

from typing import List

from chess.arena import Arena
from chess.system import Builder, BuildResult
from chess.board import Board, BoardValidator
from chess.commander import Commander, CommnderValidator



class ArenaBuilder(Builder[Arena]):
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
  Responsible for safely constructing `Arena` instances.
  """

  @classmethod
  def build(
    cls,
    white_commander: Commander,
    black_commander: Commander,
    board: Board
  ) -> BuildResult[Arena]:
    """
    Constructs team new `Arena` that works correctly.

    Args:
      - `white_commander`: White Commander
      - `black_commander`: Black Commander
      - `board_candidate`: Board

    Returns:
      `BuildResult`[`Board`]: A `BuildResult` containing either:
        - On success: A valid `Arena` instance in the payload
        - On failure: Error information and error details

    Raises:
    `ArenaBuildFailedException` wraps any exceptions raised build. These are:
      * `InvalidCommanderException`: If team `white_commander` or `black_commander` fails validation.
      * `InvalidBoardException`: If team `board_candidate` fails validation.

    """
    method = "ArenaBuilder.build"

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


