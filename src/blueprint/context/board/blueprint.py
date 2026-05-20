# src/blueprint/context/board/blueprint.py

"""
Module: blueprint.context.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import BoardContextNullException
from model import Arena, BoardContext, Blueprint, Team


@dataclass
class BoardContextBlueprint(Blueprint[BoardContext]):
    id: Optional[int] = None
    arena: Optional[Arena] = None
    team: Optional[Team] = None
    null_exception = BoardContextNullException()
    model_type = BoardContext
