# src/exchange/service/validation/model/attack/service.py

"""
Module: exchange.service.validation.model.attack.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackValidationResponse, ValidationResult
from domain import Encounter, AttackBlueprint
from err import AttackValidationServiceException, AttackValidationServiceException, EncounterCarrierEmptyException
from exchange import (
    AttackValidationService, ModelValidationService, AttackValidationRequest
)
from util import LoggingLevelRouter


class EncounterValidationService(
    ModelValidationService[Encounter]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Attack
                _   AttackBlueprint
            products from AttackValidationService.

    Attributes:
        service: AttackValidationService
        
    Provides:
        -   def extract_model(
                    request: AttackValidationRequest
            ) -> ValidationResult[Attack]
            
        -   def extract_blueprint(
                    request: AttackValidationRequest
            ) -> ValidationResult[AttackBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[AttackValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[AttackValidationService]
        """
        super().__init__(service=service or AttackValidationService())
    
    @property
    def service(self) -> AttackValidationService:
        return cast(AttackValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: AttackValidationRequest,
    ) -> ValidationResult[Encounter]:
        """
        Extract a Attack safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Attack from the success response then send it 
                to the client.
        Args:
            request: AttackValidationRequest
        Result:
            ValidationResult[Attack]
        Raises:
            AttackValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationServiceException.MSG,
                    err_code=AttackValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AttackValidationResponse, result)
        if not response.promoted_pawn:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationServiceException.MSG,
                    err_code=AttackValidationServiceException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Encounter, response.promoted_pawn)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AttackValidationRequest,
    ) -> ValidationResult[AttackBlueprint]:
        """
        Extract a AttackBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the AttackBluprint from the success response
                then send it to the client.
        Args:
            request: AttackValidationRequest
        Result:
            ValidationResult[AttackBlueprint]
        Raises:
            AttackValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationServiceException.MSG,
                    err_code=AttackValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AttackValidationResponse, result)
        if not response.valid_attack:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationServiceException.MSG,
                    err_code=AttackValidationServiceException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AttackBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)