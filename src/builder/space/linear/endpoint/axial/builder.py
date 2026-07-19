# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from service import LinearEndpointFactory, VectorService

from err import AxisEndpointFactoryException
from model import Vector
from register import VectorRegister
from result import BuildResult, MethodResultType
from schema import AxisOrientation


class AxisEndpointFactory(LinearEndpointFactory):
    """
    Role:
        -   Service
        -   Integrity Management

    Responsibilities:
        1.  Create a VectoRegister for an AxialSpace endpoints.

    Attributes:
        _origin: Vector
        _vector_service: VectorService

    Provides:
        -   def eastern_endpoints() -> VectorRegister
        -   def northern_endpoints() -> VectorRegister
        -   def western_endpoints() -> VectorRegister
        -   def southern_endpoints() -> VectorRegister

    Super Class:
    """
    _origin: Vector
    _vector_service: VectorService
    _orientation: AxisOrientation
    
    def __init__(
            self,
            origin: Vector,
            orientation: AxisOrientation,
            vector_service: Optional[VectorService] | None = VectorService()
    ):
        """
        Args:
            origin: Vector
            vector_service: Optional[VectorService]
        """
        self._origin = origin
        self._orientation = orientation
        self._vector_service = vector_service
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service
    
    @property
    def orientation(self) -> AxisOrientation:
        return self._orientation
    
    def eastern_endpoints(self) -> BuildResult[VectorRegister]:
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the origin is not safe to use.
        validation = self._vector_service.validator.execute(
            candidate=self._origin
        )
        # Send the exception chain in the result.
        if validation.is_failure:
            return BuildResult.failure(
                AxisEndpointFactoryException(
                    cls_mthd=method,
                    cls_name=self.__class__name__,
                    msg=AxisEndpointFactoryException.MSG,
                    err_code=AxisEndpointFactory.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        build_result: BuildResult
        
        if self.orientation == AxisOrientation.EAST:
            build_result = self._
        """
        East towards num_columns - 1 (right)
        """
        return VectorRegister(
            u=self._origin,
            v = Vector(
                x=self._origin.x + AxisTerminus.EAST.delta.x,
                y=self._origin.y+ AxisTerminus.EAST.delta.y,
            )
        )
    
    def northern_endpoints(self) -> VectorRegister:
        """
        North towards 0  (up)
        """
        return VectorRegister(
            u=self._origin,
            v=Vector(x=self._origin.x, y=0),
        )
    
    def southern_endpoints(self) -> VectorRegister:
        """
        South towards num_rows - 1 (up)
        """
        return VectorReg ist er(
            u=self._origin,
            v=Vector(
                x=self._origin.x + AxisTerminus.SOUTH.delta.x,
                y=self._origin.y + AxisTerminus.SOUTH.delta.y,
            )
        )
    
    def western_endpoints(self) -> VectorRegister:
        """
        West towards 0 (left)
        """
        return VectorRegister(
            u=self._origin,
            v=Vector(x=0, y=self._origin.y)
        )