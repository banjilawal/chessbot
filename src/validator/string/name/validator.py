# src/logic/system/text/validator.py

"""
Module: logic.system.text.validation
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Any

from controller import WorkerRegistryController
from err import MaxNameLengthException, MinNameLengthException, NameValidationException

from operation import StringValidator, Validator
from result import ValidationResult
from setting import StringProperty, StringPropertyTable
from util import LoggingLevelRouter


class NameValidator(Validator[str]):
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
                    candidate: Any,
                    string_validator: StringValidator,
                    string_property_table: StringPropertyTable,
            ) -> ValidationResult[String]

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            string_validator: StringValidator | None = None,
            string_property_table: StringPropertyTable | None = None,
    ) -> ValidationResult[str]:
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
            string_validator: StringValidator
            string_property_table: StringPropertyTable
        Returns:
            ValidationResult[str]
        Raises:
            TypeError
            StringNullException
            StringEmptyException
            StringValidationException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if string_property_table is None:
            string_property_table = StringPropertyTable()
        if string_validator is None:
            string_validator = StringValidator()
        
        string_validation_result = string_validator.validate(candidate)
        
        # Handle the case that, the candidate is flagged unsafe.
        if string_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NameValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NameValidationException.MSG,
                    err_code=NameValidationException.ERR_CODE,
                    ex=string_validation_result.exception,
                )
            )
        # Handle the case tha the name is too short.
        if len(string_validation_result.payload) < string_property_table.entry[StringProperty.MIN_LENGTH]:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NameValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NameValidationException.MSG,
                    err_code=NameValidationException.ERR_CODE,
                    ex=MinNameLengthException(
                        msg=MinNameLengthException.MSG,
                        err_code=MinNameLengthException.ERR_CODE,
                    )
                )
            )
        # Handle the case tha the name is too long.
        if len(string_validation_result.payload) > string_property_table.entry[StringProperty.MAX_LENGTH]:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                NameValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=NameValidationException.MSG,
                    err_code=NameValidationException.ERR_CODE,
                    ex=MaxNameLengthException(
                        msg=MaxNameLengthException.MSG,
                        err_code=MaxNameLengthException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the caller. ---#
        return string_validation_result

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=NameValidator)