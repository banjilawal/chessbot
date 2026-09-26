# src/assurance/loader/model/board/extract.py

"""
Module: assurance.loader.model.board.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelExtract
from domain import Blueprint, Board, BoardBlueprint
from transit import EntityCarrier, BoardCarrier


class BoardlExtract(ModelExtract[Board]):

    def __(
            self,
            carrier: EntityCarrier[Board],
            blueprint: Optional[Blueprint[Board]],
            model: Optional[Board],
    ):
        """
        Args:
            carrier: EntityCarrier[Board]
            blueprint: Optional[Blueprint[Board]]
            model: Optional[T]
        """
        super().__init__(
            carrier=carrier,
            blueprint=blueprint,
            model=model,
        )
        
    @property
    def carrier(self) -> BoardCarrier:
        return cast(BoardCarrier, super().carrier)
    
    @property
    def model(self) -> Optional[Board]:
        return cast(Board, super().model)
    
    @property
    def blueprint(self) -> Optional[BoardBlueprint]:
        return cast(BoardBlueprint,super().blueprint)
    
    @property
    def is_model_load(self) -> bool:
        if self._model is None:
            return False
        if (
                self.model is None or
                not isinstance(self.model, Board)
        ):
            return False
        return True
    
    @property
    def is_blueprint_load(self) -> bool:
        if self._blueprint is None:
            return False
        if (
                self.blueprint is None or
                not isinstance(self.blueprint, BoardBlueprint)
        ):
            return False
        return True