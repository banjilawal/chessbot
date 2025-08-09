from typing import List

from chess.board.board import ChessBoard
from chess.owner.model.cybernetic_owner import CyberneticOwner
from chess.engine.map.neighbor_table import NeighborTable
from chess.engine.map.neighbor_table_generator import NeighborTableGenerator
from chess.engine.scout.scout_master import ScoutMaster


class SituationMapGenerator:

    @staticmethod
    def situation_map(owner: CyberneticOwner, chess_board: ChessBoard) -> List[NeighborTable]:
        situation_map: List[NeighborTable] = []
        for scout_report in ScoutMaster.send_scouts(owner, chess_board):
            neighbor_table = NeighborTableGenerator(scout_report).issue_neighbor_table()
            if neighbor_table not in situation_map:
                situation_map.append(neighbor_table)
        return situation_map

