# src/assurance/validator/model/token/validator.py

"""
Module: assurance.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    CombatantTokenValidator, KingTokenValidator, ModelValidator, PawnTokenValidator,
    TokenValidatorToolkit
)
from domain import Token, TokenValidationRequest
from err import TokenValidationRequestNullException, TokenValidatorException
from transit import CombatantCarrier, KingTokenCarrier, PawnTokenCarrier, TokenCarrier
from util import LoggingLevelRouter


class TokenValidator(ModelValidator[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier and its contents instance is safe before use.

    Attributes:
        toolkit: TokenValidationToolkit

    Provides:
        - def execute(request: TokenValidationRequest) ->ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidationToolkit]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(
            TokenValidatorToolkit,
            super().toolkit,
        )
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenValidationRequest) -> ValidationResult[TokenCarrier]:
        """
        Certify a candidate is a TokenCarrier whose payload is either a Token
        or a Blueprint that is safe to use.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    - The candidate is not a TokenCarrier or its null.
                    - The candidate is an empty TokenCarrier.
                    - Any Token attribute is flagged.
            2.  Otherwise, Send a Carrier with the correct type of payload in the success
                result.
        Args:
            candidate, Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the request is null or the wrong type.
        priming_validation = self.toolkit.helper.priming_validator.execute(
            candidate=request,
            target_model=TokenValidationRequest,
            null_exception=TokenValidationRequestNullException(),
        )
        if priming_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=priming_validation.exception,
                )
            )
        # --- Cast the priming_validator payload for additional tests. ---#
        safe_request = cast(TokenValidationRequest, priming_validation.payload)
        
        # Handle the case that the request payload is null or the wrong type.
        carrier_validation = self.toolkit.helper.priming_validator.execute(
            candidate=safe_request.item,
            target_model=self.toolkit.metadata.types.carrier,
            null_exception=self.toolkit.metadata.nulls.carrier,
        )
        if carrier_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=carrier_validation.exception,
                )
            )
        # --- Cast the carrier_validation payload for additional tests. ---#
        carrier = cast(TokenCarrier, carrier_validation.payload)
        
        # --- Extract the blueprint to verify the attributes. ---#

        if carrier.is_king_token_carrier:
            validated_carrier = cast(KingTokenCarrier, carrier)
            helper = KingTokenValidator()
            return helper.execute(validated_carrier)
        if carrier.is_pawn_token_carrier:
            validated_carrier = cast(PawnTokenCarrier, carrier)
            helper = PawnTokenValidator()
            return helper.execute(validated_carrier)
        validated_carrier = cast(CombatantCarrier, carrier)
        helper = CombatantTokenValidator()
        return helper.execute(validated_carrier)

    
    