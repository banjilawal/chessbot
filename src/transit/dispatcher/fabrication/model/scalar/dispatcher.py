# src/transit/dispatcher/fabrication/model/scalar/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.scalar.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import ScalarBuilder
from artifcat import BuildResult
from domain import Scalar
from err import ScalarBuildDispatcherException
from transit import ModelBuildDispatcher, ScalarCarrier
from util import LoggingLevelRouter


class ScalarBuildDispatcher(ModelBuildDispatcher[Scalar]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ScalarBuild workflow.

    Attributes:
        builder: ScalarBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: ScalarBuilder | None = None,
    ):
        super().__init__(builder=builder or ScalarBuilder())
        
    @property
    def builder(self) -> ScalarBuilder:
        return cast(ScalarBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ScalarCarrier]:
        """
        Forward a job to a ScalarBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ScalarCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[ScalarCarrier]
        Raises:
             ScalarBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ScalarBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarBuildDispatcherException.MSG,
                    err_code=ScalarBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ScalarCarrier, build.payload)
        return BuildResult.success(carrier)