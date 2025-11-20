#

from chess.team import Team, TeamDTO, TeamValidator
from chess.system import BuildResult, Builder, LoggingLevelRouter


class TeamBuilder(Builder[TeamDTO]):
    """"""
    
    @classmethod
    @LoggingLevelRouter.monitor()
    def build(cls, team: Team) -> BuildResult[TeamDTO]:
        
        method = "TeamDTOBuilder.builder"
        
        try:
            validation = TeamValidator.validate(team)
            if validation.is_failure():
                return BuildResult(exception=validation.exception)
            return BuildResult(
                payload=TeamDTO(
                    id=team.id,
                    name=team.schema.name,
                    commander_id=team.commander.id,
                    commander_name=team.commander.name
                )
            )
        
        except Exception as e:
            return BuildResult(exception=e)
