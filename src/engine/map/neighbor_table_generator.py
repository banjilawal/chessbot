from typing import List

from chess.board.element.square import Square
from chess.creator.emit import id_emitter
from chess.geometry.coordinate.coordinate import CartesianDistance
from chess.token.obstruction import Obstruction
from chess.token.piece import ChessPiece

from engine.scout.scout_report import ScoutReport
from engine.map.neighbor_table import NeighborTable


class NeighborTableGenerator:
    _scout_report: ScoutReport

    def __init__(self, scout_report: ScoutReport):
        self._scout_report = scout_report

    @property
    def scout(self) -> ScoutReport:
        return self._scout_report


    @staticmethod
    def issue_neighbor_table(scout_report: ScoutReport) -> NeighborTable:
        return NeighborTable(
            neighbor_table_id=id_emitter.neighbor_table_id,
            chess_piece=scout_report.scout,
            enemies=NeighborTableGenerator.sort_enemies(scout_report),
            obstructions=NeighborTableGenerator.sort_obstructions(scout_report),
            vacant_squares=NeighborTableGenerator.sort_vacant_squares(scout_report)
        )


    @staticmethod
    def _sort_vacant_squares(scout_report: ScoutReport) -> List[Square]:
        empty_squares: List[Square] = []
        origin = scout_report.scout.coordinate_stack.current_coordinate()
        for square in scout_report.squares:
            if square.occupant is None and square not in empty_squares:
                empty_squares.append(square)
            else:
                continue
        empty_squares.sort(
            reverse=True,
            key=lambda vacant_square: CartesianDistance(origin, vacant_square.coordinate).distance
        )
        return empty_squares


    @staticmethod
    def _sort_obstructions(scout_report: ScoutReport) -> List[Obstruction]:
        obstructions: List[Obstruction] = []
        origin = scout_report.scout.coordinate_stack.current_coordinate()
        for square in scout_report.squares:
            occupant = square.occupant
            if occupant is not None and not scout_report.scout.is_enemy(occupant):
                obstruction = Obstruction(occupant)
                if obstruction not in obstructions:
                    obstructions.append(obstruction)
            else:
                continue
        obstructions.sort(
            reverse=True,
            key=lambda blocker: CartesianDistance(origin, blocker.coordinate).distance
        )
        return obstructions


    @staticmethod
    def _sort_enemies(scout_report: ScoutReport) -> List[ChessPiece]:
        enemies: List[ChessPiece] = []
        for square in scout_report.squares:
            occupant = square.occupant
            if (
                occupant is not None and scout_report.scout.is_enemy(occupant) and
                occupant not in enemies
            ):
                enemies.append(occupant)
            else:
                continue
        enemies.sort(key=lambda chess_piece: chess_piece.rank.capture_value, reverse=True)
        return enemies



