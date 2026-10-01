# src/assurance/validator/model/encounter/router.py

"""
Module: assurance.validator.model.encounter.router
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ValidationResult
from assurance import (
    CombatantEncounterValidator, KingEncounterValidator, PawnEncounterValidator,
    EncounterValidatorToolkit
)
from domain import (
    CombatantEncounterBlueprint, CombatantEncounterPrimeExtract, Coord, Formation, HomeSquare,
    KingEncounterBlueprint, KingEncounterPrimeExtract, PawnEncounterBlueprint,
    PawnEncounterPrimeExtract, Team, EncounterDeployment, EncounterPrimeExtract
)
from err import EncounterValidationRouteException
from transit import CombatantEncounterCarrier, KingEncounterCarrier, PawnEncounterCarrier, EncounterCarrier
from util import LoggingLevelRouter


class EncounterValidationRouter:
    """
    Role
        - Router

    Responsibilities:
        1.  Select the validator which matches Encounter type.

    Attributes:
        toolkit: EncounterValidatorToolkit
        king_validator: KingEncounterValidator
        pawn_validator: PawnEncounterValidator
        combatant_validator: CombatantEncounterValidator

    Provides:
        -   def execute(
                    id: int,
                    team: Team,
                    formation: Formation,
                    home_square: HomeSquare,
                    deployment: EncounterDeployment,
                    prime_extract: EncounterPrimeExtract,
            ) -> ValidationResult[EncounterCarrier]:

    Super Class:
    """
    _king_validator: KingEncounterValidator
    _pawn_validator: PawnEncounterValidator
    _combatant_validator: CombatantEncounterValidator
    _toolkit: EncounterValidatorToolkit
    
    def __init__(
            self,
            toolkit: Optional[EncounterValidatorToolkit] | None = None,
            king_validator: Optional[KingEncounterValidator] | None = None,
            pawn_validator: Optional[PawnEncounterValidator] | None = None,
            combatant_validator: Optional[CombatantEncounterValidator] | None = None,
    ):
        """
        Args:
            toolkit: Optional[EncounterValidatorToolkit]
            king_validator: Optional[KingEncounterValidator]
            pawn_validator: Optional[PawnEncounterValidator]
            combatant_validator: Optional[CombatantEncounterValidator]
        """
        self._toolkit=toolkit or EncounterValidatorToolkit()
        self._king_validator = king_validator or KingEncounterValidator()
        self._pawn_validator = pawn_validator or PawnEncounterValidator()
        self._combatant_validator = combatant_validator or CombatantEncounterValidator()
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            deployment: EncounterDeployment,
            prime_extract: EncounterPrimeExtract,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
            property_table: CommonEncounterPropertyTable
    ) -> ValidationResult[EncounterCarrier]:
        """
        Assure a candidate is a safe EncounterCarrier.

        Action:
            1.  Send an exception chain in the ValidationResult no route exists
                for the Encounter type.
            2.  Otherwise, send a EncounterCarrier in the success result.
        Args:
            id: int
            team: Team
            formation: Formation
            home_square: HomeSquare
            deployment: EncounterDeployment
            prime_extract: EncounterPrimeExtract
            previous_position: Optional[Coord]
            position: Optional[Coord]
            
        Returns:
            ValidationResult[EncounterCarrier]
        Raises:
            EncounterValidationRouteException
        """
        method = f"{self.__class__.__name__}.execute"
    
        
        original_carrier = property_table.prime_extract.carrier
        encounter_blueprint = prime_extract.blueprint
        
        # --- Select the appropriate validation route. ---#
        # KingEncounter validation route.
        if original_carrier.is_king_encounter_carrier:
            raw = cast(KingEncounterBlueprint, encounter_blueprint)
            king_blueprint = KingEncounterBlueprint(
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
            king_carrier = cast(KingEncounterCarrier, original_carrier)
            king_prime_extract = KingEncounterPrimeExtract(
                carrier=king_carrier,
                blueprint=king_blueprint
            )
            return self._king_validator.execute(
                prime_extract=king_prime_extract
            )

        # PawnEncounter validation route.
        if original_carrier.is_pawn_encounter_carrier:
            raw = cast(PawnEncounterBlueprint, encounter_blueprint)
            pawn_blueprint = PawnEncounterBlueprint(
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
            pawn_carrier = cast(PawnEncounterCarrier, original_carrier)
            pawn_prime_extract = PawnEncounterPrimeExtract(
                carrier=pawn_carrier,
                blueprint=pawn_blueprint
            )
            return self._pawn_validator.execute(
                prime_extract=pawn_prime_extract
            )
        # CombatantEncounter validation route.
        if original_carrier.is_combatant_encounter_carrier:
            raw = cast(CombatantEncounterBlueprint, encounter_blueprint)
            combatant_blueprint = CombatantEncounterBlueprint(
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
            combatant_carrier = cast(CombatantEncounterCarrier, original_carrier)
            combatant_prime_extract = CombatantEncounterPrimeExtract(
                carrier=combatant_carrier,
                blueprint=combatant_blueprint
            )
            return self._combatant_validator.execute(
                prime_extract=combatant_prime_extract
            )
        # Handle the case that the carrier is not consistent.
        return ValidationResult.failure(
            EncounterValidationRouteException(
                cls_mthd=method,
                cls_name=self.__class__.__name__,
                msg=EncounterValidationRouteException.MSG,
                err_code=EncounterValidationRouteException.ERR_CODE,
            )
        )
    