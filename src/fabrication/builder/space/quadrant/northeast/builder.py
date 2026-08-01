# src/builder/space/quadrant/northeast/builder.py

"""
Module: builder.space.quadrant.northeast.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import NortheastQuadrantBlueprint
from fabrication.builder import QuadrantBuilder
from err import NortheastQuadrantBuilderException
from result import BuildResult, MethodResultType
from geometry.space import NortheastQuadrant
from toolkit import NortheastQuadrantBuilderToolkit
from util import LoggingLevelRouter


class NorthEastQuadrantBuilder(
    QuadrantBuilder[NortheastQuadrant]
):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            builder_toolkit: Optional[NortheastQuadrantBuilderToolkit]

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
        QuadrantBuilder
    """
    def __init__(
            self, 
            builder_toolkit: Optional[NortheastQuadrantBuilderToolkit] | 
                             None = NortheastQuadrantBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[NortheastQuadrantBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: NortheastQuadrantBlueprint
    ) -> BuildResult[NortheastQuadrant]:
        """
        Build a safe NortheastQuadrant.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The blueprint is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a NortheastQuadrant then,
                send in the success result,
        Args:
            blueprint: NortheastQuadrantBlueprint
        Returns:
            BuildResult[NortheastQuadrant]
        Raises:
            NortheastQuadrantBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
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
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(NortheastQuadrantBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NortheastQuadrantBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NortheastQuadrantBuilderException.MSG,
                    err_code=NortheastQuadrantBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(NortheastQuadrant, assembly.payload))