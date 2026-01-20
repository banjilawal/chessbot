# src/chess/token/factory/factory.py

"""
Module: chess.token.factory.factory
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.square import Square
from chess.rank import King, Pawn
from chess.system import BuildResult, Builder, LoggingLevelRouter
from chess.team import EnemyCannotJoinTeamRosterException, Team, TeamService

from chess.token import (
    AddingDuplicateTokenException, CombatantToken, KingToken, PawnToken, TokenBuildFailedException, TokenBuildManifest,
    TokenBuildManifestValidator, Token
)


class TokenFactory(Builder[Token]):
    """
    # ROLE: Factory, Data Integrity Guarantor

    # RESPONSIBILITIES:
    1.  Produce Token instances whose integrity is guaranteed at creation.
    2.  Manage construction of Token instances that can be used safely by the client.
    3.  Ensure params for Token creation have met the application's safety contract.
    4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

    # PARENT:
        *   Builder

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
            manifest: TokenBuildManifest,
            # team_service: TeamService = TeamService(),
            manifest_validator: TokenBuildManifestValidator = TokenBuildManifestValidator(),
    ) -> BuildResult[Token]:
        """
        # ACTION:
            1.  If any build param fails its certification tests send the exception in the BuildResult. Else,
                route to the appropriate concrete Token builder method.
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   rank (Rank)
            *   team (Team)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   positions (CoordDataService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   BuildResult[Position] containing either:
                    - On failure: Exception.
                    - On success: Token in the payload.
        # RAISES:
            *   TokenBuildFailedException
        """
        method = "TokenFactory.builder"
        
        # Handle the case that any of the build params is not safe.
        validation = manifest_validator.validate(candidate=manifest)
        if validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=validation.exception
                )
            )
        # --- Route to the appropriate concrete Token builder method. ---#
        
        # Build path for Pawns.
        if isinstance(manifest.rank, Pawn):
            return cls._build_pawn(
                id=manifest.id,
                owner=manifest.owner,
                designation=manifest.designation,
                roster_number=manifest.roster_number,
                opening_square=manifest.opening_square,
            )
        # Build path for Kings
        elif isinstance(manifest.rank, King):
            return cls._build_king(
                id=manifest.id,
                owner=manifest.owner,
                designation=manifest.designation,
                roster_number=manifest.roster_number,
                opening_square=manifest.opening_square,
            )
        else:
            return cls._build_combatant(
                id=manifest.id,
                owner=manifest.owner,
                designation=manifest.designation,
                roster_number=manifest.roster_number,
                opening_square=manifest.opening_square,
            )
        # # Get the RelationReport between the team's roster to see if the token can be added to the team's roster.
        # relation_report = team_service.roster_relation_analyzer.analyze(
        #     candidate_primary=manifest.owner,
        #     candidate_satellite=token,
        #     team_service=team_service,
        #     piece_service=manifest.owner.roster.members.integrity_service,
        # )
        # # Handle the case that the relation analysis ran into an error.
        # if relation_report.is_failure:
        #     # Return the exception chain on failure.
        #     return BuildResult.failure(
        #         TokenBuildFailedException(
        #             message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
        #             ex=relation_report.exception
        #         )
        #     )
        # # Handle the case that the piece has a different owner.
        # if relation_report.does_not_exist:
        #     # Return the exception chain on failure.
        #     return BuildResult.failure(
        #         TokenBuildFailedException(
        #             message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
        #             ex=EnemyCannotJoinTeamRosterException(f"{method}: {EnemyCannotJoinTeamRosterException.DEFAULT_MESSAGE}")
        #         )
        #     )
        # # Handle the case that the piece is already registered with its owner.
        # if relation_report.fully_exists:
        #     # Return the exception chain on failure.
        #     return BuildResult.failure(
        #         TokenBuildFailedException(
        #             message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
        #             ex=AddingDuplicateTokenException(f"{method}: {AddingDuplicateTokenException.DEFAULT_MESSAGE}")
        #         )
        #     )
        # # Last relation outcome is the piece has not registered with its owner. Do an insertion to complete
        # # the registration process which creates a fully bidirectional relation between the token and its owner.
        # insertion_result = team_service.add_member(team=manifest.owner, token=token)
        #
        # # Handle the case that the insertion failed.
        # if insertion_result.is_failure:
        #     return BuildResult.failure(
        #         TokenBuildFailedException(
        #             message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
        #             ex=insertion_result.exception
        #         )
        #     )
        # If all the steps completed successfully return the token in the BuildResult.
        # return BuildResult.success(token)
            
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_pawn(
            cls,
            id: int,
            owner: Team,
            designation: str,
            roster_number: int,
            opening_square: Square
    ) -> PawnToken:
        return BuildResult.success(
            payload=PawnToken(
                id=id,
                team=owner,
                designation=designation,
                roster_number=roster_number,
                opening_square=opening_square,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_king(
            cls,
            id: int,
            owner: Team,
            designation: str,
            roster_number: int,
            opening_square: Square
    ) -> KingToken:
        return BuildResult.success(
                payload=KingToken(
                id=id,
                team=owner,
                designation=designation,
                roster_number=roster_number,
                opening_square=opening_square,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_combatant(
            cls,
            id: int,
            owner: Team,
            designation: str,
            roster_number: int,
            opening_square: Square
    ) -> CombatantToken:
        return BuildResult.success(
                payload=CombatantToken(
                id=id,
                team=owner,
                rank=King(),
                designation=designation,
                roster_number=roster_number,
                opening_square=opening_square,
            )
        )