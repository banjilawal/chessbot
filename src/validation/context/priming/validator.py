# src/validation/context/priming/validator.py

"""
Module: validation.context.priming.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from model import Context
from result import ValidationResult
from util import LoggingLevelRouter
from validation import Validator, PrimingValidator
from err import (
    ContextNullException, ContextValidationException, ExcessContextFlagsException, ZeroContextFlagsException
)


class ContextValidationPrimer(Validator[Context]):
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
            checks which are common to all Context validation candidates.

    Attributes:

    Provides:
        -   def validate(
                    target_context_model: Context,
                    null_exception: ContextNullException,
                    validator_primer: ValidatorPrimer,
            ) -> ValidationResult[]:

    Super Class:
        ContextValidator
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            context_model: Context,
            context_null_exception: ContextNullException | None = None,
            validation_primer: PrimingValidator | None = None,
    ) -> ValidationResult[Context]:
        """
        Run tests that are common to Context subclasses

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   A validator_primer test fails.
                    -   Exactly one attribute is not enabled.
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            context_model: Context
            context_null_exception: ContextNullException
            validation_primer: Validatorprimer
        Returns:
            ValidationResult[]
        Raises:
            ContextValidationException
            ZeroContextFlagsException
            ExcessContextFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply any missing dependencies. ---#
        if context_null_exception is None:
            context_null_exception = ContextNullException()
        if validation_primer is None:
            validation_primer = PrimingValidator()
        
        # Handle the case that, either the null or type check fails.
        validation_priming_result = validation_primer.validate(
            candidate=candidate,
            target_model=context_model,
            null_exception=context_null_exception,
        )
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ContextValidationException.MSG,
                    err_code=ContextValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        # --- Cast the candidate into the expected Context subclass for additional tests. ---#
        context = cast(context_model, candidate)

        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ContextValidationException.MSG,
                    err_code=ContextValidationException.ERR_CODE,
                    ex=ZeroContextFlagsException(
                        msg=f"{context_model.__class__.__name__} does not have any flags enabled.",
                        err_code=ZeroContextFlagsException.ERR_CODE,
                        var=context_model.__class__.__name__
                    ),
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ContextValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ContextValidationException.MSG,
                    err_code=ContextValidationException.ERR_CODE,
                    ex=ExcessContextFlagsException(
                        msg=f"{context_model.__class__.__name__} has more than one flag enabled.",
                        err_code=ExcessContextFlagsException.ERR_CODE,
                        var=context_model.__class__.__name__
                    ),
                )
            )
        
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(context)
    
