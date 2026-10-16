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
from exchange import PlayerValidationServer


class PlayerBinderDependency(BinderDependency[PlayerBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Binder needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        player: PlayerValidationServer

    Provides:

    Super Class:
        BinderDependency
    """
    _player: PlayerValidationServer
    
    def __init__(
            self,
            player: Optional[PlayerValidationServer] | None = None,
    ):
        """
        Args:
            player: Optional[PlayerValidationServer]
        """
        super().__init__()
        self._player = player or PlayerValidationServer()
        
    @property
    def player(self) -> PlayerValidationServer:
        return self._player