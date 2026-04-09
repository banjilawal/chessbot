# src/model/blueprint/context/node/blueprint.py

"""
Module: model.blueprint.context.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import DiscoveryStatus, Node, NodeContext, Blueprint, Square


@dataclass
class NodeContextBlueprint(Blueprint[NodeContext]):
    priority: Optional[int] = None
    square: Optional[Square] = None
    predecessor: Optional[Node] = None
    discovery_status: Optional[DiscoveryStatus] = None
