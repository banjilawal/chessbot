# src/transit/dispatcher/fabrication/model/rank/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.rank.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import RankBuilder
from artifcat import BuildResult
from domain import Rank
from err import RankBuildDispatcherException
from transit import ModelBuildDispatcher, RankCarrier
from util import LoggingLevelRouter


class RankBuildDispatcher(ModelBuildDispatcher[Rank]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the RankBuild workflow.

    Attributes:
        builder: RankBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: RankBuilder | None = None,
    ):
        super().__init__(builder=builder or RankBuilder())
        
    @property
    def builder(self) -> RankBuilder:
        return cast(RankBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[RankCarrier]:
        """
        Forward a job to a RankBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a RankCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[RankCarrier]
        Raises:
             RankBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuildDispatcherException.MSG,
                    err_code=RankBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(RankCarrier, build.payload)
        return BuildResult.success(carrier)