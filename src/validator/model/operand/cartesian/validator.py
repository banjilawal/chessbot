# src/validator/operand/validator.py

"""
Module: validator.operand.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, cast

from err import ExcessTogglesException, NoActiveTogglesException, NodeValidationRouteException, NullException
from operand import CartesianOperand
from result import ValidationResult
from toolkit import CartesianOperandToolkit
from util import LoggingLevelRouter
from validator import OperandValidator


class CartesianOperandValidator(OperandValidator[CartesianOperand]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Validation Process Owner

    Responsibilities:
        1.  Ensure a CartesianOperand instance is certified safe, reliable and consistent
            before use.

    Attributes:

    Properties:
        -   def validate(
                    candidate: Any,
                    toolkit : CartesianOperandToolkit,
            ) -> ValidationResult[CartesianOperand]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: CartesianOperandToolkit = CartesianOperandToolkit(),
    ):
        super().__init__(toolkit=toolkit)
        
    @property
    def toolkit(self) -> CartesianOperandToolkit:
        return cast(CartesianOperandToolkit, self.toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult:
        """
        Verify the candidate is a safe CartesianOperand.

        Action:
            1.  Send an exception in the ValidationResult any of these
                conditions occur.
                    -   candidate is null.
                    -   It's not a CartesianOperand.
                    -   The cartesianOperand's payload is flagged unsafe.
            3.  Otherwise, Send the success result.
        Args:
            candidate: Any
            toolkit : CartesianOperandToolkit
        Returns:
            ValidationResult[CartesianOperand]
        Raises:
            TypeError
            CartesianOperandNullException
            ZeroCartesianOperandFlagsException
            CartesianOperandValidationException
            ExcessCartesianOperandFlagsException
        """
        method = f"{self.__class__.__name__}.validate"
        
        bootstrap = self.toggle_validator.execute(
            candidate=candidate,
            toggle_model=self.toolkit.model,
            null_exception=NullException(),
        )
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianOperandValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianOperandValidationException.MSG,
                    err_code=CartesianOperandValidationException.ERR_CODE,
                    ex=bootstrap.exception
                )
            )
        # --- Cast candidate to a CartesianOperand for additional tests. ---#
        operand = cast(self.toolkit.model, candidate)
        
        # Handle the case that neither option is enabled.
        if operand.no_active_toggles:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianOperandValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianOperandValidationException.MSG,
                    err_code=CartesianOperandValidationException.ERR_CODE,
                    ex=NoActiveTogglesException(
                        msg=NoActiveTogglesException.MSG,
                        err_code=NoActiveTogglesException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, both options are enabled.
        if operand.excess_toggles:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianOperandValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianOperandValidationException.MSG,
                    err_code=CartesianOperandValidationException.ERR_CODE,
                    ex=ExcessTogglesException(
                        msg=ExcessTogglesException.MSG,
                        err_code=ExcessTogglesException.ERR_CODE,
                    )
                )
            )
        # Pick a route for integrity testing the operand's entity.
        validation_result = ValidationResult.failure(NodeValidationRouteException())
        if operand.is_coord_point:
            validation_result = self.toolkit.coord.validator.execute(operand.entity)
        if operand.is_vector_point:
            validation_result = self.toolkit.vector.validator.execute(operand.entity)
   
        # Handle the case that, the entity is not safe to use.
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianOperandValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianOperandValidationException.MSG,
                    err_code=CartesianOperandValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        return ValidationResult.success(operand)

        """
           Route to the appropriate validator and get its result so only have
           one failure block.
        """
        # ---  ---#
        validation_result = None
        if operand.is_vector_point:
            validation_result = toolkit.vector.validator.execute(operand.vector)
        if operand.is_coord_point:
            validation_result = toolkit.coord.validator.execute(operand.coord)
        
        # Handle the case that context was flagged.
        if validation_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CartesianOperandValidationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CartesianOperandValidationException.MSG,
                    err_code=CartesianOperandValidationException.ERR_CODE,
                    ex=validation_result.exception
                )
            )
        # --- Forward the work product to the caller ---#
        return ValidationResult.success(operand)