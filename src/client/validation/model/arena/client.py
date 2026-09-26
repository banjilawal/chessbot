# src/client/validation/model/arena/client.py

"""
Module: client.validation.model.arena.client
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, ArenaValidationResponse
from client import ModelValidatorClient, ArenaValidationRequest
from domain import Arena
from err import ArenaValidatorClientException
from transit import ArenaCarrier, ArenaValidationDispatcher
from util import LoggingLevelRouter


class ArenaValidatorClient(ModelValidatorClient[Arena]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Arena validation Request-Response workflow.

    Attributes:
        dispatcher: ArenaValidationDispatcher[T]

    Provides:
        -   def submit(request: ArenaValidationRequest[T]) -> ArenaValidationResponse[T]

    Super Class:
        ModelValidatorClient
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ArenaValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ArenaValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ArenaValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> ArenaValidationDispatcher:
        return cast(ArenaValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def transmit(
            self,
            request: ArenaValidationRequest
    ) -> ArenaValidationResponse:
        """
        Certify a candidate is a ArenaCarrier whose payload is either a Arena
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ArenaValidationRequest
        Result:
            ArenaValidationResponse
        Raises:
            ArenaValidatorClientException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ArenaValidationResponse.failure(
                request=request,
                result=result,
                exception=ArenaValidatorClientException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidatorClientException.MSG,
                    err_code=ArenaValidatorClientException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ArenaCarrier, result.payload)
        return ArenaValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )