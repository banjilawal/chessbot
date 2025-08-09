from abc import ABC

from engine.explorer import Explorer


class Engine(ABC):
    _scout_master: ScoutMaster
    _report_sorter: ReportSorter
    _target_selector: TargetSelector
