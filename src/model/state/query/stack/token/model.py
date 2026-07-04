# src/model/state/query/stack/token/model/state.py

"""
Module: model.state.query.stack.token.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from model import Token, TokenContext
from model.query import StackQuery
from stack import TokenStackService


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
        stack: List[Token]
        context: TokenContext

    Provides:

    Super Class:
        StackQuery
    """
    stack: TokenStackService
    context: TokenContext

