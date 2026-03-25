# src/logic/house/exception.py

"""
Module: logic.house.exception.py
Author: Banji Lawal
Created: 2025-11-10
version: 1.0.0
"""


from logic.house import House
from logic.enviroment import TurnScene, TurnSceneValidationProcess
from logic.system import BuildProcess, BuildResult, LoggingLevelRouter


class HouseBuildProcess(BuildProcess[House]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, turn_scene: TurnScene) -> BuildResult[House]:
        """"""
        method = "HouseBuildProcess.build"
        
        try:
            turn_scene_validation = TurnSceneValidationProcess.execute(turn_scene)
            if turn_scene_validation.is_failure():
                return BuildResult.failure(turn_scene_validation.exception)
            
            if turn_scene.actor_square is None:
                return BuildResult.failure(
                    TurnSceneActorSquareIsNullException(
                        f"{method}: {TurnSceneActorSquareIsNullException.MSG}"
                    )
                )
            
            BuildResult.success(turn_scene.actor_square)
        except Exception as e:
            return BuildResult.failure(e)