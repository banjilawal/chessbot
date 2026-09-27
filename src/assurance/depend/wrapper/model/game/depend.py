# src/assurance/depend/wrapper/model/game/depend.py

"""
Module: assurance.depend.wrapper.model.game.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import ModelWrapperDependency
from domain import Game
from exchange import PlayerValidationResponseWrapper


class GameWrapperDependency(ModelWrapperDependency[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Satisfy GameValidator's ResponseWrapper dependencies.

    Attributes:
        player: PlayerValidationResponseWrapper

    Provides:

    Super Class:
        ModelWrapperDependency
    """

    _player: PlayerValidationResponseWrapper
    
    def __init__(
            self,
            player: Optional[PlayerValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            player: Optional[PlayerValidatorClient]
        """
        super().__init__()
        self._player = player or PlayerValidationResponseWrapper()
    
    @property
    def player(self) -> PlayerValidationResponseWrapper:
        return self._player