# src/transit/dispatcher/fabrication/struct/chart/participate/dispatcher.py

"""
Module: transit.dispatcher.fabrication.chart.participate.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import BuildResult
from fabrication import ParticipationBuilder
from domain import Participation
from err import ParticipationBuildDispatcherException
from transit import ChartBuildDispatcher, ParticipationCarrier
from util import LoggingLevelRouter


class ParticipationBuildDispatcher(ChartBuildDispatcher[Participation]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Participation instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: ParticipationBuilder

    Provides:
        -   def execute(candidate: Any) -> BuildResult{Participation]

    Super Class:
        ChartBuilder
    """
    
    def __init__(
            self,
            builder: ParticipationBuilder | None = None,
    ):
        super().__init__(builder=builder or ParticipationBuilder())
        
    @property
    def builder(self) -> ParticipationBuilder:
        return cast(ParticipationBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ParticipationCarrier]:
        """
        Verify the object is a Participation that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                builder test..
            2.  Otherwise, cast the payload into a Participation and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[Participation]
        Raises:
             ParticipationBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ParticipationBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationBuildDispatcherException.MSG,
                    err_code=ParticipationBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(ParticipationCarrier, build.authorization_applicant)
        )