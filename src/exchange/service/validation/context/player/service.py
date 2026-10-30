# src/exchange/service/validation/context/player/service.py

"""
Module: exchange.service.validation.context.player.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PlayerValidationResponse, ValidationResult
from domain import Player, PlayerBlueprint
from err import PlayerContextValidationServiceException, PlayerContextValidationServiceException, PlayerCarrierEmptyException
from exchange import (
    PlayerContextValidationService, ContextValidationService, PlayerValidationRequest
)
from util import LoggingLevelRouter


class PlayerContextValidationService(
    ContextValidationService[Player]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Player
                _   PlayerBlueprint
            products from PlayerContextValidationService.

    Attributes:
        service: PlayerContextValidationService
        
    Provides:
        -   def extract_context(
                    request: PlayerValidationRequest
            ) -> ValidationResult[Player]
            
        -   def extract_blueprint(
                    request: PlayerValidationRequest
            ) -> ValidationResult[PlayerBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[PlayerContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[PlayerContextValidationService]
        """
        super().__init__(service=service or PlayerContextValidationService())
    
    @property
    def service(self) -> PlayerContextValidationService:
        return cast(PlayerContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            PlayerContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerContextValidationServiceException.MSG,
                    err_code=PlayerContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerContextValidationServiceException.MSG,
                    err_code=PlayerContextValidationServiceException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Player, response.valid_context)
        return ValidationResult.success(context)
    
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
            PlayerContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerContextValidationServiceException.MSG,
                    err_code=PlayerContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(PlayerValidationResponse, result)
        if not response.valid_player:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerContextValidationServiceException.MSG,
                    err_code=PlayerContextValidationServiceException.ERR_CODE,
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