# src/transit/dispatcher/fabrication/model/arena/validator.py

"""
Module: transit.dispatcher.fabrication.model.arena.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import ArenaValidator
from artifcat import BuildResult
from domain import Arena
from err import ArenaBuildDispatcherException
from transit import ModelBuildDispatcher, ArenaCarrier
from util import LoggingLevelRouter


class ArenaBuildDispatcher(ModelBuildDispatcher[Arena]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ArenaBuild workflow.

    Attributes:
        validator: ArenaValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: ArenaValidator | None = None,
    ):
        super().__init__(validator=validator or ArenaValidator())
        
    @property
    def validator(self) -> ArenaValidator:
        return cast(ArenaValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ArenaCarrier]:
        """
        Forward a job to a ArenaValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ArenaCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[ArenaCarrier]
        Raises:
             ArenaBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ArenaBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuildDispatcherException.MSG,
                    err_code=ArenaBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ArenaCarrier, build.payload)
        return BuildResult.success(carrier)