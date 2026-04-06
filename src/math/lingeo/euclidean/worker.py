# src/logic/vector/validator.py

"""
Module: logic.vector.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from math import sqrt

from err import LinGeoEuclideanException
from integrity import LinGeoContextValidator
from model import LinGeoContext, Scalar
from result import ComputationResult
from system import LoggingLevelRouter
from tool import LinGeoContextToolSet
from worker import Worker


class LinGeoEuclidean(Worker):
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
            u: LinGeoContext,
            v: LinGeoContext,
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
        for context in [u, v]:
            context_validation = context_validator.validate(context)
            if context_validation.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    LinGeoEuclideanException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=LinGeoEuclideanException.MSG,
                        err_code=LinGeoEuclideanException.ERR_CODE,
                        ex=context_validation.exception
                    )
            )
        # Handle the case that the contexts are different.
        if not isinstance(u, type(v)):
            # Return the exception chain on failure.
            return ComputationResult.failure(
                LinGeoEuclideanException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=LinGeoEuclideanException.MSG,
                    err_code=LinGeoEuclideanException.ERR_CODE,
                    ex=context_validation.exception
                )
            )
        distance = None
        if context.vector is not None:
            distance = sqrt(
                (u.vector.y - v.vector.y)**2 + (u.vector.x - v.vector.x)**2
            )
        if context.coord is not None:
            distance = sqrt(
                (u.coord.row - v.coord.row)**2 + (u.coord.column - v.coord.column)**2
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(distance)
        