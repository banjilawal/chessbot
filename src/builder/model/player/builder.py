# src/builder/model/player/builder.py

"""
Module: builder.model.player.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import PlayerBlueprint
from builder import ModelBuilder
from err import PlayerBuilderException
from model import Player
from result import BuildResult, MethodResultType
from toolkit import PlayerBuilderToolkit
from util import LoggingLevelRouter


class PlayerBuilder(ModelBuilder[Player]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Player instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[PlayerBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: PlayerBlueprint) -> BuildResult[Player]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[PlayerBuilderToolkit] | None = PlayerBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[PlayerBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> PlayerBuilderToolkit:
        return cast(PlayerBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: PlayerBlueprint) -> BuildResult[Player]:
        """
        Build a safe Player.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The PlayerBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Player then, send in the success result,
        Args:
            blueprint: PlayerBlueprint
        Returns:
            BuildResult[Player]
        Raises:
            PlayerBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                PlayerBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBuilderException.MSG,
                    err_code=PlayerBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                PlayerBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                PlayerBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBuilderException.MSG,
                    err_code=PlayerBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Player, assembly.payload))