# src/transit/dispatcher/builder/registry/space/quadrant/dispatcher/builder.py

"""
Module: transit.dispatcher.builder.registry.space.quadrant.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain.metadata.blueprint import QuadrantReservoirBlueprint
from transit.dispatcher.builder import SpaceReservoirBuildDispatcher
from err import QuadrantReservoirBuilderException
from topology.registry import QuadrantReservoir
from artifcat import BuildResult, MethodResultType
from operation.toolkit import QuadrantReservoirBuilderToolkit
from util import LoggingLevelRouter


class QuadrantReservoirBuilder(SpaceReservoirBuildDispatcher[QuadrantReservoir]):
    """
    Role
        -  Build Pipeline
        -  Integrity Management
        -  Consistency Assurance
        -  Workflow Owner

   Responsibilities:
        1.  Ensure a new Quadrant instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[QuadrantReservoirBuilderToolkit]

    Provides:
        -  def execute(self, blueprint: QuadrantReservoirBlueprint) -> BuildResult[Quadrant]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[QuadrantReservoirBuilderToolkit] |
                             None = QuadrantReservoirBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[QuadrantReservoirBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> QuadrantReservoirBuilderToolkit:
        return cast(QuadrantReservoirBuilderToolkit, super().assembler)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: QuadrantReservoirBlueprint) -> BuildResult[QuadrantReservoir]:
        """
        Build a safe Quadrant.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -  The QuadrantReservoirBlueprint object is flagged unsafe.
                    -  The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Quadrant then, send in the success result,
        Args:
            blueprint: QuadrantReservoirBlueprint
        Returns:
            BuildResult[Quadrant]
        Raises:
            QuadrantReservoirBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                QuadrantReservoirBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantReservoirBuilderException.MSG,
                    err_code=QuadrantReservoirBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(QuadrantReservoirBlueprint, validation.payload)
        )
        # Handle the case that assembler cannot satisfy the product request.
        if assembly.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                QuadrantReservoirBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=QuadrantReservoirBuilderException.MSG,
                    err_code=QuadrantReservoirBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=assembly.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(QuadrantReservoir, assembly.payload))