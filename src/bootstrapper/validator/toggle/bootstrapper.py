# src/bootstrapper/validator/toggle/bootstrapper.py

"""
Module: bootstrapper.validator.toggle.bootstrapper
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Type, cast
from typing_extensions import TypeVar

from bootstrapper import PrimingValidator
from err import NullException, PrimingContextValidatorException
from result import ValidationResult
from util import LoggingLevelRouter

T = TypeVar("T", bound="Context")


class ToggleValidator:
    """
    Role
        -   Transaction Worker
        -   Toggle Maintenance
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
                    model: Context,
                    exception: ContextNullException,
                    validator_primer: ValidatorPrimer,
            ) -> ValidationResult:

    Super Class:
    """
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            priming_validator: PrimingValidator = PrimingValidator(),
    ):
        """
        Args:
            priming_validator: PrimingValidator
        """
        self._priming_validator = priming_validator
        
        
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            target_model: Type[T],
            null_exception: NullException,
            max_flags: int | None = 1,
    ) -> ValidationResult:
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
            max_flags: int
            context_model: Context
            null_exception: ContextNullException
            priming_validator: PrimingValidator
        Returns:
            ValidationResult
        Raises:
            PrimingContextValidatorException
            ZeroContextFlagsException
            ExcessContextFlagsException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        # Handle the case that, the validator is not primed.
        priming = self._priming_validator.execute(
            candidate=candidate,
            target_model=target_model,
            null_exception=null_exception,
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PrimingContextValidatorException.MSG,
                    err_code=PrimingContextValidatorException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the candidate into the expected Context subclass for additional tests. ---#
        context = cast(context_model, candidate)

        # Handle the case of searching with no attribute-value provided.
        flag_count = len(context.to_dict())
        if flag_count == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PrimingContextValidatorException.MSG,
                    err_code=PrimingContextValidatorException.ERR_CODE,
                    ex=ZeroContextFlagsException(
                        msg=f"{context_model.__class__.__name__} does not have any flags enabled.",
                        err_code=ZeroContextFlagsException.ERR_CODE,
                        var=context_model.__class__.__name__
                    ),
                )
            )
        # Handle the case of too many attributes being used in a search.
        if flag_count > max_flags:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingContextValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PrimingContextValidatorException.MSG,
                    err_code=PrimingContextValidatorException.ERR_CODE,
                    ex=ExcessContextFlagsException(
                        msg=f"{context_model.__class__.__name__} has more than one flag enabled.",
                        err_code=ExcessContextFlagsException.ERR_CODE,
                        var=context_model.__class__.__name__
                    ),
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(context)
    
