# src/transit/dispatcher/validator/model/alert/validator.py

"""
Module: transit.dispatcher.validator.model.alert.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import AlertValidator
from artifcat import ValidationResult
from domain import Alert
from err import AlertValidationDispatcherException
from transit import ModelValidationDispatcher, AlertCarrier
from util import LoggingLevelRouter


class AlertValidationDispatcher(
    ModelValidationDispatcher[Alert]
):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AlertValidation workflow.

    Attributes:
        validator: AlertValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
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
    def execute(self, job: Any) -> ValidationResult[AlertCarrier]:
        """
        Forward a job to a AlertValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a AlertCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[AlertCarrier]
        Raises:
             AlertValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AlertValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AlertValidationDispatcherException.MSG,
                    err_code=AlertValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AlertCarrier, validation.payload)
        return ValidationResult.success(carrier)