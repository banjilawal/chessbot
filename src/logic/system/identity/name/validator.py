# src/logic/system/identity/designation/coord_stack_validator.py

"""
Module: logic.system.identity.designation.coord_stack_validator
Author: Banji Lawal
Created: 2025-08-27
version: 1.0.0
"""

from typing import cast

from logic.system import (
    BlankTextException, MIN_NAME_LENGTH, MAX_NAME_LENGTH, NullEmptyString, StringValidationProcess, ValidationProcess, ValidationResult,
    LongNameException,
    ShortNameException, WhiteSpaceNameException, NullNameException, LoggingLevelRouter, InvalidNameException
)


class NameValidationProcess(ValidationProcess[str]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a designation is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.
    3.  Names are required to be:
        *   Not validation.
        *   Is a STRING
        *   Not white space only (" ", tab, newline).
        *   Not empty. (".", ".\n", ".\t", ".\r").
        *   length between MIN_NAME_LENGTH and MAX_NAME_LENGTH inclusive.

    Super Class:
        *   ValidationProcess

    # PROVIDES:
        * NameValidationProcess


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: str,
            text_validator: StringValidationProcess = StringValidationProcess()
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
            *   candidate (Any): object to certify is a legal designation.
    
        # RETURNS:
        ValidationResult[str] containing either:
            - On success: str in the payload.
            - On failure: Exception.
    
        Raises:
            *   ShortNameException
            *   LongNameException
            *   InvalidNameException
        """
        method = "NameValidationProcess.validate"
        
        try:
            # Verify the candidate is not null and an int.
            validation = text_validator.execute(candidate)
            if validation.is_failure():
                return ValidationResult.failure(validation.exception)
            
            name = validation.name
            if len(name) < MIN_NAME_LENGTH:
                return ValidationResult.failure(
                    ShortNameException(f"{method}: {ShortNameException.MSG}")
                )
            if len(name) > MAX_NAME_LENGTH:
                return ValidationResult.failure(
                    LongNameException(f"{method}: {LongNameException.MSG}")
                )
            
            return ValidationResult.success(payload=name)
        # Finally, catch any missed exception, wrap an InvalidNameException around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidNameException(ex=ex, msg=f"{method}: {InvalidNameException.MSG}")
            )