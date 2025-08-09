from abc import ABC

from engine.explorer import Explorer
from engine.scout.scout_master import ScoutMaster


class Engine(ABC):
    _scout_master: ScoutMaster
    _report_sorter: ReportSorter
    _target_selector: TargetSelector
