# src/exchange/responder/authorization/model/arena/responder.py

"""
Module: exchange.responder.authorization.model.arena.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, ArenaDecision
from exchange import ModelAuthorizationResponder, ArenaAuthorizationRequest
from domain import Arena
from err import ArenaAuthorizationResponderException
from transit import ArenaCarrier, ArenaAuthorizationDispatcher
from util import LoggingLevelRouter


class ArenaAuthorizationResponder(ModelAuthorizationResponder[Arena]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Arena authorization Request-Response workflow.

    Attributes:
        dispatcher: ArenaAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: ArenaAuthorizationRequest[T]) -> ArenaDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ArenaAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ArenaAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ArenaAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ArenaAuthorizationDispatcher:
        return cast(ArenaAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ArenaAuthorizationRequest
    ) -> ArenaDecision:
        """
        Certify a candidate is a ArenaCarrier whose payload is either a Arena
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ArenaAuthorizationRequest
        Result:
            ArenaDecision
        Raises:
            ArenaAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ArenaDecision.failure(
                request=request,
                result=result,
                exception=ArenaAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaAuthorizationResponderException.MSG,
                    err_code=ArenaAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ArenaCarrier, result.payload)
        return ArenaDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )