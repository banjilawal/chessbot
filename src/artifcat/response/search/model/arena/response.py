# src/artifact/response/search/model/arena/response.py

"""
Module: artifact.response.search.model.arena.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchResponse, ResponseState, SearchResult
from exchange import Request, ArenaSearchRequest
from domain import Arena, ArenaBlueprint
from transit import ArenaCarrier


class ArenaSearchResponse(ModelSearchResponse[Arena]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Arena search request-response cycle's data and state.

    Attributes:
        result: SearchResult[ArenaCarrier],
        request: ArenaSearchRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Arena]
        -   def valid_blueprint() -> Optional[ArenaBlueprint]

        -   def success(
                    request: Request,
                    result: SearchResult[ArenaCarrier],
            ) -> ArenaSearchResponse

        -   def failure(
                    request: Request,
                    result: SearchResult[ArenaCarrier],
                    exception: Exception,
            ) -> ArenaSearchResponse
            
    Super Class:
        ModelSearchResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: ArenaSearchRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: ArenaSearchRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> ArenaSearchRequest:
        return cast(ArenaSearchRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Arena]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ArenaCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ArenaCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Arena, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Arena)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[ArenaBlueprint]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(ArenaCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, ArenaCarrier)
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
                not isinstance(blueprint, ArenaBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> ArenaSearchResponse:
        
        # Downcast the request into a ArenaSearchRequest.
        search_request = cast(
            ArenaSearchRequest,
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
    ) -> ArenaSearchResponse:
        
        # Downcast the request into a ArenaSearchRequest.
        search_request = cast(
            ArenaSearchRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )