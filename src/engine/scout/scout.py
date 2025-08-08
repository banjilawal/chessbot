from chess.team.element.piece import ChessPiece
from engine.explorer import Explorer
from engine.scout.scout_report import ScoutReport


class Scout:
    _scout: ChessPiece

    def __init__(self, scout: ChessPiece):
        self._scout = scout

    @property
    def scout(self) -> ChessPiece:
        return self._scout


    def survey(self) -> ScoutReport:
        locations = Explorer.discover_destinations(self._scout)
        return ScoutReport(self._scout.id, self._scout, locations)