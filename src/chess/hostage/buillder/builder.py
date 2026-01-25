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
from chess.token import CombatantActivityState, CombatantToken, Token, TokenService


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
            victor: Token,
            captured_square: Square,
            prisoner: CombatantToken,
            victor_square: Square,
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
            *   NullHostageManifestException
            *   KingCannotBeCapturedException
            *   TokenCannotCaptureItselfException
            *   FriendCannotCaptureFriendException
            *   PrisonerCapturedByDifferentEnemyException
            *   UnformedTokenCannotBeVictorException
            *   PrisonerCannotBeActiveCombatantException
            *   HostageManifestBuildFailedException
            *   VictorAndPrisoneOnDifferentBoardsException
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
        
        # --- Perform the square tests that are independent of the prisoner and victor. ---#
        
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
                    ex=CapturedSquareCannotBeEmptyException(
                        f"{method}: {CapturedSquareCannotBeEmptyException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the hostage is not in the
        # Handle the case that the victor_square is not certified safe.
        captured_square_validation = square_service.validator.validate(candidate=captured_square)
        if captured_square_validation.failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=captured_square_validation.exception
                )
            )
        # Handle the case that the victor_square is empty
        if victor_square.is_empty:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=VictorSquareCannotBeEmptyException(
                        f"{method}: {VictorSquareCannotBeEmptyException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # --- Perform the prisoner prebuild tests that are independent of the victor. ---#
        
        # Handle the case that the prisoner is not certified safe nor is .
        prisoner_validation = token_service.validator.verify_token_is_combatant(candidate=prisoner)
        if prisoner_validation.failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=prisoner_validation.exception
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
        # Handle the case that the prisoner was capture on a different square.
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
            
        # --- Perform tests on the victor that do not rely on the prisoner. ---#
        
        # Handle the case that the victor is not certified safe.
        victor_validation = token_service.validator.validate(candidate=victor)
        if victor_validation.failure:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=victor_validation.exception
                )
            )
        # Handle the case that the victor is not active.
        if victor.is_disabled:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=VictorCannotBeDisableTokenException(
                        f"{method}: {VictorCannotBeDisableTokenException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the victor is not occupying the square.
        if captured_square.occupant != victor:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=VictorNotOccupyingCapturedSquareException(
                        f"{method}: {VictorNotOccupyingCapturedSquareException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        # --- Perform tests that require the prisoner and victor. ---#
        
        # Handle the case that the victor and the prisoner are the same.
        if prisoner == victor:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=TokenCannotCaptureItselfException(
                        f"{method}: {TokenCannotCaptureItselfException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the tokens are not on the same board.
        if victor.team.board != prisoner.team.board:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=VictorAndPrisoneOnDifferentBoardsException(
                        f"{method}: {VictorAndPrisoneOnDifferentBoardsException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the tokens are not enemies.
        if not victor.is_enemy(prisoner):
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=FriendCannotCaptureFriendException(
                        f"{method}: {FriendCannotCaptureFriendException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that victor did not capture the prisoner
        if prisoner.captor != victor:
            # Send the exception chain on failure
            return BuildResult.failure(
                HostageManifestBuildFailedException(
                    message=f"{method}: {HostageManifestBuildFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerCapturedByDifferentEnemyException(
                        f"{method}: {PrisonerCapturedByDifferentEnemyException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
        # Build the HostageManifest.
        manifest = HostageManifest(id=id, prisoner=prisoner, victor=victor, captured_square=captured_square)
        # Update the prisoner's activity_state from to CAPTURE_ACTIVATED to ISSUED_HOSTAGE_MANIFEST
        manifest.prisoner.activity_state =  CombatantActivityState.ISSUED_HOSTAGE_MANIFEST
        
        # Return to the caller in the BuildResult.
        return BuildResult.success(payload=manifest)