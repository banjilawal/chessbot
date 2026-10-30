# src/exchange/service/validation/context/rank/service.py

"""
Module: exchange.service.validation.context.rank.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RankValidationResponse, ValidationResult
from domain import Rank, RankBlueprint
from err import RankContextValidationServiceException, RankContextValidationServiceException, RankCarrierEmptyException
from exchange import (
    RankContextValidationService, ContextValidationService, RankValidationRequest
)
from util import LoggingLevelRouter


class RankContextValidationService(
    ContextValidationService[Rank]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Rank
                _   RankBlueprint
            products from RankContextValidationService.

    Attributes:
        service: RankContextValidationService
        
    Provides:
        -   def extract_context(
                    request: RankValidationRequest
            ) -> ValidationResult[Rank]
            
        -   def extract_blueprint(
                    request: RankValidationRequest
            ) -> ValidationResult[RankBlueprint]

    Super Class:
        ContextValidationService
    """
    
    def __init__(
            self,
            service: Optional[RankContextValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[RankContextValidationService]
        """
        super().__init__(service=service or RankContextValidationService())
    
    @property
    def service(self) -> RankContextValidationService:
        return cast(RankContextValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_context(
            self, 
            request: RankValidationRequest,
    ) -> ValidationResult[Rank]:
        """
        Extract a Rank safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the Rank from the success response then send it 
                to the client.
        Args:
            request: RankValidationRequest
        Result:
            ValidationResult[Rank]
        Raises:
            RankContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankContextValidationServiceException.MSG,
                    err_code=RankContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(RankValidationResponse, result)
        if not response.valid_context:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankContextValidationServiceException.MSG,
                    err_code=RankContextValidationServiceException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        context = cast(Rank, response.valid_context)
        return ValidationResult.success(context)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: RankValidationRequest,
    ) -> ValidationResult[RankBlueprint]:
        """
        Extract a RankBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the service
                fails.
            2.  Otherwise, extract the RankBluprint from the success response
                then send it to the client.
        Args:
            request: RankValidationRequest
        Result:
            ValidationResult[RankBlueprint]
        Raises:
            RankContextValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_context"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankContextValidationServiceException.MSG,
                    err_code=RankContextValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(RankValidationResponse, result)
        if not response.valid_rank:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankContextValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankContextValidationServiceException.MSG,
                    err_code=RankContextValidationServiceException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(RankBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)