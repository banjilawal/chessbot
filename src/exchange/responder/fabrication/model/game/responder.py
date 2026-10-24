# src/exchange/responder/fabrication/model/game/responder.py

"""
Module: exchange.responder.fabrication.model.game.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, GameBuildResponse
from exchange import ModelBuildResponder, GameBuildRequest
from domain import Game
from err import GameBuildResponderException
from transit import GameCarrier, GameBuildDispatcher
from util import LoggingLevelRouter


class GameBuildResponder(ModelBuildResponder[Game]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Game build Request-Response workflow.

    Attributes:
        dispatcher: GameBuildDispatcher[T]

    Provides:
        -   def execute(request: GameBuildRequest[T]) -> GameBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[GameBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[GameBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or GameBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> GameBuildDispatcher:
        return cast(GameBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: GameBuildRequest
    ) -> GameBuildResponse:
        """
        Certify a candidate is a GameCarrier whose payload is either a Game
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: GameBuildRequest
        Result:
            GameBuildResponse
        Raises:
            GameValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return GameBuildResponse.failure(
                request=request,
                result=result,
                exception=GameBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameBuildResponderException.MSG,
                    err_code=GameBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(GameCarrier, result.payload)
        return GameBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )