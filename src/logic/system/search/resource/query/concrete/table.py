# src/logic/system/search/resource/context/concrete/schema.py

"""
Module: logic.system.search.resource.context.concrete.schema
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations

from enum import Enum
from typing import Generic, TypeVar

from logic.system import Query, Context

E = TypeVar("E", bound=Enum)

class CatalofQuery(Query, Generic[E]):
    _catalog: E
    
    def __init__(self, catalog: E, context: Context[E]):
        """
        Args:
            catalog: E
            context: Context[E]
        """
        super().__init__(context=context)
        self._catalog = catalog
    
    @property
    def catalog(self) -> E:
        return self._catalog
    
    @property
    def lookup_key(self) -> Context[E]:
        return self.context
