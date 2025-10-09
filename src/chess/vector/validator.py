# src/chess/piece/event/transaction
"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Validation, Single responsibilities,
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:
From `chess.system`:
  * `ValidationResult`, `Validator`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`

From `chess.vector`:
    `Vector`, `NullVectorException`, `InvalidVectorException`, `NullXComponentException`,
    `NullYComponentException`, `VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
 * `VectorValidator`
"""

from typing import cast, TypeVar

from chess.system import ValidationResult, Validator, KNIGHT_STEP_SIZE, LoggingLevelRouter
from chess.vector import (
  Vector, NullVectorException, NullXComponentException, NullYComponentException,
  VectorBelowBoundsException, VectorAboveBoundsException, InvalidVectorException
)

class VectorValidator(Validator[Vector]):
    """
    # ROLE: Validation

    # RESPONSIBILITIES:
    1. Prevents using an existing Vector` that will cause failures or introduce bugs if deployed.
    2. Ensures clients receive only valid Vectors for further processing.
    3. Report errors and return `ValidationResult` with error details.

    # PROVIES:
      `ValidationResult`: Return type containing the built `Vector` or error information.

    # ATTRIBUTES:
    None
    """

    @classmethod
    def validate(cls, candidate: Vector) -> ValidationResult[Vector]:
        """
        ACTION:
        Ensure an existing `Vector` object will not introduce bugs or failures.

        PARAMETERS:
            * `candidate` (`Vector`): The validation candidate.

        RETURNS:
        `ValidationResult[Vector]`: A `ValidationResult` containing either:
            `'payload'` - A `Vector` instance that satisfies the specification.
            `exception` - Details about which specification violation occurred.

        RAISES:
        `InvalidVectorException`: Wraps any specification violations including:
            * `NullXComponentException`: if `x` is None
            * `NullYComponentException`: if `y` is None
            * `VectorBelowBoundsException`: if `x` or `y` < -KNIGHT_STEP_SIZE
            * `VectorAboveBoundsException`: if `x` or `y` > KNIGHT_STEP_SIZE
        """
        method = "VectorValidator.validate"

        try:
            # Handle the null case first
            if candidate is None:
                ex = NullVectorException(f"{method}: {NullVectorException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            # Abort if the candidate is not a Vector
            if not isinstance(candidate, Vector):
                ex = TypeError(f"{method}: Expected an Vector, got {type(candidate).__name__}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            vector = cast(Vector, candidate)

            # Handle the x-component checks
            if vector.x is None:
                ex = NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            if vector.x < -KNIGHT_STEP_SIZE:
                ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            if vector.x > KNIGHT_STEP_SIZE:
                ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            # Handle the y-component checks
            if vector.y is None:
                ex = NullYComponentException(f"{method}: {NullYComponentException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            if vector.y < -KNIGHT_STEP_SIZE:
                ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            if vector.y > KNIGHT_STEP_SIZE:
                ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.route_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            return ValidationResult(payload=vector)

        except (
            TypeError,
            NullVectorException,
            NullXComponentException,
            NullYComponentException,
            VectorBelowBoundsException,
            VectorAboveBoundsException
        ) as e:
            raise InvalidVectorException(f"{method}: {e}") from e

        # This block catches any unexpected exceptions, logs and re
        except Exception as e:
            LoggingLevelRouter.route_error(context=VectorValidator, exception=e)
            raise InvalidVectorException(f"{method}: {e}") from e