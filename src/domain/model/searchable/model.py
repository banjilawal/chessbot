# src/domain/model/searchable/model.py

"""
Module: domain.model.searchable.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from collection.interface import Collectable
from domain import Searchable, Model


class SearchableModel(Model, Collectable, Searchable, ABC):
    """
    Role:
        - Data Holder

    Responsibilities:
        1. DataModel that implements the Collectable and Searchable interface

    Attributes:

    Provides:

    Super Class:
        DataModel
    """
    pass