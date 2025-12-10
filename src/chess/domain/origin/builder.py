# src/chess/domain/origin/factory.py

"""
Module: chess.domain.origin.builder
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""


from chess.domain import DomainOrigin, DomainOriginBuildFailedException
from chess.enviroment import TurnScene, TurnSceneValidator
from chess.system import Builder, BuildResult, LoggingLevelRouter


class DomainOriginBuilder(Builder[DomainOrigin]):
    """
     # ROLE: Builder, Data Integrity Guarantor, Data Integrity And Reliability Guarantor

     # RESPONSIBILITIES:
     1.  Produce DomainOrigin instances whose integrity is always guaranteed.
     2.  Manage construction of DomainOrigin instances that can be used safely by the client.
     3.  Ensure params for DomainOrigin creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     # PARENT
         * Builder

     # PROVIDES:
         *   DomainOriginBuilder

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, turn_scene: TurnScene) -> BuildResult[DomainOrigin]:
        """
        # ACTION:
        Create a new DomainOrigin object that can be safely used in the system if and only if:
            1. turn_scene parameter has passed validation checks.
            2. turn_scene parameter has verified owner and their square have the same Coord.

        # PARAMETERS:
            * candidate (int): the visitor_id.

        # Returns:
          BuildResult[DomainOrigin] containing either:
                - On success: DomainOrigin in the payload.
                - On failure: Exception.

        # RAISES:
            None
        """
        method = "DomainOriginBuilder.builder"
        
        try:
            turn_scene_validation = TurnSceneValidator.validate(turn_scene)
            if turn_scene_validation.failure():
                return BuildResult.failure(turn_scene_validation.exception)
            
            return BuildResult.success(payload=DomainOrigin(owner=turn_scene.actor, owner_square=turn_scene.square))
        
        except Exception as e:
            return BuildResult.failure(
                DomainOriginBuildFailedException(
                    f"{method}: {DomainOriginBuildFailedException.DEFAULT_MESSAGE}",
                    e
                )
            )
    
    