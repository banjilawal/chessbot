# src/operand/state/query/catalog/formation/operand/state.py

"""
Module: operand.state.query.catalog.formation.operand
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from operand import Formation, FormationContext


@dataclass
class FormationQuery(CatalogQuery[Formation]):
    """
    Role:
        -   Operand
        -   Search
        -   Stateless Data-Holder

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

