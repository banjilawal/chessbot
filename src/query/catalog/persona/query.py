# src/query/catalog/persona/query.py

"""
Module: query.catalog.persona.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model import Persona, PersonaContext
from query import CatalogQuery


@dataclass
class PersonaQuery(CatalogQuery[Persona]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

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

