# src/space/linear/segment/linear.py

"""
Module: space.linear.segment.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, cast

from builder.endpoint.old_quadrant import QuadrantEndpointFactory
from builder.endpoint.space.axis import AxisEndpointFactory
from err import BuilderException
from model import Vector
from register import VectorRegister
from result import BuildResult, MethodResultType
from selector import OrientationSelector
from util import LoggingLevelRouter


class LinearEndpointFactory:
    
    _vector_validator: VectorValidator
    _axis_endpoint_factory: AxisEndpointFactory
    _quadrant_endpoint_factory: QuadrantEndpointFactory
    
    def __init__(
            self,
            axis_endpoint_factory: Optional[AxisEndpointFactory] |
                                   None = AxisEndpointFactory(),
            quadrant_endpoint_factory: Optional[QuadrantEndpointFactory] |
                                       None = QuadrantEndpointFactory(),
    ):
        """
        Args:
            axis_endpoint_factory: Optional[AxisEndpointFactory]
            quadrant_endpoint_factory: Optional[QuadrantEndpointFactory]
        """
        self._axis_endpoint_factory = axis_endpoint_factory
        self._quadrant_endpoint_factory = quadrant_endpoint_factory
        
    @LoggingLevelRouter.monitor
    def execute(
            self,
            origin: Vector,
            selector: OrientationSelector,
    ) -> BuildResult[VectorRegister]:
        method = f"{self.__class__.__name__}"
        
        request = BuildResult.failure(BuilderException())
        
        if selector.is_axis_selector:
            request = self._axis_endpoint_factory.execute(origin=origin, selector=selector)
        else:
            request = self._quadrant_endpoint_factory.execute(origin=origin, selector=selector)
            
        if request.is_failure:
            return BuildResult.failure(
                LineEndpointFactoryException(
                    cls_mthd=method,
                    clsn_name=self.__class__.__name__,
                    msg=LineEndpointFactoryException.MSG,
                    err_code=LineEndpointFactoryException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=request.exception
                )
            )
        return BuildResult.success(cast(VectorRegister, request.payload))