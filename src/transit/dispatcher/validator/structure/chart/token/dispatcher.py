# src/transit/dispatcher/validator/struct/chart/token/validator.py

"""
Module: transit.dispatcher.validator.chart.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from assurance import TokenChartValidator
from domain.struct.chart import TokenChart
from artifcat import ValidationResult
from transit import TokenChartCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import ChartValidationDispatcher


class TokenChartValidationDispatcher(ChartValidationDispatcher[TokenChart]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenChart instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: TokenChartValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{TokenChart]

    Super Class:
        ChartValidator
    """
    
    def __init__(
            self,
            validator: TokenChartValidator | None = TokenChartValidator(),
    ):
        super().__init__(validator=validator or TokenChartValidator())
        
    @property
    def validator(self) -> TokenChartValidator:
        return cast(TokenChartValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[TokenChartCarrier]:
        """
        Verify the object is a TokenChart that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a TokenChart and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[TokenChart]
        Raises:
             TokenChartValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenChartValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenChartValidationDispatcherException.MSG,
                    err_code=TokenChartValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(TokenChartCarrier, validation.payload)
        )