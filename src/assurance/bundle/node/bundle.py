# src/assurance/bundle/node/bundle.py

"""
Module: assurance.bundle.node.bundle
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from assurance import ValidationBundle
from domain import Node, NodeNullRoster, NodeTypes


@dataclass
class NodeValidationBundle(ValidationBundle[Node]):
    types: NodeTypes
    nulls: NodeNullRoster
    resources: Dict[str, Any]