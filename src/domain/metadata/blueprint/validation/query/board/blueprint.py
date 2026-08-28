# src/domain/metadata/blueprint/validation/board/blueprint.py

"""
Module: domain.metadata.blueprint.validation.query.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from err import BoardNullException
from domain.model import Arena, Board, Blueprint, Team


@dataclass
class BoardQueryValidationBlueprint(QueryValidationBlueprint[Board]):
    id: Optional[int] = None
    arena: Optional[Arena] = None
    team: Optional[Team] = None
    domain_null_exception = BoardNullException()
    model_type = BoardValidation
