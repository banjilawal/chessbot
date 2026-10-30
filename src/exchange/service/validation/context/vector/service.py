# src/exchange/service/validation/context/vector/service.py

"""
Module: exchange.service.validation.context.vector.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import VectorValidationResponse, ValidationResult
from domain import Vector, VectorBlueprint
from err import VectorContextValidationServiceException, VectorContextValidationServiceException, VectorCarrierEmptyException
from exchange import (
    VectorContextValidationService, ContextValidationService, VectorValidationRequest
)
from util import LoggingLevelRouter


class VectorContextValidationService(
    ContextValidationService[Vector]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Vector
                _   VectorBlueprint
            products from VectorContextValidationService.

    Attributes:
        service: VectorContextValidationService
        
    Provides:
        -   def extract_context(
                    request: VectorValidationRequest
            ) -> ValidationResult[Vector]
            
        -   def extract_blueprint(
                    request: VectorValidationRequest
            ) -> ValidationResult[VectorBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[VectorContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[VectorContextValidationService]
        """
        super().__init__(service=service or VectorContextValidationService())
    
    @property
    def service(self) -> VectorContextValidationService:
        return cast(VectorContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            VectorContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorContextValidationServiceException.MSG,
                    err_code=VectorContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorContextValidationServiceException.MSG,
                    err_code=VectorContextValidationServiceException.ERR_CODE,
                    ex=VectorCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=VectorCarrierEmptyException.MSG,
                        err_code=VectorCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Vector, response.valid_context)
        return ValidationResult.success(context)
    
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
            VectorContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorContextValidationServiceException.MSG,
                    err_code=VectorContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(VectorValidationResponse, result)
        if not response.valid_vector:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                VectorContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorContextValidationServiceException.MSG,
                    err_code=VectorContextValidationServiceException.ERR_CODE,
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