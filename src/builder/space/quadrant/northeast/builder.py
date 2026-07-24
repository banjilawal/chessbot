# src/builder/space/quadrant/northeast/__init__.py

"""
Module: builder.space.quadrant.northeast.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from builder import QuadrantSpaceBuilder
from err import NortheastQuadrantBuilderException
from model import Vector, vector
from result import BuildResult, MethodResultType
from space import NortheastQuadrant
from util import LoggingLevelRouter


class NorthEastQuadrantBuilder(QuadrantSpaceBuilder[NortheastQuadrant]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
    """
    super().__init__()
    
    
    @LoggingLevelRouter.monitor
    def execute(self) -> BuildResult[NortheastQuadrant]:
        method = f"{self.__class__.__name__}"
        validation = self.math.vector.validator.execult(origin)
        if validation.is_failure:
            # Handle the case that the request is not satisfied.
            if validation.is_failure:
                # Send the exception in the result.
                return BuildResult.failure(
                    NortheastQuadrantBuilderException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NortheastQuadrantBuilderException.MSG,
                        err_code=NortheastQuadrantBuilderException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.BUILD_RESULT,
                        ex=validation.exception
                    )
                )
        root = cast(Vector, validation.payload)
        return BuildResult.success(NortheastQuadrant(origin=root))