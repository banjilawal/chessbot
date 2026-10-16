# src/transit/dispatcher/fabrication/model/maneuver/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.maneuver.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import ManeuverBuilder
from artifcat import BuildResult
from domain import Maneuver
from err import ManeuverBuildDispatcherException
from transit import ModelBuildDispatcher, ManeuverCarrier
from util import LoggingLevelRouter


class ManeuverBuildDispatcher(ModelBuildDispatcher[Maneuver]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ManeuverBuild workflow.

    Attributes:
        builder: ManeuverBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: ManeuverBuilder | None = None,
    ):
        super().__init__(builder=builder or ManeuverBuilder())
        
    @property
    def builder(self) -> ManeuverBuilder:
        return cast(ManeuverBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ManeuverCarrier]:
        """
        Forward a job to a ManeuverBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ManeuverCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[ManeuverCarrier]
        Raises:
             ManeuverBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ManeuverBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverBuildDispatcherException.MSG,
                    err_code=ManeuverBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ManeuverCarrier, build.payload)
        return BuildResult.success(carrier)