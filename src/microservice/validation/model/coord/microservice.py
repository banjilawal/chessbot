# src/exchange/service/validation/model/coord/service.py

"""
Module: exchange.service.validation.model.coord.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from domain import Coord, CoordBlueprint
from err import CoordCarrierEmptyException, CoordValidationServiceException
from exchange import CoordValidationRequest
from microservice import ValidationMicroservice
from transit import CoordCarrier, CoordValidationDispatcher
from util import LoggingLevelRouter


class CoordValidationService(ValidationMicroservice[Coord]):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from CoordValidationService.

    Attributes:
        dispatcher: CoordValidationDispatcher
        
    Provides:
        -   def extract_model(
                    request: CoordValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: CoordValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            dispatcher: Optional[CoordValidationDispatcher] | None = None,
    ):
        """
        Args:
            dispatcher: Optional[CoordValidationDispatcher]
        """
        super().__init__(dispatcher=dispatcher or CoordValidationDispatcher())
    
    @property
    def dispatcher(self) -> CoordValidationDispatcher:
        return cast(CoordValidationDispatcher, super().dispatcher)
    

    @LoggingLevelRouter.monitor
    def extract_model(self, request: CoordValidationRequest) -> ValidationResult[Coord]:
        """
        Extract an Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the Coord from the result then send it to the client.
        Args:
            request: CoordValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            CoordValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationServiceException.MSG,
                    err_code=CoordValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(CoordCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationServiceException.MSG,
                    err_code=CoordValidationServiceException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Coord, carrier.entity)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: CoordValidationRequest,
    ) -> ValidationResult[CoordBlueprint]:
        """
        Extract an CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the dispatcher
                fails.
            2.  Otherwise, extract the CoordBlueprint from the result then send it
                to the client.
        Args:
            request: CoordValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            CoordValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # --- Handoff the request for assignment to a worker. ---#
        result = self.dispatcher.execute(request)
        
        # Handle the case that safety is not certified.
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationServiceException.MSG,
                    err_code=CoordValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast the payload for additional processing. ---#
        carrier = cast(CoordCarrier, result.payload)
        
        # Handle the case that the carrier has the wrong product.
        if not carrier.has_blueprint:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordValidationServiceException.MSG,
                    err_code=CoordValidationServiceException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(CoordBlueprint, carrier.entity)
        return ValidationResult.success(blueprint)