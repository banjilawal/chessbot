# src/model/context/rank/model.py

"""
Module: model.context.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class RankContext(Context[Rank]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Rank attribute-value tuple which selects an execution path.

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
    _ransom: Optional[int]
    _team_quota: Optional[int]
    _designation: Optional[str]
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            ransom: Optional[int] = None,
            team_quota: Optional[int] = None,
            designation: Optional[str] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (Optional[int])
            *   designation (Optional[str])
            *   team (Optional[Team])
            *   game (Optional[Game])
            *   variety (Optional[RankVariety])

        # RETURNS:
        None

        Raises:
        """
        super().__init__(id=id, name=name)
        self._ransom = ransom
        self._team_quota = team_quota
        self._designation = designation
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def team_quota(self) -> Optional[int]:
        return self._team_quota
    
    @property
    def designation(self) -> Optional[str]:
        return self._designation
    
    def to_dict(self) -> dict:
        """
        # Convert the RankContext object to a dictionary.

        # PARAMETERS:
        None

        # RETURNS:
        dict

        Raises:
        """
        def to_dict(self) -> dict:
            return {
                "id": self._id,
                "designation": self._name,
                "ransom": self._ransom,
                "team_quota": self._team_quota,
                "designation": self._designation,
            }



