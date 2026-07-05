# src/validation/register/validator.py

"""
Module: validation.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import (
    VectorRegisterMismatchException, VectorRegisterNullException, VectorRegisterValidationException
)
from operation import Validator
from model import VectorOperandRegister
from result import ValidationResult
from util import LoggingLevelRouter
from toolkit import VectorRegisterToolkit


class VectorRegisterValidator(Validator[VectorOperandRegister]):
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
                    toolkit : VectorRegisterToolkit,
            ) -> ValidationResult[VectorRegister]:

    Super Class:
        Validator
    """
    OPERATION_NAME = "vector_register_validator"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: VectorRegisterToolkit | None = None,
    ) -> ValidationResult[VectorOperandRegister]:
        """
        Verify the candidate is a safe VectorRegister.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a VectorRegister.
                    -   The vectorRegister's payload is flagged unsafe.
                    -   There is a mismatch between the contexts.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            toolkit: VectorRegisterToolkit : VectorRegisterValidator
        Returns:
            ValidationResult[VectorRegister]
        Raises:
            VectorRegisterValidationException
        """
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = VectorRegisterToolkit()
        
        # Handle the case that, the candidate does not exist.
        validation_priming_result = toolkit.priming_validator.validate(
            candidate=candidate,
            target_model=VectorOperandRegister,
            context_null_exception=VectorRegisterNullException(),
        )
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorRegisterValidationException.MSG,
                    err_code=VectorRegisterValidationException.ERR_CODE,
                    ex=validation_priming_result.exception,
                )
            )
        # --- Cast candidate to a VectorRegister for additional tests. ---#
        register = cast(VectorOperandRegister, candidate)
        
        # Handle the case that, the validator flags either register
        for item in register.to_list:
            validation = toolkit.vector_operand_validator.validate(item)
            if validation.is_failure:
                # Send the exception chain on failure.
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
        if not isinstance(register.a, type(register.b)):
            return ValidationResult.failure(
                VectorRegisterValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorRegisterValidationException.MSG,
                    err_code=VectorRegisterValidationException.ERR_CODE,
                    ex=VectorRegisterMismatchException(
                        msg=VectorRegisterMismatchException.MSG,
                        err_code=VectorRegisterMismatchException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(register)
            