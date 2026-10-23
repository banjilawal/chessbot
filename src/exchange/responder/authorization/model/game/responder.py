# src/exchange/responder/authorization/model/game/responder.py

"""
Module: exchange.responder.authorization.model.game.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, GameDecision
from exchange import ModelAuthorizationResponder, GameAuthorizationRequest
from domain import Game
from err import GameAuthorizationResponderException
from transit import GameCarrier, GameAuthorizationDispatcher
from util import LoggingLevelRouter


class GameAuthorizationResponder(ModelAuthorizationResponder[Game]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Game authorization Request-Response workflow.

    Attributes:
        dispatcher: GameAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: GameAuthorizationRequest[T]) -> GameDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[GameAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[GameAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or GameAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> GameAuthorizationDispatcher:
        return cast(GameAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: GameAuthorizationRequest
    ) -> GameDecision:
        """
        Certify a candidate is a GameCarrier whose payload is either a Game
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: GameAuthorizationRequest
        Result:
            GameDecision
        Raises:
            GameAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return GameDecision.failure(
                request=request,
                result=result,
                exception=GameAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameAuthorizationResponderException.MSG,
                    err_code=GameAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(GameCarrier, result.payload)
        return GameDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )