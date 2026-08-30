# src/domain/search/model/maneuver/context.py

"""
Module: domain.search.model.maneuver.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import Attack, Maneuver, ModelContext, Path, Token


class ManeuverContext(ModelContext[Maneuver]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply ManeuverSearcher with targeting criteria.

    Attributes:
        path: Optional[Path]
        attack: Optional[Attack]
        traveller: Optional[Token]
        benefit: Optional[PathBenefit]

    Provides:
        -  to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    
    _path: Optional[Path]
    _benefit: Optional[int]
    _attack: Optional[Attack]
    _traveller: Optional[Token]
    
    def __init__(
            self,
            path: Optional[Path] | None = None,
            benefit: Optional[int] | None = None,
            attack: Optional[Attack] | None = None,
            traveller: Optional[Token] | None = None,
    ):
        """
        Args:
            path: Optional[Path]
            attack: Optional[Attack]
            traveller: Optional[Token]
            benefit: Optional[PathBenefit]
        """
        super().__init__()
        self._path = path
        self._attack = attack
        self._benefit = benefit
        self._traveller = traveller
    
    @property
    def path(self) -> Optional[Path]:
        return self._path
    
    @property
    def benefit(self) -> Optional[int]:
        return self._benefit
    
    @property
    def attack(self) -> Optional[Attack]:
        return self._attack
    
    @property
    def traveller(self) -> Optional[Token]:
        return self._traveller
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self._path,
            "attack": self._attack,
            "benefit": self._benefit,
            "traveller": self._traveller,
        }
