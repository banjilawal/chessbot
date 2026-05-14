# src/logic/system/text/validation.py

"""
Module: logic.system.text.validation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any, cast

from controller import WorkerRegistryController
from err import StringEmptyException, StringValidationException
from err.null.string import StringNullException
from util import LoggingLevelRouter, Validator, ValidationResult


class StringValidator(Validator[str]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a String instance is certified safe, reliable and consistent before use.

    Attributes:

    Provides:
       -    execute(
                    rank: Any,
                    number_validation: NumberValidator,
            ) -> ValidationResult[String]

    Super Class:
        Validator
    """
    OPERATION_NAME = "text_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(cls, candidate: Any) -> ValidationResult[str]:
        """
        Verify the object is a String that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if
                    -   the rank does not exist.
                    -   the rank is not a String.
                    -   the row or column is not between [0-7] inclusive.
            2.  Otherwise, after the rank is cast to a String, send the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[str]
        Raises:
            TypeError
            StringNullException
            StringEmptyException
            StringValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                StringValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=StringValidationException.MSG,
                    err_code=StringValidationException.ERR_CODE,
                    ex=StringNullException(
                        msg=StringNullException.MSG,
                        err_code=StringNullException.ERR_CODE,
                    )
                )
            )
        # Handle the wrong class case
        if not isinstance(candidate, str):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                StringValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=StringValidationException.MSG,
                    err_code=StringValidationException.ERR_CODE,
                    ex=TypeError(f"Expected an str, got {type(candidate).__name__} instead.")
                )
            )
        # --- Cast candidate to a string for additional tests, trimming all white space first. ---#
        text = cast(str, candidate).strip()
        
        if len(text) == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                StringValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=StringValidationException.MSG,
                    err_code=StringValidationException.ERR_CODE,
                    ex=StringEmptyException(
                        msg=StringEmptyException.MSG,
                        err_code=StringEmptyException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(text)


# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register(worker=StringValidator)