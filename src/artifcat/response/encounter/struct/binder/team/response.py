# src/artifact/response/encounter/struct/binder/team/response.py

"""
Module: artifact.response.encounter.struct.binder.team.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BinderEncounterResponse, ResponseState, EncounterResult
from exchange import Request, TeamBinderEncounterRequest
from domain import TeamBinder, TeamBinderBlueprint
from transit import TeamBinderCarrier


class TeamBinderEncounterResponse(
    BinderEncounterResponse[TeamBinder]
):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a TeamBinder encounter request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: EncounterResult[TeamBinderCarrier]
        request: TeamBinderEncounterRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Team]
        -   def valid_blueprint() -> Optional[TeamBinderBlueprint]

        -   def success(
                    request: Request,
                    result: EncounterResult[TeamBinderCarrier],
            ) -> TeamBinderEncounterResponse

        -   def failure(
                    request: Request,
                    result: EncounterResult[TeamBinderCarrier],
                    exception: Exception,
            ) -> TeamBinderEncounterResponse
            
    Super Class:
        BinderEncounterResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: EncounterResult,
            request: TeamBinderEncounterRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: EncounterResult[TeamBinderCarrier]
            request: TeamBinderEncounterRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> TeamBinderEncounterRequest:
        return cast(TeamBinderEncounterRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[TeamBinder]:
        # Handle the case that the encounter failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TeamBinderCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TeamBinderCarrier)
        ):
            return None
        # Handle the case that there is no binder in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the binder. ---#
        binder = cast(TeamBinder, carrier.entity)
        # Handle the case that the binder is null or the wrong type.
        if (
                binder is None or
                not isinstance(binder, TeamBinder)
        ):
            return None
        # Finally send the success result.
        return binder
    
    @property
    def valid_blueprint(self) -> Optional[TeamBinderBlueprint]:
        # Handle the case that the encounter failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TeamBinderCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TeamBinderCarrier)
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
                not isinstance(blueprint, TeamBinderBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: EncounterResult,
    ) -> TeamBinderEncounterResponse:
        # Downcast the request into a TeamBinderEncounterRequest.
        encounter_request = cast(
            TeamBinderEncounterRequest,
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
    ) -> TeamBinderEncounterResponse:
        # Downcast the request into a TeamBinderEncounterRequest.
        encounter_request = cast(
            TeamBinderEncounterRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=encounter_request,
            state=ResponseState.FAILURE,
        )