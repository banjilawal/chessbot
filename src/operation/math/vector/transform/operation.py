# src/operation/math/vector/conversion/operation.py
"""
Module: operation.math.vector.conversion.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any

from controller import WorkerRegistryController
from operation import Operation


class VectorTransform(Operation):
    """
    Role:
        -   Operation
        -   Transformer

    Responsibilities:
        1.  Bidirectional Coord<->Vector converter.

    Attributes:

    Properties:
    
    -   def execute(
            context: VectorContext,
            toolkit : VectorContextToolkit = VectorContextToolkit(),
            context_validator: VectorContextValidator = VectorContextValidator(),
        ) -> ComputationResult[Any]:

    Super Class:
        Operation
    """
    NAME = "vector_transform"
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            context: VectorContext,
            toolkit : VectorContextToolkit = VectorContextToolkit(),
            context_validator: VectorContextValidator = VectorContextValidator(),
    ) -> ComputationResult[Any]:
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
            context: AlgebraContext
            toolkit : VectorContextToolkit
            context_validator: VectorContextValidator
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.work"
        
        # Handle the case that, the validator flags the context.
        context_validation_result = context_validator.validate(context)
        if context_validation_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                VectorConversionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorConversionException.MSG,
                    err_code=VectorConversionException.ERR_CODE,
                    ex=context_validation_result.exception
                )
            )
        
        conversion_result = None
        if context.vector is not None:
            conversion_result = toolkit.coord_service.builder.build(
                row=context.vector.y,
                column=context.vector.x,
            )
        if context.coord is not None:
            conversion_result = toolkit.vector_service.builder.build(
                row=context.vector.y,
                column=context.vector.x,
            )
        # Handle the case that, the conversion did not work.
        if conversion_result.is_failure:
            # Send the exception chain on failure.
            return ComputationResult.failure(
                VectorConversionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorConversionException.MSG,
                    err_code=VectorConversionException.ERR_CODE,
                    ex=conversion_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return conversion_result


# Register the operation.
WorkerRegistryController.register_worker(worker=VectorTransform)
        