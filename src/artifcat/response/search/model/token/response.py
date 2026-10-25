# src/artifact/response/search/model/token/response.py

"""
Module: artifact.response.search.model.token.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchResponse, ResponseState, SearchResult
from exchange import Request, TokenSearchRequest
from domain import Token, TokenBlueprint
from transit import TokenCarrier


class TokenSearchResponse(ModelSearchResponse[Token]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Token search request-response cycle's data and state.

    Attributes:
        result: SearchResult[TokenCarrier],
        request: TokenSearchRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Token]
        -   def valid_blueprint() -> Optional[TokenBlueprint]

        -   def success(
                    request: Request,
                    result: SearchResult[TokenCarrier],
            ) -> TokenSearchResponse

        -   def failure(
                    request: Request,
                    result: SearchResult[TokenCarrier],
                    exception: Exception,
            ) -> TokenSearchResponse
            
    Super Class:
        ModelSearchResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: TokenSearchRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: TokenSearchRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> TokenSearchRequest:
        return cast(TokenSearchRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Token]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TokenCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TokenCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Token, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Token)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[TokenBlueprint]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(TokenCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, TokenCarrier)
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
                not isinstance(blueprint, TokenBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> TokenSearchResponse:
        
        # Downcast the request into a TokenSearchRequest.
        search_request = cast(
            TokenSearchRequest,
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
    ) -> TokenSearchResponse:
        
        # Downcast the request into a TokenSearchRequest.
        search_request = cast(
            TokenSearchRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )