# src/software/subscriber/metadata.py

"""
Module: software.subscriber.metdata
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from typing import List, Optional

from software import SoftwareLicense


class Subscriber:
    """
    Role:Controller

    Responsibilities:
    Interface players use to change the Arena's software.

    Super Class:
    None

    # PROVIDES:
    Subscriber

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   arena (Arena)
        *   white_player (Player)
        *   black_player (Player)

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _first_name: str
    _last_name: str
    _email: str
    _licenses: List[SoftwareLicense]
    
    def __init__(
            self,
            id: int,
            first_name: str,
            last_name: str,
            email: str,
            licenses: Optional[List[SoftwareLicense]] | None = None,
    ):
        """
        Args:
            id: int,
            first_name: str,
            last_name: str,
            email: str,
            licenses: Optional[List[SoftwareLicense]
        """
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._licenses = licenses or []
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @property
    def email(self) -> str:
        return self._email
    
    @property
    def licenses(self) -> List[SoftwareLicense]:
        return self._licenses
 