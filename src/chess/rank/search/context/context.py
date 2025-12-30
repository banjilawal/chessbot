# src/chess/rank/searcher/map

"""
Module: chess.rank.searcher.map
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.rank import Rank
from chess.system import Context


class RankContext(Context[Rank]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an RankFinder with an attribute value to find Ranks with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
        *   RankContext

    # LOCAL ATTRIBUTES:
        *   ransom (Optional[int])
        *   team_quota (Optional[int])
        *   designation (Optional[str])
        
    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
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

        # RAISES:
        None
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

        # RAISES:
        None
        """
        def to_dict(self) -> dict:
            return {
                "id": self._id,
                "designation": self._name,
                "ransom": self._ransom,
                "team_quota": self._team_quota,
                "designation": self._designation,
            }



