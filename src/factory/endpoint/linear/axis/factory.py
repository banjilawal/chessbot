# src/factory/endpoint/linear/axis/factory.py

"""
Module: factory.endpoint.linear.axis.factory
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from factory import LinearEndpointFactory
from microservice import VectorService
from model import Vector
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
    
    _east_axis_endpoint_factory: EastAxisEndpointFactory
    _north_axis_endpoint_factory: NorthAxisEndpointFactory
    _south_axis_endpoint_factory: SouthAxisEndpointFactory
    _west_axis_endpoint_factory: WestAxisEndpointFactory
    
    def __init__(
            self,
            origin: Vector,
            orientation: AxisOrientation,
            vector_service: Optional[VectorService] | None = VectorService(),
            east_axis_endpoint_factory: Optional[EastAxisEndpointFactory] |
                                        None = EastAxisEndpointFactory(),
            north_axis_endpoint_factory: Optional[NorthAxisEndpointFactory] | 
                                         None = NorthAxisEndpointFactory(),
            south_axis_endpoint_factory: Optional[SouthAxisEndpointFactory] |
                                         None = SouthAxisEndpointFactory(),
            west_axis_endpoint_factory: Optional[WestAxisEndpointFactory] |
                                        None = SouthAxisEndpointFactory(),
    ):
        """
        Args:
            origin: Vector
            vector_service: Optional[VectorService]
            east_axis_endpoint_factory: Optional[EastAxisEndpointFactory]
            north_axis_endpoint_factory: Optional[NorthAxisEndpointFactory]
            south_axis_endpoint_factory: Optional[SouthAxisEndpointFactory]
            west_axis_endpoint_factory: Optional[SouthAxisEndpointFactory]
        """
        self._origin = origin
        self._orientation = orientation
        self._vector_service = vector_service
        self._south_axis_endpoint_factory = south_axis_endpoint_factory
        self._north_axis_endpoint_factory = north_axis_endpoint_factory
        self._east_axis_endpoint_factory = east_axis_endpoint_factory
        self._west_axis_endpoint_factory = west_axis_endpoint_factory
        
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
        request = BuildResult().failure(AxisEndpointFactoryException())
        
        if self.orientation == AxisOrientation.EAST:
            request = self._east_axis_endpoint_factory.execute(
                origin=self._origin
            )
        if self.orientation == AxisOrientation.NORTH:
            request = self._north_axis_endpoint_factory.execute(
                origin=self._origin
            )
        if self.orientation == AxisOrientation.SOUTH:
            request = self._south_axis_endpoint_factory.execute(
                origin=self._origin
            )
        if self.orientation == AxisOrientation.WEST:
            request = self._west_axis_endpoint_factory.execute(
                origin=self._origin
            )
        # Handle the case that, the build request is not fulfilled.
        if request.is_failure:
            # Send the exception chain in the result.
            if validation.is_failure:
                return BuildResult.failure(
                    AxisEndpointFactoryException(
                        cls_mthd=method,
                        cls_name=self.__class__name__,
                        msg=AxisEndpointFactoryException.MSG,
                        err_code=AxisEndpointFactory.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=request.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(VectorRegister, request.payload))