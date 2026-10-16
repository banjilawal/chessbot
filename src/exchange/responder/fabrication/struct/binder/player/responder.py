# src/exchange/responder/fabrication/struct/binder/player/responder.py

"""
Module: exchange.responder.fabrication.struct.binder.player.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, PlayerBinderBuildResponse
from domain import PlayerBinder
from exchange import BinderBuildResponder, PlayerBinderBuildRequest
from err import PlayerBinderBuildResponderException
from transit import PlayerBinderCarrier, PlayerBinderBuildDispatcher
from util import LoggingLevelRouter


class PlayerBinderBuildResponder(BinderBuildResponder[PlayerBinder]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the PlayerBinder build Request-Response workflow.

    Attributes:
        dispatcher: PlayerBinderBuildDispatcher

    Provides:
        -   def submit(request: PlayerBinderBuildRequest) -> PlayerBinderBuildResponse

    Super Class:
        BinderValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PlayerBinderBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerBinderBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PlayerBinderBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> PlayerBinderBuildDispatcher:
        return cast(PlayerBinderBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PlayerBinderBuildRequest
    ) -> PlayerBinderBuildResponse:
        """
        Certify a candidate is a PlayerBinderCarrier whose payload is either a Player
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PlayerBinderBuildRequest
        Result:
            PlayerBinderBuildResponse
        Raises:
            PlayerValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PlayerBinderBuildResponse.failure(
                request=request,
                result=result,
                exception=PlayerBinderBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderBuildResponderException.MSG,
                    err_code=PlayerBinderBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PlayerBinderCarrier, result.payload)
        return PlayerBinderBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )