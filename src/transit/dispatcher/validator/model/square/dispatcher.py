# src/transit/dispatcher/validator/model/square/validator.py

"""
Module: transit.dispatcher.validator.model.square.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import SquareValidator
from artifcat import ValidationResult
from domain import Square
from err import SquareValidationDispatcherException
from transit import ModelValidationDispatcher, SquareCarrier
from util import LoggingLevelRouter


class SquareValidationDispatcher(ModelValidationDispatcher[Square]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the SquareValidation workflow.

    Attributes:
        validator: SquareValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: SquareValidator | None = None,
    ):
        super().__init__(validator=validator or SquareValidator())
        
    @property
    def validator(self) -> SquareValidator:
        return cast(SquareValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[SquareCarrier]:
        """
        Forward a job to a SquareValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
            2.  Otherwise, cast the job payload into a SquareCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[SquareCarrier]
        Raises:
             SquareValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationDispatcherException.MSG,
                    err_code=SquareValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(SquareCarrier, validation.payload)
        return ValidationResult.success(carrier)