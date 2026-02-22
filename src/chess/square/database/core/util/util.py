# src/chess/square/database/core/util/util.py

"""
Module: chess.square.database.core.util.util
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from chess.square import SquareStackAnalyzer
from chess.square.database.core.util.roster.deployer import RosterFormationCoordinator


class SquareStackUtil:
    _stats_analyzer: SquareStackAnalyzer
    _roster_deployer: RosterFormationCoordinator
    
    def __init__(
            self,
            stats_analyzer: SquareStackAnalyzer = SquareStackAnalyzer(),
            roster_deployer: RosterFormationCoordinator = RosterFormationCoordinator(),
    ):
        self._stats_analyzer = stats_analyzer
        self._roster_deployer = roster_deployer
        
    @property
    def stats_analyzer(self) -> SquareStackAnalyzer:
        return self._stats_analyzer
    
    @property
    def roster_deployer(self) -> RosterFormationCoordinator:
        return self._roster_deployer