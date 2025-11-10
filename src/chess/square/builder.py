# src/chess/system/validate/squareBuilder.py

"""
Module: chess.system.validate.squareBuilder
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10

# SECTION 1 - Purpose:
This module provides a satisfaction of the `ChessBot` integrity requirement.

# SECTION 2 - Scope:
The module covers Building `Square` objects which do not introduce inconsistencies to the service.

# SECTION 3 - Limitations:
  1. The module does not provide any actionable code.
  2. The module is limited to providing a framework for validating integrity of existing objects.
  3. The module does not provide any enforceable polices on entities using the framework.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. separating entity responsibilities into from implementation details.
  2. Loose coupling of modules while maintaining a unified, consistent interface for high cohesion among components
    that have no direct relationship with each other.
  3. A consistent interface and aids discoverability, understanding and simplicity.

# SECTION 5 - Features Supporting Requirements:
None

# SECTION G - Feature Delivery Mechanism:
None

# SECTION 7 - Dependencies:
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`

From `chess.point`:
    `Coord`, `CoordValidator`

From `chess.square`:
  `Square`, `SquareBuildFailedException`

# SECTION 8 - Contains:
1. `SquareBuilder`
"""




class SquareBuilder(Builder[Square]):
  """
  # ROLE: Builder

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Square` instances.
  2. Create new ` Square` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult[Square]`: Containing either a successfully built `Square` or an Exception.

  # ATTRIBUTES:
  None
  """
  
  @classmethod
  @LoggingLevelRouter.monitor()
  def build(cls, name: str, coord: Coord) -> BuildResult[Square]:
    """
    # ACTION:
    Create a `Square` object if parameters meet system specifications.

    # PARAMETERS:
        * `visitor_name` (`str`):
        * `point` (`Coord`): Address on the `Board`

    # RETURNS:
    `BuildResult[Square]` containing: `Square` on success. `Exception` on failure.

    # Raises:
    No Exceptions are raised. Exceptions are returned to caller in `BuildResult[Square]`
    """
    method = "SquareBuilder.build"

    try:
      # id_validation = IdSquareBuilder.validate(visitor_id)
      # if not id_validation.is_success():
      #   ThrowHelper.log_and_raise_error(SquareBuilder, id_validation.rollback_exception)

      name_validation = NameSquareBuilder.validate(name)
      if not name_validation.is_success():
        return BuildResult(exception=name_validation.exception)

      coord_result = CoordSquareBuilder.validate(coord)
      if not coord_result.is_success():
        return BuildResult(exception=coord_result.exception)

      return BuildResult(payload=Square(name=name, coord=coord))

    except Exception as e:
      return BuildResult(exception=SquareBuildFailedException(f"{method}: {e}"))