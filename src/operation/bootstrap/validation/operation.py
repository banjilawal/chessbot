# src/operation/bootstrap/validation/operation.py

"""
Module: operation.boostrap.validation.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, TypeVar, cast

from err import NullException, ValidationBootstrapException
from operation import Validator
from result import ValidationResult
from system import LoggingLevelRouter

T = TypeVar("T")


class ValidationBootstrapper(Validator[T]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Process Runner

    Responsibilities:
        1.  Run null and type checks which start all validation operations.

    Attributes:

    Provides:
        -   def validate(
                    candidate: Any,
                    target_model: T,
                    null_exception: NullException,
            ) -> ValidationResult[T]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            target_model: T,
            null_exception: NullException,
    ) -> ValidationResult[T]:
        """
        Verify that the target_model's safety checks can be run on an object. .

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
            ValidationBootstrapException
        """
        method = f"{cls.__class__.__name__}.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidationBootstrapException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    var="candidate_expected_type",
                    val=target_model.__name__,
                    msg=ValidationBootstrapException.MSG,
                    err_code=ValidationBootstrapException.ERR_CODE,
                    ex=null_exception,
                )
            )
        # Handle the wrong class case.
        if not isinstance(candidate, type(target_model)):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                ValidationBootstrapException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ValidationBootstrapException.MSG,
                    err_code=ValidationBootstrapException.ERR_CODE,
                    ex=TypeError(
                        f"Expected {type(target_model).__name}, "
                        f"got {type(candidate).__name__} instead."
                    )
                )
            )
        # --- Cast the rank to a Token for additional tests ---#
        return ValidationResult.success(cast(target_model, candidate))
    

