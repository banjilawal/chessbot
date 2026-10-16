# src/exchange/responder/fabrication/model/token/responder.py

"""
Module: exchange.responder.fabrication.model.token.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, TokenBuildResponse
from exchange import ModelBuildResponder, TokenBuildRequest
from domain import Token
from err import TokenBuildResponderException
from transit import TokenCarrier, TokenBuildDispatcher
from util import LoggingLevelRouter


class TokenBuildResponder(ModelBuildResponder[Token]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Token build Request-Response workflow.

    Attributes:
        dispatcher: TokenBuildDispatcher[T]

    Provides:
        -   def submit(request: TokenBuildRequest[T]) -> TokenBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[TokenBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[TokenBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or TokenBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> TokenBuildDispatcher:
        return cast(TokenBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: TokenBuildRequest
    ) -> TokenBuildResponse:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: TokenBuildRequest
        Result:
            TokenBuildResponse
        Raises:
            TokenValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return TokenBuildResponse.failure(
                request=request,
                result=result,
                exception=TokenBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenBuildResponderException.MSG,
                    err_code=TokenBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(TokenCarrier, result.payload)
        return TokenBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )