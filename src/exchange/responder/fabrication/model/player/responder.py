# src/exchange/responder/fabrication/model/player/responder.py

"""
Module: exchange.responder.fabrication.model.player.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, PlayerBuildResponse
from exchange import ModelBuildResponder, PlayerBuildRequest
from domain import Player
from err import PlayerBuildResponderException
from transit import PlayerCarrier, PlayerBuildDispatcher
from util import LoggingLevelRouter


class PlayerBuildResponder(ModelBuildResponder[Player]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Player build Request-Response workflow.

    Attributes:
        dispatcher: PlayerBuildDispatcher[T]

    Provides:
        -   def submit(request: PlayerBuildRequest[T]) -> PlayerBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PlayerBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PlayerBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> PlayerBuildDispatcher:
        return cast(PlayerBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PlayerBuildRequest
    ) -> PlayerBuildResponse:
        """
        Certify a candidate is a PlayerCarrier whose payload is either a Player
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PlayerBuildRequest
        Result:
            PlayerBuildResponse
        Raises:
            PlayerValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PlayerBuildResponse.failure(
                request=request,
                result=result,
                exception=PlayerBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBuildResponderException.MSG,
                    err_code=PlayerBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PlayerCarrier, result.payload)
        return PlayerBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )