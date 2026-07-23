# src/builder/model/node/builder.py

"""
Module: builder.model.node.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import NodeBlueprint
from builder import ModelBuilder
from err import NodeBuilderException
from model import Node
from result import BuildResult, MethodResultType
from toolkit import NodeBuilderToolkit
from util import LoggingLevelRouter


class NodeBuilder(ModelBuilder[Node]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Node instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[NodeBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: NodeBlueprint) -> BuildResult[Node]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[NodeBuilderToolkit] | None = NodeBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[NodeBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> NodeBuilderToolkit:
        return cast(NodeBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: NodeBlueprint) -> BuildResult[Node]:
        """
        Build a safe Node.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The NodeBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Node then, send in the success result,
        Args:
            blueprint: NodeBlueprint
        Returns:
            BuildResult[Node]
        Raises:
            NodeBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                NodeBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NodeBuilderException.MSG,
                    err_code=NodeBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                NodeBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                NodeBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=NodeBuilderException.MSG,
                    err_code=NodeBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Node, assembly.payload))