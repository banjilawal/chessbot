# src/exchange/response/validation/model/board/exchange.py

"""
Module: exchange.response.validation.model.board.exchange
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult, BoardValidationResponse
from exchange import ModelValidationResponder, BoardValidationRequest
from domain import Board
from err import BoardValidationResponderException
from transit import BoardCarrier, BoardValidationDispatcher
from util import LoggingLevelRouter


class BoardValidationResponder(ModelValidationResponder[Board]):
    """
    Role
        - Mediator

    Responsibilities:
        1.  Intermediary in the Board validation Request-Response workflow.

    Attributes:
        dispatcher: BoardValidationDispatcher[T]

    Provides:
        -   def submit(request: BoardValidationRequest[T]) -> BoardValidationResponse[T]

    Super Class:
        ModelValidatorExchange
    """
    
    def __init__(
            self, 
            dispatcher: Optional[BoardValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[BoardValidationDispatcher]
        """
        super().__init__(
            dispatcher=dispatcher or BoardValidationDispatcher()
        )
        
    @property
    def dispatcher(self) -> BoardValidationDispatcher:
        return cast(BoardValidationDispatcher, super().dispatcher)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            request: BoardValidationRequest
    ) -> BoardValidationResponse:
        """
        Certify a candidate is a BoardCarrier whose payload is either a Board
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResponse if the dispatcher
                aborts the job.
            2.  Otherwise, extract and cast the carrier to send in the success result.
        Args:
            request: BoardValidationRequest
        Result:
            BoardValidationResponse
        Raises:
            BoardValidatorExchangeException
        """
        method = f"{self.__class__.__name__}.submit"
        
        result = self.dispatcher.execute(job=request)
        # Handle the case that the dispatcher marks the candidate unsafe.
        if result.is_failure:
            # Send the exception chain on failure.
            return BoardValidationResponse.failure(
                request=request,
                result=result,
                exception=BoardValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationResponderException.MSG,
                    err_code=BoardValidationResponderException.ERR_CODE,
                    ex=result.exception,
                ),
            )
        # --- Otherwise cast and send the success response to the caller. ---#
        carrier = cast(BoardCarrier, result.payload)
        return BoardValidationResponse.success(
            request=request,
            result=ValidationResult(carrier),
        )