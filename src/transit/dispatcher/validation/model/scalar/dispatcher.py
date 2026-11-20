# src/transit/dispatcher/validator/model/scalar/dispatcher.py

"""
Module: transit.dispatcher.validator.model.scalar.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import ScalarValidator
from artifcat import ValidationResult
from domain import Scalar
from err import ScalarValidationDispatcherException
from transit import ValidationDispatcher, ScalarCarrier
from util import LoggingLevelRouter


class ScalarValidationDispatcher(ValidationDispatcher[Scalar]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Scalar validation jobs among workers, then forward their results.

    Attributes:
        validator: ScalarValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[ScalarValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[ScalarValidator]
        """
        super().__init__(validator=validator or ScalarValidator())
        
    @property
    def validator(self) -> ScalarValidator:
        return cast(ScalarValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ScalarCarrier]:
        """
        Send jobs to a ScalarValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
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
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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