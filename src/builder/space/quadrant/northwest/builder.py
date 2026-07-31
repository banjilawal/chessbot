# src/builder/space/quadrant/northwest/builder.py

"""
Module: builder.space.quadrant.northwest.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import NorthwestQuadrantBlueprint
from builder import QuadrantBuilder
from err import NorthwestQuadrantBuilderException
from result import BuildResult, MethodResultType
from geometry.space import NorthwestQuadrant
from toolkit import NorthwestQuadrantBuilderToolkit
from util import LoggingLevelRouter


class NorthwestQuadrantBuilder(QuadrantBuilder[NorthwestQuadrant]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            builder_toolkit: Optional[NorthwestQuadrantBuilderToolkit]

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
        QuadrantBuilder
    """
    def __init__(
            self, 
            builder_toolkit: Optional[NorthwestQuadrantBuilderToolkit] | 
                             None = NorthwestQuadrantBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[NorthwestQuadrantBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: NorthwestQuadrantBlueprint
    ) -> BuildResult[NorthwestQuadrant]:
        """
        Build a safe NorthwestQuadrant.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The blueprint is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a NorthwestQuadrant then,
                send in the success result,
        Args:
            blueprint: NorthwestQuadrantBlueprint
        Returns:
            BuildResult[NorthwestQuadrant]
        Raises:
            NorthwestQuadrantBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NorthwestQuadrantBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthwestQuadrantBuilderException.MSG,
                    err_code=NorthwestQuadrantBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(NorthwestQuadrantBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NorthwestQuadrantBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthwestQuadrantBuilderException.MSG,
                    err_code=NorthwestQuadrantBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(NorthwestQuadrant, assembly.payload))