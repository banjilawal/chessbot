# src/transit/dispatcher/validator/struct/chart/participate/validator.py

"""
Module: transit.dispatcher.validator.chart.participate.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ValidationResult
from assurance import ParticipationValidator
from domain import Participation
from err import ParticipationValidationDispatcherException
from transit import ChartValidationDispatcher, ParticipationCarrier
from util import LoggingLevelRouter


class ParticipationValidationDispatcher(ChartValidationDispatcher[Participation]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Participation instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: ParticipationValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{Participation]

    Super Class:
        ChartValidator
    """
    
    def __init__(
            self,
            validator: ParticipationValidator | None = None,
    ):
        super().__init__(validator=validator or ParticipationValidator())
        
    @property
    def validator(self) -> ParticipationValidator:
        return cast(ParticipationValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[ParticipationCarrier]:
        """
        Verify the object is a Participation that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a Participation and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[Participation]
        Raises:
             ParticipationValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ParticipationValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ParticipationValidationDispatcherException.MSG,
                    err_code=ParticipationValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(ParticipationCarrier, validation.payload)
        )