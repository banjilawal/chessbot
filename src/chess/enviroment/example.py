#
#
#
#
# resource_validation = SquareValidator.validate(resource_candidate)
# if resource_validation.is_failure():
#   return ValidationResult(rollback_exception=resource_validation.rollback_exception)
#
# square_name = cast(Square, resource_validation.payload)
#
# # If the square_name has no position history its not on the board and cannot square_name.
# if square_name.current_position is None or square_name.positions.is_empty():
#   return ValidationResult(rollback_exception=NoInitialPlacementException(
#     f"{method}: {NoInitialPlacementException.DEFAULT_MESSAGE}"
#   ))
#
# # If the square_name is not on its team_name roster it cannot be a TravelEvent resource_candidate. This might have been
# # checked by the SquareValidator
# team_name = square_name.team_name
# if square_name not in team_name.roster:
#   return ValidationResult(rollback_exception=ResourceNotOnRosterCannotMoveException(
#     f"{method}: {ResourceNotOnRosterCannotMoveException.DEFAULT_MESSAGE}"
#   ))
#
# # A captured combatant cannot be a TravelEvent resource_candidate. No need for validating a checkmated
# # occupation as an resource_candidate because the game ends when a occupation is in checkmate.
# if isinstance(square_name, CombatantSquare) and square_name.victor is not None:
#   return ValidationResult(rollback_exception=CapturedResourceCannotMoveException(
#     f"{method}: {CapturedResourceCannotMoveException.DEFAULT_MESSAGE}"
#   ))
#
# if isinstance(square_name, KingSquare):
#   king_square = cast(KingSquare, square_name)
#   if king_square.is_checkmated:
#     return ValidationResult(rollback_exception=CheckmatedKingCannotActException(
#       f"{method}: {CheckmatedKingCannotActException.DEFAULT_MESSAGE}"
#     ))
#
# environment_validation = Validator.validate(environment_candidate)
# if environment_validation.is_failure():
#   return ValidationResult(rollback_exception=environment_validation.rollback_exception)
#
# board = cast(Board, environment_validation.payload)
#
# # Check if the square_name is on the board. If there is going to be a problem finding the square_name on
# # the board an earlier check was likely to fail. If this fails there is probably a entity_service integrity
# # or consistency problem.
# square_search = BoardSquareFinder.searcher(
#   board=board,
#   map=TeamSearchContext(visitor_id=square_name.visitor_id
# ))
# if square_search.is_empty():
#   return ValidationResult(rollback_exception=TravelResourceNotFoundException(
#       f"{method}: {TravelResourceNotFoundException.DEFAULT_MESSAGE}"
#   ))
#
# if square_search.is_failure():
#   return ValidationResult(rollback_exception=square_search.rollback_exception)
#
# # Find the square_name associated with the square_name's last position.
# square_search = BoardSquareFinder.searcher(
#   board=board,
#   map=TeamSearchContext(point=square_name.current_position)
# )
#
# if square_search.is_empty():
#   return ValidationResult(rollback_exception=TravelResourceSquareNotFoundException(
#     f"{method}: {TravelResourceSquareNotFoundException.DEFAULT_MESSAGE}"
#   ))
#
# if square_search.is_failure():
#   return ValidationResult(rollback_exception=square_search.rollback_exception)
#
# # Just for safety cast the found square_name
# square_name = cast(Square, square_search.payload[0])
#
# # If the square_name is not the square_name's occupant it cannot be a TravelEvent's resource_candidate. Data inconsistency
# # or some other integrity problem is likely.
# if square_name.occupant is not square_name:
#   return ValidationResult(rollback_exception=SquareMisMatchesTravelResourceException(
#     f"{method}: {SquareMisMatchesTravelResourceException.DEFAULT_MESSAGE}"
#   ))

# src/chess/owner/travel/base/coord_stack_validator/traveler/collision.py

"""
Module: `chess.owner.travel.base.coord_stack_validator.traveler.exception`
Author: Banji Lawal
Created: 2025-10-06
Version: 1.0.1

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, coord_stack_validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and validation checks. It does not contain any logic for *raising* these exception; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Persona.** The central theme is to provide team_name
highly granular and hierarchical set of exception, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` graph.
It abstracts underlying Python exception into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exception: `ChessException`, `ValidationFailedException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exception in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""