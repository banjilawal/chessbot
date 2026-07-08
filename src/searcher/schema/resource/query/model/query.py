# src/logic/schema/database/searcher/context/context.py

"""
Module: logic.schema.database.searcher.context.context
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations

from typing import Type

from model.catalog import Schema
from system import CatalogQuery
from model.catalog import SchemaContext


class SchemaQuery(CatalogQuery[Schema]):
    
    def __init__(
            self,
            context: SchemaContext,
            catalog: Schema = Type[Schema],
    ):
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
        return Schema(self.catalog)