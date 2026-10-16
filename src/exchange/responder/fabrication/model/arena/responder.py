# src/exchange/responder/fabrication/model/arena/responder.py

"""
Module: exchange.responder.fabrication.model.arena.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, ArenaBuildResponse
from exchange import ModelBuildResponder, ArenaBuildRequest
from domain import Arena
from err import ArenaBuildResponderException
from transit import ArenaCarrier, ArenaBuildDispatcher
from util import LoggingLevelRouter


class ArenaBuildResponder(ModelBuildResponder[Arena]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Arena build Request-Response workflow.

    Attributes:
        dispatcher: ArenaBuildDispatcher[T]

    Provides:
        -   def submit(request: ArenaBuildRequest[T]) -> ArenaBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[ArenaBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ArenaBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or ArenaBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> ArenaBuildDispatcher:
        return cast(ArenaBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: ArenaBuildRequest
    ) -> ArenaBuildResponse:
        """
        Certify a candidate is a ArenaCarrier whose payload is either a Arena
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: ArenaBuildRequest
        Result:
            ArenaBuildResponse
        Raises:
            ArenaValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return ArenaBuildResponse.failure(
                request=request,
                result=result,
                exception=ArenaBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuildResponderException.MSG,
                    err_code=ArenaBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(ArenaCarrier, result.payload)
        return ArenaBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )