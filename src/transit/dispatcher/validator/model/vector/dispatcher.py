# src/transit/dispatcher/validator/model/vector/validator.py

"""
Module: transit.dispatcher.validator.model.vector.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import VectorValidator
from artifcat import ValidationResult
from domain import Vector
from err import VectorValidationDispatcherException
from transit import ModelValidationDispatcher, VectorCarrier
from util import LoggingLevelRouter


class VectorValidationDispatcher(ModelValidationDispatcher[Vector]):
    """
    Role
        -   Transport
        -   Forwarding
        -   Integrity Assurance

    Responsibilities:
        1.  Direct the VectorValidation workflow.
        1.  Forward requests to a VectorValidator.
        2.  Send the ValidationResult back to the caller.

    Attributes:
        validator: VectorValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: VectorValidator | None = None,
    ):
        super().__init__(validator=validator or VectorValidator())
        
    @property
    def validator(self) -> VectorValidator:
        return cast(VectorValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[VectorCarrier]:
        """
        Forward a job to a VectorValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
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
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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