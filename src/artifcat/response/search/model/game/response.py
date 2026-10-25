# src/artifact/response/search/model/game/response.py

"""
Module: artifact.response.search.model.game.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchResponse, ResponseState, SearchResult
from exchange import Request, GameSearchRequest
from domain import Game, GameBlueprint
from transit import GameCarrier


class GameSearchResponse(ModelSearchResponse[Game]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Game search request-response cycle's data and state.

    Attributes:
        result: SearchResult[GameCarrier],
        request: GameSearchRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Game]
        -   def valid_blueprint() -> Optional[GameBlueprint]

        -   def success(
                    request: Request,
                    result: SearchResult[GameCarrier],
            ) -> GameSearchResponse

        -   def failure(
                    request: Request,
                    result: SearchResult[GameCarrier],
                    exception: Exception,
            ) -> GameSearchResponse
            
    Super Class:
        ModelSearchResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: GameSearchRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: GameSearchRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> GameSearchRequest:
        return cast(GameSearchRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Game]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(GameCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, GameCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Game, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Game)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[GameBlueprint]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(GameCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, GameCarrier)
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
                not isinstance(blueprint, GameBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> GameSearchResponse:
        
        # Downcast the request into a GameSearchRequest.
        search_request = cast(
            GameSearchRequest,
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
    ) -> GameSearchResponse:
        
        # Downcast the request into a GameSearchRequest.
        search_request = cast(
            GameSearchRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )