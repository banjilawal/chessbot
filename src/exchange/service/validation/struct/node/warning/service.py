# src/exchange/service/validation/struct/node/warning/service.py

"""
Module: exchange.service.validation.struct.node.warning.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import EncounterWarningNode
from exchange import NodeValidationService
from util import LoggingLevelRouter


class EncounterWarningNodeValidationService(
    NodeValidationService[EncounterWarningNode]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Warning
                _   WarningBlueprint
            products from WarningNodeValidationService.

    Attributes:
        service: WarningNodeValidationService
        
    Provides:
        -   def extract_model(
                    request: WarningNodeValidationRequest
            ) -> ValidationResult[Warning]
            
        -   def extract_blueprint(
                    request: WarningNodeValidationRequest
            ) -> ValidationResult[WarningBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[WarningNodeValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[WarningNodeValidationService]
        """
        super().__init__(service=service or WarningNodeValidationService())
    
    @property
    def service(self) -> WarningNodeValidationService:
        return cast(WarningNodeValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: EncounterWarningNodeValidationRequest,
    ) -> ValidationResult[EncounterWarningNode]:
        """
        Extract a Warning safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Warning from the success response then send it 
                to the client.
        Args:
            request: WarningNodeValidationRequest
        Result:
            ValidationResult[Warning]
        Raises:
            WarningNodeValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationServiceException.MSG,
                    err_code=WarningNodeValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(WarningNodeValidationResponse, result)
        if not response.valid_node:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationServiceException.MSG,
                    err_code=WarningNodeValidationServiceException.ERR_CODE,
                    ex=EmptyWarningCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyWarningCarrierException.MSG,
                        err_code=EmptyWarningCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        node = cast(EncounterWarningNode, response.valid_node)
        return ValidationResult.success(node)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: EncounterWarningNodeValidationRequest,
    ) -> ValidationResult[EncounterWarningNodeBlueprint]:
        """
        Extract a WarningBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the WarningBluprint from the success response
                then send it to the client.
        Args:
            request: WarningNodeValidationRequest
        Result:
            ValidationResult[WarningBlueprint]
        Raises:
            WarningNodeValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationServiceException.MSG,
                    err_code=WarningNodeValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(WarningNodeValidationResponse, result)
        if not response.valid_warning:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                WarningNodeValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=WarningNodeValidationServiceException.MSG,
                    err_code=WarningNodeValidationServiceException.ERR_CODE,
                    ex=EmptyWarningCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyWarningCarrierException.MSG,
                        err_code=EmptyWarningCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(EncounterWarningNodeBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)