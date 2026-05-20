# src/blueprint/validation/edge/blueprint.py

"""
Module: blueprint.validation.query.edge.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import EdgeNullException
from model import Edge, Blueprint, Game, Node, Player


@dataclass
class EdgeQueryValidationBlueprint(QueryValidationBlueprint[Edge]):
    label: Optional[int] = None
    head: Optional[Node] = None
    tail: Optional[Node] = None
    weight: Optional[int] = None
    distance: Optional[int] = None
    heuristic: Optional[int] = None
    null_exception = EdgeNullException()
    model_type = EdgeValidation
