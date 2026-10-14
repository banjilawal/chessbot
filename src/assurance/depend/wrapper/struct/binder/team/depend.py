# src/assurance/depend/wrapper/struct/binder/depend.py

"""
Module: assurance.depend.wrapper.struct.binder.depend
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""


from __future__ import annotations

from typing import Optional

from assurance import BinderDependency
from domain import TeamBinder
from exchange import TeamValidationResponseWrapper


class TeamBinderDependency(BinderDependency[TeamBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Bundles validatorClients a Binder needs for its primitive and
            upstream relational partners attributes.

    Attributes:
        team: TeamValidationResponseWrapper

    Provides:

    Super Class:
        BinderDependency
    """
    _team: TeamValidationResponseWrapper
    
    def __init__(
            self,
            team: Optional[TeamValidationResponseWrapper] | None = None,
    ):
        """
        Args:
            team: Optional[TeamValidationResponseWrapper]
        """
        super().__init__()
        self._team = team or TeamValidationResponseWrapper()
        
    @property
    def team(self) -> TeamValidationResponseWrapper:
        return self._team