# src/artifact/response/deletion/model/team/response.py

"""
Module: artifact.response.deletion.model.team.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelDeletionResponse, ResponseState, DeletionResult
from exchange import Request, TeamDeletionRequest
from domain import Team, TeamBlueprint
from transit import TeamCarrier


class TeamDeletionResponse(ModelDeletionResponse[Team]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Team deletion request-response cycle's data and state.

    Attributes:
        result: DeletionResult[TeamCarrier],
        request: TeamDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Team]
        -   def valid_blueprint() -> Optional[TeamBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[TeamCarrier],
            ) -> TeamDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[TeamCarrier],
                    exception: Exception,
            ) -> TeamDeletionResponse
            
    Super Class:
        ModelDeletionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: TeamDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult,
            request: TeamDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> TeamDeletionRequest:
        return cast(TeamDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Team]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TeamCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TeamCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Team, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Team)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[TeamBlueprint]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TeamCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TeamCarrier)
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
                not isinstance(blueprint, TeamBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: DeletionResult,
    ) -> TeamDeletionResponse:
        
        # Downcast the request into a TeamDeletionRequest.
        deletion_request = cast(
            TeamDeletionRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=deletion_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: DeletionResult,
            exception: Exception,
    ) -> TeamDeletionResponse:
        
        # Downcast the request into a TeamDeletionRequest.
        deletion_request = cast(
            TeamDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )