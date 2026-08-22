# src/domain/transit/node/carrier.py

"""
Module: domain.transit.node.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain.structure.node import Node
from domain.transit import EntityCarrier


class NodeCarrier(EntityCarrier[Node], ABC):
    """
    Role:
        -   Boundary Carrier

    Responsibilities:
        1.  Transport either a hydrated Node or its Blueprint across validation and other processing
            boundaries.

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
        EntityCarrier
    """
    def __init__(self):
        super().__init__()


    