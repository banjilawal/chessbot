# src/domain/model/state/query/stack/__init__.py

"""
Module: domain.model.searchable.state.query.stack.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from domain.model import Context
from domain.model import Query
from collection.stack import StackService

T = TypeVar("T")

@dataclass
class StackQuery(Query[T]):
    """
    Role:
        - Model
        -  Search
        -  Stateless Data-Holder

    Responsibilities:
        1.  Contains
                -  The entity Stac[T]
                -  The criteria for searching the list
        2.  Delivers it's contents to SearchRouter[T]


    Attributes:
        context: Context[T]
        stack: StackService[T]

    Provides:

    Super Class:
        Query
    """
    context: Context[T]
    stack: StackService[T]

