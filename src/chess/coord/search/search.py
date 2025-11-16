# src/chess/coord/search/search.py

"""
Module: chess.coord.search.search
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""
from typing import List



from chess.coord import Coord, CoordService, CoordSearchContext
from chess.system import LoggingLevelRouter, Search, SearchResult


class CoordSearch(Search[CoordService, List[Coord]]):
    """"""

    @classmethod
    @LoggingLevelRouter.monitor
    def search(cls, data_owner: CoordService, search_context: CoordSearchContext) -> SearchResult[List[Coord]]:
        """"""
        pass