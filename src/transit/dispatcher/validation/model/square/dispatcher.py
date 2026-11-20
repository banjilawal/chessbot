# src/transit/dispatcher/validator/model/square/dispatcher.py

"""
Module: transit.dispatcher.validator.model.square.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import SquareValidator
from artifcat import ValidationResult
from domain import Square
from err import SquareValidationDispatcherException
from transit import ValidationDispatcher, SquareCarrier
from util import LoggingLevelRouter


class SquareValidationDispatcher(ValidationDispatcher[Square]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Square validation jobs among workers, then forward their results.

    Attributes:
        validator: SquareValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[SquareValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[SquareValidator]
        """
        super().__init__(validator=validator or SquareValidator())
        
    @property
    def validator(self) -> SquareValidator:
        return cast(SquareValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[SquareCarrier]:
        """
        Send jobs to a SquareValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
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
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
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