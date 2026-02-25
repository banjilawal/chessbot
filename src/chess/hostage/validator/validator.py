# src/chess/hostage/validator/validator.py

"""
Module: chess.hostage.validator
Author: Banji Lawal
Created: 2026-01-18
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, cast

from chess.square import SquareService
from chess.token import TokenBoardState, TokenService
from chess.hostage import (
    PrisonerCannotBeActiveCombatantException, FriendCannotCaptureFriendException, Hostage,
    HostageValidationException, NullHostageException, PrisonerAlreadyHasHostageException,
    PrisonerCapturedByDifferentEnemyException, TokenCannotCaptureItselfException, UnformedTokenCannotBeVictorException,
    VictorAndPrisoneOnDifferentBoardsException, PrisonerCapturedOnDifferentSquareException,
)
from chess.system import IdentityService, LoggingLevelRouter, ValidationResult,Validator



class HostageValidator(Validator[Hostage]):
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
            token_service: TokenService = TokenService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[Hostage]:
        """
        # ACTION:
            1.  verify hostage_variety is a not-null HostageVariety object.
            2.  Use hostage_variety to pick which Validation method will create the concrete Hostage object.
        # PARAMETERS:
            *   candidate (int)
            *   token_service (TokenService)
            *   square_service (SquareService)
            *   identity_service (IdentityService)
        # RETURN:
            *   ValidationResult[Hostage] containing either:
                    - On failure: Exception.
                    - On success: Hostage in the payload.
        # RAISES:
            *   TypeError
            *   NullHostageException
            *   KingCannotBeCapturedException
            *   TokenCannotCaptureItselfException
            *   FriendCannotCaptureFriendException
            *   PrisonerCapturedByDifferentEnemyException
            *   UnformedTokenCannotBeVictorException
            *   PrisonerCannotBeActiveCombatantException
            *   HostageValidationException
            *   VictorAndPrisonerOnDifferentBoardsException
            *   PrisonerAlreadyHasHostageException
            *   PrisonerCapturedOnDifferentSquareException
        """
        method = "HostageValidator.validate"
        
        # Handle the case that, the candidate does not exist.
        if candidate is None:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=NullHostageException(f"{method}: {NullHostageException.MSG}")
                )
            )
        # Handle the case, that the candidate is the wrong type.
        if not isinstance(candidate, Hostage):
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=TypeError(f"{method}: Expected Hostage, {type(candidate).__name__} instead.")
                )
            )
        
        # --- Cast the candidate into a Hostage for additional testing. ---#
        manifest = cast(Hostage, candidate)
        
        # Handle the case that, the id is not certified safe.
        id_validation = identity_service.validate_id(candidate=id)
        if id_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=id_validation.exception
                )
            )
        # Handle the case that, the item where the capture occurred is not certified safe.
        captured_square_validation = square_service.validator.validate(candidate=manifest.captured_square)
        if captured_square_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=captured_square_validation.exception
                )
            )
        # Handle the case that, the victor's item is not certified safe.
        victor_square_validation = square_service.validator.validate(candidate=manifest.victor_square)
        if victor_square_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=victor_square_validation.exception
                )
            )
        # --- Perform tests on the matrix.prisoner that do not rely on the victor. ---#
        
        # Handle the case that, the prisoner is not a safe combatant
        prisoner_validation = token_service.validator.verify_token_is_combatant(candidate=manifest.prisoner)
        if prisoner_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=prisoner_validation.exception
                )
            )
        # Handle the case that, the prisoner is still active:
        if manifest.prisoner.is_active:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=PrisonerCannotBeActiveCombatantException(
                        f"{method}: {PrisonerCannotBeActiveCombatantException.MSG}"
                    )
                )
            )
        # Handle the case that, prisoner already has a manifest.
        if not manifest.prisoner.has_hostage:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=PrisonerAlreadyHasHostageException(
                        f"{method}: {PrisonerAlreadyHasHostageException.MSG}"
                    )
                )
            )
        # Handle the case that, the prisoner was capture on a different item.
        if manifest.prisoner.current_position != manifest.captured_square.coord:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=PrisonerCapturedOnDifferentSquareException(
                        f"{method}: {PrisonerCapturedOnDifferentSquareException.MSG}"
                    )
                )
            )
        # Extract the prisoner into a temporary variable.
        prisoner = manifest.prisoner
            
            # --- Perform tests on the manifest.victor that do not rely on the prisoner. ---#
            
        # Handle the case that, the victor is not certified safe.
        victor_validation = token_service.validator.validate(candidate=manifest.victor)
        if victor_validation.failure:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=victor_validation.exception
                )
            )
        # The victor can get captured later. Only test that is has been formed.
        if manifest.victor.board_state == TokenBoardState.NEVER_BEEN_PLACED:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=UnformedTokenCannotBeVictorException(
                        f"{method}: {UnformedTokenCannotBeVictorException.MSG}"
                    )
                )
            )
        # Extract the victor into a temporary variable.
        victor = manifest.victor

        # --- Perform tests that require the prisoner and victor. ---#
    
        # Handle the case that, the victor and the prisoner are the same.
        if prisoner == victor:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=TokenCannotCaptureItselfException(
                        f"{method}: {TokenCannotCaptureItselfException.MSG}"
                    )
                )
            )
        # Handle the case that, the tokens are not on the same board.
        if victor.team.board != prisoner.team.board:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=VictorAndPrisoneOnDifferentBoardsException(
                        f"{method}: {VictorAndPrisoneOnDifferentBoardsException.MSG}"
                    )
                )
            )
        # Handle the case that, the tokens are not enemies.
        if not victor.is_enemy(prisoner):
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=FriendCannotCaptureFriendException(
                        f"{method}: {FriendCannotCaptureFriendException.MSG}"
                    )
                )
            )
        # Handle the case that, prisoner.captor != victor
        if prisoner.captor != victor:
            # Send the exception chain on failure
            return ValidationResult.failure(
                HostageValidationException(
                    msg=f"{method}: {HostageValidationException.MSG}",
                    ex=PrisonerCapturedByDifferentEnemyException(
                        f"{method}: {PrisonerCapturedByDifferentEnemyException.MSG}"
                    )
                )
            )
        # --- Candidate has been successfully validated. Return to the caller. ---#
        return ValidationResult.success(payload=manifest)