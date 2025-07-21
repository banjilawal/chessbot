from chess.team.team import Team
from podscape.constants import GameColor


def TeamBuilder():

    def __init__(self):
        pass

    def build_team(self, team_id: int, team_color: GameColor) -> Team:
        product = Team(team_id=team_id, color=team_color)
        self.populate_team(product)
        return product

    def populate_team(self, team: Team) -> None:
        pass

    create