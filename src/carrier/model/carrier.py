# src/carrier/carrier.py

"""
Module: carrier.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC

from carrier import EntityCarrier


class ModelCarrier(EntityCarrier, ABC):
    """
    Role:
        -   Data Transport

    Responsibilities:
        1.  Transports either a Model or its Blueprint.

    Attributes:
        is_model_carrier: bool
        is_blueprint_carrier: bool
        
        entity: [T | Blueprint[T]]
        is_empty: bool
        has_overflow: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
        Toggle
    """
    def __init__(self):
        super().__init__()


    