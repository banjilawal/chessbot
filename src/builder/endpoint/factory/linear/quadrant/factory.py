# src/space/linear/segment/axial/space.py

"""
Module: space.linear.segment.axial.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast


from builder import (
    EastQuadrantEndpointBuilder, LinearEndpointFactory, NorthQuadrantEndpointBuilder, SouthQuadrantEndpointBuilder,
    WestQuadrantEndpointBuilder
)
from err import QuadrantEndpointFactoryException
from microservice import VectorService
from model import Vector
from register import VectorRegister
from result import BuildResult, MethodResultType
from schema import QuadrantOrientation


class QuadrantEndpointFactory(LinearEndpointFactory):
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
    _orientation: QuadrantOrientation
    
    _east_quadrant_endpoint_builder: EastQuadrantEndpointBuilder
    _north_quadrant_endpoint_builder: NorthQuadrantEndpointBuilder
    _south_quadrant_endpoint_builder: SouthQuadrantEndpointBuilder
    _west_quadrant_endpoint_builder: WestQuadrantEndpointBuilder
    
    def __init__(
            self,
            origin: Vector,
            orientation: QuadrantOrientation,
            vector_service: Optional[VectorService] | None = VectorService(),
            east_quadrant_endpoint_builder: Optional[EastQuadrantEndpointBuilder] |
                                        None = EastQuadrantEndpointBuilder(),
            north_quadrant_endpoint_builder: Optional[NorthQuadrantEndpointBuilder] | 
                                         None = NorthQuadrantEndpointBuilder(),
            south_quadrant_endpoint_builder: Optional[SouthQuadrantEndpointBuilder] |
                                         None = SouthQuadrantEndpointBuilder(),
            west_quadrant_endpoint_builder: Optional[WestQuadrantEndpointBuilder] |
                                        None = SouthQuadrantEndpointBuilder(),
    ):
        """
        Args:
            origin: Vector
            vector_service: Optional[VectorService]
            east_quadrant_endpoint_builder: Optional[EastQuadrantEndpointBuilder]
            north_quadrant_endpoint_builder: Optional[NorthQuadrantEndpointBuilder]
            south_quadrant_endpoint_builder: Optional[SouthQuadrantEndpointBuilder]
            west_quadrant_endpoint_builder: Optional[SouthQuadrantEndpointBuilder]
        """
        self._origin = origin
        self._orientation = orientation
        self._vector_service = vector_service
        self._south_quadrant_endpoint_builder = south_quadrant_endpoint_builder
        self._north_quadrant_endpoint_builder = north_quadrant_endpoint_builder
        self._east_quadrant_endpoint_builder = east_quadrant_endpoint_builder
        self._west_quadrant_endpoint_builder = west_quadrant_endpoint_builder
        
    @property
    def origin(self) -> Vector:
        return self._origin
    
    @property
    def vector_service(self) -> VectorService:
        return self._vector_service
    
    @property
    def orientation(self) -> QuadrantOrientation:
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
                QuadrantEndpointFactoryException(
                    cls_mthd=method,
                    cls_name=self.__class__name__,
                    msg=QuadrantEndpointFactoryException.MSG,
                    err_code=QuadrantEndpointFactory.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        request = BuildResult().failure(QuadrantEndpointFactoryException())
        
        if self.orientation == QuadrantOrientation.EAST:
            request = self._east_quadrant_endpoint_builder.execute(
                origin=self._origin
            )
        if self.orientation == QuadrantOrientation.NORTH:
            request = self._north_quadrant_endpoint_builder.execute(
                origin=self._origin
            )
        if self.orientation == QuadrantOrientation.SOUTH:
            request = self._south_quadrant_endpoint_builder.execute(
                origin=self._origin
            )
        if self.orientation == QuadrantOrientation.WEST:
            request = self._west_quadrant_endpoint_builder.execute(
                origin=self._origin
            )
        # Handle the case that, the build request is not fulfilled.
        if request.is_failure:
            # Send the exception chain in the result.
            if validation.is_failure:
                return BuildResult.failure(
                    QuadrantEndpointFactoryException(
                        cls_mthd=method,
                        cls_name=self.__class__name__,
                        msg=QuadrantEndpointFactoryException.MSG,
                        err_code=QuadrantEndpointFactory.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=request.exception
                    )
                )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(VectorRegister, request.payload))