# src/artifact/response/deletion/model/player/response.py

"""
Module: artifact.response.deletion.model.player.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelDeletionResponse, ResponseState, DeletionResult
from exchange import Request, PlayerDeletionRequest
from domain import Player, PlayerBlueprint
from transit import PlayerCarrier


class PlayerDeletionResponse(ModelDeletionResponse[Player]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Player deletion request-response cycle's data and state.

    Attributes:
        result: DeletionResult[PlayerCarrier],
        request: PlayerDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Player]
        -   def valid_blueprint() -> Optional[PlayerBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[PlayerCarrier],
            ) -> PlayerDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[PlayerCarrier],
                    exception: Exception,
            ) -> PlayerDeletionResponse
            
    Super Class:
        ModelDeletionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: PlayerDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult,
            request: PlayerDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> PlayerDeletionRequest:
        return cast(PlayerDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Player]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PlayerCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PlayerCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Player, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Player)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[PlayerBlueprint]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PlayerCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PlayerCarrier)
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
                not isinstance(blueprint, PlayerBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: DeletionResult,
    ) -> PlayerDeletionResponse:
        
        # Downcast the request into a PlayerDeletionRequest.
        deletion_request = cast(
            PlayerDeletionRequest,
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
    ) -> PlayerDeletionResponse:
        
        # Downcast the request into a PlayerDeletionRequest.
        deletion_request = cast(
            PlayerDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )