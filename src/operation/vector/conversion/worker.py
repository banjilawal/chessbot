# src/worker/lingeo/conversion/worker.py
"""
Module: worker.lingeo.conversion.worker
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any

from err import LinGeoConversionException
from integrity import LinGeoContextValidator
from model import VectorContext
from result import ComputationResult
from system import LoggingLevelRouter
from tool import LinGeoContextToolSet
from worker import Worker


class ConversionWorker(Worker):
    """
    Role:
        -   Worker
        -   Transformer

    Responsibilities:
        1.  Bidirectional Coord<->Vector converter.

    Attributes:

    Properties:
    
    -   def work(
            context: LinGeoContext,
            tool_set: LinGeoContextToolSet = LinGeoContextToolSet(),
            context_validator: LinGeoContextValidator = LinGeoContextValidator(),
        ) -> ComputationResult[Any]:

    Super Class:
        Worker
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            context: VectorContext,
            tool_set: LinGeoContextToolSet = LinGeoContextToolSet(),
            context_validator: LinGeoContextValidator = LinGeoContextValidator(),
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
            tool_set: LinGeoContextToolSet
            context_validator: LinGeoContextValidator
        Result:
            ComputationResult[Union[Vector, Coord]]:
        Raises:
           VectorCoordConversionException
        """
        method = f"{cls.__name__}.work"
        
        # Handle the case that, the validator flags the context.
        context_validation_result = context_validator.validate(context)
        if context_validation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                LinGeoConversionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoConversionException.MSG,
                    err_code=LinGeoConversionException.ERR_CODE,
                    ex=context_validation_result.exception
                )
            )
        
        conversion_result = None
        if context.vector is not None:
            conversion_result = tool_set.coord_service.builder.build(
                row=context.vector.y,
                column=context.vector.x,
            )
        if context.coord is not None:
            conversion_result = tool_set.vector_service.builder.build(
                row=context.vector.y,
                column=context.vector.x,
            )
        # Handle the case that, the conversion did not work.
        if conversion_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                LinGeoConversionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoConversionException.MSG,
                    err_code=LinGeoConversionException.ERR_CODE,
                    ex=conversion_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return conversion_result
        