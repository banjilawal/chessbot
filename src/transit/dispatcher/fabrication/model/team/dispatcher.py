# src/transit/dispatcher/fabrication/model/team/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.team.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import TeamBuilder
from artifcat import BuildResult
from domain import Team
from err import TeamBuildDispatcherException
from transit import ModelBuildDispatcher, TeamCarrier
from util import LoggingLevelRouter


class TeamBuildDispatcher(ModelBuildDispatcher[Team]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the TeamBuild workflow.

    Attributes:
        builder: TeamBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: TeamBuilder | None = None,
    ):
        super().__init__(builder=builder or TeamBuilder())
        
    @property
    def builder(self) -> TeamBuilder:
        return cast(TeamBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[TeamCarrier]:
        """
        Forward a job to a TeamBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a TeamCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[TeamCarrier]
        Raises:
             TeamBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBuildDispatcherException.MSG,
                    err_code=TeamBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(TeamCarrier, build.payload)
        return BuildResult.success(carrier)