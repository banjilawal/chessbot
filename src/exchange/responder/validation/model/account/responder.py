# src/exchange/responder/validation/model/account/exchange.py

"""
Module: exchange.responder.validation.model.account.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, AccountValidationResponse
from exchange import ModelValidationResponder, AccountValidationRequest
from domain import Account
from err import AccountValidationResponderException
from transit import AccountCarrier, AccountValidationDispatcher
from util import LoggingLevelRouter


class AccountValidationResponder(ModelValidationResponder[Account]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Account validation Request-Response workflow.

    Attributes:
        dispatcher: AccountValidationDispatcher[T]

    Provides:
        -   def submit(request: AccountValidationRequest[T]) -> AccountValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AccountValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AccountValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AccountValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> AccountValidationDispatcher:
        return cast(AccountValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AccountValidationRequest
    ) -> AccountValidationResponse:
        """
        Certify a candidate is a AccountCarrier whose payload is either a Account
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AccountValidationRequest
        Result:
            AccountValidationResponse
        Raises:
            AccountValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AccountValidationResponse.failure(
                request=request,
                result=result,
                exception=AccountValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountValidationResponderException.MSG,
                    err_code=AccountValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AccountCarrier, result.payload)
        return AccountValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )