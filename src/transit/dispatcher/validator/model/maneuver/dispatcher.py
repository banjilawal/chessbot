# src/transit/dispatcher/validator/model/maneuver/validator.py

"""
Module: transit.dispatcher.validator.model.maneuver.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import ManeuverValidator
from artifcat import ValidationResult
from domain import Maneuver
from err import ManeuverValidationDispatcherException
from transit import ModelValidationDispatcher, ManeuverCarrier
from util import LoggingLevelRouter


class ManeuverValidationDispatcher(ModelValidationDispatcher[Maneuver]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ManeuverValidation workflow.

    Attributes:
        validator: ManeuverValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
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
    def execute(self, job: Any) -> ValidationResult[ManeuverCarrier]:
        """
        Forward a job to a ManeuverValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ManeuverCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[ManeuverCarrier]
        Raises:
             ManeuverValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationDispatcherException.MSG,
                    err_code=ManeuverValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ManeuverCarrier, validation.payload)
        return ValidationResult.success(carrier)