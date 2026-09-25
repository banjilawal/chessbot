# src/transit/dispatcher/validator/model/scalar/validator.py

"""
Module: transit.dispatcher.validator.model.scalar.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import ScalarValidator
from artifcat import ValidationResult
from domain import Scalar
from err import ScalarValidationDispatcherException
from transit import ModelValidationDispatcher, ScalarCarrier
from util import LoggingLevelRouter


class ScalarValidationDispatcher(ModelValidationDispatcher[Scalar]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the ScalarValidation workflow.

    Attributes:
        validator: ScalarValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: ScalarValidator | None = None,
    ):
        super().__init__(validator=validator or ScalarValidator())
        
    @property
    def validator(self) -> ScalarValidator:
        return cast(ScalarValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ScalarCarrier]:
        """
        Forward a job to a ScalarValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a ScalarCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[ScalarCarrier]
        Raises:
             ScalarValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationDispatcherException.MSG,
                    err_code=ScalarValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(ScalarCarrier, validation.payload)
        return ValidationResult.success(carrier)