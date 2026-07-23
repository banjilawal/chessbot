# src/builder/model/edge/builder.py

"""
Module: builder.model.edge.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import EdgeBlueprint
from builder import ModelBuilder
from err import EdgeBuilderException
from model import Edge
from result import BuildResult, MethodResultType
from toolkit import EdgeBuilderToolkit
from util import LoggingLevelRouter


class EdgeBuilder(ModelBuilder[Edge]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Edge instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[EdgeBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: EdgeBlueprint) -> BuildResult[Edge]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[EdgeBuilderToolkit] | None = EdgeBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[EdgeBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> EdgeBuilderToolkit:
        return cast(EdgeBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: EdgeBlueprint) -> BuildResult[Edge]:
        """
        Build a safe Edge.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The EdgeBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Edge then, send in the success result,
        Args:
            blueprint: EdgeBlueprint
        Returns:
            BuildResult[Edge]
        Raises:
            EdgeBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EdgeBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EdgeBuilderException.MSG,
                    err_code=EdgeBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                EdgeBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                EdgeBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EdgeBuilderException.MSG,
                    err_code=EdgeBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Edge, assembly.payload))