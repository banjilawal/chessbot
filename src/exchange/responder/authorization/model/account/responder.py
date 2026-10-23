# src/exchange/responder/authorization/model/account/responder.py

"""
Module: exchange.responder.authorization.model.account.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, AccountDecision
from exchange import ModelAuthorizationResponder, AccountAuthorizationRequest
from domain import Account
from err import AccountAuthorizationResponderException
from transit import AccountCarrier, AccountAuthorizationDispatcher
from util import LoggingLevelRouter


class AccountAuthorizationResponder(ModelAuthorizationResponder[Account]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Account authorization Request-Response workflow.

    Attributes:
        dispatcher: AccountAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: AccountAuthorizationRequest[T]) -> AccountDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[AccountAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[AccountAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or AccountAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> AccountAuthorizationDispatcher:
        return cast(AccountAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: AccountAuthorizationRequest
    ) -> AccountDecision:
        """
        Certify a candidate is a AccountCarrier whose payload is either a Account
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: AccountAuthorizationRequest
        Result:
            AccountDecision
        Raises:
            AccountAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return AccountDecision.failure(
                request=request,
                result=result,
                exception=AccountAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountAuthorizationResponderException.MSG,
                    err_code=AccountAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(AccountCarrier, result.payload)
        return AccountDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )