# src/artifact/response/validation/struct/chart/coord/response.py

"""
Module: artifact.response.validation.struct.chart.coord.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ChartValidationResponse, ResponseState, ValidationResult
from exchange import Request, CoordChartValidationRequest
from domain import CoordChart, CoordChartBlueprint
from transit import CoordChartCarrier


class CoordChartValidationResponse(
    ChartValidationResponse[CoordChart]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a CoordChart validation request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: ValidationResult[CoordChartCarrier]
        request: CoordChartValidationRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Coord]
        -   def valid_blueprint() -> Optional[CoordChartBlueprint]

        -   def success(
                    request: Request,
                    result: ValidationResult[CoordChartCarrier],
            ) -> CoordChartValidationResponse

        -   def failure(
                    request: Request,
                    result: ValidationResult[CoordChartCarrier],
                    exception: Exception,
            ) -> CoordChartValidationResponse
            
    Super Class:
        ChartValidationResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: ValidationResult,
            request: CoordChartValidationRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: ValidationResult[CoordChartCarrier]
            request: CoordChartValidationRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> CoordChartValidationRequest:
        return cast(CoordChartValidationRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[CoordChart]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(CoordChartCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, CoordChartCarrier)
        ):
            return None
        # Handle the case that there is no chart in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the chart. ---#
        chart = cast(CoordChart, carrier.entity)
        # Handle the case that the chart is null or the wrong type.
        if (
                chart is None or
                not isinstance(chart, CoordChart)
        ):
            return None
        # Finally send the success result.
        return chart
    
    @property
    def valid_blueprint(self) -> Optional[CoordChartBlueprint]:
        # Handle the case that the validation failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(CoordChartCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, CoordChartCarrier)
        ):
            return None
        # Handle the case that there is no blueprint in the carrier.
        if not carrier.has_blueprint:
            return None
        # --- Extract the blueprint. ---#
        blueprint = carrier.extract_blueprint()
        # Handle the case that the blueprint is null or the wrong type.
        if (
                blueprint is None or
                not isinstance(blueprint, CoordChartBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: ValidationResult,
    ) -> CoordChartValidationResponse:
        # Downcast the request into a CoordChartValidationRequest.
        validation_request = cast(
            CoordChartValidationRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=validation_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: ValidationResult,
            exception: Exception,
    ) -> CoordChartValidationResponse:
        # Downcast the request into a CoordChartValidationRequest.
        validation_request = cast(
            CoordChartValidationRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=validation_request,
            state=ResponseState.FAILURE,
        )