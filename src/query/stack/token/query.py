# src/query/stack/token/query.py

"""
Module: query.stack.token.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from model import Token, TokenContext
from query import StackQuery


@dataclass
class TokenQuery(StackQuery[Token]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

    Responsibilities:
        1.  A list of tokens to search with context.


    Attributes:
        stack: List[Token]
        context: TokenContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: List[Token]
    context: TokenContext

