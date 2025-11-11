# src/chess/domain/origin/builder.py

"""
Module: chess.domain.origin.builder
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""


from chess.domain import DomainOrigin
from chess.enviroment import TurnScene, TurnSceneValidator
from chess.system import Builder, BuildResult, LoggingLevelRouter



class DomainOriginBuilder(Builder[DomainOrigin]):
    """
    # ROLE:
    
    # RESPONSIBILITIES:
    
    # PROVIDES:
        DomainOrigin
    
    # ATTRIBUTES:
        None.
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, turn_scene: TurnScene) -> BuildResult[DomainOrigin]:
        """"""
        method = "DomainOriginBuilder.build"
        
        try:
            turn_scene_validation = TurnSceneValidator.validate(turn_scene)
            if turn_scene_validation.failure():
                return BuildResult.failure(turn_scene_validation.exception)
            
            return BuildResult.success(payload=DomainOrigin(owner=turn_scene.actor, owner_square=turn_scene.square))
        except Exception as e:
            return BuildResult.failure(e)
    
    