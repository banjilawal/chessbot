# src/fabrication/builder/space/axis/north/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.north.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.blueprint import NorthAxisBlueprint
from fabrication.builder import AxisBuilder
from err import NorthAxisBuilderException
from result import BuildResult, MethodResultType
from space import NorthAxis
from toolkit import NorthAxisBuilderToolkit
from util import LoggingLevelRouter


class NorthAxisBuilder(AxisBuilder[NorthAxis]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            builder_toolkit: Optional[NorthAxisBuilderToolkit]

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
        AxisBuilder
    """
    def __init__(
            self, 
            builder_toolkit: Optional[NorthAxisBuilderToolkit] | None = None,
    ):
        """
        Args:
            builder_toolkit: Optional[NorthAxisBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit or NorthAxisBuilderToolkit())
    
    @LoggingLevelRouter.monitor
    def execute( self, blueprint: NorthAxisBlueprint) -> BuildResult[NorthAxis]:
        """
        Build a safe NorthAxis.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The blueprint is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a NorthAxis then,
                send in the success result,
        Args:
            blueprint: NorthAxisBlueprint
        Returns:
            BuildResult[NorthAxis]
        Raises:
            NorthAxisBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NorthAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisBuilderException.MSG,
                    err_code=NorthAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(NorthAxisBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NorthAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NorthAxisBuilderException.MSG,
                    err_code=NorthAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(NorthAxis, assembly.payload))