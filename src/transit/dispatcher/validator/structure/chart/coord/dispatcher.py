# src/transit/dispatcher/validator/struct/chart/walk/validator.py

"""
Module: transit.dispatcher.validator.chart.walk.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import WalkValidator
from domain.struct.chart import Walk
from artifcat import ValidationResult
from err import WalkValidationDispatcherException
from transit import WalkCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import ChartValidationDispatcher


class WalkValidationDispatcher(ChartValidationDispatcher[Walk]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a Walk instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: WalkValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{Walk]

    Super Class:
        ChartValidator
    """
    
    def __init__(
            self,
            validator: WalkValidator | None = WalkValidator(),
    ):
        super().__init__(validator=validator or WalkValidator())
        
    @property
    def validator(self) -> WalkValidator:
        return cast(WalkValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[WalkCarrier]:
        """
        Verify the object is a Walk that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a Walk and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[Walk]
        Raises:
             WalkValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WalkValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WalkValidationDispatcherException.MSG,
                    err_code=WalkValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        carrier = validation.payload
        return ValidationResult.success(
            cast(WalkCarrier, validation.payload)
        )