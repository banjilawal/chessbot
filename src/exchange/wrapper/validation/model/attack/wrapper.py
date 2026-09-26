# src/exchange/wrapper/validation/model/attack/wrapper.py

"""
Module: exchange.wrapper.validation.model.attack.wrapper
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackValidationResponse, ValidationResult
from domain import Attack, AttackBlueprint
from err import AttackValidationResponderException, AttackValidationResponseWrapperException, EmptyAttackCarrierException
from exchange import (
    AttackValidationResponder, ModelValidationResponseWrapper, AttackValidationRequest
)
from util import LoggingLevelRouter


class AttackValidationResponseWrapper(
    ModelValidationResponseWrapper[Attack]
):
    """
    Role
        -   Wrapper

    Responsibilities:
        1.  Extract either safe:
                -   Attack
                _   AttackBlueprint
            products from AttackValidationResponder.

    Attributes:
        responder: AttackValidationResponder
        
    Provides:
        -   def extract_model(
                    request: AttackValidationRequest
            ) -> ValidationResult[Attack]
            
        -   def extract_blueprint(
                    request: AttackValidationRequest
            ) -> ValidationResult[AttackBlueprint]

    Super Class:
        ValidationResponseWrapper
    """
    
    def __init__(
            self,
            responder: Optional[AttackValidationResponder] | None = None,
    ):
        """
        Args:
            responder: Optional[AttackValidationResponder]
        """
        super().__init__(responder=responder or AttackValidationResponder())
    
    @property
    def responder(self) -> AttackValidationResponder:
        return cast(AttackValidationResponder, super().responder)
    

    @LoggingLevelRouter.monitor
    def extract_model(
            self, 
            request: AttackValidationRequest,
    ) -> ValidationResult[Attack]:
        """
        Extract a Attack safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the Attack from the success response then send it 
                to the client.
        Args:
            request: AttackValidationRequest
        Result:
            ValidationResult[Attack]
        Raises:
            AttackValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationResponseWrapperException.MSG,
                    err_code=AttackValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AttackValidationResponse, result)
        if not response.valid_model:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationResponderException.MSG,
                    err_code=AttackValidationResponderException.ERR_CODE,
                    ex=EmptyAttackCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAttackCarrierException.MSG,
                        err_code=EmptyAttackCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        model = cast(Attack, response.valid_model)
        return ValidationResult.success(model)
    
    @LoggingLevelRouter.monitor
    def extract_blueprint(
            self,
            request: AttackValidationRequest,
    ) -> ValidationResult[AttackBlueprint]:
        """
        Extract a AttackBlueprint safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if the responder
                fails.
            2.  Otherwise, extract the AttackBluprint from the success response
                then send it to the client.
        Args:
            request: AttackValidationRequest
        Result:
            ValidationResult[AttackBlueprint]
        Raises:
            AttackValidationResponseWrapperException
        """
        method = f"{self.__class__.__name__}.extract_model"
        
        # Handle the case that a failure response is received.
        result = self.responder.execute(request)
        if result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationResponseWrapperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationResponseWrapperException.MSG,
                    err_code=AttackValidationResponseWrapperException.ERR_CODE,
                    ex=result.exception,
                )
            )
        response = cast(AttackValidationResponse, result)
        if not response.valid_attack:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                AttackValidationResponderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackValidationResponderException.MSG,
                    err_code=AttackValidationResponderException.ERR_CODE,
                    ex=EmptyAttackCarrierException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=EmptyAttackCarrierException.MSG,
                        err_code=EmptyAttackCarrierException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        blueprint = cast(AttackBlueprint, response.valid_blueprint)
        return ValidationResult.success(blueprint)