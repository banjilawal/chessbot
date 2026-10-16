# src/transit/dispatcher/fabrication/model/path/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.path.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import PathBuilder
from artifcat import BuildResult
from domain import Path
from err import PathBuildDispatcherException
from transit import ModelBuildDispatcher, PathCarrier
from util import LoggingLevelRouter


class PathBuildDispatcher(ModelBuildDispatcher[Path]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the PathBuild workflow.

    Attributes:
        builder: PathBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: PathBuilder | None = None,
    ):
        super().__init__(builder=builder or PathBuilder())
        
    @property
    def builder(self) -> PathBuilder:
        return cast(PathBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[PathCarrier]:
        """
        Forward a job to a PathBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a PathCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[PathCarrier]
        Raises:
             PathBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                PathBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathBuildDispatcherException.MSG,
                    err_code=PathBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(PathCarrier, build.payload)
        return BuildResult.success(carrier)