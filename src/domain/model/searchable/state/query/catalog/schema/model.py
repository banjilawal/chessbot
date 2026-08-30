# src/domain/model/searchable/state/query/catalog/schema/model.py

"""
Module: domain.model.searchable.state.query.catalog.schema.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Schema, SchemaContext
from domain.model import CatalogQuery


@dataclass
class SchemaQuery(CatalogQuery[Schema]):
    """
    Role:
        - Model
        -  Search
        -  Stateless Data-Holder

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

