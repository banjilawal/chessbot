# src/chess/team_name/factory.py

"""
Module: chess.team_name.builder
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""


from chess.agent import PlayerAgent, CommanderService
from chess.system import Builder, BuildResult, IdentityService, LoggingLevelRouter
from chess.team import Team, TeamBuildFailedException, TeamSchema, TeamSchemaValidator


class TeamBuilder(Builder[Team]):
    """
    # ROLE: Builder, Data Integrity Guarantor
  
    # RESPONSIBILITIES:
    Produce Team instances whose integrity is always guaranteed. If any attributes do not pass
    their integrity checks, send an exception instead.
  
    # PROVIDES:
    BuildResult[Team] containing either:
        - On success: Team in the payload.
        - On failure: Exception.
  
    # ATTRIBUTES:
    None
    """
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(
            cls,
            id: int,
            commander: PlayerAgent,
            team_schema: TeamSchema,
            identity_service: IdentityService = IdentityService(),
            commander_validator: CommanderService = CommanderValidator(),
            team_schema_validator: type[TeamSchemaValidator] = TeamSchemaValidator,
    ) -> BuildResult[Team]:
        """
        # ACTION:
        1.  Check ID safety with IdentityService.validate_id.
        2.  Check schema correctness with TeamSchemaValidator.validate.
        3.  Check agent safety with CommanderService.validate_commander.
        4.  If any check fails, return the exception inside a BuildResult.
        5.  When all checks create a new Team object.
        6.  Add the new Team to the agent's teams collection if it is not already there.
    
        # PARAMETERS:
            *   x (int): value in the x-plane
            *   y (int): value in the y-plane
    
        # Returns:
        BuildResult[Team] containing either:
            - On success: T in the payload.
            - On failure: Exception.
    
        RAISES:
            *   TeamBuildFailedException
        """
        method = "TeamBuilder.build"
        
        try:
            id_validation = identity_service.validate_id(id)
            if id_validation.is_failure():
                return BuildResult.failure(id_validation.exception)
            
            team_schema_validation = team_schema_validator.validate(team_schema)
            if team_schema_validation.is_failure():
                return BuildResult.failure(team_schema_validation.exception)
            
            commander_validation = commander_service.validate_commander(commander)
            if commander_validation.is_failure():
                return BuildResult.failure(commander_validation.exception)
            
            team = Team(id=id, commander=commander, team_schema=team_schema)
            
            if team not in commander.teams:
                commander.teams.add_team(team)
            
            if team not in commander.teams:
                return BuildResult.failure(
                    AddingTeamToCommanderHisstoryFailedException(
                        f"{method}: {AddingTeamToCommanderHisstoryFailedException.DEFAULT_MESSAGE}"
                    )
                )
            
            return BuildResult.success(team)
        
        except Exception as ex:
            return BuildResult.failure(
                TeamBuildFailedException(
                    f"{method}: {TeamBuildFailedException.DEFAULT_MESSAGE}",
                    ex
                )
            )