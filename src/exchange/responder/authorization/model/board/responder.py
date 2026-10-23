# src/exchange/responder/authorization/model/board/responder.py

"""
Module: exchange.responder.authorization.model.board.responder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AuthorizationResult, BoardDecision
from exchange import ModelAuthorizationResponder, BoardAuthorizationRequest
from domain import Board
from err import BoardAuthorizationResponderException
from transit import BoardCarrier, BoardAuthorizationDispatcher
from util import LoggingLevelRouter


class BoardAuthorizationResponder(ModelAuthorizationResponder[Board]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Board authorization Request-Response workflow.

    Attributes:
        dispatcher: BoardAuthorizationDispatcher[T]

    Provides:
        -   def submit(request: BoardAuthorizationRequest[T]) -> BoardDecision[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[BoardAuthorizationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[BoardAuthorizationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or BoardAuthorizationDispatcher()
        )
        
    @property
    def dispatcher(self) -> BoardAuthorizationDispatcher:
        return cast(BoardAuthorizationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: BoardAuthorizationRequest
    ) -> BoardDecision:
        """
        Certify a candidate is a BoardCarrier whose payload is either a Board
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the Decision if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: BoardAuthorizationRequest
        Result:
            BoardDecision
        Raises:
            BoardAuthorizationResponderException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return BoardDecision.failure(
                request=request,
                result=result,
                exception=BoardAuthorizationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardAuthorizationResponderException.MSG,
                    err_code=BoardAuthorizationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(BoardCarrier, result.payload)
        return BoardDecision.success(
            request=request,
            result=AuthorizationResult(carrier),
        )