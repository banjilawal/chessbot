# src/domain/model/state/query/catalog/persona/dossier/model/state.py

"""
Module: domain.model.state.query.catalog.persona.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Persona, PersonaContext
from domain.model import CatalogQuery


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

