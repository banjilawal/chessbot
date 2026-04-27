# src/operation/vector/product/operation.py

"""
Module: operation.vector.product.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from result import ComputationResult
from system import LoggingLevelRouter
from err import ScalarProductException
from model import Coord, CoordBlueprint, OperandCategory, Vector, VectorBlueprint, VectorOperand, Scalar
from pipeline import CoordBuildPipeline, VectorBuildPipeline

from operation import Operation, ScalarValidator, VectorOperandValidator


class ScalarProductOperation(Operation[VectorOperand]):
    """
    Role:
        -   Operation
        -   Computation

    Responsibilities:
        1.  Multiply a Vector or Coord by a Scalar.

    Attributes:

    Properties:
    
    -   def execute(
            operand: VectorOperand,
            toolkit : VectorOperandToolkit = VectorOperandToolkit(),
            operand_validator: VectorOperandValidator = VectorOperandValidator(),
        ) -> ComputationResult[Any]:

    Super Class:
        Operation
    """
    OPERATION_NAME = "scalar_product"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            scalar: Scalar,
            operand: VectorOperand,
            scalar_validator: ScalarValidator | None = None,
            operand_validator: VectorOperandValidator | None = None,
            vector_build_pipeline: VectorBuildPipeline | None = None,
            coord_build_pipeline: CoordBuildPipeline | None = None,
    ) -> ComputationResult[Vector|Coord]:
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
            operand: VectorOperand
            scalar_validator: ScalarValidator
            operand_validator: VectorOperandValidator
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.execute"
        
        if scalar_validator is None:
            scalar_validator = ScalarValidator()
        if operand_validator is None:
            operand_validator = VectorOperandValidator()
        if vector_build_pipeline is None:
            vector_build_pipeline = VectorBuildPipeline()
        if coord_build_pipeline is None:
            coord_build_pipeline = CoordBuildPipeline()
        
        # Handle the case that, the scalar is not safe.
        scalar_validation = scalar_validator.validate(scalar)
        if scalar_validation.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                ScalarProductException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=scalar_validation.exception
                )
            )
        # Handle the case that, the validator flags the operand.
        operand_validation = operand_validator.validate(operand)
        if operand_validation.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                ScalarProductException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=operand_validation.exception
                )
            )
        build_result = None
        if operand.category == OperandCategory.VECTOR_OPERAND:
            blueprint = VectorBlueprint(
                x=operand.vector.x * scalar.magnitude,
                y=operand.vector.y * scalar.magnitude,
            )
            build_result = vector_build_pipeline.run(blueprint=blueprint,)
        if operand.category == OperandCategory.COORD_OPERAND:
            blueprint = CoordBlueprint(
                row=operand.coord.row * scalar.magnitude,
                column=operand.coord.column * scalar.magnitude,
            )
            build_result = coord_build_pipeline.run(blueprint=blueprint, )
        # Handle the case that, the build did not produce a result.
        if build_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                ScalarProductException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=build_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(build_result.payload)
        