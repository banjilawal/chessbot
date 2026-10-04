# src/exchange/responder/validation/structure/game/exchange.py

"""
Module: exchange.responder.validation.structure.game.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, GameValidationResponse
from exchange import StructureValidationResponder, GameValidationRequest
from domain import Game
from err import GameValidationResponderException
from transit import GameCarrier, GameValidationDispatcher
from util import LoggingLevelRouter


class GameValidationResponder(StructureValidationResponder[Game]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Game validation Request-Response workflow.

    Attributes:
        dispatcher: GameValidationDispatcher[T]

    Provides:
        -   def submit(request: GameValidationRequest[T]) -> GameValidationResponse[T]

    Super Class:
        StructureValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[GameValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[GameValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or GameValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> GameValidationDispatcher:
        return cast(GameValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: GameValidationRequest
    ) -> GameValidationResponse:
        """
        Certify a candidate is a GameCarrier whose payload is either a Game
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: GameValidationRequest
        Result:
            GameValidationResponse
        Raises:
            GameValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return GameValidationResponse.failure(
                request=request,
                result=result,
                exception=GameValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationResponderException.MSG,
                    err_code=GameValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(GameCarrier, result.payload)
        return GameValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )