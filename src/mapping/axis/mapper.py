# src/mapping/axis/mapping.py

"""
Module: mapping.axis.mapping
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar, cast

from err import AxisMappingException
from model import Vector
from result import ComputationResult, MethodResultType
from mapping import SpaceMappingFunction
from util import LoggingLevelRouter

T = TypeVar("T", bound="AxialSpace")

class AxialMapFunction(SpaceMappingFunction, Generic[T]):
    """
    Role:
        -   Computation

    Responsibilities:
        1.  Get the next vector, V, after U in Axial Space, by addition of a delta_vector
                -   V.x = U.x + delta.x
                -   V.y = U.x + delta.y

    Attributes:
        delta: Vector

    Provides:
        def next(self, vector: Vector) -> ComputationResult[Vector]

    Super Class:
        SpaceMappingFunction
    """
    _delta: Vector
    
    def __init__(self, delta: Vector,):
        """
        Args:
            delta: Vector
        """
        super().__init__()
        self._delta = delta
        
    @property
    def delta(self) -> Vector:
        return self._delta
    
    @LoggingLevelRouter.monitor
    def next(self, vector: Vector) -> ComputationResult[Vector]:
        """
        Get the next Vector using addition.

        Action:
            1.  Set
                    x_next = x_current + x_step
                    y_next = (2 * slope * y_current) + slope
            2.  If VectorBuilder cannot create a safe Vector from x_next, y_next, send
                an exception chain in the ComputationResult.
            3.  Otherwise, cast the build product, then send in the success result.
        Args:
            vector: Vector
        Returns:
            ComputationResult[Vector]
        Raises:
             AxisMappingException
        """
        method = f"{self.__class__.__name__}.next"
        
        # Handle the case that, the argument is not safe to use.
        validation = self.math.vector.validator.execute(vector)
        if validation.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                AxisMappingException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisMappingException.MSG,
                    err_code=AxisMappingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=validation.exception,
                ),
            )
        current = cast(Vector, validation.payload)
        
        # --- Get next by adding current and delta. ---#
        addition = self.math.add_vector.execute(
            u=current,
            v=self._delta,
        )
        # Handle the case that, the addition does not produce a result.
        if addition.is_failure:
            # Send an exception chain in the result.
            return ComputationResult.failure(
                AxisMappingException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisMappingException.MSG,
                    err_code=AxisMappingException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.COMPUTATION_RESULT,
                    ex=addition.exception,
                ),
            )
        # --- Forward the work product to the caller. ---#
        return ComputationResult.success(cast(Vector, addition.payload))