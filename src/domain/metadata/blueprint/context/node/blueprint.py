# src/domain/metadata/blueprint/context/node/blueprint.py

"""
Module: domain.metadata.blueprint.context.node.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import NodeSearchContextNullException
from domain.model import DiscoveryStatus, Node, NodeContext, Blueprint, Square


@dataclass
class NodeContextBlueprint(Blueprint[NodeContext]):
    priority: Optional[int] = None
    square: Optional[Square] = None
    predecessor: Optional[Node] = None
    discovery_status: Optional[DiscoveryStatus] = None
    domain_null_exception = NodeSearchContextNullException()
    model_type = NodeContext
