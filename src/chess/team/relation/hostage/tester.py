from chess.system import LoggingLevelRouter, RelationReport, RelationTester
from chess.system.relation.tester import P, S
from chess.team import Team, TeamValidator
from chess.team.relation.hostage.wrapper import TeamHostageRelationTestFailedException
from chess.token import Token, TokenService


class TeamHostageRelationTester(RelationTester[Team, Token]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def test(
            cls,
            candidate_primary: Team,
            candidate_satellite: Token,
            team_validator: TeamValidator = TeamValidator(),
            token_service: TokenService = TokenService(),
    ) -> RelationReport[Team, Token]:
        team_validation = team_validator.validate(candidate_primary)
        if team_validation.is_failure:
            return RelationReport(
                TeamHostageRelationTestFailedException(
                
                )
            )
        return RelationReport(P(candidate_primary), S(candidate_satellite), team_valiation)