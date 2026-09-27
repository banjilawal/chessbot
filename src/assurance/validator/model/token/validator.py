# src/assurance/validator/model/token/validator.py

"""
Module: assurance.validator.model.token.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ValidationResult
from assurance import (
    CombatantTokenValidator, KingTokenValidator, ModelValidator, PawnTokenValidator,
    TokenValidatorToolkit
)
from domain import Token, TokenPrimeExtract
from err import TokenValidationRouteException, TokenValidatorException
from transit import CombatantCarrier, KingTokenCarrier, PawnTokenCarrier, TokenCarrier
from util import LoggingLevelRouter


class TokenValidator(ModelValidator[Token]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Ensure a TokenCarrier is safe to use.

    Attributes:
        toolkit: TokenValidatorToolkit
        king_validator: KingTokenValidator
        pawn_validator: PawnTokenValidator
        combatant_validator: CombatantTokenValidator

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[TokenCarrier]:

    Super Class:
        ModelValidator
    """
    _king_validator: KingTokenValidator
    _pawn_validator: PawnTokenValidator
    _combatant_validator: CombatantTokenValidator
    
    def __init__(
            self,
            toolkit: Optional[TokenValidatorToolkit] | None = None,
            king_validator: Optional[KingTokenValidator] | None = None,
            pawn_validator: Optional[PawnTokenValidator] | None = None,
            combatant_validator: Optional[CombatantTokenValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[TokenValidatorToolkit]
            king_validator: Optional[KingTokenValidator]
            pawn_validator: Optional[PawnTokenValidator]
            combatant_validator: Optional[CombatantTokenValidator]
        """
        super().__init__(toolkit=toolkit or TokenValidatorToolkit())
        self._king_validator = king_validator or KingTokenValidator()
        self._pawn_validator = pawn_validator or PawnTokenValidator()
        self._combatant_validator = combatant_validator or CombatantTokenValidator()
    
    @property
    def toolkit(self) -> TokenValidatorToolkit:
        return cast(TokenValidatorToolkit, super().toolkit)
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
    ) -> ValidationResult[TokenCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult if any of the following
                occur
                    -   The Loader fails.
                    -   The TokenCarrier subclass does not have a validation route.
                    -   Any of the following sub-validators fail.
                        -   KingTokenValidator
                        -   PawnTokenValidator
                        -   CombatantTokenValidator
            2.  Otherwise, send a TokenCarrier in the success result.
        Args:
            candidate: Any
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidatorException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the blueprint cannot be extracted.
        load_result = self.toolkit.loader.execute(candidate)
        if load_result.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenValidatorException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidatorException.MSG,
                    err_code=TokenValidatorException.ERR_CODE,
                    ex=load_result.exception,
                )
            )
        # --- Get the PrimeExtract and Blueprint for additional processing. ---#
        prime_extract = cast(TokenPrimeExtract, load_result.payload)
        carrier = cast(TokenCarrier, prime_extract.carrier)
        
        # --- Select the appropriate validation route. ---#
        # KingToken validation route.
        if carrier.is_king_token_carrier:
            return self._king_validator.execute(
                carrier=cast(KingTokenCarrier, carrier)
            )
        # PawnToken validation route.
        if carrier.is_pawn_token_carrier:
            return self._pawn_validator.execute(
                carrier=cast(PawnTokenCarrier, carrier)
            )
        # CombatantToken validation route.
        if carrier.is_combatant_token_carrier:
            return self._combatant_validator.execute(
                carrier=cast(CombatantCarrier, carrier)
            )
        # Handle the case that the carrier is not consistent.
        return ValidationResult.failure(
            TokenValidatorException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=TokenValidatorException.MSG,
                err_code=TokenValidatorException.ERR_CODE,
                ex=TokenValidationRouteException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationRouteException.MSG,
                    err_code=TokenValidationRouteException.ERR_CODE,
                )
            )
        )
    