# src/logic/vector/validator.py

"""
Module: logic.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Union

from logic.coord import Coord, CoordService

from integrity import LinGeoContextValidator
from model import LinGeoContext
from tool import LinGeoContextToolSet
from worker.worker import Worker
from model.geometry.vector import Vector, VectorService
from system import (
    ComputationResult, LoggingLevelRouter, NumberValidator
)
from model.geometry.vector import (
    VectorCoordConversionException,
    VectorCoordConversionOperandNullException
)


class LinGeoConverter(Worker):
    """
    Role:
        -   Worker
        -   Transformer

    Responsibilities:
        1.  Bidirectional Coord<->Vector converter.

    Attributes:

    Properties:
    
    -   def work(
                operand: AlgebraContext,
                coord_service: CoordService,
                vector_service: VectorService,
                number_validator: NumberValidator,
        ) -> ComputationResult[Union[Vector, Coord]]:
    
    -   def _conversion_helper(
                operand: AlgebraContext,
                coord_service: CoordService,
                vector_service: VectorService,
                number_validator: NumberValidator,
        ) -> ComputationResult[Union[Vector, Coord]]:
    
    -   def _vector_to_coord(
                vector: Vector,
                coord_service: CoordService,
                vector_service: VectorService,
                number_validator: NumberValidator,
        ) -> ComputationResult[Coord]:
 
    -   def _coord_to_vector(
            coord: Coord,
            coord_service: CoordService,
            vector_service: VectorService,
            number_validator: NumberValidator,
        ) -> ComputationResult[Vector]:

    Super Class:
        Worker
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            context: LinGeoContext,
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
            return ComputationResult(
                LinGeoConversionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoConversionException.MSG,
                    err_code=LinGeoConversionException.ERR_CODE,
                    ex=context_validation_result.exception.
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
            return ComputationResult(
                LinGeoConversionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoConversionException.MSG,
                    err_code=LinGeoConversionException.ERR_CODE,
                    ex=conversion_result.exception.
                )
            )
        