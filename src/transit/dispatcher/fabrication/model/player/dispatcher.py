# src/transit/dispatcher/fabrication/model/player/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.player.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import PlayerBuilder
from artifcat import BuildResult
from domain import Player
from err import PlayerBuildDispatcherException
from transit import ModelBuildDispatcher, PlayerCarrier
from util import LoggingLevelRouter


class PlayerBuildDispatcher(ModelBuildDispatcher[Player]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the PlayerBuild workflow.

    Attributes:
        builder: PlayerBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: PlayerBuilder | None = None,
    ):
        super().__init__(builder=builder or PlayerBuilder())
        
    @property
    def builder(self) -> PlayerBuilder:
        return cast(PlayerBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[PlayerCarrier]:
        """
        Forward a job to a PlayerBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a PlayerCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[PlayerCarrier]
        Raises:
             PlayerBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                PlayerBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBuildDispatcherException.MSG,
                    err_code=PlayerBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(PlayerCarrier, build.payload)
        return BuildResult.success(carrier)