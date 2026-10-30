# src/exchange/service/validation/context/coord/service.py

"""
Module: exchange.service.validation.context.coord.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CoordValidationResponse, ValidationResult
from domain import Coord, CoordBlueprint
from err import CoordContextValidationServiceException, CoordContextValidationServiceException, CoordCarrierEmptyException
from exchange import (
    CoordContextValidationService, ContextValidationService, CoordValidationRequest
)
from util import LoggingLevelRouter


class CoordContextValidationService(
    ContextValidationService[Coord]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from CoordContextValidationService.

    Attributes:
        service: CoordContextValidationService
        
    Provides:
        -   def extract_context(
                    request: CoordValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: CoordValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[CoordContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[CoordContextValidationService]
        """
        super().__init__(service=service or CoordContextValidationService())
    
    @property
    def service(self) -> CoordContextValidationService:
        return cast(CoordContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: CoordValidationRequest,
    ) -> ValidationResult[Coord]:
        """
        Extract a Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Coord from the success response then send it 
                to the client.
        Args:
            request: CoordValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            CoordContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextValidationServiceException.MSG,
                    err_code=CoordContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextValidationServiceException.MSG,
                    err_code=CoordContextValidationServiceException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Coord, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: CoordValidationRequest,
    ) -> ValidationResult[CoordBlueprint]:
        """
        Extract a CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the CoordBluprint from the success response
                then send it to the client.
        Args:
            request: CoordValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            CoordContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextValidationServiceException.MSG,
                    err_code=CoordContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordValidationResponse, result)
        if not response.valid_coord:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordContextValidationServiceException.MSG,
                    err_code=CoordContextValidationServiceException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(CoordBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)