# src/logic/points/origin/exception.py

"""
Module: logic.points.origin.build
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""


from logic.domain import DomainOrigin, DomainOriginBuildException
from logic.enviroment import TurnScene, TurnSceneValidationProcess
from logic.system import BuildProcess, BuildResult, LoggingLevelRouter


class DomainOriginBuildProcess(BuildProcess[DomainOrigin]):
    """
     Role:BuildProcess, Data Integrity And Reliability Guarantor

     Responsibilities:
     1.  Produce DomainOrigin instances whose integrity is guaranteed at creation.
     2.  Manage construction of DomainOrigin instances that can be used safely by the client.
     3.  Ensure params for DomainOrigin creation have met the application's safety contract.
     4.  Return an exception to the client if a build resource does not satisfy integrity requirements.

     Super Class:
         * BuildProcess

     # PROVIDES:
         *   DomainOriginBuildProcess

     # LOCAL ATTRIBUTES:
     None

     # INHERITED ATTRIBUTES:
     None
     """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, turn_scene: TurnScene) -> BuildResult[DomainOrigin]:
        """
        # ACTION:
        Create a new DomainOrigin object that can be safely used in the system if and only if:
            1. turn_scene parameter has passed validation checks.
            2. turn_scene parameter has verified owner and their square_name have the same Coord.

        # PARAMETERS:
            * candidate (int): the visitor_id.

        # RETURNS:
          BuildResult[DomainOrigin] containing either:
                - On success: DomainOrigin in the payload.
                - On failure: Exception.

        Raises:
            None
        """
        method = "DomainOriginBuildProcess.build"
        
        try:
            turn_scene_validation = TurnSceneValidationProcess.execute(turn_scene)
            if turn_scene_validation.failure():
                return BuildResult.failure(turn_scene_validation.exception)
            
            return BuildResult.success(payload=DomainOrigin(owner=turn_scene.actor, owner_square=turn_scene.square))
        
        except Exception as e:
            return BuildResult.failure(
                DomainOriginBuildException(
                    f"{method}: {DomainOriginBuildException.MSG}",
                    e
                )
            )
    
    