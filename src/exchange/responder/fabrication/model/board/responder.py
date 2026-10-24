# src/exchange/responder/fabrication/model/board/responder.py

"""
Module: exchange.responder.fabrication.model.board.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult, BoardBuildResponse
from exchange import ModelBuildResponder, BoardBuildRequest
from domain import Board
from err import BoardBuildResponderException
from transit import BoardCarrier, BoardBuildDispatcher
from util import LoggingLevelRouter


class BoardBuildResponder(ModelBuildResponder[Board]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Board build Request-Response workflow.

    Attributes:
        dispatcher: BoardBuildDispatcher[T]

    Provides:
        -   def execute(request: BoardBuildRequest[T]) -> BoardBuildResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[BoardBuildDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[BoardBuildDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or BoardBuildDispatcher()
        )
        
    @property
    def dispatcher(self) -> BoardBuildDispatcher:
        return cast(BoardBuildDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: BoardBuildRequest
    ) -> BoardBuildResponse:
        """
        Certify a candidate is a BoardCarrier whose payload is either a Board
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the BuildResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: BoardBuildRequest
        Result:
            BoardBuildResponse
        Raises:
            BoardValidationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return BoardBuildResponse.failure(
                request=request,
                result=result,
                exception=BoardBuildResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuildResponderException.MSG,
                    err_code=BoardBuildResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(BoardCarrier, result.payload)
        return BoardBuildResponse.success(
            request=request,
            result=BuildResult(carrier),
        )