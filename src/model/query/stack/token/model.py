# src/model/query/stack/token/model.py

"""
Module: model.query.stack.token.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Token, TokenContext
from model.query import StackQuery


@dataclass
class TokenQuery(StackQuery[Token]):
    """
    Role:
        -   Model
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of tokens to search with context.


    Attributes:
        items: List[Token]
        context: TokenContext

    Provides:

    Super Class:
        StackQuery
    """
    items: List[Token]
    context: TokenContext

