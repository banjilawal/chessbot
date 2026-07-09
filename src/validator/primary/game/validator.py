# src/certifier/game/validator.py

"""
Module: certifier.game.validator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class GameCertifier(Certifier[Game]):
    """
     Role:Validation, Data Integrity Guarantor, Security.

    Responsibilities:
    1.  Ensure a GameBlueprint instance is certified safe, reliable and consistent before use.
    2.  If verification fails indicate the reason in an exception, returned to the caller.

    Super Class:
        *   Validator

    # PROVIDES:
        * GameCertifier

    
    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def validate(
            cls,
            candidate: Any,
            agent_service: AgentService = AgentService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Game]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, owner) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate entity_service and validator.
            3.  If any check fais return a BuildResult containing the exception raised by the failure.
            4.  On success send the verified GameBlueprint in a ValidationResult.

        # PARAMETERS:
        Only one these must be provided:
            *   id (Optional[int])
            *   owner (Optional[Player])

        These Parameters must be provided:
            *   player_service (AgentService)
            *   identity_service (IdentityService)

        # RETURNS:
        BuildResult[Game] containing either:
            - On success: GameBlueprint in the payload.
            - On failure: Exception.

        Raises:
            *   TypeError
            *   NullGameBlueprintException
            *   ZeroGameBlueprintFlagsException
            *   ArenaGameBlueprintFlagsException
            *   InvalidGameBlueprintException
        """
        method = "GameCertifier.execute"
        try:
            # Handle the case that, the rank does not exist.
            if candidate is None:
                return ValidationResult.failure(
                    NullGameBlueprintException(f"{method}: {NullGameBlueprintException.MSG}")
                )
            # Handle the case that, the rank is not a GameBlueprint.
            if not isinstance(candidate, GameBlueprint):
                return ValidationResult.failure(
                    TypeError(f"{method}: Expected GameBlueprint, got {type(candidate).__name__} instead.")
                )
            # After existence and type checks cast the rank for further processing.
            blueprint = cast(GameBlueprint, candidate)
            
            # Handle the case that, no attribute-value tuple is enabled.
            if len(blueprint.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroGameBlueprintFlagsException(f"{method}: {ZeroGameBlueprintFlagsException.MSG}")
                )
            # Handle the case that, more than one attribute-value tuple is enabled.
            if len(blueprint.to_dict()) == 0:
                return ValidationResult.failure(
                    ArenaGameBlueprintFlagsException(f"{method}: {ArenaGameBlueprintFlagsException.MSG}")
                )
            # Make sure a search target exists in the map. Cannot perform a search without an
            
            # property-value pair.
            if len(blueprint.to_dict()) == 0:
                return ValidationResult.failure(
                    ZeroGameBlueprintFlagsException(f"{method}: {ZeroGameBlueprintFlagsException.MSG}")
                )
            # Return an error if more than one property value pair exists in the map.
            if len(blueprint.to_dict()) > 1:
                return ValidationResult.failure(
                    ArenaGameBlueprintFlagsException(
                        f"{method}: {ArenaGameBlueprintFlagsException.MSG}"
                    )
                )
            
            # Build the id GameBlueprint if its flag is enabled.
            if blueprint.id is not None:
                validation = identity_service.validate_id(candidate=blueprint.id)
                if validation.is_failure:
                    return ValidationResult.failure(certifier.exception)
                # On validation success return the id_game_blueprint in a ValidationResult.
                return ValidationResult.success(blueprint)
            
            # Verify the id flag if its enabled.
            if blueprint.agent is not None:
                validation = agent_service.run.search_service(candidate=blueprint.agent)
                if validation.is_failure:
                    return ValidationResult.failure(certifier.exception)
                # On validation success return the agent_game_blueprint in a ValidationResult.
                return ValidationResult.success(blueprint)
            
        # Finally, for unhandled exception, wrap it inside an InvalidGameBlueprintException. Then send the
        # exception-chain in a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                InvalidGameBlueprintException(
                    ex=ex, msg=f"{method}: {InvalidGameBlueprintException.MSG}"
                )
            )
