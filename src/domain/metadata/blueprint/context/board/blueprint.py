# src/domain/metadata/blueprint/context/board/blueprint.py

"""
Module: domain.metadata.blueprint.context.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import BoardStackContextNullException
from domain.model import Arena, BoardContext, Blueprint, Team


@dataclass
class BoardContextBlueprint(Blueprint[BoardContext]):
    id: Optional[int] = None
    arena: Optional[Arena] = None
    team: Optional[Team] = None
    domain_null_exception = BoardStackContextNullException()
    model_type = BoardContext
