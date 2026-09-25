# src/transit/dispatcher/validator/model/coord/validator.py

"""
Module: transit.dispatcher.validator.model.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast


from assurance import CoordValidator
from artifcat import ValidationResult
from domain import Coord
from err import CoordValidationDispatcherException
from transit import ModelValidationDispatcher, CoordCarrier
from util import LoggingLevelRouter


class CoordValidationDispatcher(ModelValidationDispatcher[Coord]):
    """
    Role
        -   Integrity Assurance Manager

    Responsibilities:
        1.  Direct the CoordValidation workflow.

    Attributes:
        validator: CoordValidator

    Provides:
        -   def execute(self, candidate: Any) -> ValidationResult[validatorCarrier]

    Super Class:
        ModelValidationDispatcher
    """

    def __init__(
            self,
            validator: CoordValidator | None = None,
    ):
        super().__init__(validator=validator or CoordValidator())
        
    @property
    def validator(self) -> CoordValidator:
        return cast(CoordValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[CoordCarrier]:
        """
        Forward a job to a CoordValidator then deliver the result.

        Action:
            1.  Send an exception chain in the ValidationResult if the validator cannot
                certify the job's content.
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
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
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