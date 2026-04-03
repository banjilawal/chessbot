# src/logic/system/search/resource/query/model/catalog/model.py

"""
Module: logic.system.search.resource.query.model.catalog.model
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations

from enum import Enum
from typing import Generic, TypeVar

from logic.system import Context, Query

E = TypeVar("E", bound=Enum)

class CatalogQuery(Query, Generic[E]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

    Responsibilities:
        1.  Contains
                -   The ConfigTable, EnumTable of entity keys.
                -   The criteria for searching the EnumTable
        2.  Delivers it's contents to SearchRouter[E]


    Attributes:
        catalog: E
        context: Context[E]

    Provides:

    Super Class:
        Query
    """
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
