# src/transit/dispatcher/validator/model/attack/validator.py

"""
Module: transit.dispatcher.validator.model.attack.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import AttackValidator
from artifcat import ValidationResult
from domain import Attack
from err import AttackValidationDispatcherException
from transit import ModelValidationDispatcher, AttackCarrier
from util import LoggingLevelRouter


class AttackValidationDispatcher(ModelValidationDispatcher[Attack]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the AttackValidation workflow.

    Attributes:
        validator: AttackValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: AttackValidator | None = None,
    ):
        super().__init__(validator=validator or AttackValidator())
        
    @property
    def validator(self) -> AttackValidator:
        return cast(AttackValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[AttackCarrier]:
        """
        Forward a job to a AttackValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a AttackCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[AttackCarrier]
        Raises:
             AttackValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationDispatcherException.MSG,
                    err_code=AttackValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(AttackCarrier, validation.payload)
        return ValidationResult.success(carrier)