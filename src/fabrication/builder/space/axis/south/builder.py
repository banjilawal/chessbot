# src/builder/space/axis/south/builder.py

"""
Module: builder.space.axis.south.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import SouthAxisBlueprint
from fabrication.builder import AxisBuilder
from err import SouthAxisBuilderException
from result import BuildResult, MethodResultType
from geometry.space import SouthAxis
from toolkit import SouthAxisBuilderToolkit
from util import LoggingLevelRouter


class SouthAxisBuilder(AxisBuilder[SouthAxis]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            builder_toolkit: Optional[SouthAxisBuilderToolkit]

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
        AxisBuilder
    """
    def __init__(
            self, 
            builder_toolkit: Optional[SouthAxisBuilderToolkit] | 
                             None = SouthAxisBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[SouthAxisBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: SouthAxisBlueprint
    ) -> BuildResult[SouthAxis]:
        """
        Build a safe SouthAxis.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The blueprint is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a SouthAxis then,
                send in the success result,
        Args:
            blueprint: SouthAxisBlueprint
        Returns:
            BuildResult[SouthAxis]
        Raises:
            SouthAxisBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SouthAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthAxisBuilderException.MSG,
                    err_code=SouthAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(SouthAxisBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SouthAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SouthAxisBuilderException.MSG,
                    err_code=SouthAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(SouthAxis, assembly.payload))