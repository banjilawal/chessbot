# src/exchange/responder/validation/struct/binder/player/responder.py

"""
Module: exchange.responder.validation.struct.binder.player.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, PlayerBinderValidationResponse
from domain import PlayerBinder
from exchange import BinderValidationResponder, PlayerBinderValidationRequest
from err import PlayerBinderValidationResponderException
from transit import PlayerBinderCarrier, PlayerBinderValidationDispatcher
from util import LoggingLevelRouter


class PlayerBinderValidationResponder(BinderValidationResponder[PlayerBinder]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the PlayerBinder validation Request-Response workflow.

    Attributes:
        dispatcher: PlayerBinderValidationDispatcher

    Provides:
        -   def execute(request: PlayerBinderValidationRequest) -> PlayerBinderValidationResponse

    Super Class:
        BinderValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PlayerBinderValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerBinderValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PlayerBinderValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> PlayerBinderValidationDispatcher:
        return cast(PlayerBinderValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PlayerBinderValidationRequest
    ) -> PlayerBinderValidationResponse:
        """
        Certify a candidate is a PlayerBinderCarrier whose payload is either a Player
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PlayerBinderValidationRequest
        Result:
            PlayerBinderValidationResponse
        Raises:
            PlayerValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PlayerBinderValidationResponse.failure(
                request=request,
                result=result,
                exception=PlayerBinderValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationResponderException.MSG,
                    err_code=PlayerBinderValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PlayerBinderCarrier, result.payload)
        return PlayerBinderValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )