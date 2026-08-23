# src/fabrication/builder/space/axis/east/fabrication/builder.py

"""
Module: fabrication.builder.space.axis.east.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import EastAxisBlueprint
from fabrication.builder import AxisBuilder
from err import EastAxisBuilderException
from artifcat.result import BuildResult, MethodResultType
from space import EastAxis
from operation.toolkit import EastAxisBuilderToolkit
from util import LoggingLevelRouter


class EastAxisBuilder(AxisBuilder[EastAxis]):
    """
    Role:
        -   Builder
        -   Integrity Management

    Responsibilities:
        1.  Create an EastAxis from the origin.

    Attributes:
            builder_toolkit: Optional[EastAxisBuilderToolkit]

    Provides:
        -   def execute(origin: Vector) -> BuildResult[EastAxis]

    Super Class:
        AxisBuilder
    """
    def __init__(
            self, 
            builder_toolkit: Optional[EastAxisBuilderToolkit] |  None = None
    ):
        """
        Args:
            builder_toolkit: Optional[EastAxisBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit or EastAxisBuilderToolkit())
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            blueprint: EastAxisBlueprint
    ) -> BuildResult[EastAxis]:
        """
        Build a safe EastAxis.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The blueprint is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a EastAxis then,
                send in the success result,
        Args:
            blueprint: EastAxisBlueprint
        Returns:
            BuildResult[EastAxis]
        Raises:
            EastAxisBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EastAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EastAxisBuilderException.MSG,
                    err_code=EastAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(EastAxisBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EastAxisBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EastAxisBuilderException.MSG,
                    err_code=EastAxisBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(EastAxis, assembly.payload))