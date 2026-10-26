# src/exchange/service/validation/model/rank/service.py

"""
Module: exchange.service.validation.model.rank.service
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RankValidationResponse, ValidationResult
from domain import Rank, RankBlueprint
from err import RankValidationServiceException, RankValidationServiceException, RankCarrierEmptyException
from exchange import (
    RankValidationService, ModelValidationService, RankValidationRequest
)
from util import LoggingLevelRouter


class RankValidationService(
    ModelValidationService[Rank]
):
    """
    Role
        -   Service

    Responsibilities:
        1.  Extract either safe:
                -   Rank
                _   RankBlueprint
            products from RankValidationService.

    Attributes:
        service: RankValidationService
        
    Provides:
        -   def extract_model(
                    request: RankValidationRequest
            ) -> ValidationResult[Rank]
            
        -   def extract_blueprint(
                    request: RankValidationRequest
            ) -> ValidationResult[RankBlueprint]

    Super Class:
        ValidationService
    """
    
    def __init__(
            self,
            service: Optional[RankValidationService] | None = None,
    ):
        """
        Args:
            service: Optional[RankValidationService]
        """
        super().__init__(service=service or RankValidationService())
    
    @property
    def service(self) -> RankValidationService:
        return cast(RankValidationService, super().service)
    

    @LoggingLevelRouter.monitor
    def extract_model(
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
            RankValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(RankValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
                    ex=RankCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=RankCarrierEmptyException.MSG,
                        err_code=RankCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Rank, response.valid_model)
        return ValidationResult.success(model)
    
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
            RankValidationServiceException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.service.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(RankValidationResponse, result)
        if not response.valid_rank:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationServiceException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationServiceException.MSG,
                    err_code=RankValidationServiceException.ERR_CODE,
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