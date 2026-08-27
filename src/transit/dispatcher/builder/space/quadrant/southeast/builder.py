# src/transit/dispatcher/builder/space/quadrant/southeast/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.space.quadrant.southeast.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import SoutheastQuadrantBlueprint
from transit.dispatcher.builder import QuadrantBuilder
from err import SoutheastQuadrantBuilderException
from artifcat import BuildResult, MethodResultType
from space import SoutheastQuadrant
from operation.toolkit import SoutheastQuadrantBuilderToolkit
from util import LoggingLevelRouter


class SoutheastQuadrantBuilder(QuadrantBuilder[SoutheastQuadrant]):
    """
    Role:
        - Builder
        -  Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            builder_toolkit: Optional[SoutheastQuadrantBuilderToolkit]

    Provides:
        -  def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
        QuadrantBuilder
    """
    def __init__(
            self, 
            builder_toolkit: Optional[SoutheastQuadrantBuilderToolkit] | 
                             None = SoutheastQuadrantBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[SoutheastQuadrantBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: SoutheastQuadrantBlueprint
    ) -> BuildResult[SoutheastQuadrant]:
        """
        Build a safe SoutheastQuadrant.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -  The blueprint is flagged unsafe.
                    -  The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a SoutheastQuadrant then,
                send in the success result,
        Args:
            blueprint: SoutheastQuadrantBlueprint
        Returns:
            BuildResult[SoutheastQuadrant]
        Raises:
            SoutheastQuadrantBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SoutheastQuadrantBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SoutheastQuadrantBuilderException.MSG,
                    err_code=SoutheastQuadrantBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(SoutheastQuadrantBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SoutheastQuadrantBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SoutheastQuadrantBuilderException.MSG,
                    err_code=SoutheastQuadrantBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(SoutheastQuadrant, assembly.payload))