# src/chess/system/validate/old_occupation_validator.py

"""
Module: chess.system.validate.validator
Author: Banji Lawal
Created: 2025-08-27
Updated: 2025-10-10

# SECTION 1 - Purpose:
1. This module provides a satisfaction of the `ChessBot` integrity requirement. The satisfaction covers
    enforcement of the minimum naming regulations in the system.
2. This module provides a satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module covers name validation only.

# SECTION 3 - Limitations:
  1. The module does not provide permissible naming guidelines.
  2. Names that are allowed by the module might not meet additional restrictions other modules, classes, or processes
      have.

# SECTION 4 - Design Considerations and Themes:
Major themes influencing the design include:
1. Easy and fast debugging.
2. Single responsibility, single source of truth.


# SECTION 5 - Features Supporting Requirements:
1. No direct support for any user level features.
2. Direct support for reliability, verification, and integrity.
3. `NameValidator` can be used as component in more complex verifications.

# SECTION G - Feature Delivery Mechanism:
1. An exception for each requirement providing granular, accurate and precise error reporting.
2. Minimizing the boilerplate error handling and logging code with the `LoggingLevelRouter` decorator.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `MIN_NAME_LENGTH`, `MAX_NAME_LENGTH`, `LongNameException`, `ShortNameException`, `BlankNameException`
    `NullNameException`, `Validator`,

* From Python `typing` Library:
    `cast`

# SECTION 8 - Contains:
1. `NameValidator`
"""

from typing import cast


from chess.system import (
  MIN_NAME_LENGTH, MAX_NAME_LENGTH, Validator, ValidationResult, LongNameException,
  ShortNameException, BlankNameException, NullNameException, LoggingLevelRouter, InvalidNameException
)


class NameValidator(Validator[str]):
  """
  # ROLE: Validation, Integrity

  # RESPONSIBILITIES:
  Verify a candidate meets minimum naming regulations about length, and white space.

  # PROVIDES:
  A `ValidationResult` to clients.

  # ATTRIBUTES:
  No attributes.
  """

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: str) -> ValidationResult[str]:
    """
    # ACTION:
    Verify the `candidate` is a valid name in the application. The Application requires
    1. Candidate is not null.
    2. Candidate is a string whose length is between `MIN_NAME_LENGTH` and `MAX_NAME_LENGTH` inclusive.
    3. Candidate does not contain only white space.


    # PARAMETERS:
        * `candidate` (`str`): the name.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`str`) - A `str` meeting the `ChessBot` standard for names.
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

    # RAISES:
    `InvalidNameException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not a `str`
        * `NullNameException`: if `candidate` is null.
        * `BlankNameException`: if `candidate` only contains white space.
        * `ShortNameException`: if `candidate` is shorter than `MIN_NAME_LENGTH`.
        * `LongNameException`: if `candidate` is longer than `MAX_NAME_LENGTH`.
    """
    method = "NameValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=NullNameException(f"{method} {NullNameException.DEFAULT_MESSAGE}"))

      if not isinstance(candidate, str):
        return ValidationResult(exception=TypeError(f"{method} Expected an str, got {type(candidate).__name__}"))

      name = cast(str, candidate)

      if not name.strip():
       return ValidationResult(exception=BlankNameException(f"{method}: {BlankNameException.DEFAULT_MESSAGE}"))

      if len(name) < MIN_NAME_LENGTH:
        return ValidationResult(exception=ShortNameException(f"{method}: {ShortNameException.DEFAULT_MESSAGE}"))

      if len(name) > MAX_NAME_LENGTH:
        return ValidationResult(exception=LongNameException(f"{method}: {LongNameException.DEFAULT_MESSAGE}"))

      return ValidationResult(payload=name)

    except Exception as e:
      return ValidationResult(exception=InvalidNameException(f"{method} {e}"))