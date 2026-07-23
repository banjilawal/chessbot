# src/validator/priming/validator.py

"""
Module: validator.priming.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Type, TypeVar, cast

from result import ValidationResult
from util import LoggingLevelRouter
from err import NullException, PrimingException


T = TypeVar("T")


class PrimingValidator:
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Priming

    Responsibilities:
        1.  Bootstrapping a priming by running existence and type checks.


    Attributes:

    Provides:
        -   validate(
                    candidate: Any,
                    target_model: Type[T],
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
            target_model: Type[T],
            null_exception: NullException,
    ) -> ValidationResult:
        """
        Makes sure a candidate is the expected type and not null.

        Action:
            1.  Send an exception chain in the ValidationResult any of the cases occur:
                    -   Candidate is null
                    -   It's not an instance of target_model
            2.  Otherwise, send the success result.
        Args:
            candidate: Any
            target_model: Type[T]
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
                PrimingException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    var="candidate_expected_type",
                    val=target_model.__name__,
                    msg=PrimingException.MSG,
                    err_code=PrimingException.ERR_CODE,
                    ex=null_exception,
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, target_model):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PrimingException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=PrimingException.MSG,
                    err_code=PrimingException.ERR_CODE,
                    ex=TypeError(
                        f"Expected {type(target_model).__name}, "
                        f"got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the candidate to the target_model then forward the work product. ---#
        return ValidationResult.success(cast(T, candidate))
    

