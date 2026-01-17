# src/chess/token/factory/factory.py

"""
Module: chess.token.factory.factory
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.coord import CoordDataService, UniqueCoordDataService
from chess.square import Square, SquareService
from chess.team import Team, TeamService
from chess.rank import King, Pawn, Rank, RankService
from chess.token import (
    CombatantToken, CombatantTokenBuildFailedException, KingToken, KingTokenBuildFailedException, PawnToken,
    PawnTokenBuildFailedException, Token, TokenBuildFailedException, TokenService
)
from chess.system import (
    BuildFailedException, BuildResult, Builder, IdentityService, LoggingLevelRouter, ValidationResult, id_emitter
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
            rank: Rank,
            owner: Team,
            designation: str,
            roster_number: int,
            opening_square: Square,
            id: int = id_emitter.token_id,
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            square_service
            piece_service: TokenService = TokenService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[PawnToken|KingToken|CombatantToken]:
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
        param_validation = cls._validate_build_params(
            id=id,
            rank=rank,
            owner=owner,
            designation=designation,
            roster_number=roster_number,
            opening_square=opening_square,
            rank_service=rank_service,
            team_service=team_service,
            identity_service=identity_service,
        )
        if param_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=param_validation.exception
                )
            )
        token = None
        # --- Route to the appropriate concrete Token builder method. ---#
        
        # Build path for Pawns.
        if isinstance(rank, Pawn):
            token = cls._build_pawn(id=id, designation=designation, owner=owner, roster_number=roster_number)
        # Build path for Kings
        elif isinstance(rank, King):
            token = cls._build_king(id=id, designation=designation, owner=owner, roster_number=roster_number)
        else:
            token = cls._build_combatant(
                id=id, designation=designation, owner=owner, rank=rank, roster_number=roster_number
            )
        # Get the RelationReport between the team's roster to see if the token can be added to the team's roster.
        relation_report = team_service.roster_relation_analyzer.analyze(
            candidate_primary=owner,
            candidate_satellite=token,
            team_service=team_service,
            piece_service=piece_service,
        )
        # Handle the case that the relation analysis ran into an error.
        if relation_report.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=relation_report.exception
                )
            )
        # Handle the case that the piece has a different owner.
        if relation_report.does_not_exist:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=relation_report.exception
                )
            )
        # Handle the case that the piece is already registered with its owner.
        if relation_report.fully_exists:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=
                )
            )
        # Last relation outcome is the piece has not registered with its owner. Do an insertion to complete
        # the registration process which creates a fully bidirectional relation between the token and its owner.
        insertion_result = team_service.roster.insert(token)
        
        # Handle the case inserting the token in the owner's roster fails.
        if insertion_result.is_failure:
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=insertion_result.exception
                )
            )
        # If all the steps completed successfully return the token in the BuildResult.
        return BuildResult.success(token)
            
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_pawn(cls, id: int, designation: str, team: Team, roster_number: int) -> PawnToken:
        return PawnToken(
            id=id,
            owner=team,
            rank=Pawn(),
            designation=designation,
            roster_number=roster_number,
            positions=UniqueCoordDataService()
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_king(cls, id: int, designation: str, owner: Team, roster_number: int) -> KingToken:
        return PawnToken(
            id=id,
            owner=owner,
            rank=King(),
            designation=designation,
            roster_number=roster_number,
            positions=UniqueCoordDataService()
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _build_combatant(cls, id: int, designation: str, owner: Team, rank: Rank, roster_number: int) -> CombatantToken:
        return PawnToken(
            id=id,
            owner=owner,
            rank=rank,
            designation=designation,
            roster_number=roster_number,
            positions=UniqueCoordDataService()
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_build_params(
            cls,
            id: int,
            rank: Rank,
            team: Team,
            designation: str,
            roster_number: int,
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[(int, str, Rank, Team, int)]:
        """
        # ACTION:
            1.  If any build parameter fails its validation send the exception in the ValidationResult. Else,
                return the certified tuple of parameters in the ValidationResult.
        # PARAMETERS:
            *   id (int)
            *   rank (str)
            *   team (Team)
            *   designation (str)
            *   roster_number (int)
            *   rank_service (RankService)
            *   team_service (TeamService)
            *   identity_service (IdentityService)
        # RETURNS:
            *   ValidationResult[(int, str, Rank, Team, int)] containing either:
                    - On failure: Exception.
                    - On success: CombatantToken in the payload.
        # RAISES:
            *   KingTokenBuildFailedException
        """
        method = "TokenFactory._validate_build_attributes"

        # Handle the case that either id or designation fail their validation.
        identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=designation)
        if identity_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=identity_validation.exception,
                )
            )
        # Handle the case that rank validation fails.
        rank_validation = rank_service.item_validator.validate(candidate=rank)
        if rank_validation.is_failure():
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=rank_validation.exception,
                )
            )
        # Handle the case that team validation fails.
        team_validation = team_service.item_validator.validate(candidate=team)
        if team_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=team_validation.exception,
                )
            )
        # Handle the case that roster_number validation fails.
        roster_number_validation = identity_service.validate_id(candidate=roster_number)
        if roster_number_validation.is_failure:
            # Return the exception chain on failure.
            return BuildResult.failure(
                TokenBuildFailedException(
                    message=f"{method}: {TokenBuildFailedException.ERROR_CODE}",
                    ex=roster_number_validation.exception,
                )
            )
        # On successfully certifying the build parameters return them as a tuple in the ValidationResult.
        return ValidationResult.success((id, designation, rank, team, roster_number))
