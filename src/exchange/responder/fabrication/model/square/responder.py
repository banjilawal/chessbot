# src/exchange/responder/fabrication/model/square/responder.py

"""
Module: exchange.responder.fabrication.model.square.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, SquareBuildResponse
from exchange import ModelBuildResponder, SquareBuildRequest
from domain import Square
from err import SquareBuildResponderException
from transit import SquareCarrier, SquareBuildDispatcher
from util import LoggingLevelRouter


class SquareBuildResponder(ModelBuildResponder[Square]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Square build Request-Response workflow.

    Attributes:
        dispatcher: SquareBuildDispatcher[T]

    Provides:
        -   def submit(request: SquareBuildRequest[T]) -> SquareBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[SquareBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or SquareBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> SquareBuildDispatcher:
        return cast(SquareBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: SquareBuildRequest
    ) -> SquareBuildResponse:
        """
        Certify a candidate is a SquareCarrier whose payload is either a Square
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: SquareBuildRequest
        Result:
            SquareBuildResponse
        Raises:
            SquareValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return SquareBuildResponse.failure(
                request=request,
                result=result,
                exception=SquareBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuildResponderException.MSG,
                    err_code=SquareBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(SquareCarrier, result.payload)
        return SquareBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )