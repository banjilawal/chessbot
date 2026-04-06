# src/logic/system/color/coord_stack_validator.py

"""
Module: logic.system.color.coord_stack_validator
Author: Banji Lawal
Created: 2025-11-17
"""

from typing import Any, cast

from system import (
    Validator, ValidationResult, NameValidator, LoggingLevelRouter, GameColor, NullGameColorException,
    InvalidGameColorException
)


class GameColorValidator(Validator[GameColor]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a GameColor is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   Validator

    # PROVIDES:
        * GameColorValidator


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
        1.  KingCheckRecord rank is not validation.
        2.  KingCheckRecord if rank is a GameColor.
        3.  When all checks pass cast candidate to a GameColor instance, then return inside a ValidationResult.

        # PARAMETERS:
            *   rank (Any): Object to validate.

        # RETURNS:
        ValidationResult[GameColor] containing either:
            - On success: GameColor in the payload.
            - On failure: Exception.

        Raises:
            * TypeError
            * NullGameColorException
            * InvalidGameColorException
        """
        method = "GameColorValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult.failure(
                    NullGameColorException(f"{method}: {NullGameColorException.MSG}")
                )
            
            if not isinstance(candidate, GameColor):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameColor, but, got {type(candidate).__name__} instead.")
                )
            
            color = cast(GameColor, candidate)
            return ValidationResult.success(payload=color)
        
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameColorException(
                    f"{method}: {InvalidGameColorException.MSG}",
                    ex
                )
            )