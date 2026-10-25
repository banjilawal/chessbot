# src/artifact/response/search/model/player/response.py

"""
Module: artifact.response.search.model.player.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchResponse, ResponseState, SearchResult
from exchange import Request, PlayerSearchRequest
from domain import Player, PlayerBlueprint
from transit import PlayerCarrier


class PlayerSearchResponse(ModelSearchResponse[Player]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Player search request-response cycle's data and state.

    Attributes:
        result: SearchResult[PlayerCarrier],
        request: PlayerSearchRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Player]
        -   def valid_blueprint() -> Optional[PlayerBlueprint]

        -   def success(
                    request: Request,
                    result: SearchResult[PlayerCarrier],
            ) -> PlayerSearchResponse

        -   def failure(
                    request: Request,
                    result: SearchResult[PlayerCarrier],
                    exception: Exception,
            ) -> PlayerSearchResponse
            
    Super Class:
        ModelSearchResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: PlayerSearchRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: PlayerSearchRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> PlayerSearchRequest:
        return cast(PlayerSearchRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Player]:
        # Handle the case that the search failed.
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
        # Handle the case that the search failed.
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
            result: SearchResult,
    ) -> PlayerSearchResponse:
        
        # Downcast the request into a PlayerSearchRequest.
        search_request = cast(
            PlayerSearchRequest,
            request,
        )
        # Send a success Response using the cast.
        return cls(
            result=result,
            request=search_request,
            state=ResponseState.SUCCESS,
        )
    
    @classmethod
    def failure(
            cls,
            request: Request,
            result: SearchResult,
            exception: Exception,
    ) -> PlayerSearchResponse:
        
        # Downcast the request into a PlayerSearchRequest.
        search_request = cast(
            PlayerSearchRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )