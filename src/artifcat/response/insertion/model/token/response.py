# src/artifact/response/insertion/model/token/response.py

"""
Module: artifact.response.insertion.model.token.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, TokenInsertionRequest
from domain import Token, TokenBlueprint
from transit import TokenCarrier


class TokenInsertionResponse(ModelInsertionResponse[Token]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Token insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[TokenCarrier],
        request: TokenInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Token]
        -   def valid_blueprint() -> Optional[TokenBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[TokenCarrier],
            ) -> TokenInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[TokenCarrier],
                    exception: Exception,
            ) -> TokenInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: TokenInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: TokenInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> TokenInsertionRequest:
        return cast(TokenInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Token]:
        # Handle the case that the insertion failed.
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
        # Handle the case that the insertion failed.
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
            result: InsertionResult,
    ) -> TokenInsertionResponse:
        
        # Downcast the request into a TokenInsertionRequest.
        insertion_request = cast(
            TokenInsertionRequest,
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
    ) -> TokenInsertionResponse:
        
        # Downcast the request into a TokenInsertionRequest.
        insertion_request = cast(
            TokenInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )