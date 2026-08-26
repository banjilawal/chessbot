# src/domain/model/searchable/model.py

"""
Module: domain.model.collectbale.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Searchable, DataModel


class SearchableModel(DataModel, Searchable, ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1. DataModel that implements the Searchable interface

    Attributes:

    Provides:

    Super Class:
        DataModel
    """
    pass