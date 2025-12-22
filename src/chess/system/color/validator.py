# src/chess/system/color/coord_stack_validator.py

"""
Module: chess.system.color.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-17
"""

from typing import Any, cast

from chess.system import (
    Validator, ValidationResult, NameValidator, LoggingLevelRouter, GameColor, NullGameColorException,
    InvalidGameColorException
)


class GameColorValidator(Validator[GameColor]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security.

    # RESPONSIBILITIES:
    1.  Ensure a GameColor is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    # PARENT:
        *   Validator

    # PROVIDES:
        * GameColorValidator

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            game_color_enum: GameColor
    ) -> ValidationResult[GameColor]:
        """
        # ACTION:
        1.  Check candidate is not validation.
        2.  Check if candidate is a GameColor.
        3.  When all checks pass cast candidate to a GameColor instance, then return inside a ValidationResult.

        # PARAMETERS:
            *   candidate (Any): Object to validate.

        # Returns:
        ValidationResult[GameColor] containing either:
            - On success: GameColor in the payload.
            - On failure: Exception.

        # RAISES:
            * TypeError
            * NullGameColorException
            * InvalidGameColorException
        """
        method = "GameColorValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullGameColorException(f"{method}: {NullGameColorException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(candidate, GameColor):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameColor, but got {type(candidate).__name__} instead.")
                )
            
            color = cast(GameColor, candidate)
            return ValidationResult.success(payload=color)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameColorException(
                    f"{method}: {InvalidGameColorException.DEFAULT_MESSAGE}",
                    ex
                )
            )