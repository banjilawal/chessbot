# src/model/blueprint/context/edge/blueprint.py

"""
Module: model.blueprint.context.edge.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from model import EdgeContext, Blueprint, Game, Node, Player


@dataclass
class EdgeContextBlueprint(Blueprint[EdgeContext]):
    label: Optional[int] = None
    head: Optional[Node] = None
    tail: Optional[Node] = None
    weight: Optional[int] = None
    distance: Optional[int] = None
    heuristic: Optional[int] = None
