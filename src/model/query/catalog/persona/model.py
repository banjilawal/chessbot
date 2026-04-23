# src/model/query/catalog/persona/model.py

"""
Module: model.query.catalog.persona.model
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model import Persona, PersonaContext
from model.query import CatalogQuery


@dataclass
class PersonaQuery(CatalogQuery[Persona]):
    """
    Role:
        -   Model
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

