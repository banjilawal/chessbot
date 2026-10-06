# src/assurance/envelope/router/tokenr.py

"""
Module: assurance.envelope.router.tokenr
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from assurance import EnvelopeRouter
from domain import Token


class TokenValidationRouter(EnvelopeRouter[Token]):
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
            validation_reference: TokenProductEnvelope,
    ) -> ValidationResult[TokenCarrier]:
        """
        Assure a candidate is a safe TokenCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult no route exists
                for the Token type.
            2.  Otherwise, send a TokenCarrier in the success result.
        Args:
            validation_reference: TokenProductEnvelope
            
        Returns:
            ValidationResult[TokenCarrier]
        Raises:
            TokenValidationRouteException
        """
        method = f"{self.__class__.__name__}.execute"
        
        
        reference = validation_reference.prime_extract.reference
        
        result = ValidationResult.failure(TokenValidationRouteException())
        # --- Select the appropriate validation route. ---#
        # KingToken validation route.
        if reference.is_king_token_carrier:
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
            king_carrier = cast(KingTokenCarrier, reference)
            king_prime_extract = KingTokenPrimeExtract(
                carrier=king_carrier,
                blueprint=king_blueprint
            )
            return self._king_validator.execute(
                prime_extract=king_prime_extract
            )

        # PawnToken validation route.
        if reference.is_pawn_token_carrier:
            return self._pawn_validator.execute(
                validation_reference=validation_reference
            )
        # CombatantToken validation route.
        if reference.is_combatant_token_carrier:
            return  self._combatant_validator.execute(
                reference=validation_reference
            )
        # Handle the case that the carrier is not consistent.
        return ValidationResult.failure(
            TokenValidationRouteException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=TokenValidationRouteException.MSG,
                err_code=TokenValidationRouteException.ERR_CODE,
                ex=TokenValidationRouteException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenValidationRouteException.MSG,
                    err_code=TokenValidationRouteException.ERR_CODE,
                )
            )
        )


    