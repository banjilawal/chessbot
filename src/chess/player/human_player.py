from chess.common.game_color import GameColor
from chess.game.record.turn_record import TurnRecord
from chess.player.player import Player


class HumanPlayer(Player):

    def __init__(self, player_id: int, name: str, color: GameColor):
        super().__init__(player_id, name, color)




