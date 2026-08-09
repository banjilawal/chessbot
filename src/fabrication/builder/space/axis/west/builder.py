# src/fabrication/builder/space/axis/west/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.west.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.blueprint import WestAxisBlueprint
from fabrication.builder import AxisBuilder
from err import WestAxisBuilderException
from result import BuildResult, MethodResultType
from space import WestAxis
from kit.toolkit import WestAxisBuilderToolkit
from util import LoggingLevelRouter


class WestAxisBuilder(AxisBuilder[WestAxis]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            builder_toolkit: Optional[WestAxisBuilderToolkit]

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
        AxisBuilder
    """
    def __init__(
            self, 
            builder_toolkit: Optional[WestAxisBuilderToolkit] | 
                             None = WestAxisBuilderToolkit()
    ):
        """
        Args:
            builder_toolkit: Optional[WestAxisBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: WestAxisBlueprint
    ) -> BuildResult[WestAxis]:
        """
        Build a safe WestAxis.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The blueprint is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a WestAxis then,
                send in the success result,
        Args:
            blueprint: WestAxisBlueprint
        Returns:
            BuildResult[WestAxis]
        Raises:
            WestAxisBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                WestAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisBuilderException.MSG,
                    err_code=WestAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(WestAxisBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                WestAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WestAxisBuilderException.MSG,
                    err_code=WestAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(WestAxis, assembly.payload))