# src/chess/square/travel/validation/resource_candidate.py

"""
Module: chess.square.travel.validation.resource_candidate
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0
"""

from typing import cast, Tuple


from chess.square import Square, SquareValidator
from chess.system import BindingValidator, LoggingLevelRouter, ValidationResult
from chess.board import Board, BoardSearchContext, BoardSquareSearch, BoardValidator, SearchBySquareIdInvariantBreachException


class ResourceBindingBoardValidator(BindingValidator[Square, Board]):
  """
  # ROLE: Validator, Data Integrity

  # RESPONSIBILITIES:
  1. Ensure `TravelEvent` resource_candidate has a valid binding to the execution environment for `TravelEventFresourcey`.
  2. If binding requirements are not satisfied return the appropriate error to `TravelEventFresourcey` in
      `ValidationResult`.
  3. Discover potential data integrity violations.

  # PROVIDES:
  `ValidationResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: Tuple[Square, Board]) -> ValidationResult[Tuple[Square, Board]]:
    """"""
    method = "ResourceBindingBoardValidator.validate"

    try:
      resource_candidate, environment_candidate = candidate

      resource_validation = SquareValidator.validate(resource_candidate)
      if resource_validation.is_failure():
        return ValidationResult(exception=resource_validation.exception)

      square = cast(Square, resource_validation.payload)

      exec_environment_validation = BoardValidator.validate(environment_candidate)
      if exec_environment_validation.is_failure():
        return ValidationResult(exception=exec_environment_validation.exception)

      board = cast(Board, exec_environment_validation.payload)

      search_result = BoardSquareSearch.search(board=board, search_context=BoardSearchContext(id=square.id))
      if search_result.is_empty():
        return ValidationResult(exception=SearchBySquareIdInvariantBreachException(
          f"{method}: {SearchBySquareIdInvariantBreachException.DEFAULT_MESSAGE}"
        ))

      if search_result.is_failure():
        return ValidationResult(exception=search_result.exception)


      return ValidationResult(payload=Tuple[square, board])
    except Exception as e:
      return ValidationResult(exception=e)