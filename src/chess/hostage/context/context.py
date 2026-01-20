# src/chess/hostage/context/context.py

"""
Module: chess.hostage.context.context
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from typing import Optional

from chess.square import Square
from chess.system import Context
from chess.hostage import HostageManifest
from chess.token import CombatantToken, Token


class CaptivityContext(Context[HostageManifest]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an HostageManifestFinder with an attribute-value which finds HostageManifests which match the targeted attribute-value.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   victor (Optional[Token])
        *   prisoner (Optional[CombatantToken])
        *   capturedSquare (Optional[Square])


    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _id: Optional[int] = None
    _victor: Optional[Token] = None
    _prisoner: Optional[CombatantToken] = None
    _captured_square: Optional[Square] = None
    
    def __init__(
            self,
            id: Optional[int],
            victor: Optional[Token] = None,
            captured_square: Optional[Square] = None,
            prisoner: Optional[CombatantToken] = None,
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   prisoner (Optional[int])
            *   hostageManifest (Optional[HostageManifest])
            *   victor (Optional[int])
        # RETURNS:
            None
        # RAISES:
            None
        """
        super().__init__(id=id, name=None)
        self._prisoner = prisoner
        self._victor = victor
        self._captured_square = captured_square
    
    @property
    def prisoner(self) -> Optional[CombatantToken]:
        return self._prisoner
    
    @property
    def victor(self) -> Optional[Token]:
        return self._victor
    
    @property
    def captured_square(self) -> Optional[Square]:
        return self._captured_square
    
    def to_dict(self) -> dict:
        return {
            "id:": self.id,
            "prisoner": self._prisoner,
            "victor": self._victor,
            "captured_square": self._captured_square,
        }
