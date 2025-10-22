# src/chess/square/travel/validation/resource_candidate.py

"""
Module: chess.square.travel.validation.resource_candidate
Author: Banji Lawal
Created: 2025-10-18
Version: 1.0.0
"""

from typing import cast, Tuple


from chess.square import Square, SquareValidator
from chess.system import LoggingLevelRouter, ValidationResult, Validator
from chess.board import Board, BoardSearchContext, BoardSquareSearch, BoardValidator, SquareIdSearchInvariantBreachException


class TravelResourceValidator(Validator[Square, Board]):
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
    method = "TravelResourceValidator.validate"

    try:
      if candidate is None:
        return ValidationResult.failure(
          NullResourceEnvironmentTupleException(f"{method}: {NullResourceEnvironmentTupleException.DEFAULT_MESSAGE}")
        )
      
      resource_candidate, environment_candidate = candidate

      resource_validation = SquareValidator.validate(resource_candidate)
      if resource_validation.is_failure():
        return ValidationResult.failure(resource_validation.exception)

      resource = cast(Square, resource_validation.payload)

      environment_validation = BoardValidator.validate(environment_candidate)
      if environment_validation.is_failure():
        return ValidationResult.failure(environment_validation.exception)

      environment = cast(Board, environment_validation.payload)

      search_result = BoardSquareSearch.search(board=environment, search_context=BoardSearchContext(id=resource.id))
      if search_result.is_empty():
        return ValidationResult.failure(
          SquareIdSearchInvariantBreachException(f"{method}: {SquareIdSearchInvariantBreachException.DEFAULT_MESSAGE}")
        )

      if search_result.is_failure():
        return ValidationResult.failure(exception=search_result.exception)

      return ValidationResult.success(payload=Tuple[resource, environment])
    
    except Exception as e:
      return ValidationResult(exception=e)