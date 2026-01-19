# src/chess/hostage/validator/validator.py

"""
Module: chess.hostage.validator
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from typing import Any, cast

from chess.square import SquareService
from chess.hostage import (
    FreeEnemyContradictsCaptureException, FriendCannotCaptureFriendException, HostageManifest,
    HostageManifestValidationFailedException, KingCannotBeCapturedException, NullHostageManifestException,
    PrisonerDoesNotHaveCaptorException, PrisonerHasDifferentCaptorException, TokenCannotCaptureItselfException,
    UnformedTokenCannotBePrisonerException, UnformedTokenCannotBeVictorException,
    VictorAndPrisonerConflictingBoardException, VictorAndPrisonerConflictingCoordException,
)
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult,Validator
from chess.token import CombatantActivityStatue, CombatantToken, TokenBoardState, TokenService


class HostageManifestValidator(Validator[HostageManifest]):
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
    def validate(
            cls,
            candidate: Any,
            square_service: SquareService = SquareService(),
            token_service: TokenService = TokenService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[HostageManifest]:
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
        ValidationResult[Hostage] containing either:
            - On success: Hostage in the payload.
            - On failure: Exception.

        # RAISES:
            *   HostageManifestValidationFailedException
        """
        method = "HostageValidator.validate"
        
        # Handle the case that the candidate does not exist.
        if candidate is None:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullHostageManifestException(f"{method}: {NullHostageManifestException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case, that the candidate is the wrong type.
        if not isinstance(candidate, HostageManifest):
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TypeError(f"{method}: Expected Hostage, {type(candidate).__name__} instead.")
                )
            )
        
        # --- Cast the candidate into a HostageManifest for additional testing. ---#
        manifest = cast(HostageManifest, candidate)
        
        # Handle the case that the id is not certified safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that the square where the capture occurred is not certified safe.
        square_validation = square_service.validator.validate(candidate=manifest.capture_location)
        if square_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=square_validation.exception
                )
            )
        
        # --- Perform tests on the matrix.prisoner that do not rely on the victor. ---#
        
        # Handle the case that the prisoner is not certified safe.
        prisoner_validation = token_service.validator.validate(candidate=manifest.prisoner)
        if prisoner_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=prisoner_validation.exception
                )
            )
        # Handle the case that prisoner is not a CombatantToken.
        if not isinstance(manifest.prisoner, CombatantToken):
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=KingCannotBeCapturedException(
                        f"{method}: {KingCannotBeCapturedException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the prisoner was not placed on the board
        if manifest.prisoner.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=UnformedTokenCannotBePrisonerException(
                        f"{method}: {UnformedTokenCannotBePrisonerException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that prisoner does not have a captor
        if manifest.prisoner.captor is None:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerDoesNotHaveCaptorException(
                        f"{method}: {PrisonerDoesNotHaveCaptorException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the prisoner is free
        if manifest.prisoner.activity_status == CombatantActivityStatue.FREE:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=FreeEnemyContradictsCaptureException(
                        f"{method}: {FreeEnemyContradictsCaptureException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the prisoner was capture on a different square.
        if manifest.prisoner.current_position != manifest.capture_location.coord:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerCapturedOnDifferentSquareException(
                        f"{method}: {PrisonerCaputeredOnDifferentSquare.DEFAULT_MESSAGE}"
                    )
                )
            )
            
            # --- Perform tests on the matrix.victor that do not rely on the prisoner. ---#
            
        # Handle the case that the victor is not certified safe.
        victor_validation = token_service.validator.validate(candidate=manifest.victor)
        if victor_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=victor_validation.exception
                )
            )

        # --- Assign the certified tokens to local variables for additional testing.. ---#
        victor = manifest.victor
        prisoner = manifest.prisoner
    
        # Handle the case that the victor and the prisoner are the same.
        if prisoner == victor:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=TokenCannotCaptureItselfException(
                        f"{method}: {TokenCannotCaptureItselfException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the tokens are not on the same board.
        if victor.team.board != prisoner.team.board:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=VictorAndPrisonerConflictingBoardException(
                        f"{method}: {VictorAndPrisonerConflictingBoardException.DEFAULT_MESSAGE}"
                    )
                )
            )
        # Handle the case that the tokens are not enemies.
        if not victor.is_enemy(prisoner):
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=FriendCannotCaptureFriendException(
                        f"{method}: {FriendCannotCaptureFriendException.DEFAULT_MESSAGE}"
                    )
                )
            )




        # Handle the case that prisoner.captor != victor
        if prisoner.captor != victor:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=PrisonerHasDifferentCaptorException(
                        f"{method}: {PrisonerHasDifferentCaptorException.DEFAULT_MESSAGE}"
                    )
                )
            )

        # Handle the case that the victor was not placed on the board
        if victor.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageManifestValidationFailedException(
                    message=f"{method}: {HostageManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=UnformedTokenCannotBeVictorException(
                        f"{method}: {UnformedTokenCannotBeVictorException.DEFAULT_MESSAGE}"
                    )
                )
            )

        # --- Candidate has been successfully validated. Return to the caller. ---#
        return ValidationResult.success(payload=manifest)