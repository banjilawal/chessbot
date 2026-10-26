# src/exchange/service/validation/struct/register/vector/service.py

"""
Module: exchange.service.validation.struct.register.vector.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import VectorRegisterValidationResponse, ValidationResult
from domain import Vector, VectorBlueprint, VectorRegister, VectorRegisterBlueprint
from err import VectorRegisterValidationServiceException, VectorRegisterValidationServiceException, VectorCarrierEmptyException
from exchange import (
    VectorRegisterValidationService, RegisterValidationService, VectorRegisterValidationRequest
)
from util import LoggingLevelRouter


class VectorRegisterValidationService(
    RegisterValidationService[VectorRegister]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorRegisterValidationService.

    Attributes:
        service: VectorRegisterValidationService
        
    Provides:
        -   def extract_model(
                    request: VectorRegisterValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorRegisterValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[VectorRegisterValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[VectorRegisterValidationService]
        """
        super().__init__(service=service or VectorRegisterValidationService())
    
    @property
    def service(self) -> VectorRegisterValidationService:
        return cast(VectorRegisterValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: VectorRegisterValidationRequest,
    ) -> ValidationResult[VectorRegister]:
        """
        Extract a Vector safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Vector from the success response then send it 
                to the client.
        Args:
            request: VectorRegisterValidationRequest
        Result:
            ValidationResult[Vector]
        Raises:
            VectorRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorRegisterValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        register = cast(VectorRegister, response.valid_model)
        return ValidationResult.success(register)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorRegisterValidationRequest,
    ) -> ValidationResult[VectorRegisterBlueprint]:
        """
        Extract a VectorBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the VectorBluprint from the success response
                then send it to the client.
        Args:
            request: VectorRegisterValidationRequest
        Result:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorRegisterValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorRegisterValidationResponse, result)
        if not response.valid_vector:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorRegisterValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorRegisterValidationServiceException.MSG,
                    err_code=VectorRegisterValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorRegisterBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)