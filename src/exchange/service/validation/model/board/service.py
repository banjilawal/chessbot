# src/exchange/service/validation/model/board/service.py

"""
Module: exchange.service.validation.model.board.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BoardValidationResponse, ValidationResult
from domain import Board, BoardBlueprint
from err import (
    BoardValidationServiceException, BoardValidationServiceException,
    BoardCarrierEmptyException
)
from exchange import (
    BoardValidationService, ModelValidationService, BoardValidationRequest
)
from util import LoggingLevelRouter


class BoardValidationService(
    ModelValidationService[Board]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Board
                _   BoardBlueprint
            products from BoardValidationService.

    Attributes:
        service: BoardValidationService
        
    Provides:
        -   def extract_model(
                    request: BoardValidationRequest
            ) -> ValidationResult[Board]
            
        -   def extract_blueprint(
                    request: BoardValidationRequest
            ) -> ValidationResult[BoardBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[BoardValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[BoardValidationService]
        """
        super().__init__(service=service or BoardValidationService())
    
    @property
    def service(self) -> BoardValidationService:
        return cast(BoardValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
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
            BoardValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationServiceException.MSG,
                    err_code=BoardValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(BoardValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationServiceException.MSG,
                    err_code=BoardValidationServiceException.ERR_CODE,
                    ex=BoardCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BoardCarrierEmptyException.MSG,
                        err_code=BoardCarrierEmptyException.ERR_CODE,
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
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the BoardBluprint from the success response
                then send it to the client.
        Args:
            request: BoardValidationRequest
        Result:
            ValidationResult[BoardBlueprint]
        Raises:
            BoardValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationServiceException.MSG,
                    err_code=BoardValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(BoardValidationResponse, result)
        if not response.valid_board:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                BoardValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardValidationServiceException.MSG,
                    err_code=BoardValidationServiceException.ERR_CODE,
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