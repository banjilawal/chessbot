# src/transit/dispatcher/validator/model/vector/dispatcher.py

"""
Module: transit.dispatcher.validator.model.vector.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import VectorValidator
from artifcat import ValidationResult
from domain import Vector
from err import VectorValidationDispatcherException
from transit import ValidationDispatcher, VectorCarrier
from util import LoggingLevelRouter


class VectorValidationDispatcher(ValidationDispatcher[Vector]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Vector validation jobs among workers, then forward their results.

    Attributes:
        validator: VectorValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[VectorValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[VectorValidator]
        """
        super().__init__(validator=validator or VectorValidator())
        
    @property
    def validator(self) -> VectorValidator:
        return cast(VectorValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[VectorCarrier]:
        """
        Send jobs to a VectorValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a VectorCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[VectorCarrier]
        Raises:
             VectorValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationDispatcherException.MSG,
                    err_code=VectorValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(VectorCarrier, validation.payload)
        return ValidationResult.success(carrier)