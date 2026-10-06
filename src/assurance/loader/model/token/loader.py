# src/assurance/load/model/token/loader.py

"""
Module: assurance.load.model.token.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ModelLoader, TokenValidatorToolkit
from domain import Token, TokenBlueprint, TokenPrimeExtract
from err import (
    TokenCarrierEmptyException, TokenLoaderException, TokenValidationRequestNullException
)
from exchange import TokenValidationRequest
from transit import TokenCarrier

from util import LoggingLevelRouter


class TokenLoader(ModelLoader[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run type safety checks on a Candidate for:
            -   TokenValidationRequest
            -   TokenCarrier
            -   TokenBlueprint

    Attributes:
        toolkit: TokenValidatorToolkit

    Provides:
        -   def execute(
                    candidate: Any
            ) -> ValidationResult[TokenPrimeExtract[T]

    Super Class:
        ModelLoader
    """
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ValidationResult[TokenPrimeExtract]:
        """
        Extract the TokenBlueprint to validate the candidate.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                -   The candidate is null or not a TokenValidatorRequest.
                -   The request payload is either:
                        -   Null
                        -   Not a TokenCarrier
                        -   An empty TokenCarrier.
                -   A blueprint cannot be extracted from the carrier.
            2.  Otherwise, pack the original carrier and the blueprint in a TokenPrimeExtract
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenPrimeExtract]
        Raises:
            TokenLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming_result = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_model=TokenValidationRequest,
            null_exception=TokenValidationRequestNullException(),
        )
        if priming_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenLoaderException.MSG,
                    err_code=TokenLoaderException.ERR_CODE,
                    ex=priming_result.exception,
                )
            )
        # --- Cast priming_result to request for additional tests. ---#
        request = cast(Type[TokenValidationRequest], priming_result.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_model=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenLoaderException.MSG,
                    err_code=TokenLoaderException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast carrier_validation payload to carrier then extract blueprint. ---#
        carrier = cast(TokenCarrier, carrier_validation.payload)
        blueprint = carrier.extract_blueprint()
        
        # Handle the case that the blueprint is null.
        if blueprint is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenLoaderException.MSG,
                    err_code=TokenLoaderException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = TokenPrimeExtract(reference=carrier, safe_blueprint=blueprint)
        return ValidationResult.success(extract)