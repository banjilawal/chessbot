# src/transit/dispatcher/fabrication/model/vector/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.vector.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from fabrication import VectorBuilder
from artifcat import BuildResult
from domain import Vector
from err import VectorBuildDispatcherException
from request import VectorBuildRequest
from transit import ModelBuildDispatcher, VectorCarrier
from util import LoggingLevelRouter


class VectorBuildDispatcher(ModelBuildDispatcher[Vector]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the VectorBuild workflow.

    Attributes:
        builder: VectorBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            worker: Optional[VectorBuilder] | None = None,
    ):
        super().__init__(worker=worker or VectorBuilder())
        
    @property
    def worker(self) -> VectorBuilder:
        return cast(VectorBuilder, super().worker)
    

    @LoggingLevelRouter.monitor
    def execute(self, request: VectorBuildRequest) -> BuildResult[Vector]:
        """
        Forward a job to a VectorBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a VectorCarrier and send in
                the success result.
        Args:
            request: Any
        Returns:
            BuildResult[VectorCarrier]
        Raises:
             VectorBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(request)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuildDispatcherException.MSG,
                    err_code=VectorBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(VectorCarrier, build.payload)
        return BuildResult.success(carrier)