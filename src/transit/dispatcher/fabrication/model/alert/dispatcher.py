# src/transit/dispatcher/fabrication/model/alert/validator.py

"""
Module: transit.dispatcher.fabrication.model.alert.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import AlertValidator
from artifcat import BuildResult
from domain import Alert
from err import AlertBuildDispatcherException
from transit import ModelBuildDispatcher, AlertCarrier
from util import LoggingLevelRouter


class AlertBuildDispatcher(
    ModelBuildDispatcher[Alert]
):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AlertBuild workflow.

    Attributes:
        validator: AlertValidator

    Provides:
        -   def execute(self, candidate: Any) -> BuildResult[validatorCarrier]

    Super Class:
        ModelBuildDispatcher
    """

    def __init__(
            self,
            validator: AlertValidator | None = None,
    ):
        super().__init__(validator=validator or AlertValidator())
        
    @property
    def validator(self) -> AlertValidator:
        return cast(AlertValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> BuildResult[AlertCarrier]:
        """
        Forward a job to a AlertValidator then deliver the result.

        Action:
            1.  Send an exception chain in the BuildResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a AlertCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            BuildResult[AlertCarrier]
        Raises:
             AlertBuildDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        build = self.validator.execute(job)
        if build.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                AlertBuildDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertBuildDispatcherException.MSG,
                    err_code=AlertBuildDispatcherException.ERR_CODE,
                    ex=build.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AlertCarrier, build.payload)
        return BuildResult.success(carrier)