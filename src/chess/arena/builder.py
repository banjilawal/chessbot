# src/chess/arena/old_occupation_validator.py

"""
Module: `chess.arena.coord_stack_validator`
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
from chess.agent import Agent, CommnderValidator



class ArenaBuilder(Builder[Arena]):
  """
  # ACTION:
  Verify the `candidate` is a valid ID. The Application requires
  1. Candidate is not validation.
  2. Is a positive integer.

  # PARAMETERS:
      * `candidate` (`int`): the visitor_id.

  # RETURNS:
  `ValidationResult[str]`: A `ValidationResult` containing either:
      `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
      `rollback_exception` (`Exception`) - An exception detailing which naming rule was broken.

  # RAISES:
  `InvalidIdException`: Wraps any specification violations including:
      * `TypeError`: if candidate is not an `int`
      * `IdNullException`: if candidate is validation
      * `NegativeIdException`: if candidate is negative `
  """
  """
  Responsible for safely constructing `Arena` instances.
  """

  @classmethod
  def build(
    cls,
    white_commander: Agent,
    black_commander: Agent,
    board: Board
  ) -> BuildResult[Arena]:
    """
    Constructs team_name new `Arena` that works correctly.

    Args:
      - `white_commander`: White Agent
      - `black_commander`: Black Agent
      - `board_validator`: Board

    Returns:
      `BuildResult`[`Board`]: A `BuildResult` containing either:
        - On success: A valid `Arena` instance in the payload
        - On failure: Error information and error details

    Raises:
    `ArenaBuildFailedException` wraps any exceptions raised builder. These are:
      * `InvalidCommanderException`: If team_name `white_commander` or `black_commander` fails coord_stack_validator.
      * `InvalidBoardException`: If team_name `board_validator` fails coord_stack_validator.

    """
    method = "ArenaBuilder.builder"

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


