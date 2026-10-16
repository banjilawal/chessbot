# src/transit/dispatcher/fabrication/model/square/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.square.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import SquareBuilder
from artifcat import BuildResult
from domain import Square
from err import SquareBuildDispatcherException
from transit import ModelBuildDispatcher, SquareCarrier
from util import LoggingLevelRouter


class SquareBuildDispatcher(ModelBuildDispatcher[Square]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the SquareBuild workflow.

    Attributes:
        builder: SquareBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: SquareBuilder | None = None,
    ):
        super().__init__(builder=builder or SquareBuilder())
        
    @property
    def builder(self) -> SquareBuilder:
        return cast(SquareBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[SquareCarrier]:
        """
        Forward a job to a SquareBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a SquareCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[SquareCarrier]
        Raises:
             SquareBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildDispatcherException.MSG,
                    err_code=SquareBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(SquareCarrier, build.payload)
        return BuildResult.success(carrier)