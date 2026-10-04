# src/transit/dispatcher/validator/structure/chart/coord/validator.py

"""
Module: transit.dispatcher.validator.chart.coord.validator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from domain.structure.chart import CoordChart
from artifcat import ValidationResult
from transit import CoordChartCarrier
from util import LoggingLevelRouter
from transit.dispatcher.validator import ChartValidationDispatcher


class CoordChartValidationDispatcher(ChartValidationDispatcher[CoordChart]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a CoordChart instance is certified safe, reliable, and consistent before use.

    Attributes:
        validator: CoordChartValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult{CoordChart]

    Super Class:
        ChartValidator
    """
    
    def __init__(
            self,
            validator: CoordChartValidator | None = CoordChartValidator(),
    ):
        super().__init__(validator=validator or CoordChartValidator())
        
    @property
    def validator(self) -> CoordChartValidator:
        return cast(CoordChartValidator, super().validator)
    

    @LoggingLevelRouter.monitor
    def execute(self, job: Any) -> ValidationResult[CoordChartCarrier]:
        """
        Verify the object is a CoordChart that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate fails a
                validator test..
            2.  Otherwise, cast the payload into a CoordChart and send in the success result.
                success result.
        Args:
            job: Any
        Returns:
            ValidationResult[CoordChart]
        Raises:
             CoordChartValidationDispatcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is not safe.
        validation = self.validator.execute(job)
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordChartValidationDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordChartValidationDispatcherException.MSG,
                    err_code=CoordChartValidationDispatcherException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # --- Forward the work product to the caller. ---#
        return ValidationResult.success(
            cast(CoordChartCarrier, validation.payload)
        )