# src/exchange/service/validation/context/maneuver/service.py

"""
Module: exchange.service.validation.context.maneuver.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverValidationResponse, ValidationResult
from domain import Maneuver, ManeuverBlueprint
from err import ManeuverContextValidationServiceException, ManeuverContextValidationServiceException, ManeuverCarrierEmptyException
from exchange import (
    ManeuverContextValidationService, ContextValidationService, ManeuverValidationRequest
)
from util import LoggingLevelRouter


class ManeuverContextValidationService(
    ContextValidationService[Maneuver]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Maneuver
                _   ManeuverBlueprint
            products from ManeuverContextValidationService.

    Attributes:
        service: ManeuverContextValidationService
        
    Provides:
        -   def extract_context(
                    request: ManeuverValidationRequest
            ) -> ValidationResult[Maneuver]
            
        -   def extract_blueprint(
                    request: ManeuverValidationRequest
            ) -> ValidationResult[ManeuverBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[ManeuverContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[ManeuverContextValidationService]
        """
        super().__init__(service=service or ManeuverContextValidationService())
    
    @property
    def service(self) -> ManeuverContextValidationService:
        return cast(ManeuverContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: ManeuverValidationRequest,
    ) -> ValidationResult[Maneuver]:
        """
        Extract a Maneuver safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Maneuver from the success response then send it 
                to the client.
        Args:
            request: ManeuverValidationRequest
        Result:
            ValidationResult[Maneuver]
        Raises:
            ManeuverContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverContextValidationServiceException.MSG,
                    err_code=ManeuverContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ManeuverValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverContextValidationServiceException.MSG,
                    err_code=ManeuverContextValidationServiceException.ERR_CODE,
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Maneuver, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ManeuverValidationRequest,
    ) -> ValidationResult[ManeuverBlueprint]:
        """
        Extract a ManeuverBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the ManeuverBluprint from the success response
                then send it to the client.
        Args:
            request: ManeuverValidationRequest
        Result:
            ValidationResult[ManeuverBlueprint]
        Raises:
            ManeuverContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverContextValidationServiceException.MSG,
                    err_code=ManeuverContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ManeuverValidationResponse, result)
        if not response.valid_maneuver:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverContextValidationServiceException.MSG,
                    err_code=ManeuverContextValidationServiceException.ERR_CODE,
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ManeuverBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)