# src/exchange/service/validation/model/player/service.py

"""
Module: exchange.service.validation.model.player.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PlayerValidationResponse, ValidationResult
from domain import Player, PlayerBlueprint
from err import PlayerValidationServiceException, PlayerValidationServiceException, PlayerCarrierEmptyException
from exchange import (
    PlayerValidationService, ModelValidationService, PlayerValidationRequest
)
from util import LoggingLevelRouter


class PlayerValidationService(
    ModelValidationService[Player]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Player
                _   PlayerBlueprint
            products from PlayerValidationService.

    Attributes:
        service: PlayerValidationService
        
    Provides:
        -   def extract_model(
                    request: PlayerValidationRequest
            ) -> ValidationResult[Player]
            
        -   def extract_blueprint(
                    request: PlayerValidationRequest
            ) -> ValidationResult[PlayerBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[PlayerValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[PlayerValidationService]
        """
        super().__init__(service=service or PlayerValidationService())
    
    @property
    def service(self) -> PlayerValidationService:
        return cast(PlayerValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: PlayerValidationRequest,
    ) -> ValidationResult[Player]:
        """
        Extract a Player safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Player from the success response then send it 
                to the client.
        Args:
            request: PlayerValidationRequest
        Result:
            ValidationResult[Player]
        Raises:
            PlayerValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationServiceException.MSG,
                    err_code=PlayerValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationServiceException.MSG,
                    err_code=PlayerValidationServiceException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Player, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: PlayerValidationRequest,
    ) -> ValidationResult[PlayerBlueprint]:
        """
        Extract a PlayerBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the PlayerBluprint from the success response
                then send it to the client.
        Args:
            request: PlayerValidationRequest
        Result:
            ValidationResult[PlayerBlueprint]
        Raises:
            PlayerValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationServiceException.MSG,
                    err_code=PlayerValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerValidationResponse, result)
        if not response.valid_player:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerValidationServiceException.MSG,
                    err_code=PlayerValidationServiceException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(PlayerBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)