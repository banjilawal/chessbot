# src/operation/vector/euclidean/operation.py

"""
Module: operation.vector.euclidean.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from math import sqrt

from err import VectorRegisterMismatchException
from integrity import VectorContextValidator
from model import VectorContext
from result import ComputationResult
from system import LoggingLevelRouter
from toolkit  import VectorContextToolkit
from operation import Operation


class EuclideanOperation(Operation):
    """
    Role:
        -   Operation
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
        Operation
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def work(
            cls,
            u: VectorContext,
            v: VectorContext,
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
        for context in [u, v]:
            context_validation = context_validator.validate(context)
            if context_validation.is_failure:
                # Return the exception chain on failure.
                return ComputationResult.failure(
                    VectorEuclideanException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=VectorEuclideanException.MSG,
                        err_code=VectorEuclideanException.ERR_CODE,
                        ex=context_validation.exception
                    )
            )
        # Handle the case that the contexts are different.
        if not isinstance(u, type(v)):
            # Return the exception chain on failure.
            return ComputationResult.failure(
                VectorEuclideanException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=VectorEuclideanException.MSG,
                    err_code=VectorEuclideanException.ERR_CODE,
                    ex=VectorRegisterMismatchException(
                        msg=VectorEuclideanException.MSG,
                        err_code=VectorEuclideanException.ERR_CODE,
                    )
                )
            )
        # --- The euclidean distance is an int.  ---#
        distance = None
        
        # For vector contexts
        if context.vector is not None:
            distance = sqrt(
                (u.vector.y - v.vector.y)**2 + (u.vector.x - v.vector.x)**2
            )
        # For Coord contexts
        if context.coord is not None:
            distance = sqrt(
                (u.coord.row - v.coord.row)**2 + (u.coord.column - v.coord.column)**2
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(distance)
        