# src/transit/dispatcher/fabrication/model/footstep/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.footstep.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from fabrication import FootstepBuilder
from artifcat import BuildResult
from domain import Footstep
from err import FootstepBuildDispatcherException
from transit import ModelBuildDispatcher, FootstepCarrier
from util import LoggingLevelRouter


class FootstepBuildDispatcher(ModelBuildDispatcher[Footstep]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Footstep instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: FootstepBuilder

    Provides:
        -   def execute(candidate: Any) -> BuildResult{Footstep]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            builder: FootstepBuilder | None = FootstepBuilder(),
    ):
        super().__init__(builder=builder or FootstepBuilder())
        
    @property
    def builder(self) -> FootstepBuilder:
        return cast(FootstepBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[FootstepCarrier]:
        """
        Verify the object is a Footstep that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                builder test..
            2.  Otherwise, cast the payload into a Footstep and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[Footstep]
        Raises:
             FootstepBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                FootstepBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepBuildDispatcherException.MSG,
                    err_code=FootstepBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(FootstepCarrier, build.payload)
        )