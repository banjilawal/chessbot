# src/linear/segment/linear.py

"""
Module: space.linear.segment.linear
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import Optional, cast

from builder.endpoint.old_quadrant import QuadrantEndpointFactory
from builder.endpoint.axis import AxisEndpointFactory
from err import BuilderException
from model import Vector
from register import VectorRegister
from result import BuildResult, MethodResultType
from toggle import OrientationToggle

from util import LoggingLevelRouter
from validator import VectorValidator


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
            toggle: OrientationToggle,
    ) -> BuildResult[VectorRegister]:
        method = f"{self.__class__.__name__}"
        
        request = BuildResult.failure(BuilderException())
        
        if toggle.is_axis_toggle:
            request = self._axis_endpoint_factory.execute(origin=origin, toggle=toggle)
        else:
            request = self._quadrant_endpoint_factory.execute(origin=origin, toggle=toggle)
            
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