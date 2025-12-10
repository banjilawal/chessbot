# src/chess/system/err/text/validator.py

"""
Module: chess.system.err.text.validator_
Author: Banji Lawal
Created: 2025-11-29
version: 1.0.0
"""

from typing import cast

from chess.system import (
    BlankTextException, InvalidTextException, LoggingLevelRouter, NullStringException, ValidationResult, Validator
)


class TextValidator(Validator[str]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security., Integrity

    # RESPONSIBILITIES:
    Verifies a candidate is a string that is neither null, empty, nor white space only.

    # PROVIDES:
    ValidationResult[str] containing either:
        - On success: str in the payload.
        - On failure: Exception.

    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: str) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Verify the candidate is not null.
        2.  Verify the candidate is a string that is neither null, empty nor white space only.
        3.  If all the checks pass the candidate is converted to a string and returned in a ValidationResult.

        # PARAMETERS:
            *   candidate (Any)
            *   text_validator (TextValidator)

        # Returns:
        ValidationResult[str] containing either:
            - On success: str in the payload.
            - On failure: Exception.

        # Raises:
            *   NullTextError
            *   TypeError
            *   BlankTextError
        """
        method = "TextValidator.validate"
        
        try:
            # Verify the candidate is not null and an int.
            if candidate is None:
                return ValidationResult.failure(
                    NullStringException(f"{method}: {NullStringException.DEFAULT_MESSAGE}")
                )
                # Raise an error if its not a str.
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected an str, got {type(candidate).__name__} instead.")
                )
            
            # Cast the candidate to a string and strip of all the white space.
            text = cast(str, candidate).strip()
            # Check if the string is empty after stripping of the white space.
            if len(text.strip()) == 0:
                return ValidationResult.failure(
                    BlankTextException(f"{method}: {BlankTextException.DEFAULT_MESSAGE}")
                )
            # If no errors are detected return the text in ValidationResult.
            return ValidationResult.success(payload=text)
        # Finally, if there is an unhandled exception Wrap an InvalidNameException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidTextException(ex=ex, message=f"{method}: {InvalidTextException.DEFAULT_MESSAGE}")
            )