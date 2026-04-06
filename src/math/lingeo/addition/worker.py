# src/logic/vector/validator.py

"""
Module: logic.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from err import LinGeoAdditionException
from integrity import LinGeoContextValidator
from model import LinGeoContext, Scalar
from result import ComputationResult
from system import LoggingLevelRouter
from tool import LinGeoContextToolSet
from worker import Worker


class LinGeoAddition(Worker):
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
            a: LinGeoContext,
            b: LinGeoContext,
            tool_set: LinGeoContextToolSet = LinGeoContextToolSet(),
            context_validator: LinGeoContextValidator = LinGeoContextValidator(),
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
            context: LinGeoContext,
            tool_set: LinGeoContextToolSet = LinGeoContextToolSet(),
            context_validator: LinGeoContextValidator = LinGeoContextValidator(),
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
                    LinGeoAdditionException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=LinGeoAdditionException.MSG,
                        err_code=LinGeoAdditionException.ERR_CODE,
                        ex=context_validation.exception
                    )
            )
        # Handle the case that the contexts are different.
        if not isinstance(a, type(b)):
            # Return the exception chain on failure.
            return ComputationResult.failure(
                LinGeoAdditionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoAdditionException.MSG,
                    err_code=LinGeoAdditionException.ERR_CODE,
                    ex=context_validation.exception
                )
            )
        summation_result = None
        if context.vector is not None:
            summation_result = tool_set.vector_service.builder.build(
                x= a.vector.x + b.vector.x,
                y= a.vector.y + b.vector.y,
            )
        if context.coord is not None:
            summation_result = tool_set.coord_service.builder.build(
                row=a.coord.row + b.coord.row,
                column=a.coord.column + b.coord.column,
            )
        # Handle the case that, the multiplication did not produce a result.
        if summation_result.is_failure:
            # Return the exception chain on failure.
            return ComputationResult.failure(
                LinGeoAdditionException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoAdditionException.MSG,
                    err_code=LinGeoAdditionException.ERR_CODE,
                    ex=summation_result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return summation_result
        