# src/operand/dto/prisoner/operand.py

"""
Module: operand.dto.prisoner.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import PrisonerBlueprint
from model import Prisoner
from operand import DtoOperand


class PrisonerDtoOperand(DtoOperand[Prisoner]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Dto for transporting either a Prisoner or PrisonerBlueprint
    
    Attributes:
        model: Optional[Prisoner]
        blueprint: Optional[PrisonerBlueprint]
        is_model_operand: bool
        is_blueprint_operand: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        DtoOperand
    """
    _model: Optional[Prisoner]
    _blueprint: Optional[PrisonerBlueprint]
    
    def __init__(
            self,
            model: Optional[Prisoner] | None = None,
            blueprint: Optional[PrisonerBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Prisoner]
            blueprint: Optional[PrisonerBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Prisoner | PrisonerBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_operand(self) -> bool:
        return self._model is not None and self._blueprint is None
    
    @property
    def is_blueprint_operand(self) -> bool:
        return self._model is None and self._blueprint is not None
    
    @property
    def is_empty(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def has_overflow(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def size(self) -> int:
        if self.is_empty: return 0
        if self.is_model_operand or self.is_blueprint_operand: return 1
        return 2
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, PrisonerDtoOperand):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

