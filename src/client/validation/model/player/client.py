# src/client/validation/model/player/client.py

"""
Module: client.validation.model.player.client
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, PlayerValidationResponse
from client import ModelValidationResponseService, PlayerValidationRequest
from domain import Player
from err import PlayerValidatorClientException
from transit import PlayerCarrier, PlayerValidationDispatcher
from util import LoggingLevelRouter


class PlayerValidationResponseService(ModelValidationResponseService[Player]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Player validation Request-Response workflow.

    Attributes:
        dispatcher: PlayerValidationDispatcher[T]

    Provides:
        -   def submit(request: PlayerValidationRequest[T]) -> PlayerValidationResponse[T]

    Super Class:
        ModelValidatorClient
    """
    
    def __init__(
            self, 
            dispatcher: Optional[PlayerValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or PlayerValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> PlayerValidationDispatcher:
        return cast(PlayerValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: PlayerValidationRequest
    ) -> PlayerValidationResponse:
        """
        Certify a candidate is a PlayerCarrier whose payload is either a Player
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: PlayerValidationRequest
        Result:
            PlayerValidationResponse
        Raises:
            PlayerValidatorClientException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return PlayerValidationResponse.failure(
                request=request,
                result=result,
                exception=PlayerValidatorClientException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidatorClientException.MSG,
                    err_code=PlayerValidatorClientException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(PlayerCarrier, result.payload)
        return PlayerValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )