#
#
#
#
# resource_validation = SquareValidator.validate(resource_candidate)
# if resource_validation.is_failure():
#   return ValidationResult(rollback_exception=resource_validation.rollback_exception)
#
# square = cast(Square, resource_validation.payload)
#
# # If the square has no position history its not on the board and cannot square.
# if square.current_position is None or square.positions.is_empty():
#   return ValidationResult(rollback_exception=NoInitialPlacementException(
#     f"{method}: {NoInitialPlacementException.DEFAULT_MESSAGE}"
#   ))
#
# # If the square is not on its team roster it cannot be a TravelEvent resource_candidate. This might have been
# # checked by the SquareValidator
# team = square.team
# if square not in team.roster:
#   return ValidationResult(rollback_exception=ResourceNotOnRosterCannotMoveException(
#     f"{method}: {ResourceNotOnRosterCannotMoveException.DEFAULT_MESSAGE}"
#   ))
#
# # A captured combatant cannot be a TravelEvent resource_candidate. No need for validating a checkmated
# # occupation as an resource_candidate because the game ends when a occupation is in checkmate.
# if isinstance(square, CombatantSquare) and square.captor is not None:
#   return ValidationResult(rollback_exception=CapturedResourceCannotMoveException(
#     f"{method}: {CapturedResourceCannotMoveException.DEFAULT_MESSAGE}"
#   ))
#
# if isinstance(square, KingSquare):
#   king_square = cast(KingSquare, square)
#   if king_square.is_checkmated:
#     return ValidationResult(rollback_exception=CheckMatedKingCannotMoveException(
#       f"{method}: {CheckMatedKingCannotMoveException.DEFAULT_MESSAGE}"
#     ))
#
# environment_validation = Validator.validate(environment_candidate)
# if environment_validation.is_failure():
#   return ValidationResult(rollback_exception=environment_validation.rollback_exception)
#
# board = cast(Board, environment_validation.payload)
#
# # Check if the square is on the board. If there is going to be a problem finding the square on
# # the board an earlier check was likely to fail. If this fails there is probably a service integrity
# # or consistency problem.
# square_search = BoardSquareSearch.search(
#   board=board,
#   search_context=BoardSearchContext(id=square.id
# ))
# if square_search.is_empty():
#   return ValidationResult(rollback_exception=TravelResourceNotFoundException(
#       f"{method}: {TravelResourceNotFoundException.DEFAULT_MESSAGE}"
#   ))
#
# if square_search.is_failure():
#   return ValidationResult(rollback_exception=square_search.rollback_exception)
#
# # Find the square associated with the square's last position.
# square_search = BoardSquareSearch.search(
#   board=board,
#   search_context=BoardSearchContext(coord=square.current_position)
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
# # Just for safety cast the found square
# square = cast(Square, square_search.payload[0])
#
# # If the square is not the square's occupant it cannot be a TravelEvent's resource_candidate. Data inconsistency
# # or some other integrity problem is likely.
# if square.occupant is not square:
#   return ValidationResult(rollback_exception=SquareMisMatchesTravelResourceException(
#     f"{method}: {SquareMisMatchesTravelResourceException.DEFAULT_MESSAGE}"
#   ))

# chess/owner/travel/base/validator/traveler/exception.py

"""
Module: `chess.owner.travel.base.validator.traveler.exception`
Author: Banji Lawal
Created: 2025-10-06
Version: 1.0.1

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validator, and manipulation of **Coord objects**. It handles boundary checks (row/column)
limits and null checks. It does not contain any logic for *raising* these exceptions; that responsibility
falls to the `CoordValidator` and `CoordBuilder`processes.

THEME:
-----
**Comprehensive Domain Error Catalog.** The central theme is to provide team
highly granular and hierarchical set of exceptions, ensuring that callers can
catch and handle errors based on both the **type of failure** (e.g., `NullException`)
and the **affected graph** (e.g., `CoordException`). This enables precise error
logging and handling throughout the system.

PURPOSE:
-------
To serve as the **centralized error dictionary** for the `Coord` graph.
It abstracts underlying Python exceptions into graph-specific, custom error types
to improve code clarity and facilitate robust error handling within the chess engine.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Constants: `ROW_SIZE`, `COLUMN_SIZE`
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `CoordException`,
`NullCoordException`, `RowAboveBoundsException`).
"""