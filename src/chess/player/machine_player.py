from typing import Optional, List, Dict

from chess.common.game_color import GameColor
from chess.game.record.turn_record import TurnRecord
from chess.geometry.coordinate import Coordinate
from chess.piece.label import Label
from chess.piece.piece import Piece
from chess.player.player import Player


class MachinePlayer(Player):

    def __init__(self, player_id: int, name: str, color: GameColor):
        super().__init__(player_id, name, color)


    def piece_to_coordinate(self, piece: 'Piece', destination: Coordinate, board: 'Board') -> Optional[TurnRecord]:
        pass

    def hunt(self, board: 'Board') -> Dict[Label, List[Piece]]:
        pass

    def prepare_kill_list(self) -> List['Piece']:
        pass

    def select_killer(self) -> 'Piece':
        pass

    def select_target(self, board: 'Board') -> Optional[TurnRecord]:
        pass

    def __init__(self, player_id: int,  name: str):
        super().__init__(player_id, name)