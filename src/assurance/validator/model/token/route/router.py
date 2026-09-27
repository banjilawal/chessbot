# src/assurance/validator/model/token/router.py

"""
Module: assurance.validator.model.token.router
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    CombatantTokenValidator, KingTokenValidator, PawnTokenValidator,
    TokenValidatorToolkit
)
from domain import (
    CombatantTokenBlueprint, CombatantTokenPrimeExtract, Coord, Formation, HomeSquare,
    KingTokenBlueprint, KingTokenPrimeExtract, PawnTokenBlueprint,
    PawnTokenPrimeExtract, Team, TokenDeployment, TokenPrimeExtract
)
from err import TokenValidationRouteException
from transit import CombatantTokenCarrier, KingTokenCarrier, PawnTokenCarrier, TokenCarrier
from util import LoggingLevelRouter


class TokenValidationRouter:
    """
    Role
        - Router

    Responsibilities:
        1.  Select the validator which matches Token type.

    Attributes:
        toolkit: TokenValidatorToolkit
        king_validator: KingTokenValidator
        pawn_validator: PawnTokenValidator
        combatant_validator: CombatantTokenValidator

    Provides:
        -   def execute(
                    id: int,
                    team: Team,
                    formation: Formation,
                    home_square: HomeSquare,
                    deployment: TokenDeployment,
                    prime_extract: TokenPrimeExtract,
            ) -> ValidationResult[TokenCarrier]:

    Super Class:
    """
    _king_validator: KingTokenValidator
    _pawn_validator: PawnTokenValidator
    _combatant_validator: CombatantTokenValidator
    _toolkit: TokenValidatorToolkit
    
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
        self._toolkit=toolkit or TokenValidatorToolkit()
        self._king_validator = king_validator or KingTokenValidator()
        self._pawn_validator = pawn_validator or PawnTokenValidator()
        self._combatant_validator = combatant_validator or CombatantTokenValidator()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            deployment: TokenDeployment,
            prime_extract: TokenPrimeExtract,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
            property_table: CommonTokenPropertyTable
    ) -> ValidationResult[TokenCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult no route exists
                for the Token type.
            2.  Otherwise, send a TokenCarrier in the success result.
        Args:
            id: int
            team: Team
            formation: Formation
            home_square: HomeSquare
            deployment: TokenDeployment
            prime_extract: TokenPrimeExtract
            previous_position: Optional[Coord]
            position: Optional[Coord]
            
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidationRouteException
        """
        method = f"{self.__class__.__name__}.execute"
    
        
        original_carrier = property_table.prime_extract.carrier
        token_blueprint = prime_extract.blueprint
        
        # --- Select the appropriate validation route. ---#
        # KingToken validation route.
        if original_carrier.is_king_token_carrier:
            raw = cast(KingTokenBlueprint, token_blueprint)
            king_blueprint = KingTokenBlueprint(
                id=id,
                team=team,
                formation=formation,
                deployment=deployment,
                home_square=home_square,
                position=position,
                previous_position=previous_position,
                readiness=raw.readiness,
                checkmate=raw.checkmate,
                check_warning=raw.check_warning,
            )
            king_carrier = cast(KingTokenCarrier, original_carrier)
            king_prime_extract = KingTokenPrimeExtract(
                carrier=king_carrier,
                blueprint=king_blueprint
            )
            return self._king_validator.execute(
                prime_extract=king_prime_extract
            )

        # PawnToken validation route.
        if original_carrier.is_pawn_token_carrier:
            raw = cast(PawnTokenBlueprint, token_blueprint)
            pawn_blueprint = PawnTokenBlueprint(
                id=id,
                team=team,
                formation=formation,
                deployment=deployment,
                home_square=home_square,
                position=position,
                previous_position=previous_position,
                readiness=raw.readiness,
                rank=raw.rank,
                captor=raw.captor,
                promotion_state=raw.promotion_state,
            )
            pawn_carrier = cast(PawnTokenCarrier, original_carrier)
            pawn_prime_extract = PawnTokenPrimeExtract(
                carrier=pawn_carrier,
                blueprint=pawn_blueprint
            )
            return self._pawn_validator.execute(
                prime_extract=pawn_prime_extract
            )
        # CombatantToken validation route.
        if original_carrier.is_combatant_token_carrier:
            raw = cast(CombatantTokenBlueprint, token_blueprint)
            combatant_blueprint = CombatantTokenBlueprint(
                id=id,
                team=team,
                formation=formation,
                deployment=deployment,
                home_square=home_square,
                position=position,
                previous_position=previous_position,
                readiness=raw.readiness,
                captor=raw.captor,
            )
            combatant_carrier = cast(CombatantTokenCarrier, original_carrier)
            combatant_prime_extract = CombatantTokenPrimeExtract(
                carrier=combatant_carrier,
                blueprint=combatant_blueprint
            )
            return self._combatant_validator.execute(
                prime_extract=combatant_prime_extract
            )
        # Handle the case that the carrier is not consistent.
        return ValidationResult.failure(
            TokenValidationRouteException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=TokenValidationRouteException.MSG,
                err_code=TokenValidationRouteException.ERR_CODE,
            )
        )
    