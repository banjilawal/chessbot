# src/artifact/response/insertion/struct/chart/participate/response.py

"""
Module: artifact.response.insertion.struct.chart.participate.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ChartInsertionResponse, ResponseState, InsertionResult
from exchange import Request, FootstepInsertionRequest
from domain import Participation, ParticipationBlueprint
from transit import ParticipationCarrier


class ParticipationInsertionResponse(
    ChartInsertionResponse[Participation]
):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Participation insertion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: InsertionResult[ParticipationCarrier]
        request: ParticipationInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Token]
        -   def valid_blueprint() -> Optional[ParticipationBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[ParticipationCarrier],
            ) -> ParticipationInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[ParticipationCarrier],
                    exception: Exception,
            ) -> ParticipationInsertionResponse
            
    Super Class:
        ChartInsertionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: FootstepInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult[ParticipationCarrier]
            request: ParticipationInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> FootstepInsertionRequest:
        return cast(FootstepInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Participation]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ParticipationCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ParticipationCarrier)
        ):
            return None
        # Handle the case that there is no chart in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the chart. ---#
        chart = cast(Participation, carrier.entity)
        # Handle the case that the chart is null or the wrong type.
        if (
                chart is None or
                not isinstance(chart, Participation)
        ):
            return None
        # Finally send the success result.
        return chart
    
    @property
    def valid_blueprint(self) -> Optional[ParticipationBlueprint]:
        # Handle the case that the insertion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ParticipationCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ParticipationCarrier)
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
                not isinstance(blueprint, ParticipationBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: InsertionResult,
    ) -> ParticipationInsertionResponse:
        # Downcast the request into a ParticipationInsertionRequest.
        insertion_request = cast(
            FootstepInsertionRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=insertion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: InsertionResult,
            exception: Exception,
    ) -> ParticipationInsertionResponse:
        # Downcast the request into a ParticipationInsertionRequest.
        insertion_request = cast(
            FootstepInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )