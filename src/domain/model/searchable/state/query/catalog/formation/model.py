# src/domain/model/state/query/catalog/formation/dossier/model/state.py

"""
Module: domain.model.searchable.state.query.catalog.formation.model
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass

from domain.model import Formation, FormationContext


@dataclass
class FormationQuery(CatalogQuery[Formation]):
    """
    Role:
        -  Model
        -  Search
        -  Stateless Data-Holder

    Responsibilities:
        1.  A list of formations to search with context.

    Attributes:
        catalog: Formation
        context: FormationContext

    Provides:

    Super Class:
        CatalogQuery
    """
    catalog: Formation
    context: FormationContext

