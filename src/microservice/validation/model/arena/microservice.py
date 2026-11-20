# src/exchange/service/validation/model/arena/service.py

"""
Module: exchange.service.validation.model.arena.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Arena, ArenaBlueprint
from err import ArenaCarrierEmptyException, ArenaValidationServiceException
from exchange import ArenaValidationRequest
from microservice import ValidationMicroservice
from transit import ArenaCarrier, ArenaValidationDispatcher
from util import LoggingLevelRouter


class ArenaValidationService(ValidationMicroservice[Arena]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Arena
                _   ArenaBlueprint
            products from ArenaValidationService.

    Attributes:
        dispatcher: ArenaValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: ArenaValidationRequest
            ) -> ValidationResult[Arena]
            
        -   def extract_blueprint(
                    request: ArenaValidationRequest
            ) -> ValidationResult[ArenaBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[ArenaValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[ArenaValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or ArenaValidationDispatcher())
    
    @property
    def dispatcher(self) -> ArenaValidationDispatcher:
        return cast(ArenaValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: ArenaValidationRequest) -> ValidationResult[Arena]:
        """
        Extract an Arena safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Arena from the result then send it to the client.
        Args:
            request: ArenaValidationRequest
        Result:
            ValidationResult[Arena]
        Raises:
            ArenaValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(ArenaCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=ArenaCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ArenaCarrierEmptyException.MSG,
                        err_code=ArenaCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Arena, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ArenaValidationRequest,
    ) -> ValidationResult[ArenaBlueprint]:
        """
        Extract an ArenaBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the ArenaBlueprint from the result then send it
                to the client.
        Args:
            request: ArenaValidationRequest
        Result:
            ValidationResult[ArenaBlueprint]
        Raises:
            ArenaValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(ArenaCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=ArenaCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ArenaCarrierEmptyException.MSG,
                        err_code=ArenaCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ArenaBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)