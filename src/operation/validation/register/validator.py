# src/operation/validation/context/vector/validator.py

"""
Module: operation.validation.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import (
    VectorEuclideanException, VectorRegisterMismatchException, VectorRegisterNullException,
    VectorRegisterValidationException
)
from operation import Validator, VectorContextValidator
from model import VectorRegister
from result import ValidationResult
from system import LoggingLevelRouter
from toolkit  import VectorContextToolkit



class VectorRegisterValidator(Validator[VectorRegister]):
    """
    Role
        -   Transaction Worker
        -   Operation Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a VectorRegister instance is certified safe, reliable and consistent
            before use in a binary arithmetic operation.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : VectorContextToolSe,
            ) -> ValidationResult[VectorContext]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            context_validator: VectorContextValidator = None,
    ) -> ValidationResult[VectorRegister]:
        """
        Verify the candidate is a safe VectorRegister.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a VectorContext.
                    -   The vectorContext's payload is flagged unsafe.
                    -   There is a mismatch between the contexts.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            context_validator : VectorContextValidator
        Returns:
            ValidationResult[VectorContextRegister]
        Raises:
            TypeError
            VectorRegisterNullException
            VectorRegisterValidationException
        """
        method = f"{cls.__name__}.validate"
            
        if context_validator is None:
            context_validator = VectorContextValidator()
        
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorRegisterValidationException.MSG,
                    err_code=VectorRegisterValidationException.ERR_CODE,
                    ex=VectorRegisterNullException(
                        msg=VectorRegisterNullException.MSG,
                        err_code=VectorRegisterNullException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the candidate is wrong type.
        if not isinstance(candidate, VectorRegister):
            # Return the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorRegisterValidationException.MSG,
                    err_code=VectorRegisterValidationException.ERR_CODE,
                    ex=TypeError(
                        f"Expected Vector type, got ({candidate}.__name__) instead."
                    )
                )
            )
        # --- Cast candidate to a VectorRegist for additional tests. ---#
        register = cast(VectorRegister, candidate)
        
        # Handle the case that, the validator flags either register
        for item in register.to_list:
            validation = context_validator.validate(item)
            if validation.is_failure:
                # Return the exception chain on failure.
                return ValidationResult.failure(
                    VectorRegisterValidationException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorRegisterValidationException.MSG,
                        err_code=VectorRegisterValidationException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
        # Handle the case that the contexts are different.
        if not isinstance(register.u, type(register.v)):
            return ValidationResult.failure(
                VectorRegisterValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorRegisterValidationException.MSG,
                    err_code=VectorRegisterValidationException.ERR_CODE,
                    ex=VectorRegisterMismatchException(
                        msg=VectorEuclideanException.MSG,
                        err_code=VectorEuclideanException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(register)
            