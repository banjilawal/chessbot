# src/domain/search/model/path/context.py

"""
Module: domain.search.model.path.context
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from domain import ModelContext, Path, Square


class PathContext(ModelContext[Path]):
    """
    Role:
        - Option Selector

    Responsibilities:
        1.  Supply PathSearcher with targeting criteria.

    Attributes:
        label: Optional[int]
        origin: Optional[Square]
        destination: Optional[Square]

    Provides:
        -  def to_dict() -> Dict[str, Any]

    Super Class:
        ModelContext
    """
    
    _label: Optional[int]
    _origin: Optional[Square]
    _destination: Optional[Square]
    
    def __init__(
            self,
            label: Optional[int] | None = None,
            origin: Optional[Square] | None = None,
            destination: Optional[Square] | None = None,
    ):
        """
        Args:
            label: Optional[int]
            origin: Optional[Square]
            destination: Optional[Square]n
        """
        super().__init__()
        self._label = label
        self._origin = origin
        self._destination = destination
    
    @property
    def label(self) -> Optional[int]:
        return self._label
    
    @property
    def origin(self) -> Optional[Square]:
        return self._origin
    
    @property
    def destination(self) -> Optional[Square]:
        return self._destination
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "label": self._label,
            "origin": self._origin,
            "destination": self._destination,
        }
