# src/exchange/responder/validation/context/account/responder.py

"""
Module: exchange.responder.validation.context.account.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AccountContextValidationResponse, ValidationResult
from domain import AccountContext
from exchange import AccountContextValidationRequest, ContextValidationResponder
from transit import AccountCarrier, AccountContextValidationDispatcher
from util import LoggingLevelRouter


class AccountContextValidationResponder(
    ContextValidationResponder[AccountContext]
):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Account validation Request-Response workflow.

    Attributes:
        dispatcher: AccountContextValidationDispatcher[T]

    Provides:
        -   def execute(request: AccountContextValidationRequest[T]) -> AccountContextValidationResponse[T]

    Super Class:
        ContextValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AccountContextValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AccountContextValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AccountContextValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> AccountContextValidationDispatcher:
        return cast(AccountContextValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AccountContextValidationRequest
    ) -> AccountContextValidationResponse:
        """
        Certify a candidate is a AccountCarrier whose payload is either a Account
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AccountContextValidationRequest
        Result:
            AccountContextValidationResponse
        Raises:
            AccountContextValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AccountContextValidationResponse.failure(
                request=request,
                exception=AccountContextValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountContextValidationResponderException.MSG,
                    err_code=AccountContextValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AccountCarrier, result.payload)
        return AccountContextValidationResponse.success(
            request=request,
            result=ValidationResult.success(carrier),
        )