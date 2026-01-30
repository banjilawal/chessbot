# src/chess/hostage/builder/builder.py

"""
Module: chess.hostage.builder
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from __future__ import annotations
from chess.hostage import (
    CapturedSquareCannotBeEmptyException, PrisonerCannotBeActiveCombatantException, FriendCannotCaptureFriendException,
    HostageManifest, HostageManifestBuildFailedException, PrisonerAlreadyHasHostageManifestException,
    PrisonerCapturedByDifferentEnemyException, TokenCannotCaptureItselfException,
    VictorAndPrisoneOnDifferentBoardsException, PrisonerCapturedOnDifferentSquareException,
    VictorCannotBeDisableTokenException, VictorNotOccupyingCapturedSquareException,
)
from chess.square import Square, SquareService
from chess.system import IdentityService, LoggingLevelRouter, BuildResult, Builder, id_emitter
from chess.token import CombatantActivityState, CombatantReadinessEnum, CombatantToken, Token, TokenService


class HostageManifestBuilder(Builder[HostageManifest]):
    """
    # ROLE: Validation, Data Integrity And Reliability Guarantor

    # RESPONSIBILITIES:
    1.  Produce Hostage instances whose integrity is guaranteed at creation.
    2.  Manage construction of Hostage instances that can be used safely by the client.
    3.  Ensure params for Hostage creation have met the application's safety contract.
    4.  Return an exception to the client if a Validation resource does not satisfy integrity requirements.

    # PARENT:
        *   Validation

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
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
    ) -> BuildResult[HostageManifest]:
        """
        # ACTION:
        1.  verify hostage_variety is a not-null HostageVariety object.
        2.  Use hostage_variety to pick which Validation method will create the concrete Hostage object.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   hostage_variety (HostageVariety)
            *   engine_service (Optional[EngineService])

        # RETURN:
        BuildResult[Hostage] containing either:
            - On success: Hostage in the payload.
            - On failure: Exception.

        # RAISES:
            *   TypeError
            *   PrisonerCapturedByDifferentEnemyException
            *   PrisonerCannotBeActiveCombatantException
            *   HostageManifestBuildFailedException
            *   PrisonerAlreadyHasHostageManifestException
            *   PrisonerCapturedOnDifferentSquareException
        """
        method = "HostageBuilder.build"
        
        # Handle the case that the id is not certified safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that the captured_square is not certified safe.
        captured_square_validation = square_service.validator.validate(candidate=captured_square)
        if captured_square_validation.failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=captured_square_validation.exception
                )
            )
        # Handle the case that the captured_square is empty
        if captured_square.is_empty:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=VictorNotOccupyingCapturedSquareException(
                        f"{method}: {VictorNotOccupyingCapturedSquareException.DEFAULT_MESSAGE}"
                    )
                )
            )
 

        # --- Perform the prisoner prebuild tests that are independent of the victor. ---#
        
        # Handle the case that the prisoner is not a safe combatant.
        prisoner_is_combatant_validation = token_service.validator.verify_token_is_combatant(
            candidate=prisoner
        )
        if prisoner_is_combatant_validation.is_failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=prisoner_is_combatant_validation.exception
                )
            )
        # Handle the case that the prisoner is still active:
        if prisoner.is_active:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerCannotBeActiveCombatantException(
                        f"{method}: {PrisonerCannotBeActiveCombatantException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that prisoner already has a manifest.
        if prisoner.has_hostage_manifest:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerAlreadyHasHostageManifestException(
                        f"{method}: {PrisonerAlreadyHasHostageManifestException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the prisoner was capture on a different item.
        if prisoner.current_position != captured_square.coord:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerCapturedOnDifferentSquareException(
                        f"{method}: {PrisonerCapturedOnDifferentSquareException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the victor did not capture the prisoner
        if prisoner.captor != captured_square.occupant:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerCapturedByDifferentEnemyException(
                        f"{method}: {PrisonerCapturedByDifferentEnemyException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Build the HostageManifest the updated the prisoner's state
        manifest = HostageManifest(
            id=id,
            prisoner=prisoner,
            captured_square=captured_square,
            victor=captured_square.occupant,
        )
        manifest.prisoner.activity.classification = CombatantReadinessEnum.ISSUED_HOSTAGE_MANIFEST
        
        # Return to the caller in the BuildResult.
        return BuildResult.success(payload=manifest)