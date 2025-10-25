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
# # king as an resource_candidate because the game ends when a king is in checkmate.
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
# # the board an earlier check was likely to fail. If this fails there is probably a data integrity
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