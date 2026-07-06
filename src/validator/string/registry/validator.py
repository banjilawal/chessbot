# src/validator/string/registry/validator.py

"""
Module: validator.string.registry.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import List, cast

from controller import WorkerRegistryController
from err import (
    EmptyListException, ListNullException, RegistryEntryKeyStringValidationException, StringValidationException
)
from operation import PrimingValidator, Validator
from validator.string import NameValidator
from result import ValidationResult
from util import LoggingLevelRouter


class RegistryEntryNameValidator(Validator):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure registry entry names and domains are valida strings.

    Attributes:

    Provides:
       -    execute(
                candidates: List[str],
                name_validator: NameValidator,
                priming_validator: PrimingValidator,
            ) -> ValidationResult[List[String]]

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidates: List[str],
            name_validator: NameValidator | None = None,
            priming_validator: PrimingValidator | None = None,
    ) -> ValidationResult[List[str]]:
        """
        Verify the list of names are safe to use as domains and keys in Registries.

        Action:
            1.  Send an exception chain in the ValidationResult if ay of the following occur
                    -   The candidates is not a List or its empty.
                    -   The names are not in a List.
                    -   Any name in the list fails string validator.
            2.  Otherwise, send the success result.
        Args:
            candidates: List[str]
            name_validator: NameValidator
            priming_validator: PrimingValidator
        Returns:
            ValidationResult[List[str]]
        Raises:
            ListNullException
            EmptyListException
            StringValidationException
            RegistryEntryKeyStringValidationException
        """
        method = f"{cls.__name__}.execute"
        
        # --- Supply any missing dependencies. ---#
        if name_validator is None:
            name_validator = NameValidator()
        if priming_validator is None:
            priming_validator = PrimingValidator()
        
        list_validation_result = priming_validator.validate(
            candidate=candidates,
            target_model=List[str],
            null_exception=ListNullException()
        )
        # Handle the case that, the candidate is not a List.
        if list_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RegistryEntryKeyStringValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RegistryEntryKeyStringValidationException.MSG,
                    err_code=RegistryEntryKeyStringValidationException.ERR_CODE,
                    ex=list_validation_result.exception,
                )
            )
        # --- Cast the candidate into a Team for additional tests ---#
        names = cast(List[str], candidates)
        
        # Handle the case that, there are no names in the list.
        if len(names) == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RegistryEntryKeyStringValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=RegistryEntryKeyStringValidationException.MSG,
                    err_code=RegistryEntryKeyStringValidationException.ERR_CODE,
                    ex=EmptyListException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=EmptyListException.MSG,
                        err_code=EmptyListException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, any name in the list cannot be used as Registry key.
        for name in names:
            name_validation_result = name_validator.validate(name)
            # Send the exception chain on failure.
            if name_validation_result.is_failure:
                return ValidationResult.failure(
                    StringValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=StringValidationException.MSG,
                        err_code=StringValidationException.ERR_CODE,
                        ex=name_validation_result.exception,
                        var="name",
                        val=f"{name}"
                    )
                )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(names)

# --- FINALLY: REGISTER THE OPERATION ---#
WorkerRegistryController.register_worker(worker=RegistryEntryNameValidator)
