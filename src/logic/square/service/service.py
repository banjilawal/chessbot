# src/logic/square/service/service.py

"""
Module: logic.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations
from typing import Dict, cast

from logic.square import (
    Square, SquareBuilder, SquareCollisionDetector, SquareServiceException, SquareValidator, TokenVisitHandler
)
from logic.system import DeletionResult, IntegrityService, IdFactory, LoggingLevelRouter, UpdateResult
from logic.token import Token


class SquareService(IntegrityService[Square]):
    """
     ROLE: Service, Lifecycle Management, Encapsulation, API layer.
     
     RESPONSIBILITIES:
     1. Update the square and token states in the Visit Lifecycle.
     2.

     INHERITED RESPONSIBILITIES:
        * See IntegrityService for inherited responsibilities.

    PARENT:
         *   IntegrityService

    PROVIDES:
    None

    LOCAL ATTRIBUTES:
        SERVICE_NAME: str
        token_visit_handler: TokenVisitHandler
        collision_detector: SquareCollisionDetector

    INHERITED ATTRIBUTES:
        *   See IntegrityService for inherited attributes.

    CONSTRUCTOR PARAMETERS:
        id: int
        name: str
        builder: Builder
        validator: Validator
        token_visit_handler: TokenVisitHandler
        collision_detector: SquareCollisionDetector

      LOCAL METHODS:
         *   begin_square_visit(square: Square, visitor: Token) -> UpdateResult[Square]
         *   end_square_visit(square: Square) -> DeletionResult[Token]

     # INHERITED METHODS:
     None
     """
    SERVICE_NAME = "SquareService"
    _token_visit_handler: TokenVisitHandler
    _collision_detector: SquareCollisionDetector
    
    def __init__(
            self,
            name: str = SERVICE_NAME,
            builder: SquareBuilder = SquareBuilder(),
            validator: SquareValidator = SquareValidator(),
            id: int = IdFactory.next_id(class_name="SquareService"),
            token_visit_handler: TokenVisitHandler = TokenVisitHandler(),
            collision_detector: SquareCollisionDetector = SquareCollisionDetector(),
    ):
        """
        Args:
            id: int
            name: str
            builder: Builder
            validator: Validator
            token_visit_handler: TokenVisitHandler
            collision_detector: SquareCollisionDetector
        """
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._collision_detector = collision_detector
        self._token_visit_handler = token_visit_handler
        self._commands = {"begin_visit": (Square, Token), "end_visit": (Square,)}
    
    @property
    def builder(self) -> SquareBuilder:
        return cast(SquareBuilder, self.entity_builder)
    
    @property
    def validator(self) -> SquareValidator:
        return cast(SquareValidator, self.entity_validator)
    
    @property
    def collision_detector(self) -> SquareCollisionDetector:
        return self._collision_detector
    
    @property
    def token_visit_handler(self) -> TokenVisitHandler:
        return self._token_visit_handler
    
    @LoggingLevelRouter.monitor
    def begin_square_visit(self, square: Square, visitor: Token) -> UpdateResult[Square]:
        """
        # ACTION:
            1.  Handoff validation and occupation responsibilities to token_visit_handler.
            2.  If token_visit_handler fails, wrap the exception in SquareServiceException, send in the UpdateResult.
            3.  Else forward the success result to the client.
        Args:
            square: Square
            visitor: Token
        Returns:
            UpdateResult[Square]
        Raises:
            SquareServiceException
        """
        method = "SquareService.begin_square_visit"
        
        # --- Handoff validation and occupation processing responsibilities to token_visit_handler. ---#
        visitation_update_result = self._token_visit_handler.start_visit(
            square=square,
            visitor=visitor
        )
        # Handle the case that, the occupation was aborted.
        if visitation_update_result.is_failure:
            # Encapsulate visitation_update_result.{original, exception} in exception chain returned on failure.
            return UpdateResult.update_failure(
                original=visitation_update_result.original,
                exception=SquareServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareServiceException.MSG,
                    err_code=SquareServiceException.ERR_CODE,
                    ex=visitation_update_result.exception,
                )
            )
        # --- Forward the success result to the client. ---#
        return visitation_update_result

    
    @LoggingLevelRouter.monitor
    def end_square_visit(self, square: Square) -> DeletionResult[Token]:
        """
        # ACTION:
            1.  Handoff validation and ejection responsibilities to token_visit_handler.
            2.  If token_visit_handler fails, wrap the exception in SquareServiceException, send in
                the DeletionResult.
            3.  Else forward the success result to the client.
        Args:
            square: Square
        Returns:
            DeletionResult[Token]
        Raises:
            SquareServiceException
        """
        method = "SquareService.begin_square_visit"
        
        # --- Handoff validation and visit termination responsibilities to token_visit_handler. ---#
        visit_termination_result = self._token_visit_handler.terminate_visit(square=square)
        # Handle the case that, the visit did not end.
        if visit_termination_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareServiceException.MSG,
                    err_code=SquareServiceException.ERR_CODE,
                    ex=visit_termination_result.exception
                )
            )
        # --- Forward the success result to the client. ---#
        return visit_termination_result