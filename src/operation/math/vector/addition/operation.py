# src/operation/vector/addition/operation.py

"""
Module: operation.vector.addition.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import VectorAdditionException
from model import VectorRegister
from operation import Operation, VectorRegisterValidator
from result import ComputationResult
from system import LoggingLevelRouter


class AddOperation(Operation[VectorRegister]):
    """
    Role:
        -   Operation
        -   Transformer

    Responsibilities:
        1.  Bidirectional Coord<->Vector converter.

    Attributes:

    Properties:
    
    -   def execute(
            register: VectorRegister,
            toolkit : VectorRegisterToolkit = VectorRegisterToolkit(),
            register_validator: VectorRegisterValidator = VectorRegisterValidator(),
        ) -> ComputationResult[Any]:

    Super Class:
        Operation
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            register: VectorRegister,
            toolkit : VectorContextToolkit = None,
            operand_validator: OperandValidator | None = None,
            register_validator: VectorRegisterValidator | None = None,
    ) -> ComputationResult[int]:
        """
        Convert a vector to a coord and vice versa.
        
        Action:
            1.  Send an exception chain in the ComputationResult if any of
                these conditions occur
                    -   The operand is null
                    -   The operand is flagged unsafe.
                    -   Building the other type fails.
            2.  Otherwise, send the success result.
        Args:
            scalar: Scalar,
            register: VectorRegister,
            toolkit : VectorRegisterToolkit = VectorRegisterToolkit(),
            register_validator: VectorRegisterValidator = VectorRegisterValidator(),
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.work"
        
        # Handle the case that, the validator flags either register
        for operand in [register.u, register.v]:
            register_validation = register_validator.validate(register)
            if register_validation.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    VectorAdditionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorAdditionException.MSG,
                        err_code=VectorAdditionException.ERR_CODE,
                        ex=register_validation.exception
                    )
            )
        # Handle the case that the registers are different.
        if not isinstance(a, type(b)):
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorAdditionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=register_validation.exception
                )
            )
        summation_result = None
        if register.vector is not None:
            summation_result = toolkit.vector_service.builder.build(
                x= a.vector.x + b.vector.x,
                y= a.vector.y + b.vector.y,
            )
        if register.coord is not None:
            summation_result = toolkit.coord_service.builder.build(
                row=a.coord.row + b.coord.row,
                column=a.coord.column + b.coord.column,
            )
        # Handle the case that, the multiplication did not produce a result.
        if summation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorAdditionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=summation_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return summation_result
        