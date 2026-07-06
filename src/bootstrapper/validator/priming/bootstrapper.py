# src/validation/priming.py

"""
Module: validation.priming
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, TypeVar, cast

from bootstrapper import ValidatorBootstrapper
from result import ValidationResult
from util import LoggingLevelRouter
from validator import Validator
from err import NullException, PrimingValidatorException


T = TypeVar("T")


class PrimingValidator(ValidatorBootstrapper):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Priming

    Responsibilities:
        1.  Bootstrapping a validator by running existence and type checks.


    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    target_model: T,
                    null_exception: NullException,
            ) -> ValidationResult:

    Super Class:
        Validator
    """

    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            target_model: T,
            null_exception: NullException,
    ) -> ValidationResult[T]:
        """
        Bootstrap a validator by running existence and type checks.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not an instance of target_model
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            target_model: T
            null_exception: NullException
        Returns:
            ValidationResult[T]
        Raises:
            TypeError
            ValidationPrimingException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    var="candidate_expected_type",
                    val=target_model.__name__,
                    msg=PrimingValidatorException.MSG,
                    err_code=PrimingValidatorException.ERR_CODE,
                    ex=null_exception,
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, type(target_model)):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingValidatorException.MSG,
                    err_code=PrimingValidatorException.ERR_CODE,
                    ex=TypeError(
                        f"Expected {type(target_model).__name}, "
                        f"got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to the target_model then forward the work product. ---#
        return ValidationResult.success(cast(target_model, candidate))
    

