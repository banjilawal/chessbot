# src/transit/dispatcher/validator/model/alert/validator.py

"""
Module: transit.dispatcher.validator.model.alert.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import AlertTableValidator
from artifcat import ValidationResult
from domain import AlertTable
from err import AlertTableValidationDispatcherException
from transit import ModelValidationDispatcher, AlertTableCarrier
from util import LoggingLevelRouter


class AlertTableValidationDispatcher(
    ModelValidationDispatcher[AlertTable]
):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AlertTableValidation workflow.

    Attributes:
        validator: AlertTableValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: AlertTableValidator | None = None,
    ):
        super().__init__(validator=validator or AlertTableValidator())
        
    @property
    def validator(self) -> AlertTableValidator:
        return cast(AlertTableValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[AlertTableCarrier]:
        """
        Forward a job to a AlertTableValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a AlertTableCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[AlertTableCarrier]
        Raises:
             AlertTableValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertTableValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertTableValidationDispatcherException.MSG,
                    err_code=AlertTableValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AlertTableCarrier, validation.payload)
        return ValidationResult.success(carrier)