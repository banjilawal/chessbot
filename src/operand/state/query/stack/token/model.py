# src/operand/state/query/stack/token/operand/state.py

"""
Module: operand.state.query.stack.token.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass

from operand import Token, TokenContext
from operand.query import StackQuery
from stack import TokenStackService


@dataclass
class TokenQuery(StackQuery[Token]):
    """
    Role:
        -   Operand
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

