# src/domain/model/state/query/stack/token/dossier/model/state.py

"""
Module: domain.model.searchable.state.query.stack.token.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations
from dataclasses import dataclass

from domain.model import Token, TokenContext
from domain.model import StackQuery
from collection.stack import TokenStackService


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

