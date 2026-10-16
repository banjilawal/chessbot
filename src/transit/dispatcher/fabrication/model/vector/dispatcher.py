# src/transit/dispatcher/fabrication/model/vector/validator.py

"""
Module: transit.dispatcher.fabrication.model.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import VectorValidator
from artifcat import BuildResult
from domain import Vector
from err import VectorBuildDispatcherException
from transit import ModelBuildDispatcher, VectorCarrier
from util import LoggingLevelRouter


class VectorBuildDispatcher(ModelBuildDispatcher[Vector]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the VectorBuild workflow.

    Attributes:
        validator: VectorValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: VectorValidator | None = None,
    ):
        super().__init__(validator=validator or VectorValidator())
        
    @property
    def validator(self) -> VectorValidator:
        return cast(VectorValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[VectorCarrier]:
        """
        Forward a job to a VectorValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a VectorCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[VectorCarrier]
        Raises:
             VectorBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
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