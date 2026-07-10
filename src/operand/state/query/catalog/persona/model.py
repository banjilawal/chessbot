# src/operand/state/query/catalog/persona/operand/state.py

"""
Module: operand.state.query.catalog.persona.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from operand import Persona, PersonaContext
from operand.query import CatalogQuery


@dataclass
class PersonaQuery(CatalogQuery[Persona]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

    Responsibilities:
        1.  A list of personas to search with context.

    Attributes:
        catalog: Persona
        context: PersonaContext

    Provides:

    Super Class:
        CatalogQuery
    """
    catalog: Persona
    context: PersonaContext

