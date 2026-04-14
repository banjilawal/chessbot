# src/model/binder/exception/anchor.py

"""
Module: model.binder.exception.base
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_BINDER EXCEPTION #======================#
    "TeamBinderException",
]

from model.team import TeamException


# ======================# TEAM_BINDER EXCEPTION #======================#
class TeamBinderException(TeamException):
    """
    Role:Super Exception
  
    Responsibilities:
    1.  Parent of exceptions raised by TeamBinder objects.
    2.  Super for TeamBinder failure conditions that do not have a one-to-one mapping to a TeamBinderException
        subclass.
  
    Super Class:
        *   TeamException
  
    Provides:
  
    # ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BINDER_EXCEPTION"
    MSG = "TeamBinder raised an exception."