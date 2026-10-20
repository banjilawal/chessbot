# src/domain/interface/actionabe/interface.py

"""
Module: domain.interface.actionabe.interface
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Actionable


class Elevatable(Actionable, ABC):
    """
    Role:
        - Interface

    Responsibility:
        1.  Makes it possible to jump from the Rank to a higher one.

    Attributes:

    Provides:

    Super Class:
        Actionable
    """