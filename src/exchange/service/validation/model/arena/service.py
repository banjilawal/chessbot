# src/exchange/service/validation/model/arena/service.py

"""
Module: exchange.service.validation.model.arena.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ArenaValidationResponse, ValidationResult
from domain import Arena, ArenaBlueprint
from err import ArenaValidationServiceException, ArenaValidationServiceException, EmptyArenaCarrierException
from exchange import (
    ArenaValidationService, ModelValidationService, ArenaValidationRequest
)
from util import LoggingLevelRouter


class ArenaValidationService(
    ModelValidationService[Arena]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Arena
                _   ArenaBlueprint
            products from ArenaValidationService.

    Attributes:
        service: ArenaValidationService
        
    Provides:
        -   def extract_model(
                    request: ArenaValidationRequest
            ) -> ValidationResult[Arena]
            
        -   def extract_blueprint(
                    request: ArenaValidationRequest
            ) -> ValidationResult[ArenaBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[ArenaValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[ArenaValidationService]
        """
        super().__init__(service=service or ArenaValidationService())
    
    @property
    def service(self) -> ArenaValidationService:
        return cast(ArenaValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: ArenaValidationRequest,
    ) -> ValidationResult[Arena]:
        """
        Extract a Arena safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Arena from the success response then send it 
                to the client.
        Args:
            request: ArenaValidationRequest
        Result:
            ValidationResult[Arena]
        Raises:
            ArenaValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ArenaValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=EmptyArenaCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyArenaCarrierException.MSG,
                        err_code=EmptyArenaCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Arena, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: ArenaValidationRequest,
    ) -> ValidationResult[ArenaBlueprint]:
        """
        Extract a ArenaBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the ArenaBluprint from the success response
                then send it to the client.
        Args:
            request: ArenaValidationRequest
        Result:
            ValidationResult[ArenaBlueprint]
        Raises:
            ArenaValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ArenaValidationResponse, result)
        if not response.valid_arena:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaValidationServiceException.MSG,
                    err_code=ArenaValidationServiceException.ERR_CODE,
                    ex=EmptyArenaCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyArenaCarrierException.MSG,
                        err_code=EmptyArenaCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(ArenaBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)