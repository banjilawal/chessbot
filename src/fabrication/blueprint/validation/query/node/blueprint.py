# src/blueprint/validation/node/blueprint.py

"""
Module: blueprint.validation.query.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import NodeNullException
from model import DiscoveryStatus, Node, Node, Blueprint, Square


@dataclass
class NodeQueryValidationBlueprint(QueryValidationBlueprint[Node]):
    priority: Optional[int] = None
    square: Optional[Square] = None
    predecessor: Optional[Node] = None
    discovery_status: Optional[DiscoveryStatus] = None
    null_exception = NodeNullException()
    model_type = NodeValidation
