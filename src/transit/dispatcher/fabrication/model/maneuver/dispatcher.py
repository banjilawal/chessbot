# src/transit/dispatcher/fabrication/model/maneuver/validator.py

"""
Module: transit.dispatcher.fabrication.model.maneuver.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import ManeuverValidator
from artifcat import BuildResult
from domain import Maneuver
from err import ManeuverBuildDispatcherException
from transit import ModelBuildDispatcher, ManeuverCarrier
from util import LoggingLevelRouter


class ManeuverBuildDispatcher(ModelBuildDispatcher[Maneuver]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ManeuverBuild workflow.

    Attributes:
        validator: ManeuverValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: ManeuverValidator | None = None,
    ):
        super().__init__(validator=validator or ManeuverValidator())
        
    @property
    def validator(self) -> ManeuverValidator:
        return cast(ManeuverValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[ManeuverCarrier]:
        """
        Forward a job to a ManeuverValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ManeuverCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[ManeuverCarrier]
        Raises:
             ManeuverBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ManeuverBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverBuildDispatcherException.MSG,
                    err_code=ManeuverBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ManeuverCarrier, build.payload)
        return BuildResult.success(carrier)