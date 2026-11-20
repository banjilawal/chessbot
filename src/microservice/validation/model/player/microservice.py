# src/exchange/service/validation/model/player/service.py

"""
Module: exchange.service.validation.model.player.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Player, PlayerBlueprint
from err import PlayerCarrierEmptyException, PlayerValidationServiceException
from exchange import PlayerValidationRequest
from microservice import ValidationMicroservice
from transit import PlayerCarrier, PlayerValidationDispatcher
from util import LoggingLevelRouter


class PlayerValidationService(ValidationMicroservice[Player]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Player
                _   PlayerBlueprint
            products from PlayerValidationService.

    Attributes:
        dispatcher: PlayerValidationDispatcher
        
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
            dispatcher: Optional[PlayerValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[PlayerValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or PlayerValidationDispatcher())
    
    @property
    def dispatcher(self) -> PlayerValidationDispatcher:
        return cast(PlayerValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: PlayerValidationRequest) -> ValidationResult[Player]:
        """
        Extract an Player safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Player from the result then send it to the client.
        Args:
            request: PlayerValidationRequest
        Result:
            ValidationResult[Player]
        Raises:
            PlayerValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(PlayerCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
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
        model = cast(Player, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: PlayerValidationRequest,
    ) -> ValidationResult[PlayerBlueprint]:
        """
        Extract an PlayerBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the PlayerBlueprint from the result then send it
                to the client.
        Args:
            request: PlayerValidationRequest
        Result:
            ValidationResult[PlayerBlueprint]
        Raises:
            PlayerValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
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
        # --- Cast the payload for additional processing. ---#
        carrier = cast(PlayerCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
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
        blueprint = cast(PlayerBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)