# src/transit/dispatcher/validator/model/encounter/validator.py

"""
Module: transit.dispatcher.validator.model.encounter.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import EncounterValidator
from artifcat import ValidationResult
from domain import Encounter
from err import EncounterValidationDispatcherException
from transit import ModelValidationDispatcher, EncounterCarrier
from util import LoggingLevelRouter


class EncounterValidationDispatcher(ModelValidationDispatcher[Encounter]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the EncounterValidation workflow.

    Attributes:
        validator: EncounterValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: EncounterValidator | None = None,
    ):
        super().__init__(validator=validator or EncounterValidator())
        
    @property
    def validator(self) -> EncounterValidator:
        return cast(EncounterValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[EncounterCarrier]:
        """
        Forward a job to a EncounterValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
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
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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