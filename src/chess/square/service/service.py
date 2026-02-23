# src/chess/square/service/service.py

"""
Module: chess.square.service.service
Author: Banji Lawal
Created: 2025-11-12
version: 1.0.0
"""

from __future__ import annotations

from copy import deepcopy
from typing import cast



class SquareService(EntityService[Square]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing Square microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Authoritative, single source of truth for Square state by providing single entry and exit points to Square
        lifecycle.

    # PARENT:
        *   EntityService

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   SERVICE_NAME (str)
        *   token_visit_handler (TokenVisitHandler)
        *   collision_detector (SquareCollisionDetector)

    # INHERITED ATTRIBUTES:
        *   See EntityService for inherited attributes.
        
    # LOCAL CONSTRUCTOR PARAMETERS:
        *   token_visit_handler (TokenVisitHandler)
        *   collision_detector (SquareCollisionDetector)
        
       INHERITED CONSTRUCTOR PARAMETERS: See EntityService for inherited parameters.
        
    # LOCAL METHODS:
        *   begin_square_visit(square: Square, visitor: Token) -> UpdateResult[Square]
        *   end_square_visit(square: Square) -> DeletionResult[Token]
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
        super().__init__(id=id, name=name, builder=builder, validator=validator)
        self._collision_detector = collision_detector
        self._token_visit_handler = token_visit_handler
    
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
        # PARAMETERS:
            *   square (Square)
            *   visitor (Token)
        # RETURN:
            *   UpdateResult[Square]
        # RAISES:
            *   SquareServiceException
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
                    message=f"ServiceID:{self.id} {method}: {SquareServiceException.ERROR_CODE}",
                    ex=visitation_update_result.exception
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
        # PARAMETERS:
            *   square (Square)
        # RETURN:
            *   DeletionResult[Token]
        # RAISES:
            *   SquareServiceException
        """
        method = "SquareService.begin_square_visit"
        
        # --- Handoff validation and visit termination responsibilities to token_visit_handler. ---#
        visit_termination_result = self._token_visit_handler.terminate_visit(square=square)
        
        # Handle the case that, the visit did not end.
        if visit_termination_result.is_failure:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                SquareServiceException(
                    message=f"ServiceID:{self.id} {method}: {SquareServiceException.ERROR_CODE}",
                    ex=visit_termination_result.exception
                )
            )
        # --- Forward the success result to the client. ---#
        return visit_termination_result