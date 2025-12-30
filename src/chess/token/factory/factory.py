# src/chess/token/factory/factory.py

"""
Module: chess.token.factory.factory
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.coord import CoordDataService
from chess.square import Square, SquareService
from chess.team import Team, TeamService
from chess.rank import King, Pawn, Rank, RankService
from chess.token import (
    CombatantToken, CombatantTokenBuildFailedException, KingToken, KingTokenBuildFailedException, PawnToken,
    PawnTokenBuildFailedException, Token, TokenBuildFailedException
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
        *   build:  -> BuildResult[PawnToken|KingToken|CombatantToken]

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            name: str,
            rank: Rank,
            team: Team,
            roster_number: int,
            opening_square: Square,
            id: int = id_emitter.token_id,
            square_integrity: SquareService = SquareService(),
            rank_integrity: RankService = RankService(),
            team_integrity: TeamService = TeamService(),
            positions: CoordDataService = CoordDataService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[PawnToken|KingToken|CombatantToken]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate params returns failure include the failure in a BuildResult.
    
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
        BuildResult[Position] containing either:
            - On success: Token in the payload.
            - On failure: Exception.
    
        # RAISES:
            *   TokenBuildFailedException
        """
        method = "TokenFactory.builder"
        
        try:
            # First step in the error detection process is handing off resource certification to
            # validate_build_attributes. This decouples verification logic from build logic so
            # each factory method can run independently and build can direct which product
            # should be manufactured.
            attribute_validation = cls._validate_build_attributes(
                id=id,
                name=name,
                rank=rank,
                team=team,
                roster_number=roster_number,
                opening_square=opening_square,
            )
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            
            if isinstance(rank, Pawn):
                return cls.build_pawn_token(id=id, name=name, team=team)
            
            if isinstance(rank, King):
                return cls.build_king_token(id=id, name=name, team=team)
            
            return cls.build_combatant_token(id=id, name=name, rank=rank, team=team)
        
        # Finally, catch any missed exception and wrap A TokenBuildFailed exception around it
        # then return the exception-chain inside a BuildResult.
        except Exception as ex:
            raise BuildResult.failure(
                TokenBuildFailedException(ex=ex, message=f"{method}: {BuildFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_pawn_token(
            cls,
            id: int,
            name: str,
            team: Team,
            roster_number: int,
            opening_square: Square,
    ) -> BuildResult[PawnToken]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate_build_params returns failure include the failure in a BuildResult.
        3.  Otherwise, construct a PawnToken.
        4.  Register token with its team if its not already in team.roster.
        5.  Return the registered PawnToken inside a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   team (Team)

        # RETURNS:
        BuildResult[PawnToken] containing either:
            - On success: PawnToken in the payload.
            - On failure: Exception.

        # RAISES:
            *   PawnTokenBuildFailedException
        """
        method = "TokenFactory.build_pawn_token"
        
        try:
            # Verify the build resources.
            attribute_validation = cls._validate_build_attributes(id, name, Pawn(), team, roster_number, opening_square)
            if attribute_validation.is_failure:
                return BuildResult(exception=attribute_validation.exception)
            # If no errors are detected build the KingToken object.
            token = PawnToken(id=id, name=name, rank=Pawn(), team=team)
            
            # If the Token is not in team.roster register it.
            binding_result = cls._ensure_team_binding(token=token, team=team)
            if binding_result.is_failure:
                return BuildResult.failure(binding_result.exception)
            # Send the successfully built and registered PawnToken inside a BuildResult.
            return BuildResult.success(token)
        
        # Finally, catch any missed exception and wrap A TokenBuildFailed exception around it
        # then return the exception-chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                PawnTokenBuildFailedException(
                    ex=ex, message=f"{method}: {PawnTokenBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_king_token(
            cls,
            id: int,
            name: str,
            team: Team,
            roster_number: int,
            opening_square: Square,
    ) -> BuildResult[KingToken]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate_build_params returns failure include the failure in a BuildResult.
        3.  Otherwise, construct a KingToken.
        4.  Register token with its team if its not already in team.roster.
        5.  Return the registered KingToken inside a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   team (Team)

        # RETURNS:
        BuildResult[KingToken] containing either:
            - On success: PawnToken in the payload.
            - On failure: Exception.

        # RAISES:
            *   KingTokenBuildFailedException
        """
        method = "TokenFactory.build_king_token"
        
        try:
            # Verify the build resources.
            attribute_validation = cls._validate_build_attributes(id, name, King(), team, roster_number, opening_square)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            # If no errors are detected build the KingToken object.
            token = KingToken(id=id, name=name, rank=King(), team=team)
            
            # If the Token is not in team.roster register it.
            binding_result = cls._ensure_team_binding(token=token, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            # Send the successfully built and registered CombatantToken inside a BuildResult.
            return BuildResult.success(token)
        
        # Finally, catch any missed exception and wrap A TokenBuildFailed exception around it
        # then return the exception-chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                KingTokenBuildFailedException(
                    ex=ex, message=f"{method}: {KingTokenBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_combatant_token(
            cls,
            id: int,
            name: str,
            rank: Rank,
            team: Team,
            roster_number: int,
            opening_square: Square
    ) -> BuildResult[CombatantToken]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate_build_params returns failure include the failure in a BuildResult.
        3.  Otherwise, construct a CombatantToken.
        4.  Register token with its team if its not already in team.roster.
        5.  Return the registered CombatantToken inside a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   team (Team)

        # RETURNS:
        BuildResult[CombatantToken] containing either:
            - On success: CombatantToken in the payload.
            - On failure: Exception.

        # RAISES:
            *   KingTokenBuildFailedException
        """
        method = "TokenFactory.build_combatant_token"
        try:
            # Verify the build resources.
            attribute_validation = cls._validate_build_attributes(id, name, rank, team, roster_number, opening_square)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            # If no errors are detected build the CombatantToken object.
            token = CombatantToken(id=id, name=name, rank=rank, team=team)
            
            # If the Token is not in team.roster register it.
            binding_result = cls._ensure_team_binding(token=token, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            # Send the successfully built and registered CombatantToken inside a BuildResult.
            return BuildResult.success(token)
        
        # Finally, catch any missed exception and wrap A TokenBuildFailed exception around it
        # then return the exception-chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CombatantTokenBuildFailedException(
                    ex=ex, message=f"{method}: {CombatantTokenBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _ensure_team_binding(cls, token: Token, team: Team) -> BuildResult[(Token, Team)]:
        method = "TokenFactory._verify_team_building"
        try:
            # If the Token is not in team.roster register it.
            if token not in team.roster.items:
                team.roster.items.append(token)
                
            return BuildResult.success((token, team))
        # Finally, catch any missed exception and wrap A TokenBuildFailed exception around it
        # then return the exception-chain inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                TokenBuildFailedException(ex=ex, message=f"{method}: {TokenBuildFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_build_attributes(
            cls,
            id: int,
            name: str,
            rank: Rank,
            team: Team,
            roster_number: int,
            opening_square: Square,
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            identity_service: IdentityService = IdentityService(),
            square_service: SquareService = SquareService(),
    ) -> ValidationResult[(int, str, Rank, Team, int, Square)]:
        """
        # ACTION
        validate_build_attributes. This decouples verification logic from build logic so
        each factory method can run independently and build can direct which product
        should be manufactured.
        """
        method = "TokenFactory._validate_build_attributes"
        try:
            # Start the error detection process.
            identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
            if identity_validation.is_failure():
                return BuildResult.failure(identity_validation.exception)
            
            rank_validation = rank_service.item_validator.validate(candidate=rank)
            if rank_validation.is_failure():
                return BuildResult.failure(rank_validation.exception)
            
            team_validation = team_service.item_validator.validate(candidate=team)
            if team_validation.is_failure():
                return BuildResult.failure(team_validation.exception)

        
            square_validation = square_service.item_validator.validate(candidate=opening_square)
            if square_validation.is_failure():
                return BuildResult.failure(square_validation.exception)
            
            roster_number_validation = identity_service.validate_id(candidate=roster_number)
            if roster_number_validation.is_failure():
                return BuildResult.failure(roster_number_validation.exception)
            
            # If no errors are detected return the successfully validated (id, designation, rank, team) tuple.
            return ValidationResult.success((id, name, rank, team, roster_number, opening_square))
        
        # Finally, catch any missed exception and wrap A TokenBuildFailed exception around it
        # then return the exception-chain inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                TokenBuildFailedException(ex=ex, message=f"{method}: {TokenBuildFailedException.DEFAULT_MESSAGE}")
            )