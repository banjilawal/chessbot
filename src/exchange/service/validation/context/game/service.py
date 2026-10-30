# src/exchange/service/validation/context/game/service.py

"""
Module: exchange.service.validation.context.game.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import GameValidationResponse, ValidationResult
from domain import Game, GameBlueprint
from err import GameContextValidationServiceException, GameContextValidationServiceException, GameCarrierEmptyException
from exchange import (
    GameContextValidationService, ContextValidationService, GameValidationRequest
)
from util import LoggingLevelRouter


class GameContextValidationService(
    ContextValidationService[Game]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Game
                _   GameBlueprint
            products from GameContextValidationService.

    Attributes:
        service: GameContextValidationService
        
    Provides:
        -   def extract_context(
                    request: GameValidationRequest
            ) -> ValidationResult[Game]
            
        -   def extract_blueprint(
                    request: GameValidationRequest
            ) -> ValidationResult[GameBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[GameContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[GameContextValidationService]
        """
        super().__init__(service=service or GameContextValidationService())
    
    @property
    def service(self) -> GameContextValidationService:
        return cast(GameContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: GameValidationRequest,
    ) -> ValidationResult[Game]:
        """
        Extract a Game safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Game from the success response then send it 
                to the client.
        Args:
            request: GameValidationRequest
        Result:
            ValidationResult[Game]
        Raises:
            GameContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameContextValidationServiceException.MSG,
                    err_code=GameContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(GameValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameContextValidationServiceException.MSG,
                    err_code=GameContextValidationServiceException.ERR_CODE,
                    ex=GameCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameCarrierEmptyException.MSG,
                        err_code=GameCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Game, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: GameValidationRequest,
    ) -> ValidationResult[GameBlueprint]:
        """
        Extract a GameBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the GameBluprint from the success response
                then send it to the client.
        Args:
            request: GameValidationRequest
        Result:
            ValidationResult[GameBlueprint]
        Raises:
            GameContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameContextValidationServiceException.MSG,
                    err_code=GameContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(GameValidationResponse, result)
        if not response.valid_game:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameContextValidationServiceException.MSG,
                    err_code=GameContextValidationServiceException.ERR_CODE,
                    ex=GameCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameCarrierEmptyException.MSG,
                        err_code=GameCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(GameBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)