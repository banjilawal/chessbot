# src/chess/rank/builder.py

"""
Module: chess.rank.builder
Author: Banji Lawal
Created: 2025-08-25
version: 1.0.0
"""


from chess.system import Builder, BuildResult, LoggingLevelRouter
from chess.rank import (
    Rank, King, Pawn, Knight, Bishop, Rook, Queen, RankSpec, NullRankSpecException,
    RankBuildFailedException
)


class RankFactory(Builder[Rank]):
    """
    # ROLE: Factory
  
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
    def build(cls, rank_spec: RankSpec) -> BuildResult[Rank]:
        """
        # Action:
        If the absolute value of the param is within BOARD_DIMENSION return a new Rank instance.
        Otherwise, return an exception.

        # Parameters:
            * value (int): selected if search target is an id.

        # Returns:
          BuildResult[Rank] containing either:
                - On success: Rank in payload.
                - On failure: Exception.

        # Raises:
            * NullNumberException
            * RankBelowBoundsException
            * RankAboveBoundsException
            * RankBuildFailedException
        """
        method = "RankFactory.build"
        
        try:
            if rank_spec is None:
                return BuildResult.failure(
                    NullRankSpecException(f"{method}: {NullRankSpecException.DEFAULT_MESSAGE}")
                )
            
            if not isinstance(rank_spec, RankSpec):
                return BuildResult.failure(
                    TypeError(f"{method}: Expected an RankSpec, got {type(rank_spec).__name__} instead.")
                )
            
            if rank_spec == RankSpec.KING:
                return cls.build_king_rank()
            if rank_spec == RankSpec.PAWN:
                return cls.build_pawn_rank()
            if rank_spec == RankSpec.KNIGHT:
                return cls.build_knight_rank()
            if rank_spec == RankSpec.BISHOP:
                return cls.build_bishop_rank()
            if rank_spec == RankSpec.ROOK:
                return cls.build_rook_rank()
            if rank_spec == RankSpec.QUEEN:
                return cls.build_queen_rank()
        
        except Exception as ex:
            return BuildResult.failure(
                RankBuildFailedException(
                    f"{method}: {RankBuildFailedException.DEFAULT_MESSAGE}", ex
                )
            )
    
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_king_rank(cls) -> BuildResult[King]:
        return BuildResult.success(
            King(
                id=RankSpec.KING.id,
                name=RankSpec.KING.name,
                letter=RankSpec.KING.letter,
                ransom=RankSpec.KING.ransom,
                quota=RankSpec.KING.quota,
                quadrants=RankSpec.KING.quadrants
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_pawn_rank(cls) -> BuildResult[Pawn]:
        return BuildResult.success(
            Pawn(
                id=RankSpec.PAWN.id,
                name=RankSpec.PAWN.name,
                letter=RankSpec.PAWN.letter,
                ransom=RankSpec.PAWN.ransom,
                quota=RankSpec.PAWN.quota,
                quadrants=RankSpec.PAWN.quadrants
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_knight_rank(cls) -> BuildResult[Knight]:
        return BuildResult.success(
            Knight(
                id=RankSpec.KNIGHT.id,
                name=RankSpec.KNIGHT.name,
                letter=RankSpec.KNIGHT.letter,
                ransom=RankSpec.KNIGHT.ransom,
                quota=RankSpec.KNIGHT.quota,
                quadrants=RankSpec.KNIGHT.quadrants
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_bishop_rank(cls) -> BuildResult[Bishop]:
        return BuildResult.success(
            Bishop(
                id=RankSpec.BISHOP.id,
                name=RankSpec.BISHOP.name,
                letter=RankSpec.BISHOP.letter,
                ransom=RankSpec.BISHOP.ransom,
                quota=RankSpec.BISHOP.quota,
                quadrants=RankSpec.BISHOP.quadrants
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_rook_rank(cls) -> BuildResult[Rook]:
        return BuildResult.success(
            Rook(
                id=RankSpec.ROOK.id,
                name=RankSpec.ROOK.name,
                letter=RankSpec.ROOK.letter,
                ransom=RankSpec.ROOK.ransom,
                quota=RankSpec.ROOK.quota,
                quadrants=RankSpec.ROOK.quadrants
            )
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build_bishop_rank(cls) -> BuildResult[Queen]:
        return BuildResult.success(
            Queen(
                id=RankSpec.QUEEN.id,
                name=RankSpec.QUEEN.name,
                letter=RankSpec.QUEEN.letter,
                ransom=RankSpec.QUEEN.ransom,
                quota=RankSpec.QUEEN.quota,
                quadrants=RankSpec.QUEEN.quadrants
            )
        )