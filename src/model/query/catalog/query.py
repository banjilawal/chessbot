# src/query/catalog/query.py

"""
Module: query.catalog.query
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar

from model import Context
from model.query import Query

E = TypeVar("E", bound=Enum)

@dataclass
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
    catalog: E
    context: Context[E]
