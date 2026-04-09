# src/query/catalog/schema/query.py

"""
Module: query.catalog.schema.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model import Schema, SchemaContext
from query import CatalogQuery


@dataclass
class SchemaQuery(CatalogQuery[Schema]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

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

