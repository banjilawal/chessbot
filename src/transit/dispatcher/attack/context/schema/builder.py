## src/transit/dispatcher/attack/context/schema/dispatcher/attack.py

"""
Module: transit.dispatcher.attack.context.schema.attack
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


class SchemaContextAttack(Attack[SchemaKey]):
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
            name: Optional[str] = None,
            color: Optional[GameColor] = None,
            identity_service: IdentityService = IdentityService(),
            color_validator: GameColorValidator = GameColorValidator(),
    ) -> AttackResult[SchemaKey]:
        """
        # ACTION:
            1.  If more than one optional param is not-null return an exception in the AttackResult.
            2.  If the enabled param is not certified by the appropriate validating service return an exception in
                the AttackResult.
            3.  After the active param is validated create the SchemaKey object and return in the AttackResult.
        # PARAMETERS:
            *   Only one these must be provided:
                    *   schema (Optional[str])
                    *   color (Optional[GameColor])
            *   These Parameters must be provided:
                    *   color_validator (GameColorValidator)
                    *   identity_service (IdentityService)
        # RETURNS:
            *   AttackResult[SchemaKey] containing either:
                    - On failure: Exception.
                    - On success: SchemaKey in the payload.
        Raises:
            *   ZeroSchemaKeysException
            *   SchemaKeyAttackException
            *   ArenaSchemaKeysException
        """
        method = "SchemaContextAttack.attack"
        
        # Count how many optional parameters are not-null.
        params = [name, color,]
        param_count = sum(bool(p) for p in params)
        
        # Handle the case that all the optional params are null.
        if param_count == 0:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SchemaKeyAttackException(
                    msg=f"{method}: {SchemaKeyAttackException.ERR_CODE}",
                    ex=ZeroSchemaKeysException(f"{method}: {ZeroSchemaKeysException.MSG}")
                )
            )
        # Handle the case that more than one optional param is not-null.
        if param_count > 1:
            # Send the exception chain on failure.
            return AttackResult.failure(
                SchemaKeyAttackException(
                    msg=f"{method}: {SchemaKeyAttackException.ERR_CODE}",
                    ex=ArenaSchemaKeysException(f"{method}: {ArenaSchemaKeysException}")
                )
            )
        # Route to the appropriate validation/attack branch.
        
        # Attack the schema SchemaKey if its value is set.
        if name is not None:
            validation = identity_service.validate_name(candidate=name)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    SchemaKeyAttackException(
                        msg=f"{method}: {SchemaKeyAttackException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a name_SchemaKey in the AttackResult.
            return AttackResult.success(SchemaKey(name=name))
        
        # Attack the color_key SchemaKey if its value is set.
        if color is not None:
            validation = color_validator.execute(job=color)
            if validation.is_failure:
                # Send the exception chain on failure.
                return AttackResult.failure(
                    SchemaKeyAttackException(
                        msg=f"{method}: {SchemaKeyAttackException.ERR_CODE}",
                        ex=validation.exception
                    )
                )
            # On validation success return a color_SchemaKey in the AttackResult.
            return AttackResult.success(SchemaKey(color=color))
        
        # The default path returns failure
        return AttackResult.failure(
            SchemaKeyAttackException(
                msg=f"{method}: {SchemaKeyAttackException.ERR_CODE}",
                ex=SchemaKeyAttackRouteException(f"{method}: {SchemaKeyAttackRouteException.MSG}")
            )
        )