# src/exchange/service/validation/model/game/service.py

"""
Module: exchange.service.validation.model.game.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import GameValidationResponse, ValidationResult
from domain import Game, GameBlueprint
from err import GameValidationServiceException, GameValidationServiceException, GameCarrierEmptyException
from exchange import (
    GameValidationService, ModelValidationService, GameValidationRequest
)
from util import LoggingLevelRouter


class GameValidationService(
    ModelValidationService[Game]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Game
                _   GameBlueprint
            products from GameValidationService.

    Attributes:
        service: GameValidationService
        
    Provides:
        -   def extract_model(
                    request: GameValidationRequest
            ) -> ValidationResult[Game]
            
        -   def extract_blueprint(
                    request: GameValidationRequest
            ) -> ValidationResult[GameBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[GameValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[GameValidationService]
        """
        super().__init__(service=service or GameValidationService())
    
    @property
    def service(self) -> GameValidationService:
        return cast(GameValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
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
            GameValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationServiceException.MSG,
                    err_code=GameValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(GameValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationServiceException.MSG,
                    err_code=GameValidationServiceException.ERR_CODE,
                    ex=GameCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=GameCarrierEmptyException.MSG,
                        err_code=GameCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Game, response.valid_model)
        return ValidationResult.success(model)
    
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
            GameValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationServiceException.MSG,
                    err_code=GameValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(GameValidationResponse, result)
        if not response.valid_game:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                GameValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameValidationServiceException.MSG,
                    err_code=GameValidationServiceException.ERR_CODE,
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