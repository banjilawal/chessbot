# src/domain/metadata/blueprint/struct/binder/player.blueprint.py

"""
Module: domain.metadata.blueprint.struct.binder.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import BinderBlueprint, Player, PlayerBinder
from err import PlayerBinderNullException


class PlayerBinderBlueprint(BinderBlueprint[PlayerBinder, Playe]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a PlayerBinder.

     Attributes:
        u: Player
        v: Player
        domain_class: Optional[Type[PlayerBinder]]
        domain_null_exception: Optional[PlayerBinderNullException]

     Provides:

     Super Class:
        BinderBlueprint
     """
    _u: Player
    _v: Player
    
    def __init__(
            self,
            u: Player,
            v: Player,
            domain_class: Optional[Type[PlayerBinder]] | None = None,
            domain_null_exception: Optional[PlayerBinderNullException] | None = None,
    ):
        """
        Args:
            u: Player
            v: Player
            domain_class: Optional[Type[PlayerBinder]]
            domain_null_exception: Optional[PlayerBinderNullException]
        """
        super().__init__(
            domain_class=domain_class or PlayerBinder,
            domain_null_exception=domain_null_exception or PlayerBinderNullException(),
        )
        self._u = u
        self._v = v
        
    @property
    def u(self) -> Player:
        return self._u
    
    @property
    def v(self) -> Player:
        return self._v
    
    @property
    def domain_class(self) -> Type[PlayerBinder]:
        return cast(Type[PlayerBinder], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PlayerBinderNullException:
        return cast(PlayerBinderNullException, super().domain_null_exception)
    
    
