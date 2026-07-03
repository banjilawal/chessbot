# src/builder/hostage/builder.py

"""
Module: builder.hostage.builder
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class HostageBuilder(Builder[Hostage]):
    """
    Role
        -   Transaction Worker
        -   Integrity Maintenance
        -   Consistency Assurance
        -   Build Process Owner

   Responsibilities:
        1.  Ensure a new Hostage instance is born safe and reliable.

    Attributes:

    Provides:

        def build(
                cls,
                captured_square: Square,
                prisoner: CombatantToken,
                id: int = id_emitter.scout_report_id,
                token_service: TokenService = TokenService(),
                square_service: SquareService = SquareService(),
                identity_service: IdentityService = IdentityService(),
        ) -> BuildResult[Hostage]:

     Super Class:
         Builder
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            captured_square: Square,
            prisoner: CombatantToken,
            id: int = id_emitter.scout_report_id,
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Hostage]:
        """
        # ACTION:
        1.  verify hostage_variety is a not-null HostageVariety object.
        2.  Use hostage_variety to pick which Validation method will create the concrete Hostage object.

        # PARAMETERS:
            *   id (int)
            *   schema (str)
            *   hostage_variety (HostageVariety)
            *   engine_service (Optional[EngineService])

        # RETURN:
        BuildResult[Hostage] containing either:
            - On success: Hostage in the payload.
            - On failure: Exception.

        Raises:
            *   TypeError
            *   PrisonerCapturedByDifferentEnemyException
            *   PrisonerCannotBeActiveCombatantException
            *   HostageBuilderException
            *   PrisonerAlreadyHasHostageException
            *   PrisonerCapturedOnDifferentSquareException
        """
        method = "HostageBuilder.build"
        
        # Handle the case that, the idis not safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that, the captured_squareis not safe.
        captured_square_validation = square_service.validate.build(candidate=captured_square)
        if captured_square_validation.failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=captured_square_validation.exception
                )
            )
        # Handle the case that, the captured_square is empty
        if captured_square.is_empty:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=VictorNotOccupyingCapturedSquareException(
                        f"{method}: {VictorNotOccupyingCapturedSquareException.MSG}"
                    )
                )
            )
 

        # --- Perform the prisoner prebuild tests that are independent of the victor. ---#
        
        # Handle the case that, the prisoner is not a safe combatant.
        prisoner_is_combatant_validation = token_service.validate.verify_token_is_combatant(
            candidate=prisoner
        )
        if prisoner_is_combatant_validation.is_failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=prisoner_is_combatant_validation.exception
                )
            )
        # Handle the case that, the prisoner is still active:
        if prisoner.is_active:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=PrisonerCannotBeActiveCombatantException(
                        f"{method}: {PrisonerCannotBeActiveCombatantException.MSG}"
                    )
                )
            )
        # Handle the case that, prisoner already has a manifest.
        if prisoner.being_processed_as_hostage:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=PrisonerAlreadyHasHostageException(
                        f"{method}: {PrisonerAlreadyHasHostageException.MSG}"
                    )
                )
            )
        # Handle the case that, the prisoner was capture on a different item.
        if prisoner.current_position != captured_square.hostage:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=PrisonerCapturedOnDifferentSquareException(
                        f"{method}: {PrisonerCapturedOnDifferentSquareException.MSG}"
                    )
                )
            )
        # Handle the case that, the victor did not capture the prisoner
        if prisoner.captor != captured_square.occupant:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageBuilderException(
                    msg=f"{method}: {HostageBuilderException.MSG}",
                    ex=PrisonerCapturedByDifferentEnemyException(
                        f"{method}: {PrisonerCapturedByDifferentEnemyException.MSG}"
                    )
                )
            )
        # Build the Hostage the updated the prisoner's state
        manifest = Hostage(
            id=id,
            prisoner=prisoner,
            captured_square=captured_square,
            victor=captured_square.occupant,
        )
        manifest.prisoner.activity.classification = CombatantReadinessEnum.ISSUED_HOSTAGE
        
        # Return to the caller in the BuildResult.
        return BuildResult.success(payload=manifest)