# src/exchange/service/validation/context/board/service.py

"""
Module: exchange.service.validation.context.board.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BoardValidationResponse, ValidationResult
from domain import Board, BoardBlueprint
from err import (
    BoardContextValidationServiceException, BoardContextValidationServiceException,
    BoardCarrierEmptyException
)
from exchange import (
    BoardContextValidationService, ContextValidationService, BoardValidationRequest
)
from util import LoggingLevelRouter


class BoardContextValidationService(
    ContextValidationService[Board]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Board
                _   BoardBlueprint
            products from BoardContextValidationService.

    Attributes:
        service: BoardContextValidationService
        
    Provides:
        -   def extract_context(
                    request: BoardValidationRequest
            ) -> ValidationResult[Board]
            
        -   def extract_blueprint(
                    request: BoardValidationRequest
            ) -> ValidationResult[BoardBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[BoardContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[BoardContextValidationService]
        """
        super().__init__(service=service or BoardContextValidationService())
    
    @property
    def service(self) -> BoardContextValidationService:
        return cast(BoardContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: BoardValidationRequest,
    ) -> ValidationResult[Board]:
        """
        Extract a Board safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Board from the success response then send it 
                to the client.
        Args:
            request: BoardValidationRequest
        Result:
            ValidationResult[Board]
        Raises:
            BoardContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardContextValidationServiceException.MSG,
                    err_code=BoardContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(BoardValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardContextValidationServiceException.MSG,
                    err_code=BoardContextValidationServiceException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Board, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: BoardValidationRequest,
    ) -> ValidationResult[BoardBlueprint]:
        """
        Extract a BoardBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the BoardBluprint from the success response
                then send it to the client.
        Args:
            request: BoardValidationRequest
        Result:
            ValidationResult[BoardBlueprint]
        Raises:
            BoardContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardContextValidationServiceException.MSG,
                    err_code=BoardContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(BoardValidationResponse, result)
        if not response.valid_board:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardContextValidationServiceException.MSG,
                    err_code=BoardContextValidationServiceException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(BoardBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)