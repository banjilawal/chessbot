# src/logic/system/search/query/concrete/table.py

"""
Module: logic.system.search.query.concrete.table
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations

from enum import Enum
from typing import Generic, TypeVar

from logic.system import Query, Context

E = TypeVar("E", bound=Enum)

class TableQuery(Query, Generic[E]):
    _table: E
    
    def __init__(self, table: E, lookup_key: Context[E]):
        """
        Args:
            table: E
            lookup_key: Context[E]
        """
        super().__init__(context=lookup_key)
        self._table = table
    
    @property
    def table(self) -> E:
        return self._table
    
    @property
    def lookup_key(self) -> Context[E]:
        return self.context
