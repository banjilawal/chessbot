# src/assurance/load/context/token/loader.py

"""
Module: assurance.load.context.token.loader
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, Type, cast

from artifcat import ValidationResult
from assurance import ContextValidationLoader, TokenValidatorToolkit
from domain import Token, TokenBlueprint, Token
from err import (
    TokenCarrierEmptyException, TokenContextValidationLoaderException, TokenValidationRequestNullException
)
from exchange import TokenValidationRequest
from transit import TokenCarrier

from util import LoggingLevelRouter


class TokenContextValidationLoader(ContextValidationLoader[Token]):
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
            ) -> ValidationResult[Token[T]

    Super Class:
        ContextLoader
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
    def execute(self, candidate: Any) -> ValidationResult[Token]:
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
            2.  Otherwise, pack the original carrier and the blueprint in a Token
                for the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[Token]
        Raises:
            TokenLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate is null or the rong type.
        priming = self.toolkit.priming_validator.execute(
            candidate=candidate,
            target_context=TokenValidationRequest,
            null_exception=TokenValidationRequestNullException(),
        )
        if priming.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationLoaderException.MSG,
                    err_code=TokenContextValidationLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast priming to request for additional tests. ---#
        request = cast(Type[TokenValidationRequest], priming.payload)
        
        # Handle the case that request.item is the wrong carrier type.
        carrier_validation = self.toolkit.priming_validator.execute(
            candidate=request.item,
            target_context=self.toolkit.types.carrier,
            null_exception=self.toolkit.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationLoaderException.MSG,
                    err_code=TokenContextValidationLoaderException.ERR_CODE,
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
                TokenContextValidationLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenContextValidationLoaderException.MSG,
                    err_code=TokenContextValidationLoaderException.ERR_CODE,
                    ex=TokenCarrierEmptyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenCarrierEmptyException.MSG,
                        err_code=TokenCarrierEmptyException.ERR_CODE,
                    ),
                )
            )
        # --- Send the work product. ---#
        extract = Token(reference=carrier, blueprint=blueprint)
        return ValidationResult.success(extract)