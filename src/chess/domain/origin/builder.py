# src/chess/domain/origin/builder.py

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
    # ROLE:
        Build, Validation
        
    # RESPONSIBILITIES:
        1. Perform sanity checks on resources for creating a new DomainOrigin object.
        2. Report any errors preventing a successful build.
        3. Provide a DomainOrigin object that meets minimal requirements for usage in the system.
        
    # PROVIDES:
        BuildResult
    
    # ATTRIBUTES:
        None.
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
                - On success: DomainOrigin in payload.
                - On failure: Exception.

        # RAISES:
            None
        """
        method = "DomainOriginBuilder.build"
        
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
    
    