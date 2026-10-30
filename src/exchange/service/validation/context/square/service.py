# src/exchange/service/validation/context/square/service.py

"""
Module: exchange.service.validation.context.square.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import SquareValidationResponse, ValidationResult
from domain import Square, SquareBlueprint
from err import SquareContextValidationServiceException, SquareContextValidationServiceException, SquareCarrierEmptyException
from exchange import (
    SquareContextValidationService, ContextValidationService, SquareValidationRequest
)
from util import LoggingLevelRouter


class SquareContextValidationService(
    ContextValidationService[Square]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Square
                _   SquareBlueprint
            products from SquareContextValidationService.

    Attributes:
        service: SquareContextValidationService
        
    Provides:
        -   def extract_context(
                    request: SquareValidationRequest
            ) -> ValidationResult[Square]
            
        -   def extract_blueprint(
                    request: SquareValidationRequest
            ) -> ValidationResult[SquareBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[SquareContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[SquareContextValidationService]
        """
        super().__init__(service=service or SquareContextValidationService())
    
    @property
    def service(self) -> SquareContextValidationService:
        return cast(SquareContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: SquareValidationRequest,
    ) -> ValidationResult[Square]:
        """
        Extract a Square safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Square from the success response then send it 
                to the client.
        Args:
            request: SquareValidationRequest
        Result:
            ValidationResult[Square]
        Raises:
            SquareContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidationServiceException.MSG,
                    err_code=SquareContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidationServiceException.MSG,
                    err_code=SquareContextValidationServiceException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Square, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: SquareValidationRequest,
    ) -> ValidationResult[SquareBlueprint]:
        """
        Extract a SquareBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the SquareBluprint from the success response
                then send it to the client.
        Args:
            request: SquareValidationRequest
        Result:
            ValidationResult[SquareBlueprint]
        Raises:
            SquareContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidationServiceException.MSG,
                    err_code=SquareContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareValidationResponse, result)
        if not response.valid_square:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareContextValidationServiceException.MSG,
                    err_code=SquareContextValidationServiceException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(SquareBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)