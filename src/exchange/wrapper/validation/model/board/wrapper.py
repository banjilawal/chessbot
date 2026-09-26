# src/exchange/wrapper/validation/model/board/wrapper.py

"""
Module: exchange.wrapper.validation.model.board.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BoardValidationResponse, ValidationResult
from domain import Board, BoardBlueprint
from err import BoardValidationResponderException, BoardValidationResponseWrapperException, EmptyBoardCarrierException
from exchange import (
    BoardValidationResponder, ModelValidationResponseWrapper, BoardValidationRequest
)
from util import LoggingLevelRouter


class BoardValidationResponseWrapper(
    ModelValidationResponseWrapper[Board]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Board
                _   BoardBlueprint
            products from BoardValidationResponder.

    Attributes:
        responder: BoardValidationResponder
        
    Provides:
        -   def extract_model(
                    request: BoardValidationRequest
            ) -> ValidationResult[Board]
            
        -   def extract_blueprint(
                    request: BoardValidationRequest
            ) -> ValidationResult[BoardBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[BoardValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[BoardValidationResponder]
        """
        super().__init__(responder=responder or BoardValidationResponder())
    
    @property
    def responder(self) -> BoardValidationResponder:
        return cast(BoardValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: BoardValidationRequest,
    ) -> ValidationResult[Board]:
        """
        Extract a Board safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Board from the success response then send it 
                to the client.
        Args:
            request: BoardValidationRequest
        Result:
            ValidationResult[Board]
        Raises:
            BoardValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationResponseWrapperException.MSG,
                    err_code=BoardValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(BoardValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationResponderException.MSG,
                    err_code=BoardValidationResponderException.ERR_CODE,
                    ex=EmptyBoardCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyBoardCarrierException.MSG,
                        err_code=EmptyBoardCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Board, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: BoardValidationRequest,
    ) -> ValidationResult[BoardBlueprint]:
        """
        Extract a BoardBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the BoardBluprint from the success response
                then send it to the client.
        Args:
            request: BoardValidationRequest
        Result:
            ValidationResult[BoardBlueprint]
        Raises:
            BoardValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationResponseWrapperException.MSG,
                    err_code=BoardValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(BoardValidationResponse, result)
        if not response.valid_board:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationResponderException.MSG,
                    err_code=BoardValidationResponderException.ERR_CODE,
                    ex=EmptyBoardCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyBoardCarrierException.MSG,
                        err_code=EmptyBoardCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(BoardBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)