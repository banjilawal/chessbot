# src/transit/dispatcher/validator/model/encounter/dispatcher.py

"""
Module: transit.dispatcher.validator.model.encounter.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import EncounterValidator
from artifcat import ValidationResult
from domain import Encounter
from err import EncounterValidationDispatcherException
from transit import ValidationDispatcher, EncounterCarrier
from util import LoggingLevelRouter


class EncounterValidationDispatcher(ValidationDispatcher[Encounter]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Encounter validation jobs among workers, then forward their results.

    Attributes:
        validator: EncounterValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[EncounterValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[EncounterValidator]
        """
        super().__init__(validator=validator or EncounterValidator())
        
    @property
    def validator(self) -> EncounterValidator:
        return cast(EncounterValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[EncounterCarrier]:
        """
        Send jobs to a EncounterValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a EncounterCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[EncounterCarrier]
        Raises:
             EncounterValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                EncounterValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterValidationDispatcherException.MSG,
                    err_code=EncounterValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(EncounterCarrier, validation.payload)
        return ValidationResult.success(carrier)