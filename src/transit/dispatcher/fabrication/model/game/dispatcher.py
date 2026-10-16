# src/transit/dispatcher/fabrication/model/game/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.game.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import GameBuilder
from artifcat import BuildResult
from domain import Game
from err import GameBuildDispatcherException
from transit import ModelBuildDispatcher, GameCarrier
from util import LoggingLevelRouter


class GameBuildDispatcher(ModelBuildDispatcher[Game]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the GameBuild workflow.

    Attributes:
        builder: GameBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: GameBuilder | None = None,
    ):
        super().__init__(builder=builder or GameBuilder())
        
    @property
    def builder(self) -> GameBuilder:
        return cast(GameBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[GameCarrier]:
        """
        Forward a job to a GameBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a GameCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[GameCarrier]
        Raises:
             GameBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                GameBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameBuildDispatcherException.MSG,
                    err_code=GameBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(GameCarrier, build.payload)
        return BuildResult.success(carrier)