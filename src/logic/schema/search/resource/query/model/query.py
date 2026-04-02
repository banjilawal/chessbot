# src/logic/schema/database/search/query/query.py

"""
Module: logic.schema.database.search.query.query
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations

from logic.schema import Schema
from logic.system import CatalofQuery
from logic.schema.search import SchemaContext


class SchemaQuery(CatalofQuery[Schema]):
    
    def __init__(self, catalog: Schema, context: SchemaContext):
        """
        Args:
            catalog: Schema
            context: SchemaContext
        """
        super().__init__(catalog=catalog, context=context)
        
    @property
    def context(self) -> SchemaContext:
        return self.context
    
    @property
    def catalog(self) -> Schema:
        return self.catalog