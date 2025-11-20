# src/chess/house/factory.py

"""
Module: chess.house.factory.py
Author: Banji Lawal
Created: 2025-11-10
version: 1.0.0
"""


from chess.house import House
from chess.enviroment import TurnScene, TurnSceneValidator
from chess.system import Builder, BuildResult, LoggingLevelRouter


class HouseBuilder(Builder[House]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, turn_scene: TurnScene) -> BuildResult[House]:
        """"""
        method = "HouseBuilder.builder"
        
        try:
            turn_scene_validation = TurnSceneValidator.validate(turn_scene)
            if turn_scene_validation.is_failure():
                return BuildResult.failure(turn_scene_validation.exception)
            
            if turn_scene.actor_square is None:
                return BuildResult.failure(
                    TurnSceneActorSquareIsNullException(
                        f"{method}: {TurnSceneActorSquareIsNullException.DEFAULT_MESSAGE}"
                    )
                )
            
            BuildResult.success(turn_scene.actor_square)
        except Exception as e:
            return BuildResult.failure(e)