# src/validation/register/validator.py

"""
Module: validation.register.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import VectorOperandRegisterValidatorException, VectorOperandRegisterMismatchException
from model import VectorOperandRegister
from result import ValidationResult
from toolkit import VectorOperandRegisterToolkit
from util import LoggingLevelRouter
from validation import Validator


class VectorOperandRegisterValidator(Validator[VectorOperandRegister]):
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
                    toolkit : VectorOperandRegisterToolkit,
            ) -> ValidationResult[VectorRegister]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            toolkit: VectorOperandRegisterToolkit | None = None,
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
            toolkit: VectorOperandRegisterToolkit
        Returns:
            ValidationResult[VectorRegister]
        Raises:
            VectorOperandRegisterValidatorException
            VectorOperandRegisterMismatchException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply missing dependencies. ---#
        if toolkit is None:
            toolkit = VectorOperandRegisterToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.validate(
            candidate=candidate,
            target_model=toolkit.model,
            context_null_exception=toolkit.null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandRegisterValidatorException.MSG,
                    err_code=VectorOperandRegisterValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception,
                )
            )
        # --- Cast candidate to a VectorRegister for additional tests. ---#
        register = cast(toolkit.model, candidate)
        
        # Handle the case that the register has mixed contents.
        if register.is_mismatched_register:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandRegisterValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandRegisterValidatorException.MSG,
                    err_code=VectorOperandRegisterValidatorException.ERR_CODE,
                    ex=VectorOperandRegisterMismatchException(
                        msg=VectorOperandRegisterMismatchException.MSG,
                        err_code=VectorOperandRegisterMismatchException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, either slot is not safe.
        for item in register.to_list:
            validation = toolkit.vector_operand_validator.validate(item)
            if validation.is_failure:
                # Send the exception chain on failure.
                return ValidationResult.failure(
                    VectorOperandRegisterValidatorException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorOperandRegisterValidatorException.MSG,
                        err_code=VectorOperandRegisterValidatorException.ERR_CODE,
                        ex=validation.exception,
                    )
                )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(register)
            