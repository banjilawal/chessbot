# src/model/query/stack/__init__.py

"""
Module: model.query.stack.model
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
class StackQuery(Query(T, List[T])):
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
        items: List[T]
        context: Context[T]

    Provides:

    Super Class:
        Query
    """
    items: List[T]
    context: Context[T]

