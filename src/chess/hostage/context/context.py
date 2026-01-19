# src/chess/hostage/context/context.py

"""
Module: chess.hostage.context.context
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""
from typing import Optional

from chess.coord import Coord
from chess.hostage import HostageManifest
from chess.system import Context
from chess.token import CombatantToken, TokenContext
from chess.token.model import Token


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
        *   prisoner (Optional[int])
        *   hostageManifest (Optional[HostageManifest])
        *   victor (Optional[int])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _id: Optional[int] = None
    _victor: Optional[Token] = None
    _prisoner: Optional[CombatantToken] = None
    _capture_location: Optional[Coord] = None
    _token_context: TokenContext
    
    def __init__(
            self,
            id: Optional[int],
            prisoner: Optional[CombatantToken] = None,
            victor: Optional[Token] = None,
            capture_location: Optional[Coord] = None,
            token_context: TokenContext= TokenContext(),
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
        self._capture_location = capture_location
        self._token_context = token_context
    
    @property
    def prisoner(self) -> Optional[int]:
        return self._prisoner
    
    @property
    def victor(self) -> Optional[int]:
        return self._victor
    
    @property
    def capture_location(self) -> Optional[Coord]:
        return self._capture_location
    
    @property
    def token_context(self) -> TokenContext:
        return self._token_context
    
    def to_dict(self) -> dict:
        return {
            "prisoner": self._prisoner,
            "victor": self._victor,
            "capture_location": self._capture_location,
        }
