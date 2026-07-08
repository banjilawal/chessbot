# src/validator/operand/validator.py

"""
Module: validator.operand.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import ExcessVectorOperandFlagsException, VectorOperandValidatorException, ZeroVectorOperandFlagsException
from model import VectorOperand
from result import ValidationResult
from toolkit import VectorOperandToolkit
from util import LoggingLevelRouter
from validator import ModelValidator


class VectorOperandValidator(ModelValidator[VectorOperand]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a VectorOperand instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : VectorOperandToolkit,
            ) -> ValidationResult[VectorOperand]:

    Super Class:
        Validator
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            candidate: Any,
            toolkit: VectorOperandToolkit | None = None,
    ) -> ValidationResult[VectorOperand]:
        """
        Verify the candidate is a safe VectorOperand.
        
        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a VectorOperand.
                    -   The vectorOperand's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            toolkit : VectorOperandToolkit
        Returns:
            ValidationResult[VectorOperand]
        Raises:
            TypeError
            VectorOperandNullException
            ZeroVectorOperandFlagsException
            VectorOperandValidatorException
            ExcessVectorOperandFlagsException
        """
        method = f"{cls.__name__}.validate"
        
        # --- Supply missing dependencies. ---#
        if toolkit is None:
            toolkit = VectorOperandToolkit()
        
        # Handle the case that, the validator is not primed.
        validator_priming_result = toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=toolkit.model,
            context_null_exception=toolkit.null_exception,
        )
        if validator_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidatorException.MSG,
                    err_code=VectorOperandValidatorException.ERR_CODE,
                    ex=validator_priming_result.exception
                )
            )
        # --- Cast candidate to a VectorOperand for additional tests. ---#
        operand = cast(toolkit.model, candidate)
        
        # Handle the case that neither option is enabled.
        if len(operand.to_dict) == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidatorException.MSG,
                    err_code=VectorOperandValidatorException.ERR_CODE,
                    ex=ZeroVectorOperandFlagsException(
                        msg=ZeroVectorOperandFlagsException.MSG,
                        err_code=ZeroVectorOperandFlagsException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if len(operand.to_dict) > 1:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidatorException.MSG,
                    err_code=VectorOperandValidatorException.ERR_CODE,
                    ex=ExcessVectorOperandFlagsException(
                        msg=ExcessVectorOperandFlagsException.MSG,
                        err_code=ExcessVectorOperandFlagsException.ERR_CODE,
                    )
                )
            )
        """
           Route to the appropriate validator and get its result so only have
           one failure block.
        """
        # ---  ---#
        validation_result = None
        if operand.is_vector:
            validation_result = toolkit.vector.validator.execute(operand.vector)
        if operand.is_coord:
            validation_result = toolkit.coord.validator.execute(operand.coord)
            
        # Handle the case that context was flagged.
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidatorException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidatorException.MSG,
                    err_code=VectorOperandValidatorException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(operand)

            