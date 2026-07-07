# src/bootstrapper/assembly/context/arena/operation.py

"""
Module: bootstrapper.assembly.context.arena.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from model import ArenaContextBlueprint

from operation import AssemblyPriming
from system import AssemblyResult, ExecutionRouteException, LoggingLevelRouter
from logic.arena import (
    ArenaContext, ArenaContextAssemblyException, ExcessArenaContextFlagsException, ZeroArenaContextFlagsException,
)


class ArenaContextAssemblyPrimer(AssemblyPriming[ArenaContext]):
    """
    Role:Assembly, Data Integrity And Reliability Guarantor

    Responsibilities:
    1.  Produce ArenaContext instances whose integrity is guaranteed at creation.
    2.  Manage construction of ArenaContext instances that can be used safely by the client.
    3.  Ensure params for ArenaContext creation have met the application's safety contract.
    4.  Return an exception to the client if a assembly resource does not satisfy integrity requirements.

    Super Class:
        *   Assembly

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def assembly(
            cls,
            blueprint: ArenaContextBlueprint[ArenaContext],
            toolkit: ArenaContextToolKit[ArenaContext],
    ) -> AssemblyResult[ArenaContext]:
        """
        # ACTION:
            1.  Confirm that only one in the (id, designation, team, game, arena_variety) tuple is not null.
            2.  Certify the not-null attribute is safe using the appropriate validating service.
            3.  If all checks pass assembly a ArenaContext and send in a AssemblyResult. Else, return an exception
                in the AssemblyResult.

        # PARAMETERS:
            Only one these must be provided:
                *   id (Optional[int])
                *   designation (Optional[str])
                *   team (Optional[Team])
                *   game (Optional[Game])
                *   arena_variety (Optional[ArenaVariety])

            These Parameters must be provided:
                *   team_service (TeamService)
                *   game_service (GameService)
                *   identity_service (IdentityService)

        # RETURNS:
          AssemblyResult[ArenaContext] containing either:
                - On success: ArenaContext in the payload.
                - On failure: Exception.

        Raises:
            *   ZeroArenaContextFlagsException
            *   ArenaContextAssemblyException
            *   ExcessArenaContextFlagsException
        """
        method = "ArenaSearchContextAssembly.assembly"
        try:
            # Count how many optional parameters are not-null. One param needs to be not-null.
            params = [id, name, team, game, variety, ]
            param_count = sum(bool(p) for p in params)
            
            # Test if no params are set. Need an attribute-value pair to find which PlayerArenas match the target.
            if param_count == 0:
                return AssemblyResult.failure(
                    ZeroArenaContextFlagsException(f"{method}: {ZeroArenaContextFlagsException.MSG}")
                )
            # Test if more than one param is set. Only one attribute-value tuple is allowed in a search.
            if param_count > 1:
                return AssemblyResult.failure(
                    ExcessArenaContextFlagsException(f"{method}: {ExcessArenaContextFlagsException}")
                )
            # After verifying only one PlayerArena attribute-value-tuple is enabled, validate it.
            
            # Assembly the id ArenaContext if its flag is enabled.
            if id is not None:
                validation = identity_service.validate_id(id)
                if validation.is_failure:
                    return AssemblyResult.failure(validation.exception)
                # On validation success return an id_ArenaContext in the AssemblyResult.
                return AssemblyResult.success(ArenaContext(id=id))
            
            # Assembly the schema ArenaContext if its flag is enabled.
            if name is not None:
                validation = identity_service.validate_name(name)
                if validation.is_failure:
                    return AssemblyResult.failure(validation.exception)
                # On validation success return a name_ArenaContext in the AssemblyResult.
                return AssemblyResult.success(ArenaContext(name=name))
            
            # Assembly the team ArenaContext if its flag is enabled.
            if team is not None:
                validation = team_service.run.build(candidate=team)
                if validation.is_failure:
                    return AssemblyResult.failure(validation.exception)
                # On validation success return a team_ArenaContext in the AssemblyResult.
                return AssemblyResult.success(ArenaContext(team=team))
            
            # Assembly the game ArenaContext if its flag is enabled.
            if game is not None:
                validation = game_service.run.build(candidate=game)
                if validation.is_failure:
                    return AssemblyResult.failure(validation.exception)
                # On validation success return a game_ArenaContext in the AssemblyResult.
                return AssemblyResult.success(ArenaContext(game=game))
            
            # Assembly the arena_variety ArenaContext if its flag is enabled.
            if variety is not None:
                if not isinstance(variety, ArenaVariety):
                    return AssemblyResult.failure(
                        TypeError(f"{method}: Expected ArenaVariety, got {type(variety).__name__} instead.")
                    )
                # On validation success return a variety_ArenaContext in the AssemblyResult.
                return AssemblyResult.success(ArenaContext(variety=variety))
            
            # As a failsafe, if the none of the none of the cases are handled by the if blocks return failsafeBranchExPointException in the assemblyResult failure if a map path was missed.
            AssemblyResult.failure(
                ExecutionRouteException(f"{method}: {ExecutionRouteException.MSG}")
            )
        # Finally, catch any missed exception, wrap an ArenaContextAssemblyException around it then
        # return the exception-chain inside the ValidationResult.
        except Exception as ex:
            return AssemblyResult.failure(
                ArenaContextAssemblyException(
                    ex=ex, msg=f"{method}: {ArenaContextAssemblyException.MSG}"
                )
            )