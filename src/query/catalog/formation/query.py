# src/query/catalog/formation/query.py

"""
Module: query.catalog.formation.query
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass

from model import Formation, FormationContext
from query import CatalogQuery


@dataclass
class FormationQuery(CatalogQuery[Formation]):
    """
    Role:
        -   Model
        -   Stateless Data-Holder
        -   Messaging

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

