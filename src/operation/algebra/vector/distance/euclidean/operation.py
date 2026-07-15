# src/operation/math/vector/distance/euclidean/operation.py

"""
Module: operation.math.vector.distance.euclidean.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from math import sqrt
from typing import Optional, cast

from controller import WorkerRegistryController
from pipeline import ScalarBuilder
from result import ComputationResult
from util import LoggingLevelRouter
from err import VectorEuclideanException
from operation import Operation, VectorRegisterValidator
from model import RegisterContentType, Scalar, ScalarBlueprint, PointRegister


class EuclideanDistance(Operation[PointRegister]):
    """
    Role:
        -   Operation
        -   Computation

    Responsibilities:
        1.  Compute the Euclidean distance between the register's contents.

    Attributes:

    Properties:
        -   def execute(
                register: VectorRegister,
                register_validator: VectorRegisterValidator | None = None,
                scalar_assembler: ScalarBuilder | None = None,
            ) -> ComputationResult[Scalar]:

    Super Class:
        Operation
    """
    NAME = "euclidean_distance"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            register: PointRegister,
            register_validator: Optional[VectorRegisterValidator] | None = None,
            scalar_build_pipeline: Optional[ScalarBuilder] | None = None,
    ) -> ComputationResult[Scalar]:
        """
        Compute the Euclidean distance between the register's contents.
        
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
            scalar_build_pipeline: ScalarBuilder
        Result:
            ComputationResult[Scalar]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.execute"
        
        if register_validator is None:
            register_validator = VectorRegisterValidator()
            
        if scalar_build_pipeline is None:
            scalar_build_pipeline = ScalarBuilder()
        
        # Handle the case that, the register is flagged.
        register_validation_result = register_validator.execute(register)
        if register_validation_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                VectorEuclideanException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorEuclideanException.MSG,
                    err_code=VectorEuclideanException.ERR_CODE,
                    ex=register_validation_result.exception
                )
            )
        # --- The Euclidean distance is an int.  ---#
        magnitude = None
        
        # For vector contexts
        if register.category == RegisterContentType.VECTOR_REGISTER:
            magnitude=sqrt(
                (register.origin.vector.y - register.b.vector.y) ** 2 +
                (register.origin.vector.x - register.b.vector.x) ** 2
                )
        # For Coord contexts
        if register.category == RegisterContentType.VECTOR_REGISTER:
            magnitude = sqrt(
                (register.origin.coord.row - register.b.coord.row) ** 2 +
                (register.origin.coord.column - register.b.coord.column) ** 2
            )
        # Handle the case that, the scalar is not built.
        scalar_assembly_result = scalar_build_pipeline.run(
            blueprint=ScalarBlueprint(
                magnitude=cast(int, magnitude)
            )
        )
        if scalar_assembly_result.is_failure:
            # Send the exception chain on failure.
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
        return ComputationResult.success(cast(Scalar, scalar_assembly_result.payload))