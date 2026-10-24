# src/artifact/response/insertion/model/account/response.py

"""
Module: artifact.response.insertion.model.account.response
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelInsertionResponse, ResponseState, InsertionResult
from exchange import Request, AccountInsertionRequest
from domain import Account, AccountBlueprint
from transit import AccountCarrier


class AccountInsertionResponse(ModelInsertionResponse[Account]):
    """
    Role
        -   Messaging

    Responsibilities:
        1.  Capture a Account insertion request-response cycle's data and state.

    Attributes:
        result: InsertionResult[AccountCarrier],
        request: AccountInsertionRequest
        exception: Optional[Exception]

    Provides:
        -   def valid_model() -> Optional[Account]
        -   def valid_blueprint() -> Optional[AccountBlueprint]

        -   def success(
                    request: Request,
                    result: InsertionResult[AccountCarrier],
            ) -> AccountInsertionResponse

        -   def failure(
                    request: Request,
                    result: InsertionResult[AccountCarrier],
                    exception: Exception,
            ) -> AccountInsertionResponse
            
    Super Class:
        ModelInsertionResponse
    """
    def __init__(
            self,
            state: ResponseState,
            result: InsertionResult,
            request: AccountInsertionRequest,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            state: ResponseState
            result: InsertionResult,
            request: AccountInsertionRequest
            exception: Optional[Exception]
        """
        super().__init__(
            state=state,
            result=result,
            request=request,
            exception=exception or result.exception,
        )
        
    @property
    def request(self) -> AccountInsertionRequest:
        return cast(AccountInsertionRequest, super().request)
    
    @property
    def valid_model(self) -> Optional[Account]:
        # Handle the case that the insertion failed.
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
        # Handle the case that the insertion failed.
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
            result: InsertionResult,
    ) -> AccountInsertionResponse:
        
        # Downcast the request into a AccountInsertionRequest.
        insertion_request = cast(
            AccountInsertionRequest,
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
    ) -> AccountInsertionResponse:
        
        # Downcast the request into a AccountInsertionRequest.
        insertion_request = cast(
            AccountInsertionRequest,
            request,
        )
        # Send a failure Response using the cast.
        return cls(
            result=result,
            exception=exception,
            request=insertion_request,
            state=ResponseState.FAILURE,
        )