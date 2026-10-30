# src/transit/dispatcher/fabrication/struct/binder/player/dispatcher.py

"""
Module: transit.dispatcher.fabrication.binder.player.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from err import PlayerBinderBuildDispatcherException
from domain.struct.binder import PlayerBinder
from artifcat import BuildResult
from transit import PlayerBinderCarrier
from util import LoggingLevelRouter
from transit.dispatcher.fabrication import BinderBuildDispatcher


class PlayerBinderBuildDispatcher(BinderBuildDispatcher[PlayerBinder]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a PlayerBinder instance is certified safe, reliable, and consistent before use.

    Attributes:
        builder: PlayerBinderBuilder

    Provides:
        -   def execute(candidate: Any) -> BuildResult{PlayerBinder]

    Super Class:
        BinderBuilder
    """
    
    def __init__(
            self,
            builder: PlayerBinderBuilder | None = PlayerBinderBuilder(),
    ):
        super().__init__(builder=builder or PlayerBinderBuilder())
        
    @property
    def builder(self) -> PlayerBinderBuilder:
        return cast(PlayerBinderBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[PlayerBinderCarrier]:
        """
        Verify the object is a PlayerBinder that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                builder test..
            2.  Otherwise, cast the payload into a PlayerBinder and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[PlayerBinder]
        Raises:
             PlayerBinderBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                PlayerBinderBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderBuildDispatcherException.MSG,
                    err_code=PlayerBinderBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(PlayerBinderCarrier, build.authorization_applicant)
        )