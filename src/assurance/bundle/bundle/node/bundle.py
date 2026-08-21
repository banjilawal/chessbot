# src/assurance/manifest/bundle/manifest.py

"""
Module: assurance.manifest.bundle.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from assurance import NodeNullRoster, NodeTypes, ValidationBundle
from domain.node import Node


@dataclass
class NodeValidationBundle(ValidationBundle[Node]):
    types: NodeTypes
    nulls: NodeNullRoster
    resources: Dict[str, Any]