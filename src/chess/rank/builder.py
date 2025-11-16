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
        Given a RankSpec, return an appropriate Rank object.

        # Parameters:
            * rank_spec (RankSpec)

        # Returns:
          BuildResult[Rank] containing either:
                - On success: a concrete Rank in the payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * NullRankSpecException
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
    def build_queen_rank(cls) -> BuildResult[Queen]:
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
                id=RankSpec.QUEEN.id,
                name=RankSpec.QUEEN.name,
                letter=RankSpec.QUEEN.letter,
                ransom=RankSpec.QUEEN.ransom,
                quota=RankSpec.QUEEN.quota,
                quadrants=RankSpec.QUEEN.quadrants
            )
        )