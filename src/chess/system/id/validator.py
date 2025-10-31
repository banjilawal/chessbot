# src/chess/system/id/validator.py

"""
Module: chess.system.id.validator
Author: Banji Lawal
Created: 2025-08-12
Updated: 2025-10-10

"""

from typing import cast

from chess.system import(
  Validator, LoggingLevelRouter, ValidationResult, IdNullException, NegativeIdException, InvalidIdException
)



class IdValidator(Validator[int]):
  """
  # ROLE: Validation, Integrity 

  # RESPONSIBILITIES:
  Verify a candidate is not null and a positive number.

  # PROVIDES:
  A `ValidationResult` to clients.

  # ATTRIBUTES:
  No attributes.
  """
  
  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: int) -> ValidationResult[int]:
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
        `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    method = "IdValidator"

    try:
      if candidate is None:
        return  ValidationResult(exception=IdNullException(f"{method} {IdNullException.DEFAULT_MESSAGE}"))

      if not isinstance(candidate, int):
        return ValidationResult(exception=TypeError(f"{method} Expected an integer, got {type(candidate).__id__}"))

      id = cast(int, candidate)

      if id < 0:
        return ValidationResult(exception=NegativeIdException(f"{method} {NegativeIdException.DEFAULT_MESSAGE}"))

      return ValidationResult(payload=id)

    except Exception as e:
      return ValidationResult(exception=InvalidIdException(f"{method}: {e}"))