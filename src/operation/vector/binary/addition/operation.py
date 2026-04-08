# src/operation/vector/addition/worker.py

"""
Module: operation.vector.addition.worker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import VectorAdditionException
from model import VectorContext
from operation import Operation
from result import ComputationResult
from system import LoggingLevelRouter


class AddOperation(Operation[VectorContext]):
    """
    Role:
        -   Worker
        -   Transformer

    Responsibilities:
        1.  Bidirectional Coord<->Vector converter.

    Attributes:

    Properties:
    
    -   def work(
            context: VectorContext,
            toolkit : VectorContextToolkit = VectorContextToolkit(),
            context_validator: VectorContextValidator = VectorContextValidator(),
        ) -> ComputationResult[Any]:

    Super Class:
        Worker
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            a: VectorContext,
            b: VectorContext,
            toolkit : VectorContextToolkit = VectorContextToolkit(),
            context_validator: VectorContextValidator = VectorContextValidator(),
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
            context: VectorContext,
            toolkit : VectorContextToolkit = VectorContextToolkit(),
            context_validator: VectorContextValidator = VectorContextValidator(),
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.work"
        
        # Handle the case that, the validator flags either context
        for context in [a, b]:
            context_validation = context_validator.validate(context)
            if context_validation.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    VectorAdditionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorAdditionException.MSG,
                        err_code=VectorAdditionException.ERR_CODE,
                        ex=context_validation.exception
                    )
            )
        # Handle the case that the contexts are different.
        if not isinstance(a, type(b)):
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorAdditionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorAdditionException.MSG,
                    err_code=VectorAdditionException.ERR_CODE,
                    ex=context_validation.exception
                )
            )
        summation_result = None
        if context.vector is not None:
            summation_result = toolkit.vector_service.builder.build(
                x= a.vector.x + b.vector.x,
                y= a.vector.y + b.vector.y,
            )
        if context.coord is not None:
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
        