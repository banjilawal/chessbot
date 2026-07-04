# src/validation/blueprint/priming/validator.py

"""
Module: validation.blueprint.priming.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Blueprint
from result import ValidationResult
from util import LoggingLevelRouter
from validation import Validator, PrimingValidator
from err import (
    BlueprintNullException, BlueprintValidationException, ExcessBlueprintFlagsException, ZeroBlueprintFlagsException
)


class BlueprintValidationPrimer(Validator[Blueprint]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Run checks for
                -   existence
                -   type
                -   Flag count
            checks which are common to all Blueprint validation candidates.

    Attributes:

    Provides:
        -   def validate(
                    target_blueprint_model: Blueprint,
                    null_exception: BlueprintNullException,
                    validator_primer: ValidatorPrimer,
            ) -> ValidationResult[]:

    Super Class:
        BlueprintValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            blueprint_model: Blueprint,
            blueprint_null_exception: BlueprintNullException | None = None,
            priming_validator: PrimingValidator | None = None,
    ) -> ValidationResult[Blueprint]:
        """
        Run tests that are common to Blueprint subclasses

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   A validator_primer test fails.
                    -   Exactly one attribute is not enabled.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            blueprint_model: Blueprint
            blueprint_null_exception: BlueprintNullException
            priming_validator: Validatorprimer
        Returns:
            ValidationResult[]
        Raises:
            BlueprintValidationException
            ZeroBlueprintFlagsException
            ExcessBlueprintFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if blueprint_null_exception is None:
            blueprint_null_exception = BlueprintNullException()
        if priming_validator is None:
            priming_validator = PrimingValidator()
        
        # Handle the case that, either the null or type check fails.
        validation_priming_result = priming_validator.validate(
            candidate=candidate,
            target_model=blueprint_model,
            null_exception=blueprint_null_exception,
        )
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BlueprintValidationException.MSG,
                    err_code=BlueprintValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        # --- Cast the candidate into the expected Blueprint subclass for additional tests. ---#
        blueprint = cast(blueprint_model, candidate)

        # Handle the case of searching with no attribute-value provided.
        flag_count = len(blueprint.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BlueprintValidationException.MSG,
                    err_code=BlueprintValidationException.ERR_CODE,
                    ex=ZeroBlueprintFlagsException(
                        msg=f"{blueprint_model.__class__.__name__} does not have any flags enabled.",
                        err_code=ZeroBlueprintFlagsException.ERR_CODE,
                        var=blueprint_model.__class__.__name__
                    ),
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BlueprintValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=BlueprintValidationException.MSG,
                    err_code=BlueprintValidationException.ERR_CODE,
                    ex=ExcessBlueprintFlagsException(
                        msg=f"{blueprint_model.__class__.__name__} has more than one flag enabled.",
                        err_code=ExcessBlueprintFlagsException.ERR_CODE,
                        var=blueprint_model.__class__.__name__
                    ),
                )
            )
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(blueprint)
    
