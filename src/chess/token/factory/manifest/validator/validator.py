# src/chess/token/factory/manifest/exception/validator.py

"""
Module: chess.token.factory.manifest.exception.validator
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from typing import cast

from chess.team import TeamService
from chess.rank import RankService
from chess.coord import CoordService
from chess.square import SquareService
from chess.system import IdentityService, ValidationResult, Validator
from chess.token import NullTokenBuildManifestException, TokenBuildManifest, TokenBuildManifestValidationFailedException

class TokenBuildManifestValidator(Validator[TokenBuildManifest]):
    
    @classmethod
    def validate(
            cls,
            candidate: TokenBuildManifest,
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            coord_service: CoordService = CoordService(),
            square_service: SquareService = SquareService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[TokenBuildManifest]:
        method = "TokenBuildManifestValidator.validate"
        
        # Handle the nonexistence case.
        if candidate is None:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBuildManifestValidationFailedException(
                    message=f"{method}: {TokenBuildManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullTokenBuildManifestException(f"{method}: {NullTokenBuildManifestException.DEFAULT_MESSAGE}")
                )
            )
        # Handle the case that the candidate is the wrong type
        if not isinstance(candidate, TokenBuildManifest):
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBuildManifestValidationFailedException(
                    message=f"{method}: {TokenBuildManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=NullTokenBuildManifestException(f"{method}: {NullTokenBuildManifestException.DEFAULT_MESSAGE}")
                )
            )
        # --- Cast the candidate to a TokenBuildManifest for additional tests ---#
        manifest = cast(TokenBuildManifest, candidate)
        
        # Handle the case that the id or designation are not certified as safe.
        identity_validation = identity_service.validate_identity(
            id_candidate=manifest.id,
            name_candidate=manifest.designation
        )
        if identity_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBuildManifestValidationFailedException(
                    message=f"{method}: {TokenBuildManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=identity_validation.exception
                )
            )
        # Handle the case that the rank is not certified as safe.
        rank_validation = rank_service.validator.validate(candidate=manifest.rank)
        if rank_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBuildManifestValidationFailedException(
                    message=f"{method}: {TokenBuildManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=rank_validation.exception
                )
            )
        # Handle the case that the team is not certified as safe.
        team_validation = team_service.validator.validate(candidate=manifest.team)
        if team_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBuildManifestValidationFailedException(
                    message=f"{method}: {TokenBuildManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=team_validation.exception
                )
            )
        # Handle the case that the coord is not certified as safe.
        coord_validation = coord_service.validator.validate(candidate=manifest.coord)
        if rank_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBuildManifestValidationFailedException(
                    message=f"{method}: {TokenBuildManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=coord_validation.exception
                )
            )
        # Handle the case that the square is not certified as safe.
        square_validation = square_service.validator.validate(candidate=manifest.opening_square)
        if square_validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenBuildManifestValidationFailedException(
                    message=f"{method}: {TokenBuildManifestValidationFailedException.DEFAULT_MESSAGE}",
                    ex=square_validation.exception
                )
            )
        # --- Return the successfully validated TokenBuildManifest instance to the caller  ---#
        # With all tests passed return the token in the ValidationResult.
        return ValidationResult.success(payload=manifest)
    