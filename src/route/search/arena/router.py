# src/route/search/arena/__init__.py

"""
Module: route.search.arena.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from model import Arena
from query import ArenaQuery
from result import SearchResult
from route import Router
from system import LoggingLevelRouter


class ArenaSearchRouter(Router[Arena]):
    
    @classmethod
    @LoggingLevelRouter.monitor
    def route(
            cls,
            query: ArenaQuery,
            query_validator: ArenaQueryValidator | None = None,
    ) -> SearchResult[List[Arena]]:
        pass