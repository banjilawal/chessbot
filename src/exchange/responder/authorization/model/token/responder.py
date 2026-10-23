# src/exchange/responder/authorization/model/token/responder.py

"""
Module: exchange.responder.authorization.model.token.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, TokenDecision
from exchange import ModelAuthorizationResponder, TokenAuthorizationRequest
from domain import Token
from err import TokenAuthorizationResponderException
from transit import TokenCarrier, TokenAuthorizationDispatcher
from util import LoggingLevelRouter


class TokenAuthorizationResponder(ModelAuthorizationResponder[Token]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Token authorization Request-Response workflow.

    Attributes:
        dispatcher: TokenAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: TokenAuthorizationRequest[T]) -> TokenDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TokenAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TokenAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TokenAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> TokenAuthorizationDispatcher:
        return cast(TokenAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TokenAuthorizationRequest
    ) -> TokenDecision:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TokenAuthorizationRequest
        Result:
            TokenDecision
        Raises:
            TokenAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TokenDecision.failure(
                request=request,
                result=result,
                exception=TokenAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenAuthorizationResponderException.MSG,
                    err_code=TokenAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TokenCarrier, result.payload)
        return TokenDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )