# src/chess/house/builder.py

"""
Module: chess.house.builder.py
Author: Banji Lawal
Created: 2025-11-10
version: 1.0.0
"""


from chess.house import House
from chess.enviroment import TurnScene
from chess.system import Builder, BuildResult, LoggingLevelRouter


class HouseBuilder(Builder[House]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def build(cls, turn_scene: TurnScene) -> BuildResult[House]:
        """"""
        method = "HouseBuilder.build"
        
        try:
            return BuildResult(House(square=turn_scene.actor_square, resident=turn_scene.actor))
        except Exception as e:
            return BuildResult.failure(e)