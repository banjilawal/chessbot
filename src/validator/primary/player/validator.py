# src/certifier/player/validator.py

"""
Module: certifier.player.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class PlayerCertifier(Certifier[Player]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure an PlayerBlueprint instance is certified safe, reliable and consistent before use.
    2.  If a rank fails a safety test, the validation sends an exception in a ValidationResult.
    
    Super Class:
        *   Validator

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            team_service: TeamService = TeamService(),
            game_service: GameService = GameService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Player]:
        """
        # ACTION:
            1.  If the rank passes existence and type checks cast into a PlayerBlueprint for
                additional integrity tests. Else return an exception in the ValidationResult.
            2.  If one-and-only-one PlayerBlueprint attribute-value-tuple is enabled goto the integrity
                check. Else, return an exception in the ValidationResult.
            3.  Route to the appropriate validation subflow with the attribute as the routing key.
            4.  If the validation subflow certifies the map tuple return it in the validation result.
                Else, send the exception in the ValidationResult.

        # PARAMETERS:
            *   rank (Any)
            *   team_service (TeamService)
            *   game_service (GameService)
            *   identity_service (IdentityService)

        # RETURNS:
        ValidationResult[Player] containing either:
            - On success: PlayerBlueprint in the payload.
            - On failure: Exception.

        Raises:
            *   TypeError
            *   NullPlayerBlueprintException
            *   NoPlayerBlueprintFlagException
            *   ArenaPlayerBlueprintFlagsException
            *   InvalidPlayerBlueprintException
        """
        method = "PlayerCertifier.execute"
        try:
            # Handle the nonexistence case.
            if candidate is None:
                return ValidationResult.failure(
                    NullPlayerBlueprintException(f"{method}: {NullPlayerBlueprintException.MSG}")
                )
            # Handle the wrong class case.
            if not isinstance(candidate, PlayerBlueprint):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected PlayerBlueprint, got {type(candidate).__name__} instead.")
                )
            
            # After existence and type checks are successful cast the candidate into an PlayerBlueprint
            # for additional tests.
            blueprint = cast(PlayerBlueprint, candidate)
            
            # Handle the no map flag enabled case.
            if len(blueprint.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroPlayerBlueprintFlagsException(f"{method}: {ZeroPlayerBlueprintFlagsException.MSG}")
                )
            # Handle the arena map flags case.
            if len(blueprint.to_dict()) > 1:
                return ValidationResult.failure(
                    ArenaPlayerBlueprintFlagsException(
                        f"{method}: {ArenaPlayerBlueprintFlagsException.MSG}"
                    )
                )
            
            # Using the tuple's attribute as an address, route to appropriate validation subflow.
            
            # Which ever attribute value is not null should be certified safe by the appropriate validator.
            if blueprint.id is not None:
                validation = identity_service.validate_id(candidate=blueprint.id)
                if validation.is_failure:
                    return ValidationResult.failure(certifier.exception)
                return ValidationResult.success(blueprint)
            
            if blueprint.designation is not None:
                validation = identity_service.validate_name(candidate=blueprint.designation)
                if validation.is_failure:
                    return ValidationResult.failure(certifier.exception)
                return ValidationResult.success(blueprint)
            
            if blueprint.team is not None:
                validation = team_service.run.build(candidate=blueprint.team)
                if validation.is_failure:
                    return ValidationResult.failure(certifier.exception)
                return ValidationResult.success(blueprint)
            
            if blueprint.game is not None:
                validation = game_service.run.build(candidate=blueprint.game)
                if validation.is_failure:
                    return ValidationResult.failure(certifier.exception)
                return ValidationResult.success(blueprint)
            
            if blueprint.variety is not None:
                if blueprint.variety not in [PlayerVariety.HUMAN_PLAYER, PlayerVariety.MACHINE_PLAYER]:
                    return ValidationResult.failure(
                        TypeError(f"{method}: Expected PlayerType, got {type(candidate).__name__} instead.")
                    )
                return ValidationResult.success(blueprint)
        
        # Finally, catch any missed exception, wrap an InvalidPlayerBlueprintException around it then, return
        # the exception-chain inside the ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidPlayerBlueprintException(
                    ex=ex, msg=f"{method}: {InvalidPlayerBlueprintException.MSG}"
                )
            )
