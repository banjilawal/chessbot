# src/chess/square/validator.py

"""
Module: chess.square.validator
Author: Banji Lawal
Created: 2025-09-28
Updated: 2025-10-10

# SECTION 1 - Purpose:
This module provides a satisfaction of the `ChessBot` integrity requirement.

# SECTION 2 - Scope:
The module covers minimum verification requirements of `Square` objects

# SECTION 3 - Limitations:
  1. This module cannot only be used on existing `Square` instances. Use `SquareBuilder` for construction.
  2. A `Square` positively verified by the module may fail stricter requirements other components may have.

# SECTION 4 - Design Considerations and Themes:
  1. A `Square` must undergo sanity checking before use.
  2. As a fundamental, ubiquitous item consolidating all `Square` sanity checking into one place avoids repetition
      and inconsistent implementations.
  3. Moving all the verification code into one place creates a highly cohesive component.
  4. The component is loosely coupled to other entities even squares and can be used anywhere.
  5. This module cuts down code, increases understanding an simplicity.

# SECTION 5 - Features Supporting Requirements:
1. Testability: Unit testing the module is easy.
2. Maintainable: The component is easy to maintain.

# SECTION G - Feature Delivery Mechanism:
The order of sanity checks produces early failures. to the most granular

# SECTION 7 - Dependencies:
* From `chess.system`:
    `Validator`, `ValidationResult`, `NameValidator`, `LoggingLevelRouter`

* From `chess.square`:
    `Square`, `InvalidSquareException`

* From `chess.coord`:
    `Coord`, `CoordValidator`

* From Python `abc` Library:
    `ABC`, `abstractmethod`

* From Python `typing` Library:
    `Generic`, `TypeVar`

# SECTION 8 - Contains:
1. `SquareValidator`
"""


from typing import Any, cast

from chess.coord import CoordValidator
from chess.square import Square, InvalidSquareException, NullSquareException
from chess.system import Validator, ValidationResult, NameValidator, LoggingLevelRouter, IdValidator


class SquareValidator(Validator[Square]):
  """
  # ROLE: Validation

  # RESPONSIBILITIES:
  1. Run sanity checks on a `candidate` to make sure its a valid `Square` before use.
  2. Pass results of validation process to client.

  # PROVIDES:
  `ValidationResult[Square]` containing either a verified `Square` or an `Exception`.

  # ATTRIBUTES:
  No attributes.
  """


  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: Any) -> ValidationResult[Square]:
    """
    # Action:
    Ensures clients the candidate meets minimum system requirements for use in the system.

    # Parameters:
      * `candidate` (`Any`): The object to verify

    # Returns:
      `ValidationResult[Square]`: A `ValidationResult` containing either:
            `'payload'` - A `Square` instance that satisfies the specification.
            `exception` - Details about which specification violation occurred.

    # Raises:
    No Exceptions are raised. Exceptions are returned to caller in `ValidationResult[Square]`
    """

    method = "SquareValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=NullSquareException(f"{method} {NullSquareException.DEFAULT_MESSAGE}"))

      if not isinstance(candidate, Square):
        return ValidationResult(exception=TypeError(f"Expected Square, but got {type(candidate).__name__}."))

      square = cast(Square, candidate)

      id_validation = IdValidator.validate(square.id)
      if not id_validation.is_success():
        return ValidationResult(exception=id_validation.exception)

      name_validation = NameValidator.validate(square.name)
      if not name_validation.is_success():
        return ValidationResult(exception=name_validation.exception)

      coord_validation = CoordValidator.validate(square.coord)
      if not coord_validation.is_success():
        raise coord_validation.exception

      return ValidationResult(payload=square)

    except Exception as e:
      return ValidationResult(exception=InvalidSquareException(f"{method}: {e}"))
