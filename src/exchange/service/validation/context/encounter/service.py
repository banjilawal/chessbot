# src/exchange/service/validation/context/attack/service.py

"""
Module: exchange.service.validation.context.attack.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackValidationResponse, ValidationResult
from domain import Encounter, AttackBlueprint
from err import AttackContextValidationServiceException, AttackContextValidationServiceException, EncounterCarrierEmptyException
from exchange import (
    AttackContextValidationService, ContextValidationService, AttackValidationRequest
)
from util import LoggingLevelRouter


class EncounterContextValidationService(
    ContextValidationService[Encounter]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Attack
                _   AttackBlueprint
            products from AttackContextValidationService.

    Attributes:
        service: AttackContextValidationService
        
    Provides:
        -   def extract_context(
                    request: AttackValidationRequest
            ) -> ValidationResult[Attack]
            
        -   def extract_blueprint(
                    request: AttackValidationRequest
            ) -> ValidationResult[AttackBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[AttackContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[AttackContextValidationService]
        """
        super().__init__(service=service or AttackContextValidationService())
    
    @property
    def service(self) -> AttackContextValidationService:
        return cast(AttackContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            AttackContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackContextValidationServiceException.MSG,
                    err_code=AttackContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AttackValidationResponse, result)
        if not response.promoted_pawn:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackContextValidationServiceException.MSG,
                    err_code=AttackContextValidationServiceException.ERR_CODE,
                    ex=EncounterCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EncounterCarrierEmptyException.MSG,
                        err_code=EncounterCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Encounter, response.promoted_pawn)
        return ValidationResult.success(context)
    
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
            AttackContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackContextValidationServiceException.MSG,
                    err_code=AttackContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AttackValidationResponse, result)
        if not response.valid_attack:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackContextValidationServiceException.MSG,
                    err_code=AttackContextValidationServiceException.ERR_CODE,
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