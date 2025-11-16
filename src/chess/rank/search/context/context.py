# src/chess/rank/search/context/context

"""
Module: chess.rank.search.context.context
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from typing import Optional

from chess.rank import Rank
from chess.system import SearchContext


class RankSearchContext(SearchContext):
    """
    # ROLE: Search option filter
  
    # RESPONSIBILITIES:
    Provides options for what type of key-value pair RankSearch implementations use to find matches.
  
    # PROVIDES:
    RankSearchContext.
  
    # ATTRIBUTES:
        *   id (int):
        *   name (str):
        *   ransom (int):
        *   team_quota (int):
        *   designation (str):
    """
    _id: Optional[int]
    _nane: Optional[str]
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
        self._id = id
        self._name = name
        self._ransom = ransom
        self._team_quota = team_quota
        self._designation = designation

    @property
    def id(self) -> Optional[int]:
        return self._id
    
    @property
    def name(self) -> Optional[str]:
        return self._name
    
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
        return {
            "id": self._id,
            "name": self._name,
            "ransom": self._ransom,
            "team_quota": self._team_quota,
            "designation": self._designation,
        }
