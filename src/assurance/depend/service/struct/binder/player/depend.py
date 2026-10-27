# src/assurance/depend/service/struct/binder/depend.py

"""
Module: assurance.depend.service.struct.binder.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import BinderServiceDependency
from domain import PlayerBinder
from exchange import PlayerValidationService


class PlayerBinderDependency(BinderServiceDependency[PlayerBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Binder needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        player: PlayerValidationService

    Provides:

    Super Class:
        BinderDependency
    """
    _player: PlayerValidationService
    
    def __init__(
            self,
            player: Optional[PlayerValidationService] | None = None,
    ):
        """
        Args:
            player: Optional[PlayerValidationService]
        """
        super().__init__()
        self._player = player or PlayerValidationService()
        
    @property
    def player(self) -> PlayerValidationService:
        return self._player