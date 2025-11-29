# src/chess/system/identity/name/coord_stack_validator.py

"""
Module: chess.system.identity.name.coord_stack_validator
Author: Banji Lawal
Created: 2025-08-27
version: 1.0.0
"""

from typing import cast

from chess.system import (
    BlankTextException, MIN_NAME_LENGTH, MAX_NAME_LENGTH, NullTextException, TextValidator, Validator, ValidationResult,
    LongNameException,
    ShortNameException, WhiteSpaceNameException, NullNameException, LoggingLevelRouter, InvalidNameException
)


class NameValidator(Validator[str]):
    """
    # ROLE: Validation, Integrity
  
    # RESPONSIBILITIES:
    Verifies a candidate is
        *   Not validation.
        *   Is a STRING
        *   Not white space only (" ", tab, newline).
        *   Not empty. (".", ".\n", ".\t", ".\r").
        *   length between MIN_NAME_LENGTH and MAX_NAME_LENGTH inclusive.
    If the conditions are met NameValidator authorizes using the candidate.
  
    # PROVIDES:
    ValidationResult[str] containing either:
        - On success: str in the payload.
        - On failure: Exception.
        
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: str,
            text_validator: TextValidator = TextValidator()
    ) -> ValidationResult[str]:
        """
        # ACTION:
        1.  Test if the candidate is:
            *   Not validation.
            *   Is not a white-space string.
            *   Is not an empty string.
            *   has a length between MIN_NAME_LENGTH and MAX_NAME_LENGTH.
        2.  If any check fails send their exception inside a ValidationResult.
        3.  When all checks pass, cast the candidate to a STRING, then send to caller in a ValidationResult.
    
        # PARAMETERS:
            *   candidate (Any): object to certify is a legal name.
    
        # Returns:
        ValidationResult[str] containing either:
            - On success: str in the payload.
            - On failure: Exception.
    
        # Raises:
            *   ShortNameException
            *   LongNameException
            *   InvalidNameException
        """
        method = "NameValidator.validate"
        
        try:
            # Verify the candidate is not null and an int.
            validation = text_validator.validate(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            
            name = validation.name
            if len(name) < MIN_NAME_LENGTH:
                return ValidationResult.failure(
                    ShortNameException(f"{method}: {ShortNameException.DEFAULT_MESSAGE}")
                )
            if len(name) > MAX_NAME_LENGTH:
                return ValidationResult.failure(
                    LongNameException(f"{method}: {LongNameException.DEFAULT_MESSAGE}")
                )
            
            return ValidationResult.success(payload=name)
        # Finally, if there is an unhandled exception Wrap an InvalidNameException around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNameException(ex=ex, message=f"{method}: {InvalidNameException.DEFAULT_MESSAGE}")
            )