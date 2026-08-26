# src/domain/model/collectable/model.py

"""
Module: domain.model.collectbale.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Collectable, DataModel


class CollectableModel(DataModel, Collectable, ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1. DataModel that implements the Collectable interface

    Attributes:

    Provides:

    Super Class:
        DataModel
    """
    pass