# src/chess/piece/factory/factory.py

"""
Module: chess.piece.factory.factory
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.coord import CoordDataService
from chess.square import Square, SquareCertifier
from chess.team import Team, TeamCertifier
from chess.rank import King, Pawn, Rank, RankCertifier
from chess.piece import (
    CombatantPiece, CombatantPieceBuildFailedException, KingPiece, KingPieceBuildFailedException, PawnPiece,
    PawnPieceBuildFailedException, Piece, PieceBuildFailedException
)
from chess.system import (
    BuildFailedException, BuildResult, Builder, IdentityService, LoggingLevelRouter, ValidationResult, id_emitter
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
    
    # CONSTRUCTOR:
    None

    # CLASS METHODS:
        *   build(
                    name: str,
                    rank: Rank,
                    team: Team,
                    id: int = id_emitter.piece_id,
                    rank_certifier: RankCertifier = RankCertifier(),
                    team_certifier: TeamCertifier = TeamCertifier(),
                    positions: CoordDataService = CoordDataService(),
                    identity_service: IdentityService = IdentityService(),
        ) -> BuildResult[Piece]:
        
        For ease of use and cleaner code dependencies are given default values. All flags must
        be turned set to null byy default. Only activated flags should have a not-null value.
        
    # INSTANCE METHODS:
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
            id: int = id_emitter.piece_id,
            # square_integrity: SquareCertifier = SquareCertifier(),
            # rank_integrity: RankCertifier = RankCertifier(),
            # team_integrity: TeamCertifier = TeamCertifier(),
            # positions: CoordDataService = CoordDataService(),
            # identity_service: IdentityService = IdentityService(),
    ) -> BuildResult[Piece]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate params returns failure include the failure in a BuildResult.
    
        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   rank (Rank)
            *   team (Team)
            *   rank_certifier (RankCertifier)
            *   team_certifier (TeamCertifier)
            *   positions (CoordDataService)
            *   identity_service (IdentityService)
    
        # Returns:
        BuildResult[Position] containing either:
            - On success: Piece in the payload.
            - On failure: Exception.
    
        # Raises:
            *   PieceBuildFailedException
        """
        method = "PieceFactory.builder"
        
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
                return cls.build_pawn_piece(id=id, name=name, team=team)
            
            if isinstance(rank, King):
                return cls.build_king_piece(id=id, name=name, team=team)
            
            return cls.build_combatant_piece(id=id, name=name, rank=rank, team=team)
        
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            raise BuildResult.failure(
                PieceBuildFailedException(ex=ex, message=f"{method}: {BuildFailedException.DEFAULT_MESSAGE}")
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_pawn_piece(
            cls,
            id: int,
            name: str,
            team: Team,
            roster_number: int,
            opening_square: Square,
    ) -> BuildResult[PawnPiece]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate_build_params returns failure include the failure in a BuildResult.
        3.  Otherwise, construct a PawnPiece.
        4.  Register piece with its team if its not already in team.roster.
        5.  Return the registered PawnPiece inside a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   team (Team)

        # Returns:
        BuildResult[PawnPiece] containing either:
            - On success: PawnPiece in the payload.
            - On failure: Exception.

        # Raises:
            *   PawnPieceBuildFailedException
        """
        method = "PieceFactory.build_pawn_piece"
        
        try:
            # Verify the build resources.
            attribute_validation = cls._validate_build_attributes(id, name, Pawn(), team, roster_number, opening_square)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            # If no errors are detected build the KingPiece object.
            piece = PawnPiece(id=id, name=name, rank=Pawn(), team=team)
            
            # If the Piece is not in team.roster register it.
            binding_result = cls._ensure_team_binding(piece=piece, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            # Send the successfully built and registered PawnPiece inside a BuildResult.
            return BuildResult.success(piece)
        
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                PawnPieceBuildFailedException(
                    ex=ex, message=f"{method}: {PawnPieceBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_king_piece(
            cls,
            id: int,
            name: str,
            team: Team,
            roster_number: int,
            opening_square: Square,
    ) -> BuildResult[KingPiece]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate_build_params returns failure include the failure in a BuildResult.
        3.  Otherwise, construct a KingPiece.
        4.  Register piece with its team if its not already in team.roster.
        5.  Return the registered KingPiece inside a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   team (Team)

        # Returns:
        BuildResult[KingPiece] containing either:
            - On success: PawnPiece in the payload.
            - On failure: Exception.

        # Raises:
            *   KingPieceBuildFailedException
        """
        method = "PieceFactory.build_king_piece"
        
        try:
            # Verify the build resources.
            attribute_validation = cls._validate_build_attributes(id, name, King(), team, roster_number, opening_square)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            # If no errors are detected build the KingPiece object.
            piece = KingPiece(id=id, name=name, rank=King(), team=team)
            
            # If the Piece is not in team.roster register it.
            binding_result = cls._ensure_team_binding(piece=piece, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            # Send the successfully built and registered CombatantPiece inside a BuildResult.
            return BuildResult.success(piece)
        
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                KingPieceBuildFailedException(
                    ex=ex, message=f"{method}: {KingPieceBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_combatant_piece(
            cls,
            id: int,
            name: str,
            rank: Rank,
            team: Team,
            roster_number: int,
            opening_square: Square
    ) -> BuildResult[CombatantPiece]:
        """
        # ACTION:
        1.  Call _validate_build_params. to verify inputs are safe.
        2.  If the _validate_build_params returns failure include the failure in a BuildResult.
        3.  Otherwise, construct a CombatantPiece.
        4.  Register piece with its team if its not already in team.roster.
        5.  Return the registered CombatantPiece inside a BuildResult.

        # PARAMETERS:
            *   id (int)
            *   name (str)
            *   team (Team)

        # Returns:
        BuildResult[CombatantPiece] containing either:
            - On success: CombatantPiece in the payload.
            - On failure: Exception.

        # Raises:
            *   KingPieceBuildFailedException
        """
        method = "PieceFactory.build_combatant_piece"
        try:
            # Verify the build resources.
            attribute_validation = cls._validate_build_attributes(id, name, rank, team, roster_number, opening_square)
            if attribute_validation.is_failure():
                return BuildResult(exception=attribute_validation.exception)
            # If no errors are detected build the CombatantPiece object.
            piece = CombatantPiece(id=id, name=name, rank=rank, team=team)
            
            # If the Piece is not in team.roster register it.
            binding_result = cls._ensure_team_binding(piece=piece, team=team)
            if binding_result.is_failure():
                return BuildResult.failure(binding_result.exception)
            # Send the successfully built and registered CombatantPiece inside a BuildResult.
            return BuildResult.success(piece)
        
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                CombatantPieceBuildFailedException(
                    ex=ex, message=f"{method}: {CombatantPieceBuildFailedException.DEFAULT_MESSAGE}"
                )
            )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _ensure_team_binding(cls, piece: Piece, team: Team) -> BuildResult[(Piece, Team)]:
        method = "PieceFactory._verify_team_building"
        try:
            # If the Piece is not in team.roster register it.
            if piece not in team.roster.items:
                team.roster.items.append(piece)
                
            return BuildResult.success((piece, team))
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a BuildResult.
        except Exception as ex:
            return BuildResult.failure(
                PieceBuildFailedException(ex=ex, message=f"{method}: {PieceBuildFailedException.DEFAULT_MESSAGE}")
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
            rank_certifier: RankCertifier = RankCertifier(),
            team_certifier: TeamCertifier = TeamCertifier(),
            identity_service: IdentityService = IdentityService(),
            square_certifier: SquareCertifier = SquareCertifier(),
    ) -> ValidationResult[(int, str, Rank, Team, int, Square)]:
        """
        # ACTION
        validate_build_attributes. This decouples verification logic from build logic so
        each factory method can run independently and build can direct which product
        should be manufactured.
        """
        method = "PieceFactory._validate_build_attributes"
        try:
            # Start the error detection process.
            identity_validation = identity_service.validate_identity(id_candidate=id, name_candidate=name)
            if identity_validation.is_failure():
                return BuildResult.failure(identity_validation.exception)
            
            rank_validation = rank_certifier.item_validator.validate(candidate=rank)
            if rank_validation.is_failure():
                return BuildResult.failure(rank_validation.exception)
            
            team_validation = team_certifier.validator.validate(candidate=team)
            if team_validation.is_failure():
                return BuildResult.failure(team_validation.exception)

        
            square_validation = square_certifier.validator.validate(candidate=opening_square)
            if square_validation.is_failure():
                return BuildResult.failure(square_validation.exception)
            
            roster_number_validation = identity_service.validate_id(candidate=roster_number)
            if roster_number_validation.is_failure():
                return BuildResult.failure(roster_number_validation.exception)
            
            # If no errors are detected return the successfully validated (id, name, rank, team) tuple.
            return ValidationResult.success((id, name, rank, team, roster_number, opening_square))
        
        # Finally, if there is an unhandled exception Wrap a PieceBuildFailed exception around it
        # then return the exceptions inside a ValidationResult.
        except Exception as ex:
            return ValidationResult.failure(
                PieceBuildFailedException(ex=ex, message=f"{method}: {PieceBuildFailedException.DEFAULT_MESSAGE}")
            )