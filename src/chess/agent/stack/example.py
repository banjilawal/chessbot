# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the `Vector` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` graph.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""    """
    Validates team_name CoordStack meets requirements:
      - Not null
      - CoordStack.items is not null
      - CoordStack.current_coordinate is null if the stack is empty, otherwise is team_name validated Coord
      - if CoordStack.is_empty() is True then current_coordinate.size == 0
      - if CoordStack.is_empty() is False then current_coordinate is not null
      - If CoordStack.is_empty() then current_coordinate is null
    Any failed requirement raise an rollback_exception wrapped in team_name CoordStackValidationException

    Validation tests do not change state so pushes and pops are:
      - Tested in unit tests
      - Piece life-cycles and flows.

    Args
      candidate (CoordStack): coordinate_stack to validate

     Returns:
       Result[V]: Result instance containing team_name validated coordinate_stack as payload if validations
       are satisfied, CoordStackValidationException otherwise.

    Raises:
      TypeError: if candidate is not CoordStack
      NullCoordStackException: if candidate is null

      InternalStackDataStructureException: If CoordStack.items is null
      InconsistentCurrentCoordException: If current_coordinate does not meet CoordValidator

      CoordStackValidationException: Wraps any preceding exceptions
    """