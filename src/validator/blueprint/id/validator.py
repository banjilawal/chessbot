# src/validator/blueprint/id/validator.py

"""
Module: validator.blueprint.id.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import BlueprintIdValidatorException
from microservice import IdentityService
from result import ValidationResult
from util import IdFactory, LoggingLevelRouter
from validator import Validator


class BlueprintIdValidator(Validator[int]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Validate a Blueprint's id if one is present. Otherwise, generate a unique one.

    Attributes:

    Provides:
        -   def validate(candidate: Any, model_name: str, identity_service: IdentityService) -> ValidationResult:

    Super Class:
        BlueprintValidator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            model_name: str,
            identity_service: IdentityService | None = None
    ) -> ValidationResult[int]:
        """
        Verify the id if it already exists or create a new one.

        Action:
            1.  If the candidate is not null:
                    -   Send an exception chain in the ValidationResult when its not an int.
                    -   Otherwise, send the success result.
            2.  If the candidate is null:
                    -   Send an exception chain in the ValidationResult if the model_name is not a string.
                    -   Otherwise, generate a unique id for the next model instance.
        Args:
            candidate: Any
            model_name: str
            identity_service: IdentityService
        Returns:
            ValidationResult[int]
        Raises:
            BlueprintIdValidatorException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if identity_service is None:
            identity_service = IdentityService()
        
        # --- Process for candidates that are not null. ---#
        if candidate is not None:
            # Handle the case that, the candidate is not a number.
            id_validation = identity_service.validate_id(candidate)
            if id_validator.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    BlueprintIdValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=BlueprintIdValidatorException.MSG,
                        err_code=BlueprintIdValidatorException.ERR_CODE,
                        ex=id_validator.exception,
                    )
                )
            # --- Return the work product. ---#
            return ValidationResult.success(cast(int, candidate))
        
        # --- If the candidate is null the id has to be generated using the model_name. ---#
        
        # Handle the case that, the model_name is not a valid string.
        model_name_validation_result = identity_service.validate_name(model_name)
        if model_name_validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintIdValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BlueprintIdValidatorException.MSG,
                    err_code=BlueprintIdValidatorException.ERR_CODE,
                    ex=model_name_validation_result.exception,
                )
            )
        # --- Return the work product. ---#
        return ValidationResult.success(IdFactory.next_id(class_name=model_name))
        

