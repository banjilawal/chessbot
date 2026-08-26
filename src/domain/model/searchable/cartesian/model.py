# src/domain/model/searchable/cartesian/vector/model.py

"""
Module: domain.model.searchable.cartesian.vector.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import SearchableModel


class CartesianPoint(SearchableModel, ABC):
    """
    Role:
        - Addressing

    Responsibilities:
        1.  Model that represents a location in 2D space.
           
    Attributes:
    
    Provides:
    
    Super Class:
        SearchableModel
    """
