# src/fabrication/builder/registry/space/axis/fabrication/builder.py

"""
Module: fabrication.builder.registry.space.axis.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from fabrication.blueprint import AxisReservoirBlueprint
from fabrication.builder import SpaceReservoirBuilder
from err import AxisReservoirBuilderException
from topology.registry import AxisReservoir
from result import BuildResult, MethodResultType
from kit.toolkit import AxisReservoirBuilderToolkit
from util import LoggingLevelRouter


class AxisReservoirBuilder(SpaceReservoirBuilder[AxisReservoir]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Axis instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[AxisReservoirBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: AxisReservoirBlueprint) -> BuildResult[Axis]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[AxisReservoirBuilderToolkit] |
                             None = AxisReservoirBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[AxisReservoirBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> AxisReservoirBuilderToolkit:
        return cast(AxisReservoirBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: AxisReservoirBlueprint) -> BuildResult[AxisReservoir]:
        """
        Build a safe Axis.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The AxisReservoirBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Axis then, send in the success result,
        Args:
            blueprint: AxisReservoirBlueprint
        Returns:
            BuildResult[Axis]
        Raises:
            AxisReservoirBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AxisReservoirBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisReservoirBuilderException.MSG,
                    err_code=AxisReservoirBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(AxisReservoirBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                AxisReservoirBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AxisReservoirBuilderException.MSG,
                    err_code=AxisReservoirBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(AxisReservoir, assembly.payload))