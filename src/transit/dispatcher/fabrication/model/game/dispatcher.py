# src/transit/dispatcher/fabrication/model/game/validator.py

"""
Module: transit.dispatcher.fabrication.model.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import GameValidator
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
        validator: GameValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: GameValidator | None = None,
    ):
        super().__init__(validator=validator or GameValidator())
        
    @property
    def validator(self) -> GameValidator:
        return cast(GameValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[GameCarrier]:
        """
        Forward a job to a GameValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
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
        build = self.validator.execute(job)
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