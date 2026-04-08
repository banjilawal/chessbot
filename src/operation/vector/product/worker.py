# src/operation/vector/product/worker.py

"""
Module: operation.vector.product.worker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import ScalarProductException
from integrity import VectorContextValidator
from model import VectorContext, Scalar
from result import ComputationResult
from system import LoggingLevelRouter
from toolkit  import VectorContextToolkit
from worker import Worker


class ScalarProductWorker(Worker):
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
            scalar: Scalar,
            context: VectorContext,
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
        
        # Handle the case that, the scalar is not safe.
        scalar_validation = toolkit.scalar_service.validator.validate(scalar)
        if scalar_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                ScalarProductException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=scalar_validation.exception
                )
            )
        
        # Handle the case that, the validator flags the context.
        context_validation = context_validator.validate(context)
        if context_validation.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                ScalarProductException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=context_validation.exception
                )
            )
        
        multiplication_result = None
        if context.vector is not None:
            multiplication_result = toolkit.vector_service.builder.build(
                x=context.vector.x * scalar.value,
                y=context.vector.y * scalar.value,
            )
        if context.coord is not None:
            multiplication_result = toolkit.coord_service.builder.build(
                row=context.vector.y,
                column=context.vector.x,
            )
        # Handle the case that, the multiplication did not produce a result.
        if multiplication_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                ScalarProductException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=ScalarProductException.MSG,
                    err_code=ScalarProductException.ERR_CODE,
                    ex=multiplication_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return multiplication_result
        