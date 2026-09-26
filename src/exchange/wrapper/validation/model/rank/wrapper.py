# src/exchange/wrapper/validation/model/rank/wrapper.py

"""
Module: exchange.wrapper.validation.model.rank.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import RankValidationResponse, ValidationResult
from domain import Rank, RankBlueprint
from err import RankValidationResponderException, RankValidationResponseWrapperException, EmptyRankCarrierException
from exchange import (
    RankValidationResponder, ModelValidationResponseWrapper, RankValidationRequest
)
from util import LoggingLevelRouter


class RankValidationResponseWrapper(
    ModelValidationResponseWrapper[Rank]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Rank
                _   RankBlueprint
            products from RankValidationResponder.

    Attributes:
        responder: RankValidationResponder
        
    Provides:
        -   def extract_model(
                    request: RankValidationRequest
            ) -> ValidationResult[Rank]
            
        -   def extract_blueprint(
                    request: RankValidationRequest
            ) -> ValidationResult[RankBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[RankValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[RankValidationResponder]
        """
        super().__init__(responder=responder or RankValidationResponder())
    
    @property
    def responder(self) -> RankValidationResponder:
        return cast(RankValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: RankValidationRequest,
    ) -> ValidationResult[Rank]:
        """
        Extract a Rank safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Rank from the success response then send it 
                to the client.
        Args:
            request: RankValidationRequest
        Result:
            ValidationResult[Rank]
        Raises:
            RankValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationResponseWrapperException.MSG,
                    err_code=RankValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(RankValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationResponderException.MSG,
                    err_code=RankValidationResponderException.ERR_CODE,
                    ex=EmptyRankCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyRankCarrierException.MSG,
                        err_code=EmptyRankCarrierException.ERR_CODE,
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
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the RankBluprint from the success response
                then send it to the client.
        Args:
            request: RankValidationRequest
        Result:
            ValidationResult[RankBlueprint]
        Raises:
            RankValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationResponseWrapperException.MSG,
                    err_code=RankValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(RankValidationResponse, result)
        if not response.valid_rank:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                RankValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankValidationResponderException.MSG,
                    err_code=RankValidationResponderException.ERR_CODE,
                    ex=EmptyRankCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyRankCarrierException.MSG,
                        err_code=EmptyRankCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(RankBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)