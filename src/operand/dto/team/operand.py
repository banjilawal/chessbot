# src/operand/dto/team/operand.py

"""
Module: operand.dto.team.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from blueprint import TeamBlueprint
from model import Team
from operand import DtoOperand


class TeamDtoOperand(DtoOperand[Team]):
    """
    Role:
        -   DTO

    Responsibilities:
        2.  Transports either a Team or its Blueprint.

    Attributes:
        entity: [Team|TeamBlueprint]
        is_empty: bool
        has_overflow: bool
        is_model_operand: bool
        is_blueprint_operand: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[TeamBlueprint]

    Super Class:
        DtoOperand
    """
    _model: Optional[Team]
    _blueprint: Optional[TeamBlueprint]
    
    def __init__(
            self,
            model: Optional[Team] | None = None,
            blueprint: Optional[TeamBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Team]
            blueprint: Optional[TeamBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Team | TeamBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Team)
        )
    
    @property
    def is_blueprint_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, TeamBlueprint)
        )

    def extract_blueprint(self) -> Optional[TeamBlueprint]:
        if self.is_empty: return None
        if self.is_blueprint_operand: return self._blueprint
        return TeamBlueprint(
            id=self._model.id,
            boadr=self._model.board,
            owner=self._model.owner,
            archetype=self._model.,
            home_square=self._model.home_square,
        )
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "model": self._model,
            "blueprint": self._blueprint
        }
    
    @property
    def is_empty(self) -> bool:
        return len(self.to_dict) == 0
    
    @property
    def has_overflow(self) -> bool:
        return len(self.to_dict) > 1
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamDtoOperand):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

