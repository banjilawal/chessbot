# src/exchange/service/validation/struct/register/square/service.py

"""
Module: exchange.service.validation.struct.register.square.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import SquareRegisterValidationResponse, ValidationResult
from domain import SquareRegister, SquareRegisterBlueprint
from err import SquareCarrierEmptyException, SquareRegisterValidationServiceException
from exchange import RegisterValidationService, SquareRegisterValidationRequest
from util import LoggingLevelRouter


class SquareRegisterValidationService(
    RegisterValidationService[SquareRegister]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Square
                _   SquareBlueprint
            products from SquareRegisterValidationService.

    Attributes:
        service: SquareRegisterValidationService
        
    Provides:
        -   def extract_model(
                    request: SquareRegisterValidationRequest
            ) -> ValidationResult[Square]
            
        -   def extract_blueprint(
                    request: SquareRegisterValidationRequest
            ) -> ValidationResult[SquareBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[SquareRegisterValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[SquareRegisterValidationService]
        """
        super().__init__(service=service or SquareRegisterValidationService())
    
    @property
    def service(self) -> SquareRegisterValidationService:
        return cast(SquareRegisterValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: SquareRegisterValidationRequest,
    ) -> ValidationResult[SquareRegister]:
        """
        Extract a Square safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Square from the success response then send it 
                to the client.
        Args:
            request: SquareRegisterValidationRequest
        Result:
            ValidationResult[Square]
        Raises:
            SquareRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareRegisterValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        register = cast(SquareRegister, response.valid_model)
        return ValidationResult.success(register)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: SquareRegisterValidationRequest,
    ) -> ValidationResult[SquareRegisterBlueprint]:
        """
        Extract a SquareBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the SquareBluprint from the success response
                then send it to the client.
        Args:
            request: SquareRegisterValidationRequest
        Result:
            ValidationResult[SquareBlueprint]
        Raises:
            SquareRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(SquareRegisterValidationResponse, result)
        if not response.valid_square:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                SquareRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareRegisterValidationServiceException.MSG,
                    err_code=SquareRegisterValidationServiceException.ERR_CODE,
                    ex=SquareCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareCarrierEmptyException.MSG,
                        err_code=SquareCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(SquareRegisterBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)