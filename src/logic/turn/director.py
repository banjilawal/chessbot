from domain.model import Game
from system import GameColor
from logic.turn.marker import Marker


class TurnDirector:
    _marker: Marker
    
    def __init__(self, marker: Marker = Marker()):
        self._marker = marker
        
    @property
    def marker(self) -> Marker:
        return self._marker
    

    def issue_turn_marker(self, game: Game, player_color: GameColor) -> Marker:
        player = None
        if player_color == GameColor.WHITE:
            player = game.arena.white_team.domain_class
        else:
            player = game.arena.black_team.domain_class
        self._marker.current_holder(player)
        return self._marker