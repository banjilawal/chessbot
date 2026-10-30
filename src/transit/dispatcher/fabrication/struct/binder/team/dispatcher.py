# src/transit/dispatcher/fabrication/struct/binder/team/dispatcher.py

"""
Module: transit.dispatcher.fabrication.binder.team.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import TeamBinderBuildDispatcherException
from domain.struct.binder import TeamBinder
from artifcat import BuildResult
from transit import TeamBinderCarrier
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import BinderBuildDispatcher


class TeamBinderBuildDispatcher(BinderBuildDispatcher[TeamBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TeamBinder instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: TeamBinderBuilder

    Provides:
        -   def execute(candidate: Any) -> BuildResult{TeamBinder]

    Super Class:
        BinderBuilder
    """
    
    def __init__(
            self,
            builder: TeamBinderBuilder | None = TeamBinderBuilder(),
    ):
        super().__init__(builder=builder or TeamBinderBuilder())
        
    @property
    def builder(self) -> TeamBinderBuilder:
        return cast(TeamBinderBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[TeamBinderCarrier]:
        """
        Verify the object is a TeamBinder that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                builder test..
            2.  Otherwise, cast the payload into a TeamBinder and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[TeamBinder]
        Raises:
             TeamBinderBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                TeamBinderBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TeamBinderBuildDispatcherException.MSG,
                    err_code=TeamBinderBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(TeamBinderCarrier, build.authorization_applicant)
        )