# src/chess/persona/key/key.py

"""
Module: chess.persona.key.key
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from typing import Optional

from chess.persona import Persona
from chess.system import Context


class PersonaSuperKey(Context[Persona]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    The for A PersonaSuperKey is used to run Forward Persona lookups use a PersonaSuperKey
    1.  Provides information to complete run forward-lookups on the Persona
    2.  Define a SuperKey from an attribute-value pair. The attribute must exist in the persona.
    3.  A forward lookup for a Persona variant requires a PersonaSuperKey.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   quota (Optional[int])
        *   ransom (Optional[int])
        *   designation (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _name: Optional[str]
    _quota: Optional[int]
    _ransom: Optional[int]
    _designation: Optional[str]
    
    def __init__(
            self,
            name: Optional[str] = None,
            quota: Optional[int] = None,
            ransom: Optional[int] = None,
            designation: Optional[str] = None,
    ):
        """
        # ACTION:
            Constructor
        # PARAMETERS:
            *   name (Optional[str])
            *   quota (Optional[int])
            *   ransom (Optional[int])
            *   designation (Optional[str])
        # RETURN:
            None
        # RAISES:
            None
        """
        super().__init__(id=None, name=name)
        self._quota = quota
        self._ransom = ransom
        self._designation = designation
    
    @property
    def quota(self) -> Optional[int]:
        return self._quota
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def designation(self) -> Optional[str]:
        return self._designation
    
    def to_dict(self) -> dict:
        """
        # ACTION
            1.  Convert the PersonaSuperKey object to a dictionary.
        # PARAMETERS:
            *   None
        # RETURNS:
            *   dict
        # RAISES:
            *   None
        """
        return {
            "name": self.name,
            "ransom": self._ransom,
            "quota": self._quota,
            "designation": self.designation,
        }