# src/chess/ square/builder.py

"""
Module: chess. square.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation***: There is no guarantee properly created `Square` objects released by the module will satisfy 
    client requirements. Clients are responsible for ensuring a `SquareBuilder` product will not fail when used. 
    
***Related Features***:
    Authenticating existing  squares -> See  SquareValidator, module[chess. square.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error prevention

***Design Concepts***:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Central, single producer of authenticated `Square` objects.
2. Putting all the steps and logging into one place makes modules using `Square` objects cleaner, easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `BuildFailedException`

From `chess.coord`:
    `Coord`, `CoordValidator`
    
From `chess.square`:
  `Square`, `SquareBuildFailedException`

# CONTAINS:
----------
 * ` SquareBuilder`
"""


from chess.coord import Coord, CoordValidator
from chess.square import Square, SquareBuildFailedException
from chess.system import BuildResult, NameValidator, Builder, LoggingLevelRouter


class SquareBuilder(Builder[[Square]]):
  """
  # ROLE: Builder

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating ` Square` instances.
  2. Create new ` Square` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult[Square]`: Return type containing the built ` Square` or error information.

  # ATTRIBUTES:
  None
  """
  
  @classmethod
  @LoggingLevelRouter.monitor()
  def build(cls, name: str, coord: Coord) -> BuildResult[Square]:
    """
    ACTION:
    Create a ` Square` object if the parameters have correctness.

    PARAMETERS:
        * `name` (`str`): unique within the board
        * `coord` (`Coord`): row and column where `Square` is on the `Board`.

    RETURNS:
    `BuildResult[Square]`: A `BuildResult` containing either:
        `'payload'` - A valid ` Square` instance in the payload
        `exception` - Error information and error details

    RAISES:
    `SquareBuildFailedException`:  Wraps any specification violations including:
        * `InvalidIdException`: if `id` fails validate checks`
        * `InvalidCoordException`: if `coord` fails validate checks
    """
    method = "SquareBuilder.build"

    try:
      # id_validation = IdValidator.validate(square_id)
      # if not id_validation.is_success():
      #   ThrowHelper.log_and_raise_error(SquareBuilder, id_validation.exception)

      name_validation = NameValidator.validate(name)
      if not name_validation.is_success():
        # ThrowHelper.log_and_raise_error(SquareBuilder, name_validation.exception)
        return BuildResult(exception=name_validation.exception)

      coord_result = CoordValidator.validate(coord)
      if not coord_result.is_success():
        # ThrowHelper.log_and_raise_error(SquareBuilder, coord_result.exception)
        return BuildResult(exception=coord_result.exception)

      return BuildResult(payload=Square(name=name, coord=coord))

    except Exception as e:
      return BuildResult(exception=SquareBuildFailedException(f"{method}: {e}"))