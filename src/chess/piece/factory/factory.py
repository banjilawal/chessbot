# src/chess/piece/factory/factory.py

"""
Module: chess.piece.factory.factory
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.team import Team, TeamService
from chess.rank import King, Pawn, Rank, RankService
from chess.piece import CombatantPiece, KingPiece, PawnPiece, Piece, PieceBuildFailedException
from chess.system import (
    BuildFailedException, BuildResult, Builder, IdentityService, LoggingLevelRouter, ValidationResult
)



class PieceFactory(Builder[Piece]):
    """
    # ROLE: Builder, Data Integrity Guarantor
  
    # RESPONSIBILITIES:
    Produce Piece instances whose integrity is always guaranteed. If any attributes do not pass
    their integrity checks, send an exception instead.
  
    # PROVIDES:
    BuildResult[Piece] containing either:
        - On success: Piece in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            id: int,
            name: str,
            rank: Rank,
            team: Team,
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Piece]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate params returns failure include the failure in a BuildResult.
        3.  If the engine is not validation call build_machine_agent. Otherwise, call build_human_agent.
    
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   identity_service (IdentityService)
            *   team_stack_service (teamStackService)
            *   engine_service (Optional[EngineService])
    
        # Returns:
        ValidationResult[TeamStackService] containing either:
            - On success: TeamStackService in the payload.
            - On failure: Exception.
    
        # Raises:
            *   AgentBuildFailedException
        """
        """
        Constructs team_name new Square that works correctly.
    
        Args:
          visitor_name(str): Must pass NameValidator checks.
          bounds(Rank): The bounds which determines how the owner moves and its capture value.
          team_name(Team): Specifies if the owner is white or black.
    
        Returns:
        BuildResult[Piece]: A BuildResult containing either:
          - On success: A valid Piece instance in the payload
          - On failure: Error information and error details
    
        Raises:
        SquareBuildFailedException: Wraps any exceptions raised builder. These are:
          * InvalidNameException: if visitor_name fails validate checks
          * InvalidRankException: if bounds fails validate checks
          * InvalidTeamException: if team_name fails validate checks
          * InvalidTeamAssignmentException: If owner.team_name is different from team_name parameter
          * FullRankQuotaException: If the team_name has no empty slots for the owner.bounds
          * FullRankQuotaException: If owner.team_name is equal to team_name parameter but team_name.roster still does
            not have the owner
        """
        method = "PieceFactory.builder"
        
        try:
            attribute_validation = cls._validate_build_attributes(
                id=id,
                name=name,
                rank=rank,
                team=team
            )
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            
            if isinstance(rank, Pawn):
                return cls.build_pawn_piece(id=id, name=name, team=team)
            
            if isinstance(rank, King):
                return cls.build_king_piece(id=id, name=name, team=team)
            
            return cls.build_combatant_piece(id=id, name=name, rank=rank, team=team)
        
        except Exception as ex:
            raise BuildResult.failure(
                BuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{BuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_pawn_piece(cls, id: int, name: str, team: Team) -> BuildResult[PawnPiece]:
        """"""
        method = "PieceFactory.build_pawn_piece"
        try:
            attribute_validation = cls._validate_build_attributes(id, name, PawnPiece(), team)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            
            piece = PawnPiece(id=id, name=name, rank=Pawn(), team=team)
            
            binding_result = cls._ensure_team_binding(piece=piece, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            
            return BuildResult.success(piece)
        
        except Exception as ex:
            return BuildResult.failure(
                PieceBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_king_piece(cls, id: int, name: str, team: Team) -> BuildResult[KingPiece]:
        """"""
        method = "PieceFactory.build_king_piece"
        try:
            attribute_validation = cls._validate_build_attributes(id, name, King(), team)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            
            piece = KingPiece(id=id, name=name, rank=King(), team=team)
            
            binding_result = cls._ensure_team_binding(piece=piece, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            
            return BuildResult.success(piece)
        
        except Exception as ex:
            return BuildResult.failure(
                PieceBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_combatant_piece(
            cls,
            id: int,
            name: str,
            rank: Rank,
            team: Team
    ) -> BuildResult[CombatantPiece]:
        """"""
        method = "PieceFactory.build_combatant_piece"
        try:
            attribute_validation = cls._validate_build_attributes(id, name, rank, team)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            
            piece = CombatantPiece(id=id, name=name, rank=rank, team=team)
            
            binding_result = cls._ensure_team_binding(piece=piece, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            
            return BuildResult.success(piece)
        
        except Exception as ex:
            return BuildResult.failure(
                PieceBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )
        
    @classmethod
    @LoggingLevelRouter.monitor
    def _ensure_team_binding(cls, piece: Piece, team: Team) -> BuildResult[(Piece, Team)]:
        method = "PieceFactory._verify_team_building"
        try:
            if piece not in team.roster.items:
                team.roster.items.append(piece)
            return BuildResult.success((piece, team))
        except Exception as ex:
            return BuildResult.failure(
                PieceBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _validate_build_attributes(
            cls,
            id: int,
            name: str,
            rank: Rank,
            team: Team,
            rank_service: RankService = RankService(),
            team_service: TeamService = TeamService(),
            identity_service: IdentityService = IdentityService(),
    ) -> ValidationResult[(int, str, Rank, Team)]:
        """"""
        method = "PieceFactory._validate_build_attributes"
        
        try:
            identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
            if identity_validation.is_failure():
                return BuildResult.failure(identity_validation.exception)
            
            rank_validation = rank_service.validator.validate(candidate=rank)
            if rank_validation.is_failure():
                return BuildResult.failure(rank_validation.exception)
            
            team_validation = team_service.validate_team(candidate=team)
            if team_validation.is_failure():
                return BuildResult.failure(team_validation.exception)
            
            return ValidationResult.success((id, name, rank, team))
        except Exception as ex:
            return ValidationResult(
                PieceBuildFailedException(
                    ex=ex,
                    message=(
                        f"{method}: "
                        f"{PieceBuildFailedException.DEFAULT_MESSAGE}"
                    )
                )
            )

# def main():
#   build_outcome = PieceFactory.builder()
#   if build_outcome.is_success():
#     owner = build_outcome.payload
#     print(f"Successfully built owner: {owner}")
#   else:
#     print(f"Failed to builder owner: {build_outcome.err}")
#   #
#   build_outcome = PieceFactory.builder(1, None)
#   if build_outcome.is_success():
#     owner = build_outcome.payload
#     print(f"Successfully built owner: {owner}")
#   else:
#     print(f"Failed to builder owner: {build_outcome.err}")
#
# if __name__ == "__main__":
#   main()
