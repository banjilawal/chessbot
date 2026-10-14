# src/assurance/depend/wrapper/struct/binder/depend.py

"""
Module: assurance.depend.wrapper.struct.binder.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import BinderDependency
from domain import PlayerBinder
from exchange import PlayerValidationResponseWrapper


class PlayerBinderDependency(BinderDependency[PlayerBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Binder needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        player: PlayerValidationResponseWrapper

    Provides:

    Super Class:
        BinderDependency
    """
    _player: PlayerValidationResponseWrapper
    
    def __init__(
            self,
            player: Optional[PlayerValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            player: Optional[PlayerValidationResponseWrapper]
        """
        super().__init__()
        self._player = player or PlayerValidationResponseWrapper()
        
    @property
    def player(self) -> PlayerValidationResponseWrapper:
        return self._player