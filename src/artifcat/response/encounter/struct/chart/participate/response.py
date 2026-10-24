# src/artifact/response/encounter/struct/chart/participate/response.py

"""
Module: artifact.response.encounter.struct.chart.participate.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ChartEncounterResponse, ResponseState, EncounterResult
from exchange import Request, FootstepEncounterRequest
from domain import Participation, ParticipationBlueprint
from transit import ParticipationCarrier


class ParticipationEncounterResponse(
    ChartEncounterResponse[Participation]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Participation encounter request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: EncounterResult[ParticipationCarrier]
        request: ParticipationEncounterRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Token]
        -   def valid_blueprint() -> Optional[ParticipationBlueprint]

        -   def success(
                    request: Request,
                    result: EncounterResult[ParticipationCarrier],
            ) -> ParticipationEncounterResponse

        -   def failure(
                    request: Request,
                    result: EncounterResult[ParticipationCarrier],
                    exception: Exception,
            ) -> ParticipationEncounterResponse
            
    Super Class:
        ChartEncounterResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: EncounterResult,
            request: FootstepEncounterRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: EncounterResult[ParticipationCarrier]
            request: ParticipationEncounterRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> FootstepEncounterRequest:
        return cast(FootstepEncounterRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Participation]:
        # Handle the case that the encounter failed.
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
        # Handle the case that the encounter failed.
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
            result: EncounterResult,
    ) -> ParticipationEncounterResponse:
        # Downcast the request into a ParticipationEncounterRequest.
        encounter_request = cast(
            FootstepEncounterRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=encounter_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: EncounterResult,
            exception: Exception,
    ) -> ParticipationEncounterResponse:
        # Downcast the request into a ParticipationEncounterRequest.
        encounter_request = cast(
            FootstepEncounterRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=encounter_request,
            state=ResponseState.FAILURE,
        )