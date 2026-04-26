# src/operation/vector/euclidean/operation.py

"""
Module: operation.vector.euclidean.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from math import sqrt
from typing import cast

from result import ComputationResult
from system import LoggingLevelRouter
from err import VectorEuclideanException
from operation import Operation, VectorRegisterValidator
from model import RegisterCategory, Scalar, ScalarBlueprint, VectorRegister


class EuclideanOperation(Operation):
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
                register_validator: VectorRegisterValidator | None = None,
                scalar_assembler: ScalarAssembler | None = None,
            ) -> ComputationResult[Scalar]:

    Super Class:
        Operation
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            register: VectorRegister,
            register_validator: VectorRegisterValidator | None = None,
            scalar_assembler: ScalarAssembler | None = None,
    ) -> ComputationResult[Scalar]:
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
            register: VectorRegister
            register_validator: VectorRegisterValidator
            operand_toolkit: VectorOperandToolkit
            scalar_assembler: ScalarAssembler
        Result:
            ComputationResult[Scalar]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.execute"
        
        if register_validator is None:
            register_validator = VectorRegisterValidator()
            
        if scalar_assembler is None:
            scalar_assembler = ScalarAssembler()
        
        # Handle the case that, the register is flagged.
        register_validation_result = register_validator.validate(register)
        if register_validation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorEuclideanException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorEuclideanException.MSG,
                    err_code=VectorEuclideanException.ERR_CODE,
                    ex=register_validation_result.exception
                )
            )
        # --- The euclidean distance is an int.  ---#
        magnitude = None
        
        # For vector contexts
        if register.category == RegisterCategory.VECTOR_REGISTER:
            magnitude=sqrt(
                    (register.a.vector.y - register.b.vector.y)**2 +
                    (register.a.vector.x - register.b.vector.x)**2
                )
        # For Coord contexts
        if register.category == RegisterCategory.VECTOR_REGISTER:
            magnitude = sqrt(
                (register.a.coord.row - register.b.coord.row) ** 2 +
                (register.a.coord.column - register.b.coord.column) ** 2
            )
        # Handle the case that, the scalar is not built.
        scalar_assembly_result = scalar_assembler.execute(
            blueprint=ScalarBlueprint(
                magnitude=cast(int, magnitude)
            )
        )
        if scalar_assembly_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorEuclideanException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorEuclideanException.MSG,
                    err_code=VectorEuclideanException.ERR_CODE,
                    ex=scalar_assembly_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(scalar_assembly_result.payload)
        