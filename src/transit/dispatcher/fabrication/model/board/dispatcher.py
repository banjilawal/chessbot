# src/transit/dispatcher/fabrication/model/board/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.board.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import BoardBuilder
from artifcat import BuildResult
from domain import Board
from err import BoardBuildDispatcherException
from transit import ModelBuildDispatcher, BoardCarrier
from util import LoggingLevelRouter


class BoardBuildDispatcher(ModelBuildDispatcher[Board]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the BoardBuild workflow.

    Attributes:
        builder: BoardBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: BoardBuilder | None = None,
    ):
        super().__init__(builder=builder or BoardBuilder())
        
    @property
    def builder(self) -> BoardBuilder:
        return cast(BoardBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[BoardCarrier]:
        """
        Forward a job to a BoardBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a BoardCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[BoardCarrier]
        Raises:
             BoardBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildDispatcherException.MSG,
                    err_code=BoardBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(BoardCarrier, build.payload)
        return BuildResult.success(carrier)