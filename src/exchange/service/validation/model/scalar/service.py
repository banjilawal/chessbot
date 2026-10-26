# src/exchange/service/validation/model/scalar/service.py

"""
Module: exchange.service.validation.model.scalar.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ScalarValidationResponse, ValidationResult
from domain import Scalar, ScalarBlueprint
from err import ScalarValidationServiceException, ScalarValidationServiceException, ScalarCarrierEmptyException
from exchange import (
    ScalarValidationService, ModelValidationService, ScalarValidationRequest
)
from util import LoggingLevelRouter


class ScalarValidationService(
    ModelValidationService[Scalar]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Scalar
                _   ScalarBlueprint
            products from ScalarValidationService.

    Attributes:
        service: ScalarValidationService
        
    Provides:
        -   def extract_model(
                    request: ScalarValidationRequest
            ) -> ValidationResult[Scalar]
            
        -   def extract_blueprint(
                    request: ScalarValidationRequest
            ) -> ValidationResult[ScalarBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[ScalarValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[ScalarValidationService]
        """
        super().__init__(service=service or ScalarValidationService())
    
    @property
    def service(self) -> ScalarValidationService:
        return cast(ScalarValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: ScalarValidationRequest,
    ) -> ValidationResult[Scalar]:
        """
        Extract a Scalar safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Scalar from the success response then send it 
                to the client.
        Args:
            request: ScalarValidationRequest
        Result:
            ValidationResult[Scalar]
        Raises:
            ScalarValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationServiceException.MSG,
                    err_code=ScalarValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ScalarValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationServiceException.MSG,
                    err_code=ScalarValidationServiceException.ERR_CODE,
                    ex=ScalarCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ScalarCarrierEmptyException.MSG,
                        err_code=ScalarCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Scalar, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ScalarValidationRequest,
    ) -> ValidationResult[ScalarBlueprint]:
        """
        Extract a ScalarBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the ScalarBluprint from the success response
                then send it to the client.
        Args:
            request: ScalarValidationRequest
        Result:
            ValidationResult[ScalarBlueprint]
        Raises:
            ScalarValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationServiceException.MSG,
                    err_code=ScalarValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ScalarValidationResponse, result)
        if not response.valid_scalar:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ScalarValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarValidationServiceException.MSG,
                    err_code=ScalarValidationServiceException.ERR_CODE,
                    ex=ScalarCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ScalarCarrierEmptyException.MSG,
                        err_code=ScalarCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ScalarBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)