# src/exchange/service/validation/model/square/service.py

"""
Module: exchange.service.validation.model.square.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Square, SquareBlueprint
from err import SquareCarrierEmptyException, SquareValidationServiceException
from exchange import SquareValidationRequest
from microservice import ValidationMicroservice
from transit import SquareCarrier, SquareValidationDispatcher
from util import LoggingLevelRouter


class SquareValidationService(ValidationMicroservice[Square]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Square
                _   SquareBlueprint
            products from SquareValidationService.

    Attributes:
        dispatcher: SquareValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: SquareValidationRequest
            ) -> ValidationResult[Square]
            
        -   def extract_blueprint(
                    request: SquareValidationRequest
            ) -> ValidationResult[SquareBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[SquareValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[SquareValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or SquareValidationDispatcher())
    
    @property
    def dispatcher(self) -> SquareValidationDispatcher:
        return cast(SquareValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: SquareValidationRequest) -> ValidationResult[Square]:
        """
        Extract an Square safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Square from the result then send it to the client.
        Args:
            request: SquareValidationRequest
        Result:
            ValidationResult[Square]
        Raises:
            SquareValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationServiceException.MSG,
                    err_code=SquareValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(SquareCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationServiceException.MSG,
                    err_code=SquareValidationServiceException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Square, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: SquareValidationRequest,
    ) -> ValidationResult[SquareBlueprint]:
        """
        Extract an SquareBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the SquareBlueprint from the result then send it
                to the client.
        Args:
            request: SquareValidationRequest
        Result:
            ValidationResult[SquareBlueprint]
        Raises:
            SquareValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationServiceException.MSG,
                    err_code=SquareValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(SquareCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareValidationServiceException.MSG,
                    err_code=SquareValidationServiceException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(SquareBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)