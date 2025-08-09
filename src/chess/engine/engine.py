from abc import ABC

from chess.engine.scout.scout_master import ScoutMaster


class Engine(ABC):
    _scout_master: ScoutMaster
    _report_sorter: ReportSorter
    _target_selector: TargetSelector
