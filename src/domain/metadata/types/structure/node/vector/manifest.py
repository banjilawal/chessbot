# src/domain/metadata/types/structurenode/vector/manifest.py

"""
Module: domain.metadata.types.structure.node.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Type

from assurance import NodeTypes
from fabrication import VectorNodeBlueprint
from domain.structure.node import VectorNode
from domain.transit import VectorNodeCarrier


@dataclass
class VectorNodeTypes(NodeTypes):
    model: Type[VectorNode] = VectorNode
    carrier: Type[VectorNodeCarrier] = VectorNodeCarrier
    blueprint: Type[VectorNodeBlueprint] = VectorNodeBlueprint