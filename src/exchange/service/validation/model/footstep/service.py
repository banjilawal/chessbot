# src/exchange/service/validation/model/footstep/service.py

"""
Module: exchange.service.validation.model.footstep.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import FootstepValidationResponse, ValidationResult
from domain import Footstep, FootstepBlueprint
from err import (
    FootstepValidationServiceException, FootstepValidationServiceException, 
    FootstepCarrierEmptyException
)
from exchange import (
    FootstepValidationService, ModelValidationService, FootstepValidationRequest
)
from util import LoggingLevelRouter


class FootstepValidationService(
    ModelValidationService[Footstep]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Footstep
                _   FootstepBlueprint
            products from FootstepValidationService.

    Attributes:
        service: FootstepValidationService
        
    Provides:
        -   def extract_model(
                    request: FootstepValidationRequest
            ) -> ValidationResult[Footstep]
            
        -   def extract_blueprint(
                    request: FootstepValidationRequest
            ) -> ValidationResult[FootstepBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[FootstepValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[FootstepValidationService]
        """
        super().__init__(service=service or FootstepValidationService())
    
    @property
    def service(self) -> FootstepValidationService:
        return cast(FootstepValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: FootstepValidationRequest,
    ) -> ValidationResult[Footstep]:
        """
        Extract a Footstep safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Footstep from the success response then send it 
                to the client.
        Args:
            request: FootstepValidationRequest
        Result:
            ValidationResult[Footstep]
        Raises:
            FootstepValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationServiceException.MSG,
                    err_code=FootstepValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(FootstepValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationServiceException.MSG,
                    err_code=FootstepValidationServiceException.ERR_CODE,
                    ex=FootstepCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FootstepCarrierEmptyException.MSG,
                        err_code=FootstepCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Footstep, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: FootstepValidationRequest,
    ) -> ValidationResult[FootstepBlueprint]:
        """
        Extract a FootstepBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the FootstepBluprint from the success response
                then send it to the client.
        Args:
            request: FootstepValidationRequest
        Result:
            ValidationResult[FootstepBlueprint]
        Raises:
            FootstepValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationServiceException.MSG,
                    err_code=FootstepValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(FootstepValidationResponse, result)
        if not response.valid_footstep:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepValidationServiceException.MSG,
                    err_code=FootstepValidationServiceException.ERR_CODE,
                    ex=FootstepCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FootstepCarrierEmptyException.MSG,
                        err_code=FootstepCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(FootstepBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)