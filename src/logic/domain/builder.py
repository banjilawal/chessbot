# src/logic/points/factory.py

"""
Module: logic.points.builder
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from logic.board import Board
from logic.piece import Piece
from logic.domain import Domain, DomainOriginBuildProcess
from logic.system import BuildProcess, BuildResult, LoggingLevelRouter


class DomainBuildProcess(BuildProcess[Domain]):
    """
     Role:BuildProcess, Data Integrity And Reliability Guarantor

     Responsibilities:
     1.  Produce Domain instances whose integrity is guaranteed at creation.
     2.  Manage construction of Domain instances that can be used safely by the client.
     3.  Ensure params for Domain creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     Super Class:
         * BuildProcess

     # PROVIDES:
         *   DomainBuildProcess

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            piece: Piece,
            board: Board,
            domain_origin_builder: DomainOriginBuildProcess
    ) -> BuildResult[Domain]:
        """
        # ACTION:
        Construct a new Domain object after verifying its inputs will not cause an error.
        
        # PARAMETERS:
          * piece (Token): The points owner
          * board (Board): Provides the Square of the Domain owner.
          * domain_origin_builder (DomainOriginBuildProcess): Creates the DomainOwner object.

        # RETURNS:
          BuildResult[Domain] containing either:
                - On success: Square in the payload.
                - On failure: Exception.

        Raises:
            * TypeError
            * NullDomainException
            * DomainNullSquaresListException
            * DomainNullEnemiesDictException
            * DomainNullFriendsDictException
            * InvalidDomainException
        """
        method = "DomainBuildProcess.builder"
        
        try:
            board_actor_validation = BoardActorValidator.execute(piece, board)
            if board_actor_validation.is_failure():
                return BuildResult.failure(board_actor_validation.exception)
            
            return BuildResult.success(Domain(piece=piece))
        except Exception as e:
            return BuildResult.failure(e)
