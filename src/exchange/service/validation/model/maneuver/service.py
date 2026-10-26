# src/exchange/service/validation/model/maneuver/service.py

"""
Module: exchange.service.validation.model.maneuver.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverValidationResponse, ValidationResult
from domain import Maneuver, ManeuverBlueprint
from err import ManeuverValidationServiceException, ManeuverValidationServiceException, ManeuverCarrierEmptyException
from exchange import (
    ManeuverValidationService, ModelValidationService, ManeuverValidationRequest
)
from util import LoggingLevelRouter


class ManeuverValidationService(
    ModelValidationService[Maneuver]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Maneuver
                _   ManeuverBlueprint
            products from ManeuverValidationService.

    Attributes:
        service: ManeuverValidationService
        
    Provides:
        -   def extract_model(
                    request: ManeuverValidationRequest
            ) -> ValidationResult[Maneuver]
            
        -   def extract_blueprint(
                    request: ManeuverValidationRequest
            ) -> ValidationResult[ManeuverBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[ManeuverValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[ManeuverValidationService]
        """
        super().__init__(service=service or ManeuverValidationService())
    
    @property
    def service(self) -> ManeuverValidationService:
        return cast(ManeuverValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
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
            ManeuverValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationServiceException.MSG,
                    err_code=ManeuverValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ManeuverValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationServiceException.MSG,
                    err_code=ManeuverValidationServiceException.ERR_CODE,
                    ex=ManeuverCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverCarrierEmptyException.MSG,
                        err_code=ManeuverCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Maneuver, response.valid_model)
        return ValidationResult.success(model)
    
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
            ManeuverValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationServiceException.MSG,
                    err_code=ManeuverValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ManeuverValidationResponse, result)
        if not response.valid_maneuver:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ManeuverValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverValidationServiceException.MSG,
                    err_code=ManeuverValidationServiceException.ERR_CODE,
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