# src/chess/rank/factory/factory.py

"""
Module: chess.rank.factory.factory
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""
from typing import Optional
from wsgiref.validate import validator

from chess.system import Builder, BuildResult, IdEmitter, LoggingLevelRouter, id_emitter
from chess.rank import (
    Rank, King, Pawn, Knight, Bishop, RankSpecValidator, Rook, Queen, RankSpec, NullRankSpecException,
    RankBuildFailedException
)


class RankFactory(Builder[Rank]):
    """
    # ROLE: Factory, Data Integrity Guarantor
  
    # RESPONSIBILITIES:
        1. Manage construction of Rank instances that can be used safely by the client.
        2. Ensure params for Rank creation have met the application's safety contract.

    # PROVIDES:
      ValidationResult[Rank] containing either:
            - On success: Rank in the payload.
            - On failure: Exception.
  
    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            rank_spec: RankSpec,
            id: Optional[int] = None,
            rank_spec_validator: RankSpecValidator = RankSpecValidator(),
    ) -> BuildResult[Rank]:
        """
        # Action:
        Given a RankSpec, return an appropriate Rank object.

        # Parameters:
            * rank_spec (RankSpec)

        # Returns:
          BuildResult[Rank] containing either:
                - On success: a concrete Rank in the payload.
                - On failure: Exception.

        # Raises:
            * RankBuildFailedException
        """
        method = "RankFactory.builder"
        try:
            validation = rank_spec_validator.validate(rank_spec)
            if validation.is_failure():
                return BuildResult.failure(validation.exception)
            
            if rank_spec == RankSpec.KING:
                return cls.build_king_rank(id=id)
            if rank_spec == RankSpec.PAWN:
                return cls.build_pawn_rank(id=id)
            if rank_spec == RankSpec.KNIGHT:
                return cls.build_knight_rank(id=id)
            if rank_spec == RankSpec.BISHOP:
                return cls.build_bishop_rank(id=id)
            if rank_spec == RankSpec.ROOK:
                return cls.build_rook_rank(id=id)
            if rank_spec == RankSpec.QUEEN:
                return cls.build_queen_rank(id=id)
            
        except Exception as ex:
            return BuildResult.failure(
                RankBuildFailedException(ex=ex, message=f"{method}: {RankBuildFailedException.DEFAULT_MESSAGE}")
            )
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_king_rank(cls, id: int = id_emitter.king_id) -> BuildResult[King]:
        """
        # Action:
        Returns a BuildResult containing a King instance.

        # Parameters:
        None

        # Returns:
          BuildResult[King] containing either:
                - On success: a King in the payload.
                - On failure: Exception.

        # Raises:
        None
        """
        method = "RankFactory.build_king_rank"
        return BuildResult.success(
            King(
                id=id,
                name=RankSpec.KING.name,
                designation=RankSpec.KING.designation,
                ransom=RankSpec.KING.ransom,
                team_quota=RankSpec.KING.team_quota,
                quadrants=RankSpec.KING.quadrants,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_pawn_rank(cls, id: int = id_emitter.pawn_id) -> BuildResult[Pawn]:
        """
        # Action:
        Returns a BuildResult containing a Pawn instance.

        # Parameters:
        None

        # Returns:
          BuildResult[Pawn] containing either:
                - On success: a Pawn in the payload.
                - On failure: Exception.

        # Raises:
        None
        """
        method = "RankFactory.build_pawn_rank"
        return BuildResult.success(
            Pawn(
                id=id_emitter.pawn_id,
                name=RankSpec.PAWN.name,
                designation=RankSpec.PAWN.designation,
                ransom=RankSpec.PAWN.ransom,
                team_quota=RankSpec.PAWN.team_quota,
                quadrants=RankSpec.PAWN.quadrants,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_knight_rank(cls, id: int = id_emitter.knight_id) -> BuildResult[Knight]:
        """
        # Action:
        Returns a BuildResult containing a Knight instance.

        # Parameters:
        None

        # Returns:
          BuildResult[Knight] containing either:
                - On success: a Knight in the payload.
                - On failure: Exception.

        # Raises:
        None
        """
        method = "RankFactory.build_knight_rank"
        return BuildResult.success(
            Knight(
                id=id_emitter.knight_id,
                name=RankSpec.KNIGHT.name,
                designation=RankSpec.KNIGHT.designation,
                ransom=RankSpec.KNIGHT.ransom,
                team_quota=RankSpec.KNIGHT.team_quota,
                quadrants=RankSpec.KNIGHT.quadrants,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_bishop_rank(cls, id: int = id_emitter.bishop_id) -> BuildResult[Bishop]:
        """
        # Action:
        Returns a BuildResult containing a Bishop instance.

        # Parameters:
        None

        # Returns:
          BuildResult[Bishop] containing either:
                - On success: a Bishop in the payload.
                - On failure: Exception.

        # Raises:
        None
        """
        method = "RankFactory.build_bishop_rank"
        return BuildResult.success(
            Bishop(
                id=id_emitter.bishop_id,
                name=RankSpec.BISHOP.name,
                designation=RankSpec.BISHOP.designation,
                ransom=RankSpec.BISHOP.ransom,
                team_quota=RankSpec.BISHOP.team_quota,
                quadrants=RankSpec.BISHOP.quadrants,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_rook_rank(cls, i: int = id_emitter.rook_id) -> BuildResult[Rook]:
        """
        # Action:
        Returns a BuildResult containing a Rook instance.

        # Parameters:
        None

        # Returns:
          BuildResult[Rook] containing either:
                - On success: a Rook in the payload.
                - On failure: Exception.

        # Raises:
        None
        """
        method = "RankFactory.build_rook_rank"
        return BuildResult.success(
            Rook(
                id=id_emitter.rook_id,
                name=RankSpec.ROOK.name,
                designation=RankSpec.ROOK.designation,
                ransom=RankSpec.ROOK.ransom,
                team_quota=RankSpec.ROOK.team_quota,
                quadrants=RankSpec.ROOK.quadrants,
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_queen_rank(cls, id: int = id_emitter.queen_id) -> BuildResult[Queen]:
        """
        # Action:
        Returns a BuildResult containing a Queen instance.

        # Parameters:
        None

        # Returns:
          BuildResult[Queen] containing either:
                - On success: a Queen in the payload.
                - On failure: Exception.

        # Raises:
        None
        """
        method = "RankFactory.build_queen_rank"
        return BuildResult.success(
            Queen(
                id=id_emitter.queen_id,
                name=RankSpec.QUEEN.name,
                designation=RankSpec.QUEEN.designation,
                ransom=RankSpec.QUEEN.ransom,
                team_quota=RankSpec.QUEEN.team_quota,
                quadrants=RankSpec.QUEEN.quadrants,
            )
        )