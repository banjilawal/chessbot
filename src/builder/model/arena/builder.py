# src/builder/model/arena/builder.py

"""
Module: builder.model.arena.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import ArenaBlueprint
from builder import ModelBuilder
from err import ArenaBuilderException
from model import Arena
from result import BuildResult, MethodResultType
from toolkit import ArenaBuilderToolkit
from util import LoggingLevelRouter


class ArenaBuilder(ModelBuilder[Arena]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Arena instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[ArenaBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: ArenaBlueprint) -> BuildResult[Arena]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[ArenaBuilderToolkit] | None = ArenaBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[ArenaBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> ArenaBuilderToolkit:
        return cast(ArenaBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: ArenaBlueprint) -> BuildResult[Arena]:
        """
        Build a safe Arena.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The ArenaBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Arena then, send in the success result,
        Args:
            blueprint: ArenaBlueprint
        Returns:
            BuildResult[Arena]
        Raises:
            ArenaBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ArenaBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuilderException.MSG,
                    err_code=ArenaBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                ArenaBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                ArenaBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuilderException.MSG,
                    err_code=ArenaBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Arena, assembly.payload))