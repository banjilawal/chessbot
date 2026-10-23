# src/exchange/responder/authorization/model/player/responder.py

"""
Module: exchange.responder.authorization.model.player.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, PlayerDecision
from exchange import ModelAuthorizationResponder, PlayerAuthorizationRequest
from domain import Player
from err import PlayerAuthorizationResponderException
from transit import PlayerCarrier, PlayerAuthorizationDispatcher
from util import LoggingLevelRouter


class PlayerAuthorizationResponder(ModelAuthorizationResponder[Player]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Player authorization Request-Response workflow.

    Attributes:
        dispatcher: PlayerAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: PlayerAuthorizationRequest[T]) -> PlayerDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PlayerAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PlayerAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> PlayerAuthorizationDispatcher:
        return cast(PlayerAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PlayerAuthorizationRequest
    ) -> PlayerDecision:
        """
        Certify a candidate is a PlayerCarrier whose payload is either a Player
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PlayerAuthorizationRequest
        Result:
            PlayerDecision
        Raises:
            PlayerAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PlayerDecision.failure(
                request=request,
                result=result,
                exception=PlayerAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerAuthorizationResponderException.MSG,
                    err_code=PlayerAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PlayerCarrier, result.payload)
        return PlayerDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )