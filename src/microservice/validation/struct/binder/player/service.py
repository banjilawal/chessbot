# src/exchange/service/validation/struct/binder/player/service.py

"""
Module: exchange.service.validation.struct.binder.player.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import PlayerBinderValidationResponse, ValidationResult
from domain import Player, PlayerBlueprint, PlayerBinder, PlayerBinderBlueprint
from err import PlayerBinderValidationServiceException, PlayerBinderValidationServiceException, PlayerCarrierEmptyException
from exchange import (
    PlayerBinderValidationService, BinderValidationService, PlayerBinderValidationRequest
)
from util import LoggingLevelRouter


class PlayerBinderValidationService(
    BinderValidationService[PlayerBinder]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Player
                _   PlayerBlueprint
            products from PlayerBinderValidationService.

    Attributes:
        dispatcher: PlayerBinderValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: PlayerBinderValidationRequest
            ) -> ValidationResult[Player]
            
        -   def extract_blueprint(
                    request: PlayerBinderValidationRequest
            ) -> ValidationResult[PlayerBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[PlayerBinderValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerBinderValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or PlayerBinderValidationDispatcher())
    
    @property
    def dispatcher(self) -> PlayerBinderValidationDispatcher:
        return cast(PlayerBinderValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: PlayerBinderValidationRequest,
    ) -> ValidationResult[PlayerBinder]:
        """
        Extract a Player safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Player from the success response then send it 
                to the client.
        Args:
            request: PlayerBinderValidationRequest
        Result:
            ValidationResult[Player]
        Raises:
            PlayerBinderValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.dispatcher.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationServiceException.MSG,
                    err_code=PlayerBinderValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        carrier = cast(PlayerBinderValidationResponse, result)
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationServiceException.MSG,
                    err_code=PlayerBinderValidationServiceException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        binder = cast(PlayerBinder, carrier.has_model)
        return ValidationResult.success(binder)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: PlayerBinderValidationRequest,
    ) -> ValidationResult[PlayerBinderBlueprint]:
        """
        Extract a PlayerBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the PlayerBluprint from the success response
                then send it to the client.
        Args:
            request: PlayerBinderValidationRequest
        Result:
            ValidationResult[PlayerBlueprint]
        Raises:
            PlayerBinderValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.dispatcher.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationServiceException.MSG,
                    err_code=PlayerBinderValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        carrier = cast(PlayerBinderValidationResponse, result)
        if not response.valid_player:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                PlayerBinderValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBinderValidationServiceException.MSG,
                    err_code=PlayerBinderValidationServiceException.ERR_CODE,
                    ex=PlayerCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PlayerCarrierEmptyException.MSG,
                        err_code=PlayerCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(PlayerBinderBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)