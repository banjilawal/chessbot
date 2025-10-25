# src/chess/vector/old_occupation_validator.py

"""
Module: chess.vector.validator
Author: Banji Lawal
Created: 2025-10-08

# SCOPE:
-------
***Limitation 1***: This module cannot prevent classes, processes or modules using `Vector`
    instances that pass sanity checks will not fail when using the validated `Vector`.
    Once client's processes might fail, experience data inconsistency or have other
    faults.
***Limitation 2***: Objects authenticated by `VectorValidator` might fail additional requirements
    a client has for a `Vector`. It is the client's responsibility to ensure the validated
    `Vector` passes and additional checks before deployment.

**Related Features**:
    Building vectors -> See VectorBuilder, module[chess.vector.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error detection, error prevention

# PURPOSE:
---------
1. Central, single source of truth for correctness of existing `Vector` objects.
2. Putting all the steps and logging into one place makes modules using `Vector` objects
    cleaner and easier to follow.

***Satisfies***: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
  * `ValidationResult`, `Validator`, `KNIGHT_STEP_SIZE`, `LoggingLevelRouter`

From `chess.vector`:
    `Vector`, `NullVectorException`, `InvalidVectorException`, `NullXComponentException`,
    `NullYComponentException`, `VectorBelowBoundsException`, `VectorAboveBoundsException`

# CONTAINS:
----------
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
    3. Sending granular error report via `ValidationResult`.

    # PROVIDES:
      `ValidationResult`: Return type containing the built `Vector` or error information.

    # ATTRIBUTES:
    None
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Vector) -> ValidationResult[Vector]:
        """
        ACTION:
        Ensure an existing `Vector` object will not introduce bugs or failures.

        PARAMETERS:
            * `candidate` (`Vector`): The validator candidate.

        RETURNS:
        `ValidationResult[Vector]`: A `ValidationResult` containing either:
            `'payload'` - A `Vector` instance that satisfies the specification.
            `rollback_exception` - Details about which specification violation occurred.

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
                # ex = NullVectorException(f"{method}: {NullVectorException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=ex)
                return ValidationResult(exception=NullVectorException(
                    f"{method}: {NullVectorException.DEFAULT_MESSAGE}"
                ))

            # Abort if the candidate is not a Vector
            if not isinstance(candidate, Vector):
                # ex = TypeError(f"{method}: Expected an Vector, got {type(candidate).__name__}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=ex)
                return ValidationResult(exception=TypeError(
                    f"{method}: Expected an Vector, got {type(candidate).__name__}"
                ))

            vector = cast(Vector, candidate)

            # Handle the x-component checks
            if vector.x is None:
                # ex = NullXComponentException(f"{method}: {NullXComponentException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=ex)
                return ValidationResult(exception=NullXComponentException(
                    f"{method}: {NullXComponentException.DEFAULT_MESSAGE}"
                ))

            if vector.x < -KNIGHT_STEP_SIZE:
                ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                LoggingLevelRouter.log_and_raise_error(context=VectorValidator, exception=ex)
                return ValidationResult(exception=ex)

            if vector.x > KNIGHT_STEP_SIZE:
                # ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=ex)
                return ValidationResult(exception=VectorBelowBoundsException(
                    f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                ))

            # Handle the y-component checks
            if vector.y is None:
                # ex = NullYComponentException(f"{method}: {NullYComponentException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=ex)
                return ValidationResult(exception=NullYComponentException(
                    f"{method}: {NullYComponentException.DEFAULT_MESSAGE}"
                ))

            if vector.y < -KNIGHT_STEP_SIZE:
                # ex = VectorBelowBoundsException(f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=ex)
                return ValidationResult(exception=VectorBelowBoundsException(
                    f"{method}: {VectorBelowBoundsException.DEFAULT_MESSAGE}"
                ))

            if vector.y > KNIGHT_STEP_SIZE:
                # ex = VectorAboveBoundsException(f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}")
                # LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=ex)
                return ValidationResult(exception=VectorAboveBoundsException(
                    f"{method}: {VectorAboveBoundsException.DEFAULT_MESSAGE}"
                ))

            return ValidationResult(payload=vector)

        # This block lets the monitor log and re-raise the error.
        except Exception as e:
            return ValidationResult(exception=InvalidVectorException(f"{method}: {e}"))


        # This block catches any unexpected exceptions, logs and re-raises them.
        # except Exception as e:
        #     LoggingLevelRouter.log_and_raise_error(context=VectorValidator, rollback_exception=e)
        #     raise InvalidVectorException(f"{method}: {e}") from e