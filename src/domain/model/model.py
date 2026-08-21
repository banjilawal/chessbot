# src/dossier/model/dossier/model.py

"""
Module: domain.model.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Domain


class Model(Domain, ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1. Represent an item that has properties.

    Attributes:

    Provides:

    Super Class:
        Domain
    """
    pass