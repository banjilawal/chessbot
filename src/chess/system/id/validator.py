# src/chess/system/travel/old_occupation_validator.py

"""
Module: chess.system.id.validator
Author: Banji Lawal
Created: 2025-08-12
Updated: 2025-10-10

# SECTION 1 - Purpose:
1. This module provides a satisfaction of the `ChessBot` integrity requirement. The satisfaction covers
    enforcement of regulations for unique IDs in the system.
2. This module provides a satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module only covers the `IdValidator` provider.

# SECTION 3 - Limitations:
  1. This module is not responsible for verifying the uniqueness of an ID. the `AutoId` class in
      `chess.system.id.auto_id` module.
  1. The module is not responsible for supplying or publishing IDs that meet system requirements. 
      For details about publishing IDs see the `AutoId` class in module `chess.system.id.auto_id`.

# SECTION 4 - Design Considerations and Themes:
Major themes influencing the design include:
1. Easy and fast debugging.
2. Single responsibility, single source of truth.

# SECTION 5 - Features Supporting Requirements:
1. No direct support for any user level features.
2. Direct support for reliability, verification, and integrity.

# SECTION G - Feature Delivery Mechanism:
1. An exception for each requirement providing granular, accurate and precise error reporting.
2. Minimizing the boilerplate error handling and logging code with the `LoggingLevelRouter` decorator.
3. `IdValidator` can be used as component in more complex verifications.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `Validator`, `NegativeIdException`, `IdNullException`, `InvalidIdException`

* From Python `typing` Library:
    `cast`

# SECTION 8 - Contains:
1. `IdValidator`
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
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

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