from chess.player.player import Player


class MachinePlayer(Player):
    def __init__(self, player_id: int,  name: str):
        super().__init__(player_id, name)