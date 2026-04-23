# src/query/stack/__init__.py

"""
Module: query.stack.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, TypeVar

from model import Context
from model.query import Query

T = TypeVar("T")

@dataclass
class StackQuery(Query, Generic[T]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  Contains
                -   The entity list[T]
                -   The criteria for searching the list
        2.  Delivers it's contents to SearchRouter[T]


    Attributes:
        stack: List[T]
        context: Context[T]

    Provides:

    Super Class:
        Query
    """
    stack: List[T]
    context: Context[T]

