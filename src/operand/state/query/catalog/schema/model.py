# src/operand/state/query/catalog/schema/operand/state.py

"""
Module: operand.state.query.catalog.schema.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from operand import Schema, SchemaContext
from operand.query import CatalogQuery


@dataclass
class SchemaQuery(CatalogQuery[Schema]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of schemas to search with context.

    Attributes:
        catalog: Schema
        context: SchemaContext

    Provides:

    Super Class:
        CatalogQuery
    """
    catalog: Schema
    context: SchemaContext

