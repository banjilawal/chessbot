# src/logic/system/collection/table/lookup/exception.py

"""
Module: logic.system.collection.table.lookup.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from enum import Enum
from typing import Generic, TypeVar

from logic.system import Query, Context

E = TypeVar("E", bound=Enum)

class TableQuery(Query, Generic[E]):
    _table: E
    
    def __init__(self, table: E, super_key: Context[E]):
        """
        Args:
            table: E
            super_key: Context[E]
        """
        super().__init__(context=super_key)
        self._table = table
    
    @property
    def table(self) -> E:
        return self._table
