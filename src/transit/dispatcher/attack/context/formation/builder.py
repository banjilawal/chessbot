# src/transit/dispatcher/attack/context/formation/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.formation.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain.model import (
    ArenaFormationKeysException, FormationKey, FormationKeyAttackException,
    FormationKeyAttackRouteException, ZeroFormationKeysException
)
from domain.schema.persona import Persona, PersonaService
from logic.square import Square, SquareService
from system import AttackResult, Attack, GameColor, GameColorValidator, IdentityService, LoggingLevelRouter


class FormationContextAttack(Attack[FormationKey]):
    """
    Role
        - Transaction Worker
        - Integrity Maintenance
        - Consistency Assurance
        - Attack Process Owner

   Responsibilities:
        1.  Ensure a new Token instance is born safe and reliable.

     Attributes:

    Provides:
        -   def execute(
                    owner: Team,
                    id: int = IdFactory,
                    formation: Formation,
                    rank_service: RankService,
                    identity_service: IdentityService,
                    formation_service: FormationService,
                    team_validator: TeamValidator,
            ) -> AttackResult[Token]

     Super Class:
         Attack
     """
    @classmethod
    @LoggingLevelRouter.monitor
    def attack(
            cls,
            square: Optional[Square] = None,
            persona: Optional[Persona] = None,
            color: Optional[GameColor] = None,
            designation: Optional[str] = None,
            square_service: SquareService = SquareService(),
            persona_service: PersonaService = PersonaService(),
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> AttackResult[FormationKey]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the AttackResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the AttackResult.
            3.  After the active param is validated create the FormationKey object and return in the AttackResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   persona (Optional[Persona])
                    *   item (Optional[Square])
                    *   color (Optional[GameColor])
            *   These Parameters must be provided:
                    *   square_validator (SquareService)
                    *   identity_service (IdentityService)
                    *   color_validator (GameColorValidator)
        # RETURNS:
            *   AttackResult[FormationKey] containing either:
                    - On failure: Exception.
                    - On success: FormationKey in the payload.
        Raises:
            *   ZeroFormationKeysException
            *   FormationKeyAttackException
            *   ArenaFormationKeysException
            *   FormationKeyAttackException
        """
        method = "FormationContextAttack.attack"
        
        # Count how many optional parameters are not-null.
        params = [designation, square, color, persona]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return AttackResult.failure(
                FormationKeyAttackException(
                    msg=f"{method}: {FormationKeyAttackException.ERR_CODE}",
                    ex=ZeroFormationKeysException(
                        f"{method}: {ZeroFormationKeysException.MSG}"
                    )
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return AttackResult.failure(
                FormationKeyAttackException(
                    msg=f"{method}: {FormationKeyAttackException.ERR_CODE}",
                    ex=ArenaFormationKeysException(f"{method}: {ArenaFormationKeysException}")
                )
            )
        
        # --- Route to the appropriate validation/attack branch. ---#
        
        # Attack the square_name FormationKey if its value is set.
        if square is not None:
            validation = square_service.execute.execute(square)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    FormationKeyAttackException(
                        msg=f"{method}: {FormationKeyAttackException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a square_name_FormationKey in the AttackResult.
            return AttackResult.success(FormationKey(square_name=square.name))
        
        # Attack the designation FormationKey if its value is set.
        if designation is not None:
            validation = identity_service.validate_name(candidate=designation)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    FormationKeyAttackException(
                        msg=f"{method}: {FormationKeyAttackException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a designation_FormationKey in the AttackResult.
            return AttackResult.success(FormationKey(designation=designation))
        
        # Attack the color FormationKey if its value is set.
        if color is not None:
            validation = color_validator.execute(job=color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    FormationKeyAttackException(
                        msg=f"{method}: {FormationKeyAttackException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a color_FormationKey in the AttackResult.
            return AttackResult.success(FormationKey(color=color))
        
        # Attack the persona FormationKey if its value is set.
        if persona is not None:
            validation = persona_service.execute.execute(job=persona)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    FormationKeyAttackException(
                        msg=f"{method}: {FormationKeyAttackException.ERR_CODE}",
                        ex=validation.exception,
                    )
                )
            # On validation success return a color_FormationKey in the AttackResult.
            return AttackResult.success(FormationKey(persona=persona))
        
        # The default path returns failure.
        AttackResult.failure(
            FormationKeyAttackException(
                msg=f"{method}: {FormationKeyAttackException.ERR_CODE}",
                ex=FormationKeyAttackRouteException(
                    f"{method}: {FormationKeyAttackRouteException.MSG}"
                )
            )
        )