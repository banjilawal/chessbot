# src/assurance/manifest/types/node/manifest.py

"""
Module: assurance.manifest.types.node.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from assurance import TypesManifest
from fabrication import NodeBlueprint
from domain.node import Node
from transit import NodeCarrier


@dataclass
class NodeTypes(TypesManifest[Node]):
    model: Type[Node] = Node
    carrier: Type[NodeCarrier] = NodeCarrier
    blueprint: Type[NodeBlueprint] = NodeBlueprint