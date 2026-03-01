# src/logic/team/hash/exception/base.py

"""
Module: logic.team.hash.exception.base
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH EXCEPTION #======================#
    "TeamHashException",
]

from logic.team import TeamException


# ======================# TEAM_HASH EXCEPTION #======================#
class TeamHashException(TeamException):
    """
    # ROLE: Super Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamHash objects.
    2.  Super for TeamHash failure conditions that do not have a one-to-one mapping to a TeamHashException
        subclass.
  
    # PARENT:
        *   TeamException
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_HASH_EXCEPTION"
    MSG = "TeamHash raised an exception."