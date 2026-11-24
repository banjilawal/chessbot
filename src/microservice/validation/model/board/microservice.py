# src/exchange/service/validation/model/board/service.py

"""
Module: exchange.service.validation.model.board.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Board, BoardBlueprint
from err import BoardCarrierEmptyException, BoardValidationServiceException
from exchange import BoardValidationRequest
from microservice import ValidationMicroservice
from transit import BoardCarrier, BoardValidationDispatcher
from util import LoggingLevelRouter


class BoardValidationService(ValidationMicroservice[Board]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Board
                _   BoardBlueprint
            products from BoardValidationService.

    Attributes:
        dispatcher: BoardValidationDispatcher
        
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
            dispatcher: Optional[BoardValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[BoardValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or BoardValidationDispatcher())
    
    @property
    def dispatcher(self) -> BoardValidationDispatcher:
        return cast(BoardValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: BoardValidationRequest) -> ValidationResult[Board]:
        """
        Extract an Board safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Board from the result then send it to the client.
        Args:
            request: BoardValidationRequest
        Result:
            ValidationResult[Board]
        Raises:
            BoardValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(BoardCarrier, result.entity)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
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
        model = cast(Board, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: BoardValidationRequest,
    ) -> ValidationResult[BoardBlueprint]:
        """
        Extract an BoardBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the BoardBlueprint from the result then send it
                to the client.
        Args:
            request: BoardValidationRequest
        Result:
            ValidationResult[BoardBlueprint]
        Raises:
            BoardValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(BoardCarrier, result.entity)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
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
        blueprint = cast(BoardBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)