# src/exchange/responder/authorization/struct/binder/player/responder.py

"""
Module: exchange.responder.authorization.struct.binder.player.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, PlayerBinderDecision
from domain import PlayerBinder
from exchange import BinderAuthorizationResponder, PlayerBinderAuthorizationRequest
from err import PlayerBinderAuthorizationResponderException
from transit import PlayerBinderCarrier, PlayerBinderAuthorizationDispatcher
from util import LoggingLevelRouter


class PlayerBinderAuthorizationResponder(BinderAuthorizationResponder[PlayerBinder]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the PlayerBinder authorization Request-Response workflow.

    Attributes:
        dispatcher: PlayerBinderAuthorizationDispatcher

    Provides:
        -   def submit(request: PlayerBinderAuthorizationRequest) -> PlayerBinderDecision

    Super Class:
        BinderValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PlayerBinderAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerBinderAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PlayerBinderAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> PlayerBinderAuthorizationDispatcher:
        return cast(PlayerBinderAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PlayerBinderAuthorizationRequest
    ) -> PlayerBinderDecision:
        """
        Certify a candidate is a PlayerBinderCarrier whose payload is either a Player
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PlayerBinderAuthorizationRequest
        Result:
            PlayerBinderDecision
        Raises:
            PlayerAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PlayerBinderDecision.failure(
                request=request,
                result=result,
                exception=PlayerBinderAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderAuthorizationResponderException.MSG,
                    err_code=PlayerBinderAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PlayerBinderCarrier, result.payload)
        return PlayerBinderDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )