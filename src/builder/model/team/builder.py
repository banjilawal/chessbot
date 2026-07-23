# src/builder/model/team/builder.py

"""
Module: builder.model.team.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from blueprint import TeamBlueprint
from builder import ModelBuilder
from err import TeamBuilderException
from model import Team
from result import BuildResult, MethodResultType
from toolkit import TeamBuilderToolkit
from util import LoggingLevelRouter


class TeamBuilder(ModelBuilder[Team]):
    """
    Role
        -   Build Pipeline
        -   Integrity Management
        -   Consistency Assurance
        -   Workflow Owner

   Responsibilities:
        1.  Ensure a new Team instance is born safe and reliable.

    Attributes:
            builder_toolkit: Optional[TeamBuilderToolkit]

    Provides:
        -   def execute(self, blueprint: TeamBlueprint) -> BuildResult[Team]

     Super Class:
         ModelBuilder
     """
    
    def __init__(
            self,
            builder_toolkit: Optional[TeamBuilderToolkit] | None = TeamBuilderToolkit(),
    ):
        """
        Args:
            builder_toolkit: Optional[TeamBuilderToolkit]
        """
        super().__init__(builder_toolkit=builder_toolkit)
    
    @property
    def builder_toolkit(self) -> TeamBuilderToolkit:
        return cast(TeamBuilderToolkit, super().builder_toolkit)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, blueprint: TeamBlueprint) -> BuildResult[Team]:
        """
        Build a safe Team.

        Action:
            1.  Send an exception chain in the BuildResult if either
                    -   The TeamBlueprint object is flagged unsafe.
                    -   The assembler does not return a product.
            2.  Otherwise, cast the assembler product as a Team then, send in the success result,
        Args:
            blueprint: TeamBlueprint
        Returns:
            BuildResult[Team]
        Raises:
            TeamBuilderException
        """
        method = f"{self.__class__.__name__}.build"
        
        # Handle the case that, the blueprint is not certified safe.
        blueprint_validation = self.builder_toolkit.root_certifier.execute(
            candidate=blueprint
        )
        if blueprint_validation.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuilderException.MSG,
                    err_code=TeamBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Handoff the validated blueprint to the assembler. ---#
        assembly = self.builder_toolkit.assembler.execute(
            blueprint=cast(
                TeamBlueprint,
                blueprint_validation.payload
            )
        )
        # Handle the case that assembler cannot satisfy the product request.
        if blueprint_validation.is_failure:
        # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuilderException.MSG,
                    err_code=TeamBuilderException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.BUILD_RESULT,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(cast(Team, assembly.payload))