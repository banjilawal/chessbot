# src/chess/system/text/validator.py

"""
Module: chess.system.text.validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import cast

from chess.system import LoggingLevelRouter, Validator, ValidationResult


class StringValidator(Validator[str]):
    """
     # ROLE: Validation, Data Integrity Guarantor, Security., Integrity

    # RESPONSIBILITIES:
    1.  Ensure a String is neither null, empty, nor whitespace before use.
    2.  If a candidate fails a safety test, the validator sends an exception in a ValidationResult.
    
    # PARENT:
        *   Validator

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: str) -> ValidationResult[str]:
        """
        # ACTION:
             1. If the candidate passes existence and type checks cast into a str for
                additional integrity tests. Else return an exception in the ValidationResult.
            2.  If the text is empty, blank, no length, return an exception in the ValidationResult.
            3.  If the text contains only white space, return an exception in the ValidationResult.
            4.  If all the checks pass return the text in the ValidationResult.

        # PARAMETERS:
            *   candidate (Any)

        # Returns:
        ValidationResult[str] containing either:
            - On success: str in the payload.
            - On failure: Exception.

        # Raises:
            *   NullTextError
            *   TypeError
            *   BlankTextError
        """
        method = "StringValidator.validate"
        
        try:
            # Handle the nonexistence case.
            if candidate is None:
                return ValidationResult.failure(NullString(f"{method}: {NullString.DEFAULT_MESSAGE}"))
            # Handle the wrong class case.
            if not isinstance(candidate, str):
                return ValidationResult.failure(
                    TypeError(f"{method} Expected an str, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks are successful cast the candidate to a str, trim all white
            # space.
            text = cast(str, candidate).strip()
            
            # Handle the empty string case.
            if len(text.strip()) == 0:
                return ValidationResult.failure(
                    EmptyBlankStringException(f"{method}: {EmptyBlankStringException.DEFAULT_MESSAGE}")
                )
            # Handle the success case by sending the text in a ValidationResult.
            return ValidationResult.success(payload=text)
        
        # Finally, catch any missed exception, wrap an InvalidStringException around it then
        # return the exception inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidStringException(ex=ex, message=f"{method}: {InvalidStringException.DEFAULT_MESSAGE}")
            )