# src/transit/dispatcher/fabrication/model/coord/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.coord.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import CoordBuilder
from artifcat import BuildResult
from domain import Coord
from err import CoordBuildDispatcherException
from transit import ModelBuildDispatcher, CoordCarrier
from util import LoggingLevelRouter


class CoordBuildDispatcher(ModelBuildDispatcher[Coord]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the CoordBuild workflow.

    Attributes:
        builder: CoordBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: CoordBuilder | None = None,
    ):
        super().__init__(builder=builder or CoordBuilder())
        
    @property
    def builder(self) -> CoordBuilder:
        return cast(CoordBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[CoordCarrier]:
        """
        Forward a job to a CoordBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a CoordCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[CoordCarrier]
        Raises:
             CoordBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CoordBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuildDispatcherException.MSG,
                    err_code=CoordBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(CoordCarrier, build.payload)
        return BuildResult.success(carrier)