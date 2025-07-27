from chess.player.player import Player


class HumanPlayer(Player):
    def __init__(self, player_id: int,  name: str):
        super().__init__(player_id, name)


    def name(self, name: str):
        if name is None:
            raise ValueError("name cannot be null.")
        self._name = name