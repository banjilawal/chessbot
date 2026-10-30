# src/exchange/service/validation/context/arena/service.py

"""
Module: exchange.service.validation.context.arena.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ArenaValidationResponse, ValidationResult
from domain import Arena, ArenaBlueprint
from err import ArenaContextValidationServiceException, ArenaContextValidationServiceException, EmptyArenaCarrierException
from exchange import (
    ArenaContextValidationService, ContextValidationService, ArenaValidationRequest
)
from util import LoggingLevelRouter


class ArenaContextValidationService(
    ContextValidationService[Arena]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Arena
                _   ArenaBlueprint
            products from ArenaContextValidationService.

    Attributes:
        service: ArenaContextValidationService
        
    Provides:
        -   def extract_context(
                    request: ArenaValidationRequest
            ) -> ValidationResult[Arena]
            
        -   def extract_blueprint(
                    request: ArenaValidationRequest
            ) -> ValidationResult[ArenaBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[ArenaContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[ArenaContextValidationService]
        """
        super().__init__(service=service or ArenaContextValidationService())
    
    @property
    def service(self) -> ArenaContextValidationService:
        return cast(ArenaContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
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
            ArenaContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaContextValidationServiceException.MSG,
                    err_code=ArenaContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ArenaValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaContextValidationServiceException.MSG,
                    err_code=ArenaContextValidationServiceException.ERR_CODE,
                    ex=EmptyArenaCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyArenaCarrierException.MSG,
                        err_code=EmptyArenaCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Arena, response.valid_context)
        return ValidationResult.success(context)
    
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
            ArenaContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaContextValidationServiceException.MSG,
                    err_code=ArenaContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(ArenaValidationResponse, result)
        if not response.valid_arena:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                ArenaContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaContextValidationServiceException.MSG,
                    err_code=ArenaContextValidationServiceException.ERR_CODE,
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