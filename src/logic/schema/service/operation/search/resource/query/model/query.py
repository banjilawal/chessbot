# src/logic/schema/database/search/context/context.py

"""
Module: logic.schema.database.search.context.context
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations

from logic.schema import Schema
from logic.system import CatalofQuery
from logic.schema.service.operation.search import SchemaContext


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