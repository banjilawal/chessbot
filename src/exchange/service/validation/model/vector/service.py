# src/exchange/service/validation/model/vector/service.py

"""
Module: exchange.service.validation.model.vector.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import VectorValidationResponse, ValidationResult
from domain import Vector, VectorBlueprint
from err import VectorValidationServiceException, VectorValidationServiceException, VectorCarrierEmptyException
from exchange import (
    VectorValidationService, ModelValidationService, VectorValidationRequest
)
from util import LoggingLevelRouter


class VectorValidationService(
    ModelValidationService[Vector]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorValidationService.

    Attributes:
        service: VectorValidationService
        
    Provides:
        -   def extract_model(
                    request: VectorValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[VectorValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[VectorValidationService]
        """
        super().__init__(service=service or VectorValidationService())
    
    @property
    def service(self) -> VectorValidationService:
        return cast(VectorValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: VectorValidationRequest,
    ) -> ValidationResult[Vector]:
        """
        Extract a Vector safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Vector from the success response then send it 
                to the client.
        Args:
            request: VectorValidationRequest
        Result:
            ValidationResult[Vector]
        Raises:
            VectorValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Vector, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: VectorValidationRequest,
    ) -> ValidationResult[VectorBlueprint]:
        """
        Extract a VectorBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the VectorBluprint from the success response
                then send it to the client.
        Args:
            request: VectorValidationRequest
        Result:
            ValidationResult[VectorBlueprint]
        Raises:
            VectorValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorValidationResponse, result)
        if not response.valid_vector:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorValidationServiceException.MSG,
                    err_code=VectorValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(VectorBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)