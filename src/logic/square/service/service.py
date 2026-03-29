# src/logic/square/service/transaction.py

"""
Module: logic.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast

from logic.token import Token, TokenService
from logic.square import (
    Square, SquareBuilder, SquareOpsController, SquareServiceException,
    SquareValidationTransaction, VisitationProcessor
)
from logic.system import DeletionResult, IntegrityService, IdFactory, LoggingLevelRouter, UpdateResult


class SquareService(IntegrityService[Square]):
    """
    Role:
        -   API Layer
        -   Microservice Worker
        -   Integrity Lifecycle Manager
     
    Responsibilities:
        1.  Microservice for all Square operations.
        2.  Owner of the Square Integrity Lifecycle.

    Attributes:
        SERVICE_NAME = SquareService
        
        id: int
        name: str
        controller: SquareBuilder

    Provides:
        -   begin_square_visit(
                    square: Square,
                    visitor: Token,
                    token_service: TokenService = TokenService(),
            ) -> UpdateResult[Square]
            
        -   end_square_visit(square: Square) -> DeletionResult[Token]
            
            
    Super Class:
        IntegrityService
     """
    SERVICE_NAME = "SquareService"
    _controller: SquareOpsController
    _visit_processor: VisitationProcessor
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            controller: SquareOpsController = SquareOpsController(),
            builder: SquareBuilder = SquareBuilder(),
            validator: SquareValidationTransaction = SquareValidationTransaction(),
            id: int = IdFactory.next_id(class_name="SquareService"),
            visit_processor: VisitationProcessor = VisitationProcessor(),
    ):
        """
        Args:
            id: int
            name: str
            builder: Builder
            validator: ValidationTransaction
            visit_processor: VisitationController
        """
        super().__init__(id=id, name=name)
        self._controller = controller
        self._visit_processor = visit_processor
    
    @property
    def build(self) -> SquareBuilder:
        return self._controller.build
    
    @property
    def validation(self) -> SquareValidationTransaction:
        return self._controller.validation
    
    @property
    def visit_processor(self) -> VisitationProcessor:
        return self._visit_processor
    
    @LoggingLevelRouter.monitor
    def begin_square_visit(
            self,
            square: Square,
            visitor: Token,
            token_service: TokenService = TokenService(),
    ) -> UpdateResult[Square]:
        """
        Put a token into a square.

        Action:
            If the occupation fails, send the pre_update_square along with an exception chain in the
            UpdateResult. Otherwise, send the success result.
        Args:
            square: Square,
            visitor: Token,
            token_service: TokenService
        Returns:
            UpdateResult[Square]
        Raises:
            SquareServiceException
        """
        method = f"{self.__class__.__name__}.begin_square_visit"
        
        # Backup the square
        pre_update_square = deepcopy(square)
        # --- Forward the request to the processor. ---#
        visitation_result = self._controller.visitation.entry.execute(
            token=visitor,
            square=square,
            token_service=token_service,
            square_validator=self.validation,
        )
        # Handle the case that, the request was not completed.
        if visitation_result.is_failure:
            # Return the exception chain on failure.
            return UpdateResult.update_failure(
                original=pre_update_square,
                exception=SquareServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareServiceException.MSG,
                    err_code=SquareServiceException.ERR_CODE,
                    ex=visitation_result.exception,
                )
            )
        # --- Forward the success result to the client. ---#
        return visitation_result

    
    @LoggingLevelRouter.monitor
    def end_square_visit(self, square: Square) -> DeletionResult[Token]:
        """
        Remove a token from the square=.

        Action:
            If the deletion fails, send an exception chain. Otherwise, send the success result.
        Args:
            square: Square
        Returns:
            DeletionResult[Token]
        Raises:
            SquareServiceException
        """
        method = f"{self.__class__.__name__}.end_square_visit"
        
        # --- Forward the request to the processor. ---#
        visitation_result = self._controller.visitation.departure.execute(
            square=square,
            square_validator=self.validation,
        )
        # Handle the case that, the request was not completed.
        if visitation_result.is_failure:
            return DeletionResult.failure(
                exception=SquareServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareServiceException.MSG,
                    err_code=SquareServiceException.ERR_CODE,
                    ex=visitation_result.exception,
                )
            )
            # --- Forward the success result to the client. ---#-#
        return visitation_result