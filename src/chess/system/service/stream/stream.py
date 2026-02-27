# src/chess/system/service/stream/stream.py

"""
Module: chess.system.service.stream.stream
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

from chess.system import  CommandRouter

S = TypeVar("S")

class ServiceStream(ABC, Generic[S]):
    """
    # ROLE: Stream

    # RESPONSIBILITIES:
    1.  Collection of streams for the different operations the service supports.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   router (CommandRouter[S])
        *   streams (List[ServiceStream])

    # INHERITED ATTRIBUTES:
    None.

    # CONSTRUCTOR PARAMETERS:)
        *   router (CommandRouter[S])
        *   streams (List[ServiceStream])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _router: CommandRouter[S]
    _streams: List[ServiceStream[S]]
  

    def __init__(
            self,
            router: CommandRouter[S],
            streams: List[ServiceStream[S]],
    ):
        self._router = router
        self._streams = streams

    @property
    def router(self) -> CommandRouter[S]:
        return self._router
    
    @property
    def streams(self) -> List[ServiceStream]:
        return self._streams