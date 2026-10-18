# src/fabrication/builder/model/team/builder.py

"""
Module: fabrication.builder.model.team.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Team, TeamBlueprint
from err import TeamBlueprintIdEmptyException, TeamBuilderException, TeamConsistencyException
from exchange import TeamBuildRequest
from fabrication import ModelBuilder, TeamBuildLoader
from util import IdFactory, LoggingLevelRouter


class TeamBuilder(ModelBuilder[Team]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Team from a blueprint.

    Attributes:
       loader: TeamBuildLoader

    Provides:
        -   def execute(blueprint: TeamBlueprint) -> BuildResult[Team]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[TeamBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[TeamBuildLoader]
        """
        super().__init__(loader=loader or TeamBuildLoader())
    
    @property
    def loader(self) -> TeamBuildLoader:
        return cast(TeamBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TeamBuildRequest) -> BuildResult[Team]:
        """
        Assemble a Team from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Team for the success loading.
        Args:
            request: TeamBuildRequest
        Returns:
            BuildResult[Team]
        Raises:
            TeamBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        loading = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if loading.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuilderException.MSG,
                    err_code=TeamBuilderException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(TeamBlueprint, loading.payload)
        id = blueprint.id or IdFactory.next_id(class_name="Team")
        
        # --- Assemble and send the work product. ---#
        product = Team(
            id=id,
            board=blueprint.board,
            owner=blueprint.owner,
            archetype=blueprint.archetype,
        )
        if product not in blueprint.board.binder.to_list:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuilderException.MSG,
                    err_code=TeamBuilderException.ERR_CODE,
                    ex=TeamConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg="Board is already assigned to a different Team instance.",
                        err_code="TEAM_BOARD_CONSISTENCY_ERROR"
                    ),
                )
            )
        return BuildResult.success(product)