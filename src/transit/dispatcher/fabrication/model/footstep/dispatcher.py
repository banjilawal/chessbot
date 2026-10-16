# src/transit/dispatcher/fabrication/model/footstep/validator.py

"""
Module: transit.dispatcher.fabrication.model.footstep.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import FootstepValidator
from artifcat import BuildResult
from domain import Footstep
from err import FootstepBuildDispatcherException
from transit import ModelBuildDispatcher, FootstepCarrier
from util import LoggingLevelRouter


class FootstepBuildDispatcher(ModelBuildDispatcher[Footstep]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Footstep instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: FootstepValidator

    Provides:
        -   def execute(candidate: Any) -> BuildResult{Footstep]

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            validator: FootstepValidator | None = FootstepValidator(),
    ):
        super().__init__(validator=validator or FootstepValidator())
        
    @property
    def validator(self) -> FootstepValidator:
        return cast(FootstepValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[FootstepCarrier]:
        """
        Verify the object is a Footstep that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a Footstep and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            BuildResult[Footstep]
        Raises:
             FootstepBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                FootstepBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepBuildDispatcherException.MSG,
                    err_code=FootstepBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return BuildResult.success(
            cast(FootstepCarrier, build.payload)
        )