from typing import Optional, List, Dict


from chess.geometry.coordinate.coordinate import Coordinate

from chess.team.element.piece import ChessPiece
from chess.owner.owner import Owner
from chess.team.element.team import Team


class CyberneticOwner(Owner):

    def __init__(self, owner_id: int, name: str, team: Optional[Team] = None):
        super().__init__(owner_id, name, team)


    def request_move(self, piece: 'ChessPiece', destination: Coordinate, board: 'ObsoleteChessBoard'):
        pass

    def hunt(self, board: 'ObsoleteChessBoard') -> Dict[Label, List[ChessPiece]]:
        pass

    def prepare_kill_list(self) -> List['ChessPiece']:
        pass

    def select_killer(self) -> 'ChessPiece':
        pass

    def select_target(self, board: 'ObsoleteChessBoard') -> Optional[TurnRecord]:
        pass

    def __init__(self, player_id: int,  name: str):
        super().__init__(player_id, name)