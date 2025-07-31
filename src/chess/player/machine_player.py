from typing import Optional, List, Dict

from chess.common.game_color import GameColor
from chess.game.record.turn_record import TurnRecord
from chess.geometry.board.coordinate import Coordinate
from chess.piece.label import Label
from chess.piece.piece import ChessPiece
from chess.player.player import Player


class MachinePlayer(Player):

    def __init__(self, player_id: int, name: str, color: GameColor):
        super().__init__(player_id, name, color)


    def request_move(self, piece: 'ChessPiece', destination: Coordinate, board: 'ChessBoard') -> Optional[TurnRecord]:
        pass

    def hunt(self, board: 'ChessBoard') -> Dict[Label, List[ChessPiece]]:
        pass

    def prepare_kill_list(self) -> List['ChessPiece']:
        pass

    def select_killer(self) -> 'ChessPiece':
        pass

    def select_target(self, board: 'ChessBoard') -> Optional[TurnRecord]:
        pass

    def __init__(self, player_id: int,  name: str):
        super().__init__(player_id, name)