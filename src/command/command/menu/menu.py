# src/command/command/menu/menu.py

"""
Module: command.command.menu.menu
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

from chess.system import  CommandRouter

S = TypeVar("S")

class ServiceMenu(ABC, Generic[S]):
    """
    # ROLE: Menu

    # RESPONSIBILITIES:
    1.  Collection of menus for the different operations the service supports.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   router (CommandRouter[S])
        *   menus (List[ServiceMenu])

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   router (CommandRouter[S])
        *   menus (List[ServiceMenu])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _service: S
    _router: CommandRouter[S]
    _pipelines: List[Pipeline]
    
  

    def __init__(
            self,
            router: CommandRouter[S],
            menus: List[ServiceMenu[S]],
    ):
        self._router = router
        self._menus = menus

    @property
    def router(self) -> CommandRouter[S]:
        return self._router
    
    @property
    def menus(self) -> List[ServiceMenu]:
        return self._menus