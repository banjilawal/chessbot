# src/model/context/persona/model.py

"""
Module: model.context.persona.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""


class PersonaContext(Context[Persona]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Persona attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        current_position:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        opening_square_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
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
            *   schema (Optional[str])
            *   quota (Optional[int])
            *   ransom (Optional[int])
            *   designation (Optional[str])
        # RETURN:
            None
        Raises:
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
            1.  Convert the PersonaContext object to a dictionary.
        # PARAMETERS:
            *   None
        # RETURNS:
            *   dict
        Raises:
            *   None
        """
        return {
            "schema": self.designation,
            "ransom": self._ransom,
            "quota": self._quota,
            "designation": self.designation,
        }