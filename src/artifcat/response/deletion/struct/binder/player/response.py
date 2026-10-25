# src/artifact/response/deletion/struct/binder/player/response.py

"""
Module: artifact.response.deletion.struct.binder.player.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BinderDeletionResponse, ResponseState, DeletionResult
from exchange import Request, PlayerBinderDeletionRequest
from domain import PlayerBinder, PlayerBinderBlueprint
from transit import PlayerBinderCarrier


class PlayerBinderDeletionResponse(
    BinderDeletionResponse[PlayerBinder]
):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a PlayerBinder deletion request-response cycle's data and state.

    Attributes:
        state: ResponseState
        result: DeletionResult[PlayerBinderCarrier]
        request: PlayerBinderDeletionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Player]
        -   def valid_blueprint() -> Optional[PlayerBinderBlueprint]

        -   def success(
                    request: Request,
                    result: DeletionResult[PlayerBinderCarrier],
            ) -> PlayerBinderDeletionResponse

        -   def failure(
                    request: Request,
                    result: DeletionResult[PlayerBinderCarrier],
                    exception: Exception,
            ) -> PlayerBinderDeletionResponse
            
    Super Class:
        BinderDeletionResponse
    """
    
    def __init__(
            self,
            state: ResponseState,
            result: DeletionResult,
            request: PlayerBinderDeletionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: DeletionResult[PlayerBinderCarrier]
            request: PlayerBinderDeletionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
    
    @property
    def request(self) -> PlayerBinderDeletionRequest:
        return cast(PlayerBinderDeletionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[PlayerBinder]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PlayerBinderCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PlayerBinderCarrier)
        ):
            return None
        # Handle the case that there is no binder in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the binder. ---#
        binder = cast(PlayerBinder, carrier.entity)
        # Handle the case that the binder is null or the wrong type.
        if (
                binder is None or
                not isinstance(binder, PlayerBinder)
        ):
            return None
        # Finally send the success result.
        return binder
    
    @property
    def valid_blueprint(self) -> Optional[PlayerBinderBlueprint]:
        # Handle the case that the deletion failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(PlayerBinderCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, PlayerBinderCarrier)
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
                not isinstance(blueprint, PlayerBinderBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: DeletionResult,
    ) -> PlayerBinderDeletionResponse:
        # Downcast the request into a PlayerBinderDeletionRequest.
        deletion_request = cast(
            PlayerBinderDeletionRequest,
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
    ) -> PlayerBinderDeletionResponse:
        # Downcast the request into a PlayerBinderDeletionRequest.
        deletion_request = cast(
            PlayerBinderDeletionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=deletion_request,
            state=ResponseState.FAILURE,
        )