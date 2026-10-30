# src/exchange/service/validation/context/footstep/service.py

"""
Module: exchange.service.validation.context.footstep.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import FootstepValidationResponse, ValidationResult
from domain import Footstep, FootstepBlueprint
from err import (
    FootstepContextValidationServiceException, FootstepContextValidationServiceException, 
    FootstepCarrierEmptyException
)
from exchange import (
    FootstepContextValidationService, ContextValidationService, FootstepValidationRequest
)
from util import LoggingLevelRouter


class FootstepContextValidationService(
    ContextValidationService[Footstep]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Footstep
                _   FootstepBlueprint
            products from FootstepContextValidationService.

    Attributes:
        service: FootstepContextValidationService
        
    Provides:
        -   def extract_context(
                    request: FootstepValidationRequest
            ) -> ValidationResult[Footstep]
            
        -   def extract_blueprint(
                    request: FootstepValidationRequest
            ) -> ValidationResult[FootstepBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[FootstepContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[FootstepContextValidationService]
        """
        super().__init__(service=service or FootstepContextValidationService())
    
    @property
    def service(self) -> FootstepContextValidationService:
        return cast(FootstepContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            FootstepContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepContextValidationServiceException.MSG,
                    err_code=FootstepContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(FootstepValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepContextValidationServiceException.MSG,
                    err_code=FootstepContextValidationServiceException.ERR_CODE,
                    ex=FootstepCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=FootstepCarrierEmptyException.MSG,
                        err_code=FootstepCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Footstep, response.valid_context)
        return ValidationResult.success(context)
    
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
            FootstepContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepContextValidationServiceException.MSG,
                    err_code=FootstepContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(FootstepValidationResponse, result)
        if not response.valid_footstep:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                FootstepContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepContextValidationServiceException.MSG,
                    err_code=FootstepContextValidationServiceException.ERR_CODE,
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