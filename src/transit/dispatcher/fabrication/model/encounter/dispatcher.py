# src/transit/dispatcher/fabrication/model/encounter/dispatcher.py

"""
Module: transit.dispatcher.fabrication.model.encounter.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from fabrication import EncounterBuilder
from artifcat import BuildResult
from domain import Encounter
from err import EncounterBuildDispatcherException
from transit import ModelBuildDispatcher, EncounterCarrier
from util import LoggingLevelRouter


class EncounterBuildDispatcher(ModelBuildDispatcher[Encounter]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the EncounterBuild workflow.

    Attributes:
        builder: EncounterBuilder

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[builderCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            builder: EncounterBuilder | None = None,
    ):
        super().__init__(builder=builder or EncounterBuilder())
        
    @property
    def builder(self) -> EncounterBuilder:
        return cast(EncounterBuilder, super().builder)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[EncounterCarrier]:
        """
        Forward a job to a EncounterBuilder then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the builder cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a EncounterCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[EncounterCarrier]
        Raises:
             EncounterBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.builder.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EncounterBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuildDispatcherException.MSG,
                    err_code=EncounterBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(EncounterCarrier, build.payload)
        return BuildResult.success(carrier)