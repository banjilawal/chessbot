# src/validation/operand/validator.py

"""
Module: validation.operand.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from operation import Validator
from result import ValidationResult
from util import LoggingLevelRouter
from model import Coord, Vector, VectorOperand
from toolkit.context import VectorOperandToolkit
from err import (
    ExcessVectorOperandFlagsException, VectorOperandNullException, VectorOperandValidationException,
    ZeroVectorOperandFlagsException
)


class VectorOperandValidator(Validator[VectorOperand]):
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
    def validate(
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
            VectorOperandValidationException
            ExcessVectorOperandFlagsException
        """
        OPERATION_NAME = "operand_validator"
        
        method = f"{cls.__name__}.validate"
        
        if toolkit is None:
            toolkit = VectorOperandToolkit()
        
        # Handle the case that, the candidate does not exist or, is the wrong type.
        validation_priming_result = toolkit.validation_primer.build(
            candidate=candidate,
            target_model=VectorOperand,
            context_null_exception=VectorOperandNullException(),
        )
        if validation_priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidationException.MSG,
                    err_code=VectorOperandValidationException.ERR_CODE,
                    ex=validation_priming_result.exception
                )
            )
        # --- Cast candidate to a VectorOperand for additional tests. ---#
        operand = cast(VectorOperand, candidate)
        
        # Handle the case that neither option is enabled.
        if len(operand.to_dict) == 0:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidationException.MSG,
                    err_code=VectorOperandValidationException.ERR_CODE,
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
                VectorOperandValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidationException.MSG,
                    err_code=VectorOperandValidationException.ERR_CODE,
                    ex=ExcessVectorOperandFlagsException(
                        msg=ExcessVectorOperandFlagsException.MSG,
                        err_code=ExcessVectorOperandFlagsException.ERR_CODE,
                    )
                )
            )
        # --- Assign to the correct service for the final step. ---#
        validation_result = None
        if isinstance(operand.vector, Vector):
            validation_result = toolkit.vector_service.validator.build(operand.vector)
        if isinstance(operand.coord, Coord):
            validation_result = toolkit.coord_service.validator.build(operand.to_dict)
            
        # Handle the case that context was flagged.
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorOperandValidationException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorOperandValidationException.MSG,
                    err_code=VectorOperandValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(operand)

            