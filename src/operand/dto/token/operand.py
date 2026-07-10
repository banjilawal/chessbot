# src/operand/dto/token/operand.py

"""
Module: operand.dto.token.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import TokenBlueprint
from model import Token
from operand import DtoOperand


class TokenDtoOperand(DtoOperand[Token]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Dto for transporting either a Token or TokenBlueprint
    
    Attributes:
        model: Optional[Token]
        blueprint: Optional[TokenBlueprint]
        is_model_operand: bool
        is_blueprint_operand: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
        -   extract_blueprint() -> Optional[TokenBlueprint]
    
    Super Class:
        DtoOperand
    """
    _model: Optional[Token]
    _blueprint: Optional[TokenBlueprint]
    
    def __init__(
            self,
            model: Optional[Token] | None = None,
            blueprint: Optional[TokenBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Token]
            blueprint: Optional[TokenBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def operand(self) -> [Token|TokenBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Token)
        )
    
    @property
    def is_blueprint_operand(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, TokenBlueprint)
        )
    
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
    
    def extract_blueprint(self) -> Optional[TokenBlueprint]:
        if self.is_empty: return None
        if self.is_blueprint_operand: return self._blueprint
        return TokenBlueprint(
            id=self._model.id,
            team=self._model.team,
            rank=self._model.rank,
            formation=self._model.formation,
            home_square=self._model.home_square,
        )
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TokenDtoOperand):
            return self.operand == other.operand
        return False
    
    def __hash__(self):
        return hash(self.operand)

