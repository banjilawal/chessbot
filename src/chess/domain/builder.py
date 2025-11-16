# src/chess/domain/builder.py

"""
Module: chess.domain.builder
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from chess.board import Board
from chess.piece import Piece
from chess.domain import Domain, DomainOriginBuilder
from chess.system import Builder, BuildResult, LoggingLevelRouter


class DomainBuilder(Builder[Domain]):
    """
    # ROLE: Build

    # RESPONSIBILITIES:
    Create new Domain objects safely.

    # PROVIDES:
      BuildResult[Domain] containing either:
            - On success: Domain in the payload.
            - On failure: Exception.

    # ATTRIBUTES:
    No attributes.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(
            cls,
            piece: Piece,
            board: Board,
            domain_origin_builder: DomainOriginBuilder
    ) -> BuildResult[Domain]:
        """
        # Action:
        Construct a new Domain object after verifying its inputs will not cause an error.
        
        # Parameters:
          * piece (Piece): The domain owner
          * board (Board): Provides the Square of the Domain owner.
          * domain_origin_builder (DomainOriginBuilder): Creates the DomainOwner object.

        # Returns:
          BuildResult[Domain] containing either:
                - On success: Square in the payload.
                - On failure: Exception.

        # Raises:
            * TypeError
            * NullDomainException
            * DomainNullSquaresListException
            * DomainNullEnemiesDictException
            * DomainNullFriendsDictException
            * InvalidDomainException
        """
        method = "DomainBuilder.build"
        
        try:
            board_actor_validation = BoardActorValidator.validate(piece, board)
            if board_actor_validation.is_failure():
                return BuildResult.failure(board_actor_validation.exception)
            
            return BuildResult.success(Domain(piece=piece))
        except Exception as e:
            return BuildResult.failure(e)
