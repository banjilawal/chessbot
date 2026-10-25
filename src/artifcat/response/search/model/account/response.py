# src/artifact/response/search/model/account/response.py

"""
Module: artifact.response.search.model.account.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchResponse, ResponseState, SearchResult
from exchange import Request, AccountSearchRequest
from domain import Account, AccountBlueprint
from transit import AccountCarrier


class AccountSearchResponse(ModelSearchResponse[Account]):
    """
    Role:
        -   Persistence

    Responsibilities:
        1.  Capture a Account search request-response cycle's data and state.

    Attributes:
        result: SearchResult[AccountCarrier],
        request: AccountSearchRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Account]
        -   def valid_blueprint() -> Optional[AccountBlueprint]

        -   def success(
                    request: Request,
                    result: SearchResult[AccountCarrier],
            ) -> AccountSearchResponse

        -   def failure(
                    request: Request,
                    result: SearchResult[AccountCarrier],
                    exception: Exception,
            ) -> AccountSearchResponse
            
    Super Class:
        ModelSearchResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: SearchResult,
            request: AccountSearchRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: SearchResult,
            request: AccountSearchRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> AccountSearchRequest:
        return cast(AccountSearchRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Account]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(AccountCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, AccountCarrier)
        ):
            return None
        # Handle the case that there is no model in the carrier.
        if not carrier.has_model:
            return None
        # --- Extract the model. ---#
        model = cast(Account, carrier.entity)
        # Handle the case that the model is null or the wrong type.
        if (
            model is None or
            not isinstance(model, Account)
        ):
            return None
        # Finally send the success result.
        return model
    
    @property
    def valid_blueprint(self) -> Optional[AccountBlueprint]:
        # Handle the case that the search failed.
        if self.result.is_failure:
            return None
        # --- Otherwise extract the carrier for additional processing. ---#
        carrier = cast(AccountCarrier, self.result.payload)
        
        # Handle the case that the carrier is null or the wrong type.
        if (
                carrier is None or
                not isinstance(carrier, AccountCarrier)
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
                not isinstance(blueprint, AccountBlueprint)
        ):
            return None
        # Finally send the success result.
        return blueprint
    
    @classmethod
    def success(
            cls,
            request: Request,
            result: SearchResult,
    ) -> AccountSearchResponse:
        
        # Downcast the request into a AccountSearchRequest.
        search_request = cast(
            AccountSearchRequest,
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
    ) -> AccountSearchResponse:
        
        # Downcast the request into a AccountSearchRequest.
        search_request = cast(
            AccountSearchRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=search_request,
            state=ResponseState.FAILURE,
        )