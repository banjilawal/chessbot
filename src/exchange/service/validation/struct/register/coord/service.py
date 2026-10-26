# src/exchange/service/validation/struct/register/coord/service.py

"""
Module: exchange.service.validation.struct.register.coord.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import CoordRegisterValidationResponse, ValidationResult
from domain import Coord, CoordBlueprint, CoordRegister, CoordRegisterBlueprint
from err import CoordRegisterValidationServiceException, CoordRegisterValidationServiceException, CoordCarrierEmptyException
from exchange import (
    CoordRegisterValidationService, RegisterValidationService, CoordRegisterValidationRequest
)
from util import LoggingLevelRouter


class CoordRegisterValidationService(
    RegisterValidationService[CoordRegister]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Coord
                _   CoordBlueprint
            products from CoordRegisterValidationService.

    Attributes:
        service: CoordRegisterValidationService
        
    Provides:
        -   def extract_model(
                    request: CoordRegisterValidationRequest
            ) -> ValidationResult[Coord]
            
        -   def extract_blueprint(
                    request: CoordRegisterValidationRequest
            ) -> ValidationResult[CoordBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[CoordRegisterValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[CoordRegisterValidationService]
        """
        super().__init__(service=service or CoordRegisterValidationService())
    
    @property
    def service(self) -> CoordRegisterValidationService:
        return cast(CoordRegisterValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: CoordRegisterValidationRequest,
    ) -> ValidationResult[CoordRegister]:
        """
        Extract a Coord safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Coord from the success response then send it 
                to the client.
        Args:
            request: CoordRegisterValidationRequest
        Result:
            ValidationResult[Coord]
        Raises:
            CoordRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordRegisterValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        register = cast(CoordRegister, response.valid_model)
        return ValidationResult.success(register)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: CoordRegisterValidationRequest,
    ) -> ValidationResult[CoordRegisterBlueprint]:
        """
        Extract a CoordBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the CoordBluprint from the success response
                then send it to the client.
        Args:
            request: CoordRegisterValidationRequest
        Result:
            ValidationResult[CoordBlueprint]
        Raises:
            CoordRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(CoordRegisterValidationResponse, result)
        if not response.valid_coord:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                CoordRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordRegisterValidationServiceException.MSG,
                    err_code=CoordRegisterValidationServiceException.ERR_CODE,
                    ex=CoordCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=CoordCarrierEmptyException.MSG,
                        err_code=CoordCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(CoordRegisterBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)