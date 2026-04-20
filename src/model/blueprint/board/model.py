# src/model/blueprint/board/model.py

"""
Module: model.blueprint.board.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Arena, Blueprint, Board


class BoardBlueprint(Blueprint[Board]):
    _id: int
    _arena: Arena

    
    def __init__(
            self,
            arena: Arena,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            arena: Arena
        """
        super().__init__()
        self._id = id
        self._arena = arena
        
    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def arena(self) -> Arena:
        return self._arena
    

