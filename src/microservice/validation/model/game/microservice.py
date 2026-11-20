# src/exchange/service/validation/model/game/service.py

"""
Module: exchange.service.validation.model.game.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Game, GameBlueprint
from err import GameCarrierEmptyException, GameValidationServiceException
from exchange import GameValidationRequest
from microservice import ValidationMicroservice
from transit import GameCarrier, GameValidationDispatcher
from util import LoggingLevelRouter


class GameValidationService(ValidationMicroservice[Game]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Game
                _   GameBlueprint
            products from GameValidationService.

    Attributes:
        dispatcher: GameValidationDispatcher
        
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
            dispatcher: Optional[GameValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[GameValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or GameValidationDispatcher())
    
    @property
    def dispatcher(self) -> GameValidationDispatcher:
        return cast(GameValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: GameValidationRequest) -> ValidationResult[Game]:
        """
        Extract an Game safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Game from the result then send it to the client.
        Args:
            request: GameValidationRequest
        Result:
            ValidationResult[Game]
        Raises:
            GameValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(GameCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
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
        model = cast(Game, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: GameValidationRequest,
    ) -> ValidationResult[GameBlueprint]:
        """
        Extract an GameBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the GameBlueprint from the result then send it
                to the client.
        Args:
            request: GameValidationRequest
        Result:
            ValidationResult[GameBlueprint]
        Raises:
            GameValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(GameCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
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
        blueprint = cast(GameBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)