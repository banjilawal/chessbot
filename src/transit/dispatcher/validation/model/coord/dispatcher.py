# src/transit/dispatcher/validator/model/coord/dispatcher.py

"""
Module: transit.dispatcher.validator.model.coord.dispatcher
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast


from assurance import CoordValidator
from artifcat import ValidationResult
from domain import Coord
from err import CoordValidationDispatcherException
from transit import ValidationDispatcher, CoordCarrier
from util import LoggingLevelRouter


class CoordValidationDispatcher(ValidationDispatcher[Coord]):
    """
    Role
        -   Performance Management

    Responsibilities:
        1.  Distribute Coord validation jobs among workers, then forward their results.

    Attributes:
        validator: CoordValidator

    Provides:
        -   def execute(job: Any) -> ValidationResult[ValidatorCarrier]

    Super Class:
        ValidationDispatcher
    """

    def __init__(
            self,
            validator: Optional[CoordValidator] | None = None,
    ):
        """
        Args:
            validator: Optional[CoordValidator]
        """
        super().__init__(validator=validator or CoordValidator())
        
    @property
    def validator(self) -> CoordValidator:
        return cast(CoordValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[CoordCarrier]:
        """
        Send jobs to a CoordValidator then forward the results.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator refuses
                certification.
            2.  Otherwise, cast the job payload into a CoordCarrier and send in
                the success result.
        Args:
            job: Any
        Returns:
            ValidationResult[CoordCarrier]
        Raises:
             CoordValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff to the validator ---#
        validation = self.validator.execute(job)
        
        # Handle the case that the candidate is not safe.
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationDispatcherException.MSG,
                    err_code=CoordValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = cast(CoordCarrier, validation.payload)
        return ValidationResult.success(carrier)